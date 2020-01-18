# Generated from /Users/nacho/Documents/python-projects/Bugs-FCM/mvasm.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .mvasmParser import mvasmParser
else:
    from mvasmParser import mvasmParser

# This class defines a complete listener for a parse tree produced by mvasmParser.
class mvasmListener(ParseTreeListener):

    # Enter a parse tree produced by mvasmParser#program.
    def enterProgram(self, ctx:mvasmParser.ProgramContext):
        pass

    # Exit a parse tree produced by mvasmParser#program.
    def exitProgram(self, ctx:mvasmParser.ProgramContext):
        pass


    # Enter a parse tree produced by mvasmParser#instrLD.
    def enterInstrLD(self, ctx:mvasmParser.InstrLDContext):
        pass

    # Exit a parse tree produced by mvasmParser#instrLD.
    def exitInstrLD(self, ctx:mvasmParser.InstrLDContext):
        pass


    # Enter a parse tree produced by mvasmParser#instrST.
    def enterInstrST(self, ctx:mvasmParser.InstrSTContext):
        pass

    # Exit a parse tree produced by mvasmParser#instrST.
    def exitInstrST(self, ctx:mvasmParser.InstrSTContext):
        pass


    # Enter a parse tree produced by mvasmParser#instrMOV.
    def enterInstrMOV(self, ctx:mvasmParser.InstrMOVContext):
        pass

    # Exit a parse tree produced by mvasmParser#instrMOV.
    def exitInstrMOV(self, ctx:mvasmParser.InstrMOVContext):
        pass


    # Enter a parse tree produced by mvasmParser#memRel.
    def enterMemRel(self, ctx:mvasmParser.MemRelContext):
        pass

    # Exit a parse tree produced by mvasmParser#memRel.
    def exitMemRel(self, ctx:mvasmParser.MemRelContext):
        pass


    # Enter a parse tree produced by mvasmParser#memAbs.
    def enterMemAbs(self, ctx:mvasmParser.MemAbsContext):
        pass

    # Exit a parse tree produced by mvasmParser#memAbs.
    def exitMemAbs(self, ctx:mvasmParser.MemAbsContext):
        pass


    # Enter a parse tree produced by mvasmParser#address.
    def enterAddress(self, ctx:mvasmParser.AddressContext):
        pass

    # Exit a parse tree produced by mvasmParser#address.
    def exitAddress(self, ctx:mvasmParser.AddressContext):
        pass


    # Enter a parse tree produced by mvasmParser#gen_reg.
    def enterGen_reg(self, ctx:mvasmParser.Gen_regContext):
        pass

    # Exit a parse tree produced by mvasmParser#gen_reg.
    def exitGen_reg(self, ctx:mvasmParser.Gen_regContext):
        pass


    # Enter a parse tree produced by mvasmParser#reg.
    def enterReg(self, ctx:mvasmParser.RegContext):
        pass

    # Exit a parse tree produced by mvasmParser#reg.
    def exitReg(self, ctx:mvasmParser.RegContext):
        pass


    # Enter a parse tree produced by mvasmParser#number.
    def enterNumber(self, ctx:mvasmParser.NumberContext):
        pass

    # Exit a parse tree produced by mvasmParser#number.
    def exitNumber(self, ctx:mvasmParser.NumberContext):
        pass


