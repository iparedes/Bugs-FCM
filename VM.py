from compiler import *

"""
Keep it simple
"""


MEM_SIZE=256        # Size of memory block
PROTECTED_SIZE=20   # Protected memory cannot be modified using code, just by mutation
GEN_REGS=8          # Number of general purpose registers
CODE_PADDING=10     # Percentage of memory extra-allocated to the Code Segment. The size of the code segment is defined
                    # by de loaded program, but we put some extra space to not let the code very tight

# Description of protected memory cells (only for the initial VM)
# These cells are the first positions of memory
# Offspringed VM is created from the values in the memory
PROTECTED=[
    ('ZERO',0),
    ('MEMSIZE',MEM_SIZE),
    ('PROTECTED',PROTECTED_SIZE),
    ('GENREGS',GEN_REGS),
    ('CODEPADDING',CODE_PADDING)
]

# CS: Code Segment. Starts after the protected area
# PC: Program Counter. Points to the next instruction to execute
# CH: Code Head first position of the loaded program
# DS: Data Segment
# SP: Stack Pointer
# HP: Heap Pointer
REGS=['CS', 'CH', 'DS', 'PC', 'SP', 'HP']


class VM:

    def __init__(self,memsize=MEM_SIZE):
        """The registers, internally are representated by numbers, 0 is the first register in REGS,
        """
        self.MemSize=memsize
        self.Regs=[]
        self.ProtSymbols={} # Dictionary: Key is the protected symbol, Value is the memory absolute position
        self.RegSymbols={}  # Dictionary: Key is the register symbol, Value is the index of the registers array
        self.Memory=[0]*self.MemSize

        self._pcidx=REGS.index('PC') # Tries to accelerate access to registers
        self._csidx=REGS.index('CS')
        self._dsidx=REGS.index('DS')
        self._spidx=REGS.index('SP')
        self._hpidx=REGS.index('HP')

        # Populates protected memory
        for count,elem in enumerate(PROTECTED,0):
            self.Memory[count]=elem[1]
            self.Memory[count]=elem[1]
            self.ProtSymbols[elem[0]]=count

        # Start populating the registers list and dictionary of symbols
        for count,elem in enumerate(REGS,0):
            self.RegSymbols[elem]=count
            self.Regs.append(0)
        # Continue populating with the general registers
        start=len(REGS)
        size=self.Memory[self.ProtSymbols['GENREGS']]
        for count in range(0,size):
            self.RegSymbols['R'+str(count)]=start+count
            self.Regs.append(0)

        # Set some initial values
        # The Code Segment starts right after the protected area
        size=self.get_mem(self.ProtSymbols['PROTECTED'])
        self.set_reg('CS',size)
        # The Stack grows from the bottom of the memory upwards
        # The SP points to the current head of the stack, so as initially there is nothing in the stack,
        # it points outside the memory (MEMSIZE)
        self.set_reg('SP',self.MemSize)


    def get_reg(self,idx):
        # Look at this!!
        # Expects access to the regs by index mostly, but if gets the symbolic name catches the exception and acts
        try:
            return self.Regs[idx]
        except TypeError:
            id=self.RegSymbols[idx]
            return self.Regs[id]

    def set_reg(self,idx,val):
        try:
            self.Regs[idx]=val
        except  TypeError:
            idx=self.RegSymbols[idx]
            self.Regs[idx]=val

    def set_mem(self,addr,val):
        if addr<0 or addr>=self.MemSize:
            addr=addr%self.MemSize
        if addr>=self.get_reg('CS'):
            self.Memory[addr]=val

    def get_mem(self,addr):
        if addr<0 or addr>=self.MemSize:
            addr=addr%self.MemSize
        return self.Memory[addr]

    def set_mem_blk(self,addr,blk):
        cont=addr
        while blk:
            item=blk.pop(0)
            self.set_mem(cont,item)
            cont+=1

    def load(self,program):

        Context={}
        Context['PROTECTED']=PROTECTED
        Context['REGISTERS']=self.RegSymbols
        Context['HEAPSIZE']=0   # Size of the heap will be set during compilation

        C=Compiler(program, Context)
        length_prog=len(C.bytecode)
        paddingpct=self.get_mem(self.ProtSymbols['CODEPADDING'])
        padding=int(length_prog*(paddingpct/100))
        size_code_segment=round(length_prog*(1+(padding/100)))

        # Data Segement starts after the code segment (program+padding)
        cs=self.get_reg('CS')
        ds=cs+size_code_segment
        self.set_reg('DS',ds)
        self.set_reg('HP',Context['HEAPSIZE'])

        # Loads the program at the start of the code segment plus half the padding (Code Head)
        ch=int(cs+padding/2)
        self.set_mem_blk(ch,C.bytecode)
        # Sets the Code Header relative to CS (probably will be used by a RST function)
        ch-=cs
        self.set_reg('CH',ch)
        # And initializes the PC relative to CS
        self.set_reg('PC',ch)


    def _get_pc(self):
        cs=self.get_reg(self._csidx)
        pcrel=self.get_reg(self._pcidx)
        pcabs=pcrel+cs
        data=self.get_mem(pcabs)
        pcabs+=1

        ds=self.get_reg(self._dsidx)
        # Checks if the pc overrouns the code segment
        if pcabs==ds:
            pcabs=cs

        pcrel=pcabs-cs
        self.set_reg(self._pcidx,pcrel)
        return data

    # Runs the next instruction
    def step(self):
        op_code=self._get_pc()
        symb_op_code=OP_CODES[op_code]
        func=getattr(self,symb_op_code)
        func()

    def _push(self,val):
        # SP points to the current head, so first we make it grow
        sp=self.get_reg(self._spidx)
        hp=self.get_reg(self._hpidx)
        ds=self.get_reg(self._dsidx)
        # The stack grows upwards
        sp-=1

        if sp==ds+hp:
            # the stack has reached the heap, so roll over
            sp=self.MemSize-1

        self.set_mem(sp,val)
        self.set_reg('SP',sp)

    def _pop(self):
        sp=self.get_reg(self._spidx)
        val=self.get_mem(sp)
        sp+=1
        if sp==self.MemSize:
            # the stack goes beyond the bottom of the memory (maybe too many pops), it rolls over to the beginning
            # of the stack segment (delimited by the end of the heap)
            hp=self.get_reg(self._hpidx)
            sp=hp
        self.set_reg('SP',sp)


    def show_architecture(self):
        print("Memory size:",self.MemSize)
        print("Protected size:",self.get_mem(self.ProtSymbols['PROTECTED']))

        for r in self.RegSymbols.keys():
            print(r+': '+str(self.get_reg(r)),end=' ')
        print()

    def show_memory(self,start=0,end=MEM_SIZE):
        for i in range(start,end):
            if i%8==0:
                t='\n'+str(i)+': '
                print(t.rjust(7),end='')
            print(str(self.get_mem(i)).ljust(4),end=' ')



    # ld1 reg addr
    # loads in reg the value in addr relative to DS
    def _ld1(self):
        reg=self._get_pc()
        addr=self._get_pc()
        # Address is relative to DS
        addr+=self.get_reg('DS')
        val=self.get_mem(addr)
        self.set_reg(reg,val)

    # ld2 reg1 reg2
    # loads in reg1 the value of the addr relative to DS stored in reg2
    def _ld2(self):
        reg1=self._get_pc()
        reg2=self._get_pc()
        addr=self.get_reg(reg2)
        # Address is relative to DS
        addr+=self.get_reg('DS')
        val=self.get_mem(addr)
        self.set_reg(reg1,val)

    # ld3 reg {addr}
    # Loads in a register the content of an absolute memory address
    def _ld3(self):
        # When it gets here, the PC points to the target register
        reg=self._get_pc()
        addr=self._get_pc()
        val=self.get_mem(addr)
        self.set_reg(reg,val)

    # ld4 reg1 {reg2}
    # Loads in reg1 the content of the absolute memory address contained in reg2
    def _ld4(self):
        reg1=self._get_pc()
        reg2=self._get_pc()
        addr=self.get_reg(reg2)
        val=self.get_mem(addr)
        self.set_reg(reg1,val)

    # Loads in reg1 a numeric value
    def _ld5(self):
        reg1=self._get_pc()
        val=self._get_pc()
        self.set_reg(reg1,val)


    # st1 reg addr
    # stores in addr (relative to DS) the value in reg
    def _st1(self):
        reg=self._get_pc()
        val=self.get_reg(reg)
        addr=self._get_pc()
        # Address is relative to DS
        addr+=self.get_reg('DS')
        self.set_mem(addr,val)

    # st2 reg1 reg2
    # stores in the address in reg2 (relative to DS) the value of reg1
    def _st2(self):
        reg1=self._get_pc()
        val=self.get_reg(reg1)

        reg2=self._get_pc()
        addr=self.get_reg(reg2)
        # Address is relative to DS
        addr+=self.get_reg('DS')
        self.set_mem(addr,val)

    # st3 reg {addr}
    # Stores in absolute addr the content of register reg
    def _st3(self):
        reg=self._get_pc()
        addr=self._get_pc()
        val=self.get_reg(reg)
        self.set_mem(addr,val)

    # st4 reg1 {reg2}
    # stores in the address contained in reg2 (absoloute) the value of register reg1
    def _ld4(self):
        reg1=self._get_pc()
        reg2=self._get_pc()
        addr=self.get_reg(reg2)
        val=self.get_reg(reg1)
        self.set_mem(addr,val)


    # mov reg1 reg2
    # copies content of reg2 to reg1
    def _mov(self):
        reg1=self._get_pc()
        reg2=self._get_pc()
        val=self.get_reg(reg2)
        self.set_reg(reg1,val)

    # psh reg
    # pushes the content of register to the stack
    def _psh(self):
        reg=self._get_pc()
        val=self.get_reg(reg)
        self._push(val)

    # pop reg
    # pops the head of the stack into register
    def _pp(self):
        reg=self._get_pc()
        val=self._pop()
        self.set_reg(reg,val)

