from compiler import *


class Compiler_bug(Compiler):

    def __init__(self):
        Compiler.__init__(self)

        # Extend opcodes
        new_ops=['_srcf','_wlkt','_wlkw','_wlk']
        OP_CODES+=new_ops


    def SRCF(self):
        self.program.pop(0)
        op_code=OP_CODES.index('_srcf')
        return [op_code]

    def WLKT(self):
        self.program.pop(0)
        op_code=OP_CODES.index('_wlkt')
        return [op_code]


    def WLKW(self)
        self.program.pop(0)
        op_code=OP_CODES.index('_wlkw')
        return [op_code]

    def WLK(self)
        self.program.pop(0)
        op_code=OP_CODES.index('_wlk')
        reg=self.program.pop(0)
        return [op_code, reg]



