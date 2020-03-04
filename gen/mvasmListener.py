# Generated from /Users/nacho/Documents/python-projects/Bugs-FCM/mvasm.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .mvasmParser import mvasmParser
else:
    from mvasmParser import mvasmParser

# This class defines a complete listener for a parse tree produced by mvasmParser.
class mvasmListener(ParseTreeListener):

    # Enter a parse tree produced by mvasmParser#programs.
    def enterPrograms(self, ctx:mvasmParser.ProgramsContext):
        pass

    # Exit a parse tree produced by mvasmParser#programs.
    def exitPrograms(self, ctx:mvasmParser.ProgramsContext):
        pass


    # Enter a parse tree produced by mvasmParser#program.
    def enterProgram(self, ctx:mvasmParser.ProgramContext):
        pass

    # Exit a parse tree produced by mvasmParser#program.
    def exitProgram(self, ctx:mvasmParser.ProgramContext):
        pass


    # Enter a parse tree produced by mvasmParser#prog_type.
    def enterProg_type(self, ctx:mvasmParser.Prog_typeContext):
        pass

    # Exit a parse tree produced by mvasmParser#prog_type.
    def exitProg_type(self, ctx:mvasmParser.Prog_typeContext):
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


    # Enter a parse tree produced by mvasmParser#instrADD.
    def enterInstrADD(self, ctx:mvasmParser.InstrADDContext):
        pass

    # Exit a parse tree produced by mvasmParser#instrADD.
    def exitInstrADD(self, ctx:mvasmParser.InstrADDContext):
        pass


    # Enter a parse tree produced by mvasmParser#instrPSH.
    def enterInstrPSH(self, ctx:mvasmParser.InstrPSHContext):
        pass

    # Exit a parse tree produced by mvasmParser#instrPSH.
    def exitInstrPSH(self, ctx:mvasmParser.InstrPSHContext):
        pass


    # Enter a parse tree produced by mvasmParser#instrPOP.
    def enterInstrPOP(self, ctx:mvasmParser.InstrPOPContext):
        pass

    # Exit a parse tree produced by mvasmParser#instrPOP.
    def exitInstrPOP(self, ctx:mvasmParser.InstrPOPContext):
        pass


    # Enter a parse tree produced by mvasmParser#instrINC.
    def enterInstrINC(self, ctx:mvasmParser.InstrINCContext):
        pass

    # Exit a parse tree produced by mvasmParser#instrINC.
    def exitInstrINC(self, ctx:mvasmParser.InstrINCContext):
        pass


    # Enter a parse tree produced by mvasmParser#instrDEC.
    def enterInstrDEC(self, ctx:mvasmParser.InstrDECContext):
        pass

    # Exit a parse tree produced by mvasmParser#instrDEC.
    def exitInstrDEC(self, ctx:mvasmParser.InstrDECContext):
        pass


    # Enter a parse tree produced by mvasmParser#instrJMP.
    def enterInstrJMP(self, ctx:mvasmParser.InstrJMPContext):
        pass

    # Exit a parse tree produced by mvasmParser#instrJMP.
    def exitInstrJMP(self, ctx:mvasmParser.InstrJMPContext):
        pass


    # Enter a parse tree produced by mvasmParser#instrJMPF.
    def enterInstrJMPF(self, ctx:mvasmParser.InstrJMPFContext):
        pass

    # Exit a parse tree produced by mvasmParser#instrJMPF.
    def exitInstrJMPF(self, ctx:mvasmParser.InstrJMPFContext):
        pass


    # Enter a parse tree produced by mvasmParser#instrJMPB.
    def enterInstrJMPB(self, ctx:mvasmParser.InstrJMPBContext):
        pass

    # Exit a parse tree produced by mvasmParser#instrJMPB.
    def exitInstrJMPB(self, ctx:mvasmParser.InstrJMPBContext):
        pass


    # Enter a parse tree produced by mvasmParser#instrJZ.
    def enterInstrJZ(self, ctx:mvasmParser.InstrJZContext):
        pass

    # Exit a parse tree produced by mvasmParser#instrJZ.
    def exitInstrJZ(self, ctx:mvasmParser.InstrJZContext):
        pass


    # Enter a parse tree produced by mvasmParser#instrJNZ.
    def enterInstrJNZ(self, ctx:mvasmParser.InstrJNZContext):
        pass

    # Exit a parse tree produced by mvasmParser#instrJNZ.
    def exitInstrJNZ(self, ctx:mvasmParser.InstrJNZContext):
        pass


    # Enter a parse tree produced by mvasmParser#instrSRCF.
    def enterInstrSRCF(self, ctx:mvasmParser.InstrSRCFContext):
        pass

    # Exit a parse tree produced by mvasmParser#instrSRCF.
    def exitInstrSRCF(self, ctx:mvasmParser.InstrSRCFContext):
        pass


    # Enter a parse tree produced by mvasmParser#instrWLKT.
    def enterInstrWLKT(self, ctx:mvasmParser.InstrWLKTContext):
        pass

    # Exit a parse tree produced by mvasmParser#instrWLKT.
    def exitInstrWLKT(self, ctx:mvasmParser.InstrWLKTContext):
        pass


    # Enter a parse tree produced by mvasmParser#instrwlkW.
    def enterInstrwlkW(self, ctx:mvasmParser.InstrwlkWContext):
        pass

    # Exit a parse tree produced by mvasmParser#instrwlkW.
    def exitInstrwlkW(self, ctx:mvasmParser.InstrwlkWContext):
        pass


    # Enter a parse tree produced by mvasmParser#instrWLK.
    def enterInstrWLK(self, ctx:mvasmParser.InstrWLKContext):
        pass

    # Exit a parse tree produced by mvasmParser#instrWLK.
    def exitInstrWLK(self, ctx:mvasmParser.InstrWLKContext):
        pass


    # Enter a parse tree produced by mvasmParser#instrEAT.
    def enterInstrEAT(self, ctx:mvasmParser.InstrEATContext):
        pass

    # Exit a parse tree produced by mvasmParser#instrEAT.
    def exitInstrEAT(self, ctx:mvasmParser.InstrEATContext):
        pass


    # Enter a parse tree produced by mvasmParser#instrNOP.
    def enterInstrNOP(self, ctx:mvasmParser.InstrNOPContext):
        pass

    # Exit a parse tree produced by mvasmParser#instrNOP.
    def exitInstrNOP(self, ctx:mvasmParser.InstrNOPContext):
        pass


    # Enter a parse tree produced by mvasmParser#instrLabel.
    def enterInstrLabel(self, ctx:mvasmParser.InstrLabelContext):
        pass

    # Exit a parse tree produced by mvasmParser#instrLabel.
    def exitInstrLabel(self, ctx:mvasmParser.InstrLabelContext):
        pass


    # Enter a parse tree produced by mvasmParser#valmem.
    def enterValmem(self, ctx:mvasmParser.ValmemContext):
        pass

    # Exit a parse tree produced by mvasmParser#valmem.
    def exitValmem(self, ctx:mvasmParser.ValmemContext):
        pass


    # Enter a parse tree produced by mvasmParser#valnumber.
    def enterValnumber(self, ctx:mvasmParser.ValnumberContext):
        pass

    # Exit a parse tree produced by mvasmParser#valnumber.
    def exitValnumber(self, ctx:mvasmParser.ValnumberContext):
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


    # Enter a parse tree produced by mvasmParser#reg.
    def enterReg(self, ctx:mvasmParser.RegContext):
        pass

    # Exit a parse tree produced by mvasmParser#reg.
    def exitReg(self, ctx:mvasmParser.RegContext):
        pass


    # Enter a parse tree produced by mvasmParser#gen_reg.
    def enterGen_reg(self, ctx:mvasmParser.Gen_regContext):
        pass

    # Exit a parse tree produced by mvasmParser#gen_reg.
    def exitGen_reg(self, ctx:mvasmParser.Gen_regContext):
        pass


    # Enter a parse tree produced by mvasmParser#wrt_reg.
    def enterWrt_reg(self, ctx:mvasmParser.Wrt_regContext):
        pass

    # Exit a parse tree produced by mvasmParser#wrt_reg.
    def exitWrt_reg(self, ctx:mvasmParser.Wrt_regContext):
        pass


    # Enter a parse tree produced by mvasmParser#prt_reg.
    def enterPrt_reg(self, ctx:mvasmParser.Prt_regContext):
        pass

    # Exit a parse tree produced by mvasmParser#prt_reg.
    def exitPrt_reg(self, ctx:mvasmParser.Prt_regContext):
        pass


    # Enter a parse tree produced by mvasmParser#number.
    def enterNumber(self, ctx:mvasmParser.NumberContext):
        pass

    # Exit a parse tree produced by mvasmParser#number.
    def exitNumber(self, ctx:mvasmParser.NumberContext):
        pass


