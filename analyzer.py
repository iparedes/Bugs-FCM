import antlr4
from gen.mvasmLexer  import *
from sem import *

"""
LD: Loads the value of a memory position in a register
    LD REG MEM
    MEM can be:
      xxxxx address relative to start of data segment
      {xxxxx} absolute address
      REG value contained in the register is an address relative to the data segment
      {REG} value contained in the register is an absolute address

"""

class Analyzer():

    def __init__(self,stream):
        self.Walker=None
        self.Tree=None
        self.Stage=0
        self.seq=None
        self.Context={}
        self.Context['program']=None
        self.Context['stage']=0

        lexer = mvasmLexer(stream)
        tokens = antlr4.CommonTokenStream(lexer)
        parser = mvasmParser(tokens)

        self.Tree=parser.program()
        self.Walker=ParseTreeWalker()


    def Walk(self):
        # First time we walk is for the preprocessing of labels
        # Stes stage to one and Create the sem listener
        self.Context['stage']=1
        seq=Sem(self.Context)
        self.Walker.walk(seq,self.Tree)
        # In the next we set stage to 2 and do the walk for the semantic analysis
        self.Context['stage']=2
        self.Walker.walk(seq,self.Tree)
