
OP_CODES=["_ld1","_ld2","_ld3","_ld4","_st1","_st2","_st3","_st4","_mov"]

"""
todo: INPUT and OUTPUT
"""



class Compiler:
    def __init__(self,prog,context):
        self.program=list(prog)
        self.bytecode=[]
        self.context=context


        # todo: Needs to account for the code padding
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
    """
    def LD(self):
        # First operand is a register
        # Extract the REG keyword and reads the reg index
        self.program.pop(0)
        reg=self.program.pop(0)
        regidx=self.context['REGISTERS'][reg]
        type=self.program.pop(0)
        op=self.program.pop(0)
        val=self.program.pop(0)
        if type=='REL':
            if op=='ADDR':
                # ld1
                op_code='_ld1'
            else: # op=='REG'
                # ld2
                op_code='_ld2'
        else:
            if op=='ADDR':
                # ld3
                op_code='_ld3'
            else: # op=='REG'
                op_code='_ld4'
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
        # Second operand is also a register
        self.program.pop(0)
        reg2=self.program.pop(0)
        op_code=OP_CODES.index('_mov')
        return [op_code,reg1,reg2]
