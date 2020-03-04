import logging
import tools
from gen.mvasmListener import *

logger = tools.setup_logger('sem_logger', 'sem.log', logging.DEBUG)


class Sem(mvasmListener):

    def __init__(self, context):
        self.MemPointer = 0
        self.Programs=[]    # List of dictionaries containing
                            # {prog_type:(0-sensor|1-actor) prog_name, sequence[], maybe a register}
        self.Sequence = [] # stores the sequence of operations and operands of each program
        self.Labels = {}
        self.Context = context
        self.nProgs=0 # Index of the current subprogram

    def add(self, val):
        self.Programs[self.nProgs]['Sequence'].append(val)

    def pop(self):
        a = self.Programs[self.nProgs]['Sequence'].pop()
        return a


    # Enter a parse tree produced by mvasmParser#programs.
    def enterPrograms(self, ctx:mvasmParser.ProgramsContext):
        logger.info("")
        self.nProgs=0

    # Exit a parse tree produced by mvasmParser#programs.
    def exitPrograms(self, ctx:mvasmParser.ProgramsContext):
        logger.info("")
        if self.Context['stage']==2:
            # Returns all the shebang of programs in the attribute program of the context
            self.Context['program'] = self.Programs



    # Enter a parse tree produced by subleqasmParser#program.
    def enterProgram(self, ctx: mvasmParser.ProgramContext):
        logger.info("Stage "+str(self.Context['stage']))
        if self.Context['stage']==1:
            self.Programs.append({})
            self.Programs[self.nProgs]['MemPointer']= 0
        else:
            self.Programs[self.nProgs]['Sequence']=[]

    # Exit a parse tree produced by mvasmParser#program.
    def exitProgram(self, ctx: mvasmParser.ProgramContext):
        logger.info("")
        if self.Context['stage'] == 1:
            self.Programs[self.nProgs]['MemPointer'] += 1
        else:
            self.add("END")
        self.nProgs+=1

    # TODO: read the subprgram name and use it on exit program to create a dictionary
    # TODO: need to make all the experiment for a complex program

    # Enter a parse tree produced by mvasmParser#prog_type.
    def enterProg_type(self, ctx:mvasmParser.Prog_typeContext):
        logger.info(ctx.getText())

        if self.Context['stage']==1:
            tipo=ctx.children[0].getText()
            name=ctx.children[1].getText()
            self.Programs[self.nProgs]['prog_type']=tipo
            self.Programs[self.nProgs]['prog_name']=name
            if tipo=='SENSOR':
                reg=ctx.children[3].getText()
                self.Programs[self.nProgs]['reg']=reg


    # Exit a parse tree produced by mvasmParser#prog_type.
    def exitProg_type(self, ctx:mvasmParser.Prog_typeContext):
        logger.info(ctx.getText())
        if self.Context['stage'] == 2:
            # if the program is type Sensor...
            if self.Programs[self.nProgs]['prog_type']=='SENSOR':
                # ...we dont need the REG x in the sequence (already took care of it in enterProg_type
                self.pop()
                self.pop()

    # Enter a parse tree produced by mvasmParser#instrEAT.
    def enterInstrEAT(self, ctx:mvasmParser.InstrEATContext):
        logger.info(ctx.getText())
        if self.Context['stage'] == 1:
            self.Programs[self.nProgs]['MemPointer'] += 1
        else:
            self.add("EAT")

    # Exit a parse tree produced by mvasmParser#instrEAT.
    def exitInstrEAT(self, ctx:mvasmParser.InstrEATContext):
        pass

    # Enter a parse tree produced by mvasmParser#instrLD.
    def enterInstrLD(self, ctx: mvasmParser.InstrLDContext):
        logger.info(ctx.getText())
        if self.Context['stage'] == 1:
            self.Programs[self.nProgs]['MemPointer'] += 3
        else:
            self.add("LD")

    # Exit a parse tree produced by mvasmParser#instrLD.
    def exitInstrLD(self, ctx: mvasmParser.InstrLDContext):
        pass

    # Enter a parse tree produced by mvasmParser#instrNOP.
    def enterInstrNOP(self, ctx:mvasmParser.InstrNOPContext):
        logger.info(ctx.getText())
        if self.Context['stage'] == 1:
            self.Programs[self.nProgs]['MemPointer'] += 1
        else:
            self.add("NOP")


    # Exit a parse tree produced by mvasmParser#instrNOP.
    def exitInstrNOP(self, ctx:mvasmParser.InstrNOPContext):
        pass

    # Enter a parse tree produced by mvasmParser#instrST.
    def enterInstrST(self, ctx: mvasmParser.InstrSTContext):
        logger.info(ctx.getText())
        if self.Context['stage'] == 1:
            self.Programs[self.nProgs]['MemPointer'] += 3
        else:
            self.add("ST")

    # Exit a parse tree produced by mvasmParser#instrST.
    def exitInstrST(self, ctx: mvasmParser.InstrSTContext):
        pass

    # Enter a parse tree produced by mvasmParser#instrMOV.
    def enterInstrMOV(self, ctx: mvasmParser.InstrMOVContext):
        logger.info(ctx.getText())
        if self.Context['stage'] == 1:
            self.Programs[self.nProgs]['MemPointer'] += 3
        else:
            self.add("MOV")

    # Exit a parse tree produced by mvasmParser#instrMOV.
    def exitInstrMOV(self, ctx: mvasmParser.InstrMOVContext):
        pass

    # Enter a parse tree produced by mvasmParser#instrPSH.
    def enterInstrPSH(self, ctx: mvasmParser.InstrPSHContext):
        logger.info(ctx.getText())
        if self.Context['stage'] == 1:
            self.Programs[self.nProgs]['MemPointer'] += 2
        else:
            self.add("PSH")

    # Exit a parse tree produced by mvasmParser#instrPSH.
    def exitInstrPSH(self, ctx: mvasmParser.InstrPSHContext):
        pass

    # Enter a parse tree produced by mvasmParser#instrPOP.
    def enterInstrPOP(self, ctx: mvasmParser.InstrPOPContext):
        logger.info(ctx.getText())
        if self.Context['stage'] == 1:
            self.Programs[self.nProgs]['MemPointer'] += 2
        else:
            self.add("POP")

    # Exit a parse tree produced by mvasmParser#instrPOP.
    def exitInstrPOP(self, ctx: mvasmParser.InstrPOPContext):
        pass

    # Enter a parse tree produced by mvasmParser#instrINC.
    def enterInstrINC(self, ctx:mvasmParser.InstrINCContext):
        logger.info(ctx.getText())
        if self.Context['stage'] == 1:
            self.Programs[self.nProgs]['MemPointer'] += 2
        else:
            self.add("INC")

    # Exit a parse tree produced by mvasmParser#instrINC.
    def exitInstrINC(self, ctx:mvasmParser.InstrINCContext):
        pass


    # Enter a parse tree produced by mvasmParser#instrDEC.
    def enterInstrDEC(self, ctx:mvasmParser.InstrDECContext):
        logger.info(ctx.getText())
        if self.Context['stage'] == 1:
            self.Programs[self.nProgs]['MemPointer'] += 2
        else:
            self.add("DEC")

    # Exit a parse tree produced by mvasmParser#instrDEC.
    def exitInstrDEC(self, ctx:mvasmParser.InstrDECContext):
        pass

    # Enter a parse tree produced by mvasmParser#reg.
    def enterReg(self, ctx: mvasmParser.RegContext):
        pass

    # Exit a parse tree produced by mvasmParser#reg.
    def exitReg(self, ctx: mvasmParser.RegContext):
        pass

    # Enter a parse tree produced by mvasmParser#prt_reg.
    def enterPrt_reg(self, ctx: mvasmParser.Prt_regContext):
        pass

    # Exit a parse tree produced by mvasmParser#prt_reg.
    def exitPrt_reg(self, ctx: mvasmParser.Prt_regContext):
        logger.info(ctx.getText())
        if self.Context['stage'] == 2:
            reg = ctx.getText()
            logger.info(reg)
            self.add('REG')
            self.add(reg)

    # Enter a parse tree produced by mvasmParser#wrt_reg.
    def enterWrt_reg(self, ctx: mvasmParser.Wrt_regContext):
        pass

    # Exit a parse tree produced by mvasmParser#wrt_reg.
    def exitWrt_reg(self, ctx: mvasmParser.Wrt_regContext):
        logger.info(ctx.getText())
        if self.Context['stage'] == 2:
            reg = ctx.getText()
            logger.info(reg)
            self.add('REG')
            self.add(reg)

    # Enter a parse tree produced by mvasmParser#mem.
    def enterMemRel(self, ctx: mvasmParser.MemContext):
        logger.info(ctx.getText())
        if self.Context['stage'] == 2:
            self.add('REL')

    # Exit a parse tree produced by mvasmParser#mem.
    def exitMemRel(self, ctx: mvasmParser.MemContext):
        pass

    # Enter a parse tree produced by mvasmParser#mem.
    def enterMemAbs(self, ctx: mvasmParser.MemContext):
        logger.info(ctx.getText())
        if self.Context['stage'] == 2:
            self.add('ABS')

    # Exit a parse tree produced by mvasmParser#mem.
    def exitMemAbs(self, ctx: mvasmParser.MemContext):
        pass

    # Enter a parse tree produced by mvasmParser#address.
    def enterAddress(self, ctx: mvasmParser.AddressContext):
        logger.info(ctx.getText())
        if self.Context['stage'] == 2:
            addr = int(ctx.getText())
            self.add('ADDR')
            #self.add(addr)

    # Exit a parse tree produced by mvasmParser#address.
    def exitAddress(self, ctx: mvasmParser.AddressContext):
        pass

    # Enter a parse tree produced by mvasmParser#instrADD.
    def enterInstrADD(self, ctx: mvasmParser.InstrADDContext):
        logger.info(ctx.getText())
        if self.Context['stage'] == 1:
            self.Programs[self.nProgs]['MemPointer'] += 3
        else:
            self.add("ADD")

    # Exit a parse tree produced by mvasmParser#instrADD.
    def exitInstrADD(self, ctx: mvasmParser.InstrADDContext):
        pass

    # Enter a parse tree produced by mvasmParser#instrSRCF.
    def enterInstrSRCF(self, ctx: mvasmParser.InstrSRCFContext):
        logger.info(ctx.getText())
        if self.Context['stage'] == 1:
            self.Programs[self.nProgs]['MemPointer'] += 1
        else:
            self.add("SRCF")

    # Exit a parse tree produced by mvasmParser#instrSRCF.
    def exitInstrSRCF(self, ctx: mvasmParser.InstrSRCFContext):
        pass

    # Enter a parse tree produced by mvasmParser#instrWLKT.
    def enterInstrWLKT(self, ctx: mvasmParser.InstrWLKTContext):
        logger.info(ctx.getText())
        if self.Context['stage'] == 1:
            self.Programs[self.nProgs]['MemPointer'] += 1
        else:
            self.add("WLKT")

    # Exit a parse tree produced by mvasmParser#instrWLKT.
    def exitInstrWLKT(self, ctx: mvasmParser.InstrWLKTContext):
        pass

    # Enter a parse tree produced by mvasmParser#instrwlkW.
    def enterInstrwlkW(self, ctx: mvasmParser.InstrwlkWContext):
        logger.info(ctx.getText())
        if self.Context['stage'] == 1:
            self.Programs[self.nProgs]['MemPointer'] += 1
        else:
            self.add("WLKw")

    # Exit a parse tree produced by mvasmParser#instrwlkW.
    def exitInstrwlkW(self, ctx: mvasmParser.InstrwlkWContext):
        pass

    # Enter a parse tree produced by mvasmParser#instrWLK.
    def enterInstrWLK(self, ctx: mvasmParser.InstrWLKContext):
        logger.info(ctx.getText())
        if self.Context['stage'] == 1:
            self.Programs[self.nProgs]['MemPointer'] += 2
        else:
            self.add("WLK")

    # Exit a parse tree produced by mvasmParser#instrWLK.
    def exitInstrWLK(self, ctx: mvasmParser.InstrWLKContext):
        pass

    # Enter a parse tree produced by mvasmParser#instrJMP.
    def enterInstrJMP(self, ctx: mvasmParser.InstrJMPContext):
        logger.info(ctx.getText())
        if self.Context['stage'] == 1:
            self.Programs[self.nProgs]['MemPointer'] += 2
        else:
            self.add("JMP")
            dir = ctx.stop.text
            self.add(self.Labels[dir])

    # Exit a parse tree produced by mvasmParser#instrJMP.
    def exitInstrJMP(self, ctx: mvasmParser.InstrJMPContext):
        pass

    # Enter a parse tree produced by mvasmParser#instrJMPF.
    def enterInstrJMPF(self, ctx: mvasmParser.InstrJMPFContext):
        logger.info(ctx.getText())
        if self.Context['stage'] == 1:
            self.Programs[self.nProgs]['MemPointer'] += 2
        else:
            self.add("JMPF")

    # Exit a parse tree produced by mvasmParser#instrJMPF.
    def exitInstrJMPF(self, ctx: mvasmParser.InstrJMPFContext):
        pass

    # Enter a parse tree produced by mvasmParser#instrJMPB.
    def enterInstrJMPB(self, ctx: mvasmParser.InstrJMPBContext):
        logger.info(ctx.getText())
        if self.Context['stage'] == 1:
            self.Programs[self.nProgs]['MemPointer'] += 2
        else:
            self.add("JMPB")

    # Exit a parse tree produced by mvasmParser#instrJMPB.
    def exitInstrJMPB(self, ctx: mvasmParser.InstrJMPBContext):
        pass

    # Enter a parse tree produced by mvasmParser#instrJZ.
    def enterInstrJZ(self, ctx:mvasmParser.InstrJZContext):
        logger.info(ctx.getText())
        if self.Context['stage'] == 1:
            self.Programs[self.nProgs]['MemPointer'] += 3
        else:
            self.add("JZ")
            dir = ctx.stop.text
            self.add(self.Labels[dir])


    # Exit a parse tree produced by mvasmParser#instrJZ.
    def exitInstrJZ(self, ctx:mvasmParser.InstrJZContext):
        pass


    # Enter a parse tree produced by mvasmParser#instrJNZ.
    def enterInstrJNZ(self, ctx:mvasmParser.InstrJNZContext):
        logger.info(ctx.getText())
        if self.Context['stage'] == 1:
            self.Programs[self.nProgs]['MemPointer'] += 3
        else:
            self.add("JNZ")
            dir = ctx.stop.text
            self.add(self.Labels[dir])

    # Exit a parse tree produced by mvasmParser#instrJNZ.
    def exitInstrJNZ(self, ctx:mvasmParser.InstrJNZContext):
        pass



    # Enter a parse tree produced by mvasmParser#valmem.
    def enterValmem(self, ctx: mvasmParser.ValmemContext):
        pass

    # Exit a parse tree produced by mvasmParser#valmem.
    def exitValmem(self, ctx: mvasmParser.ValmemContext):
        pass

    # Enter a parse tree produced by mvasmParser#valnumber.
    def enterValnumber(self, ctx: mvasmParser.ValnumberContext):
        logger.info(ctx.getText())
        if self.Context['stage'] == 2:
            self.add('VAL')

    # Exit a parse tree produced by mvasmParser#valnumber.
    def exitValnumber(self, ctx: mvasmParser.ValnumberContext):
        pass

    # Enter a parse tree produced by mvasmParser#number.
    def enterNumber(self, ctx: mvasmParser.NumberContext):
        pass

    # Exit a parse tree produced by mvasmParser#number.
    def exitNumber(self, ctx: mvasmParser.NumberContext):
        logger.info(ctx.getText())
        if self.Context['stage'] == 2:
            number = int(ctx.getText())
            self.add(number)

    # Enter a parse tree produced by mvasmParser#instrLabel.
    def enterInstrLabel(self, ctx: mvasmParser.InstrLabelContext):
        logger.info(ctx.getText())
        if self.Context['stage'] == 1:
            txt = ctx.getText()[:-1]
            self.Labels[txt] = self.MemPointer

    # Exit a parse tree produced by mvasmParser#instrLabel.
    def exitInstrLabel(self, ctx: mvasmParser.InstrLabelContext):
        pass
