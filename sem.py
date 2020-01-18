import logging
logger = logging.getLogger(__name__)
FORMAT = "[%(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT,filename="sem.log",level=logging.DEBUG)


from gen.mvasmListener import *

class Sem(mvasmListener):

    def __init__(self,context):
        self.MemPointer=0
        self.Sequence=[]
        self.Labels={}
        self.Context=context


    def add(self, val):
        self.Sequence.append(val)


    def pop(self):
        a=self.Sequence.pop()
        return a

        # Enter a parse tree produced by subleqasmParser#program.
    def enterProgram(self, ctx:mvasmParser.ProgramContext):
        logger.debug(ctx.getText())



    # Exit a parse tree produced by mvasmParser#program.
    def exitProgram(self, ctx:mvasmParser.ProgramContext):
        logger.debug(ctx.getText())
        self.Context['program']=self.Sequence


    # Enter a parse tree produced by mvasmParser#instrLD.
    def enterInstrLD(self, ctx:mvasmParser.InstrLDContext):
        logger.debug(ctx.getText())
        self.add("LD")

    # Exit a parse tree produced by mvasmParser#instrLD.
    def exitInstrLD(self, ctx:mvasmParser.InstrLDContext):
        pass

    # Enter a parse tree produced by mvasmParser#instrST.
    def enterInstrST(self, ctx:mvasmParser.InstrSTContext):
        logger.debug(ctx.getText())
        self.add("ST")


    # Exit a parse tree produced by mvasmParser#instrST.
    def exitInstrST(self, ctx:mvasmParser.InstrSTContext):
        pass

    # Enter a parse tree produced by mvasmParser#instrMOV.
    def enterInstrMOV(self, ctx:mvasmParser.InstrMOVContext):
        logger.debug(ctx.getText())
        self.add("MOV")

    # Exit a parse tree produced by mvasmParser#instrMOV.
    def exitInstrMOV(self, ctx:mvasmParser.InstrMOVContext):
        pass

    # Enter a parse tree produced by mvasmParser#instrPSH.
    def enterInstrPSH(self, ctx:mvasmParser.InstrPSHContext):
        logger.debug(ctx.getText())
        self.add("PSH")

    # Exit a parse tree produced by mvasmParser#instrPSH.
    def exitInstrPSH(self, ctx:mvasmParser.InstrPSHContext):
        pass

    # Enter a parse tree produced by mvasmParser#instrPOP.
    def enterInstrPOP(self, ctx:mvasmParser.InstrPOPContext):
        logger.debug(ctx.getText())
        self.add("POP")

    # Exit a parse tree produced by mvasmParser#instrPOP.
    def exitInstrPOP(self, ctx:mvasmParser.InstrPOPContext):
        pass

    # Enter a parse tree produced by mvasmParser#reg.
    def enterReg(self, ctx:mvasmParser.RegContext):
        pass

    # Exit a parse tree produced by mvasmParser#reg.
    def exitReg(self, ctx:mvasmParser.RegContext):
        reg=ctx.getText()
        logger.debug(reg)
        self.add('REG')
        self.add(reg)



    # Enter a parse tree produced by mvasmParser#mem.
    def enterMemRel(self, ctx:mvasmParser.MemContext):
        logger.debug(ctx.getText())
        self.add('REL')

    # Exit a parse tree produced by mvasmParser#mem.
    def exitMemRel(self, ctx:mvasmParser.MemContext):
        pass

    # Enter a parse tree produced by mvasmParser#mem.
    def enterMemAbs(self, ctx:mvasmParser.MemContext):
        logger.debug(ctx.getText())
        self.add('ABS')

    # Exit a parse tree produced by mvasmParser#mem.
    def exitMemAbs(self, ctx:mvasmParser.MemContext):
        pass

    # Enter a parse tree produced by mvasmParser#address.
    def enterAddress(self, ctx:mvasmParser.AddressContext):
        pass

    # Exit a parse tree produced by mvasmParser#address.
    def exitAddress(self, ctx:mvasmParser.AddressContext):
        logger.debug(ctx.getText())
        addr=int(ctx.getText())
        self.add('ADDR')
        self.add(addr)


