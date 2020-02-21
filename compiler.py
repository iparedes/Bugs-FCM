
OP_CODES=["_ld1","_ld2","_ld3","_ld4","_ld5","_st1","_st2","_st3","_st4",
          "_mov","_psh","_pp",'_srcf','_wlkt','_wlkw','_wlk','_jmp','_jmpf','_jmpb','_nop','_add','_end']

"""
todo: INPUT and OUTPUT
"""

"""

LD get_reg, val
    Loads val into a writable register
    val can be:
        content of relative memory address
        content of an absolute { memory address }
        a ( numeric_value )
"""

# todo: there are functions that use regidx and others dont. Looks like I screwed up. Need to run tests of each instruction
# todo: actually I am putting strings into the compiled memory

class Compiler:
    def __init__(self,prog,context):
        self.program=list(prog)
        self.bytecode=[]
        self.context=context

        while self.program:
            op=self.program.pop(0)
            #func_name=switcher.get(op)
            method = getattr(self, op)
            instr=method()
            #VM.Mem[code_pointer:0]=instr
            self.bytecode+=instr



    """
    Loads the value of a memory address in a register
    Depending on the format of the operation, different op_codes will be generated:
    ld1: reg, rel_mem
    ld2: reg, rel_reg
    ld3: reg, abs_mem
    ld4: reg, abs_reg
    ld5: reg, number
    """
    def LD(self):
        # First operand is a register
        # Extract the REG keyword and reads the reg index
        self.program.pop(0)
        reg=self.program.pop(0)
        regidx=self.context['REGISTERS'][reg]
        type=self.program.pop(0)
        if type=='REL':
            op=self.program.pop(0)
            val=self.program.pop(0)
            if op=='ADDR':
                # ld1
                op_code='_ld1'
            else: # op=='REG'
                # ld2
                op_code='_ld2'
        elif type=='ABS':
            op=self.program.pop(0)
            val=self.program.pop(0)
            if op=='ADDR':
                # ld3
                op_code='_ld3'
            else: # op=='REG'
                # ld4
                op_code='_ld4'
        else: # type=='VAL':
            # ld5
            val=self.program.pop(0)
            op_code='_ld5'
        op_code=OP_CODES.index(op_code)
        return [op_code,regidx,val]

    """
    Stores the value of a register in a memory address
    Depending on the format of the operation, different op_codes will be generated:
    st1: reg, rel_mem
    st2: reg, rel_reg
    st3: reg, abs_mem
    st4: reg, abs_reg
    """
    def ST(self):
        self.program.pop(0)
        reg=self.program.pop(0)
        regidx=self.context['REGISTERS'][reg]
        type=self.program.pop(0)
        op=self.program.pop(0)
        val=self.program.pop(0)
        if type=='REL':
            if op=='ADDR':
                # st1
                op_code='_st1'
            else: # op=='REG'
                # st2
                op_code='_st2'
        else:
            if op=='ADDR':
                # st3
                op_code='_st3'
            else: # op=='REG'
                op_code='_st4'
        op_code=OP_CODES.index(op_code)
        return [op_code,regidx,val]

    # Moves the content of reg2 to reg1
    # mov reg1, reg2
    def MOV(self):
        # First operand is a register
        # Extract the REG keyword and reads the reg index
        self.program.pop(0)
        reg1=self.program.pop(0)
        reg1idx=self.context['REGISTERS'][reg1]
        # Second operand is also a register
        self.program.pop(0)
        reg2=self.program.pop(0)
        reg2idx=self.context['REGISTERS'][reg2]
        op_code=OP_CODES.index('_mov')
        return [op_code,reg1idx,reg2idx]

    # Adds value of reg2 to reg1
    # add wrt_reg1 ,reg2
    def ADD(self):
        # First operand is a register
        # Extract the REG keyword and reads the reg index
        self.program.pop(0)
        reg1=self.program.pop(0)
        reg1idx=self.context['REGISTERS'][reg1]
        # Second operand is also a register
        self.program.pop(0)
        reg2=self.program.pop(0)
        reg2idx=self.context['REGISTERS'][reg2]
        op_code=OP_CODES.index('_add')
        return [op_code, reg1idx, reg2idx]

    # Pushes the content of reg to the stack
    # psh reg
    def PSH(self):
        self.program.pop(0)
        reg=self.program.pop(0)
        regidx=self.context['REGISTERS'][reg]
        op_code=OP_CODES.index('_psh')
        return [op_code, regidx]


    # Pops the head of the stack into reg
    # pop reg
    def POP(self):
        self.program.pop(0)
        reg=self.program.pop(0)
        regidx=self.context['REGISTERS'][reg]
        op_code=OP_CODES.index('_pop')
        return [op_code, regidx]

    def SRCF(self):
        op_code=OP_CODES.index('_srcf')
        return [op_code]

    def WLKT(self):
        op_code=OP_CODES.index('_wlkt')
        return [op_code]


    def WLKW(self):
        op_code=OP_CODES.index('_wlkw')
        return [op_code]

    def WLK(self):
        self.program.pop(0)
        op_code=OP_CODES.index('_wlk')
        reg=self.program.pop(0)
        regidx=self.context['REGISTERS'][reg]
        return [op_code, regidx]

    def JMP(self):
        op_code=OP_CODES.index('_jmp')
        dir=self.program.pop(0)
        return [op_code, dir]

    # JMPF and JMPB should probably accept a Reg
    def JMPF(self):
        op_code=OP_CODES.index('_jmpf')
        dir=self.program.pop(0)
        return [op_code, dir]

    def JMPB(self):
        op_code=OP_CODES.index('_jmpb')
        dir=self.program.pop(0)
        return [op_code, dir]

    def NOP(self):
        op_code=OP_CODES.index('_nop')
        return [op_code]

    def END(self):
        op_code=OP_CODES.index('_end')
        return [op_code]



