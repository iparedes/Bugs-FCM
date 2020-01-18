

# Memory size
MEM_SIZE=256

"""
Possible modifications:
Keep registers in a list or dictionary different to the one for the memory. This will improve speed when accessing the registers
    and at the same time, we can consider it as part of the main memory using the memory access interfaces to
    consider that the registers are part of the main memory (e.g. when dumping memory it could start with the registers, then the memory)
"""

# todo: test PC overrun
# todo: test ld4


# Special memory positions
# They are in order e.g. INPUT is position 1, the tupla includes the symbolic name and initial value
# ZERO: A ZERO
# INPUT: Input from outside
# OUTPUT: Output to outside
# todo: I need a method to allow complex outputs, as it is it is just a value,
# todo: unless I use it as a pointer to memory with the instructions to transmit
# GENREGS: Number of general purpose registers. Named R0 to R7. After this, the general registers are created
# BUFFER: Just some unused space
# CS: CODESEG: Start of the code segement. Initialized at machine creation. Absolute memory address
# DS: DATASEG: Start of the data segement. Initialized after loading code. Absolute memory address
# SP: Stack Pointer. Stack grows up from the bottom of the memory
# COND: Condition register. Holds context on the last value moved to a register (zero, neg, no neg)
# PC: Program Counter. Relative to CODESEG
PROTECTED=[
    ("ZERO",0),("MEMSIZE",MEM_SIZE),("INPUT",0),("OUTPUT",0),("GENREGS",8),("BUFFER",20),("CS",0),("DS",0),
    ("SP",0),("COND",0),("PC",0)
]

OP_CODES=["ld1","ld2","ld3","ld4"]

"""
+---------------+
|   PROTECTED   |
|               |
|  (REGISTERS)  |
+---------------+
|               |
|     CODE      |
|               |
+---------------+
|  DATA v       |
|               |
|               |
|               |
|               |
|               |
|  STACK ^      |
+---------------+
"""


class VM:

    def __init__(self):
        # Stores the position in memory that a ReservedSymbol refers to. To use internally during mem initialization
        self.ReservedSymbols={}
        # Inverse search. From a memory address gives the symbol name
        self.ReservedPointers={}

        # Populate reserved memory
        memcounter=0
        for elem in PROTECTED:
            # Creates the General Registers
            if elem[0]=="GENREGS":
                # First sets the value for the number of genregs
                self.ReservedSymbols[elem[0]]={'pos':memcounter,'val':elem[1]}
                self.ReservedPointers[memcounter]=elem[0]
                memcounter+=1
                nregs=elem[1]
                for i in range(0,nregs):
                    symb="R"+str(i)
                    self.ReservedSymbols[symb]={'pos':memcounter,'val':0}
                    self.ReservedPointers[memcounter]=symb
                    memcounter+=1
            else:
                # Builds the ReservedSymbols table. It is a dictionary:
                # Key: Symbol name
                # Val: (Absolute address, Initial value)
                self.ReservedSymbols[elem[0]]={'pos':memcounter,'val':elem[1]}
                self.ReservedPointers[memcounter]=elem[0]
                if elem[0]=='BUFFER':
                    memcounter+=elem[1]
                else:
                    memcounter+=1

        # Protected positions of memory
        # Any access below ProtectedSize will be forwarded to the proper register interface
        self.ProtectedSize=memcounter
        # Initializes memory
        MemSize=self.ReservedSymbols['MEMSIZE']['val']
        self.Mem=[0]*MemSize
        # We go kinda recursive here...

        # Initialize special memory positions and registers
        self._set_mem_abs(self.ReservedSymbols['MEMSIZE']['pos'],MemSize)

        self.set_reg('GENREGS',self.ReservedSymbols['GENREGS']['val'])
        # Sets the init of the Segment code. Code starts right after the protected area
        self.set_reg('CS',self.ProtectedSize)
        # SP is initialized at the end of the memory (stack grows upwards)
        self.set_reg('SP',self.ReservedSymbols['MEMSIZE']['val']-1)
        # DS is set by the Compiler after a program is loaded, for starters is same as SP
        self.set_reg('DS',self.ReservedSymbols['MEMSIZE']['val']-1)

        # Initialize the Program Counter (it is relative to CS)
        self._set_pc(0)
        self._set_mem_abs(200,99999)




    # sets an absolute address to a value
    def _set_mem_abs(self,address,value):
        memsize=self.get_reg('MEMSIZE')
        if (address>=0 and address<self.ProtectedSize):
            try:
                # Accessing a protected address
                symbol=self.ReservedPointers[address]
                self.ReservedSymbols[symbol]['val']=value
            except KeyError as e:
                print(e)
        elif (address<0)or(address>=memsize):
            address=address%memsize
        self.Mem[address]=value

    def set_memblk_abs(self,address,block):
        try:
            for pos,i in enumerate(block,0):
                self._set_mem_abs(address+pos,i)
        except Exception as e:
            print(e)



    def _get_mem_abs(self, pos):
        memsize=self.get_reg('MEMSIZE')
        if pos>=memsize:
            pos=pos % memsize
        return self.Mem[pos]

    # sets the PC relative to the Code Segment
    def _set_pc(self,pos):
        cs=self.get_reg('CS')
        ds=self.get_reg('DS')
        cssize=ds-cs
        pc=self.get_reg('PC')
        # If PC overruns the code segment (entering the data segment) cycles back to the start of CS
        if pc>=cssize:
                pc=pc%cssize
        self.set_reg('PC',pc)


    # increments the pc
    def _inc_pc(self,inc=1):
        cs=self.get_reg('CS')
        ds=self.get_reg('DS')
        cssize=ds-cs
        pc=self.get_reg('PC')
        pc+=inc
        # If PC overruns the code segment (entering the data segment) cycles back to the start of CS
        if pc>=cssize:
                pc=0
        self.set_reg('PC',pc)

    # gets the memory content pointed by the PC and increments the PC
    def get_pc(self):
        pc=self.get_reg('PC')
        pc+=self.get_reg('CS')
        a=self._get_mem_abs(pc)
        self._inc_pc()
        return a


    def get_reg(self,name):
        v=self.ReservedSymbols[name]['val']
        return v

    def set_reg(self,name,val):
        pos=self.ReservedSymbols[name]['pos']
        self._set_mem_abs(pos,val)

    def set_gen_reg(self,idx,val):
        try:
            symb="R"+str(idx)
            self.set_reg(symb,val)
        except Keyerror as e:
            # Ignore inexistent registers
            pass

    def get_gen_reg(self,idx):
        try:
            symb="R"+str(idx)
            ret=self.get_reg(symb)
        except Keyerror as e:
            # Return 0 if non existent register
            ret=0
        return ret




    # Runs the next instruction
    def step(self):
        op_code=self.get_pc()
        symb_op_code=OP_CODES[op_code]
        func=getattr(self,symb_op_code)
        func()



    # ld3 reg {addr}
    # Loads in a register the content of an absolute memory address
    def ld3(self):
        reg=self.get_pc()
        addr=self.get_pc()
        val=self._get_mem_abs(addr)
        self.set_gen_reg(reg,val)

    # ld4 reg1 {reg2}
    # Loads in reg1 the content of the absolute memory address contained in reg2
    def ld4(self):
        reg1=self.get_pc()
        reg2=self.get_pc()
        addr=self.get_gen_reg(reg2)
        val=self._get_mem_abs(addr)
        self.set_gen_reg(reg1,val)











