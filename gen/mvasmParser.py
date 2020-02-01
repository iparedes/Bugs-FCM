# Generated from /Users/nacho/Documents/python-projects/Bugs-FCM/mvasm.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31")
        buf.write("]\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\2\7\2\26\n\2\f\2\16\2\31\13\2\3")
        buf.write("\2\3\2\7\2\35\n\2\f\2\16\2 \13\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\5\3\66\n\3\3\4\3\4\3\4\3\4\3\4\5\4=\n\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\5\5D\n\5\3\6\3\6\5\6H\n\6\3\7\3\7\6\7L\n\7")
        buf.write("\r\7\16\7M\3\b\3\b\3\b\3\b\3\b\3\b\5\bV\n\b\3\t\6\tY\n")
        buf.write("\t\r\t\16\tZ\3\t\2\2\n\2\4\6\b\n\f\16\20\2\2\2g\2\27\3")
        buf.write("\2\2\2\4\65\3\2\2\2\6<\3\2\2\2\bC\3\2\2\2\nG\3\2\2\2\f")
        buf.write("I\3\2\2\2\16U\3\2\2\2\20X\3\2\2\2\22\23\5\4\3\2\23\24")
        buf.write("\7\30\2\2\24\26\3\2\2\2\25\22\3\2\2\2\26\31\3\2\2\2\27")
        buf.write("\25\3\2\2\2\27\30\3\2\2\2\30\32\3\2\2\2\31\27\3\2\2\2")
        buf.write("\32\36\5\4\3\2\33\35\7\30\2\2\34\33\3\2\2\2\35 \3\2\2")
        buf.write("\2\36\34\3\2\2\2\36\37\3\2\2\2\37\3\3\2\2\2 \36\3\2\2")
        buf.write("\2!\"\7\t\2\2\"#\5\16\b\2#$\7\22\2\2$%\5\b\5\2%\66\3\2")
        buf.write("\2\2&\'\7\n\2\2\'(\5\16\b\2()\7\22\2\2)*\5\b\5\2*\66\3")
        buf.write("\2\2\2+,\7\13\2\2,-\5\16\b\2-.\7\22\2\2./\5\16\b\2/\66")
        buf.write("\3\2\2\2\60\61\7\f\2\2\61\66\5\16\b\2\62\63\7\r\2\2\63")
        buf.write("\66\5\16\b\2\64\66\5\6\4\2\65!\3\2\2\2\65&\3\2\2\2\65")
        buf.write("+\3\2\2\2\65\60\3\2\2\2\65\62\3\2\2\2\65\64\3\2\2\2\66")
        buf.write("\5\3\2\2\2\67=\7\16\2\28=\7\17\2\29=\7\20\2\2:;\7\21\2")
        buf.write("\2;=\5\16\b\2<\67\3\2\2\2<8\3\2\2\2<9\3\2\2\2<:\3\2\2")
        buf.write("\2=\7\3\2\2\2>D\5\n\6\2?@\7\25\2\2@A\5\n\6\2AB\7\26\2")
        buf.write("\2BD\3\2\2\2C>\3\2\2\2C?\3\2\2\2D\t\3\2\2\2EH\5\20\t\2")
        buf.write("FH\5\f\7\2GE\3\2\2\2GF\3\2\2\2H\13\3\2\2\2IK\7\3\2\2J")
        buf.write("L\7\27\2\2KJ\3\2\2\2LM\3\2\2\2MK\3\2\2\2MN\3\2\2\2N\r")
        buf.write("\3\2\2\2OV\5\f\7\2PV\7\4\2\2QV\7\5\2\2RV\7\6\2\2SV\7\7")
        buf.write("\2\2TV\7\b\2\2UO\3\2\2\2UP\3\2\2\2UQ\3\2\2\2UR\3\2\2\2")
        buf.write("US\3\2\2\2UT\3\2\2\2V\17\3\2\2\2WY\7\27\2\2XW\3\2\2\2")
        buf.write("YZ\3\2\2\2ZX\3\2\2\2Z[\3\2\2\2[\21\3\2\2\2\13\27\36\65")
        buf.write("<CGMUZ")
        return buf.getvalue()


class mvasmParser ( Parser ):

    grammarFileName = "mvasm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'R'", "'CS'", "'CH'", "'DS'", "'PC'", 
                     "'SP'", "'LD'", "'ST'", "'MOV'", "'PSH'", "'POP'", 
                     "'SRCF'", "'WLKT'", "'WLKW'", "'WLK'", "','", "'('", 
                     "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "LD", "ST", 
                      "MOV", "PSH", "POP", "SRCF", "WLKT", "WLKW", "WLK", 
                      "COMMA", "OPAR", "CPAR", "OBRACE", "CBRACE", "DIGIT", 
                      "NEWLINE", "WS" ]

    RULE_program = 0
    RULE_instr = 1
    RULE_bug_instr = 2
    RULE_mem = 3
    RULE_address = 4
    RULE_gen_reg = 5
    RULE_reg = 6
    RULE_number = 7

    ruleNames =  [ "program", "instr", "bug_instr", "mem", "address", "gen_reg", 
                   "reg", "number" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    LD=7
    ST=8
    MOV=9
    PSH=10
    POP=11
    SRCF=12
    WLKT=13
    WLKW=14
    WLK=15
    COMMA=16
    OPAR=17
    CPAR=18
    OBRACE=19
    CBRACE=20
    DIGIT=21
    NEWLINE=22
    WS=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mvasmParser.InstrContext)
            else:
                return self.getTypedRuleContext(mvasmParser.InstrContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(mvasmParser.NEWLINE)
            else:
                return self.getToken(mvasmParser.NEWLINE, i)

        def getRuleIndex(self):
            return mvasmParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = mvasmParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 16
                    self.instr()
                    self.state = 17
                    self.match(mvasmParser.NEWLINE) 
                self.state = 23
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 24
            self.instr()
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==mvasmParser.NEWLINE:
                self.state = 25
                self.match(mvasmParser.NEWLINE)
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return mvasmParser.RULE_instr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class InstrSTContext(InstrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mvasmParser.InstrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ST(self):
            return self.getToken(mvasmParser.ST, 0)
        def reg(self):
            return self.getTypedRuleContext(mvasmParser.RegContext,0)

        def COMMA(self):
            return self.getToken(mvasmParser.COMMA, 0)
        def mem(self):
            return self.getTypedRuleContext(mvasmParser.MemContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrST" ):
                listener.enterInstrST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrST" ):
                listener.exitInstrST(self)


    class InstrPSHContext(InstrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mvasmParser.InstrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PSH(self):
            return self.getToken(mvasmParser.PSH, 0)
        def reg(self):
            return self.getTypedRuleContext(mvasmParser.RegContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrPSH" ):
                listener.enterInstrPSH(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrPSH" ):
                listener.exitInstrPSH(self)


    class InstrMOVContext(InstrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mvasmParser.InstrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MOV(self):
            return self.getToken(mvasmParser.MOV, 0)
        def reg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mvasmParser.RegContext)
            else:
                return self.getTypedRuleContext(mvasmParser.RegContext,i)

        def COMMA(self):
            return self.getToken(mvasmParser.COMMA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrMOV" ):
                listener.enterInstrMOV(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrMOV" ):
                listener.exitInstrMOV(self)


    class InstrPOPContext(InstrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mvasmParser.InstrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def POP(self):
            return self.getToken(mvasmParser.POP, 0)
        def reg(self):
            return self.getTypedRuleContext(mvasmParser.RegContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrPOP" ):
                listener.enterInstrPOP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrPOP" ):
                listener.exitInstrPOP(self)


    class InstrLDContext(InstrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mvasmParser.InstrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LD(self):
            return self.getToken(mvasmParser.LD, 0)
        def reg(self):
            return self.getTypedRuleContext(mvasmParser.RegContext,0)

        def COMMA(self):
            return self.getToken(mvasmParser.COMMA, 0)
        def mem(self):
            return self.getTypedRuleContext(mvasmParser.MemContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrLD" ):
                listener.enterInstrLD(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrLD" ):
                listener.exitInstrLD(self)


    class InstrBug_InstrContext(InstrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mvasmParser.InstrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def bug_instr(self):
            return self.getTypedRuleContext(mvasmParser.Bug_instrContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrBug_Instr" ):
                listener.enterInstrBug_Instr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrBug_Instr" ):
                listener.exitInstrBug_Instr(self)



    def instr(self):

        localctx = mvasmParser.InstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instr)
        try:
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mvasmParser.LD]:
                localctx = mvasmParser.InstrLDContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.match(mvasmParser.LD)
                self.state = 32
                self.reg()
                self.state = 33
                self.match(mvasmParser.COMMA)
                self.state = 34
                self.mem()
                pass
            elif token in [mvasmParser.ST]:
                localctx = mvasmParser.InstrSTContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.match(mvasmParser.ST)
                self.state = 37
                self.reg()
                self.state = 38
                self.match(mvasmParser.COMMA)
                self.state = 39
                self.mem()
                pass
            elif token in [mvasmParser.MOV]:
                localctx = mvasmParser.InstrMOVContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                self.match(mvasmParser.MOV)
                self.state = 42
                self.reg()
                self.state = 43
                self.match(mvasmParser.COMMA)
                self.state = 44
                self.reg()
                pass
            elif token in [mvasmParser.PSH]:
                localctx = mvasmParser.InstrPSHContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 46
                self.match(mvasmParser.PSH)
                self.state = 47
                self.reg()
                pass
            elif token in [mvasmParser.POP]:
                localctx = mvasmParser.InstrPOPContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 48
                self.match(mvasmParser.POP)
                self.state = 49
                self.reg()
                pass
            elif token in [mvasmParser.SRCF, mvasmParser.WLKT, mvasmParser.WLKW, mvasmParser.WLK]:
                localctx = mvasmParser.InstrBug_InstrContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 50
                self.bug_instr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bug_instrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return mvasmParser.RULE_bug_instr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class InstrSRCFContext(Bug_instrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mvasmParser.Bug_instrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SRCF(self):
            return self.getToken(mvasmParser.SRCF, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrSRCF" ):
                listener.enterInstrSRCF(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrSRCF" ):
                listener.exitInstrSRCF(self)


    class InstrwlkWContext(Bug_instrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mvasmParser.Bug_instrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WLKW(self):
            return self.getToken(mvasmParser.WLKW, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrwlkW" ):
                listener.enterInstrwlkW(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrwlkW" ):
                listener.exitInstrwlkW(self)


    class InstrWLKContext(Bug_instrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mvasmParser.Bug_instrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WLK(self):
            return self.getToken(mvasmParser.WLK, 0)
        def reg(self):
            return self.getTypedRuleContext(mvasmParser.RegContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrWLK" ):
                listener.enterInstrWLK(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrWLK" ):
                listener.exitInstrWLK(self)


    class InstrWLKTContext(Bug_instrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mvasmParser.Bug_instrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WLKT(self):
            return self.getToken(mvasmParser.WLKT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrWLKT" ):
                listener.enterInstrWLKT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrWLKT" ):
                listener.exitInstrWLKT(self)



    def bug_instr(self):

        localctx = mvasmParser.Bug_instrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_bug_instr)
        try:
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mvasmParser.SRCF]:
                localctx = mvasmParser.InstrSRCFContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.match(mvasmParser.SRCF)
                pass
            elif token in [mvasmParser.WLKT]:
                localctx = mvasmParser.InstrWLKTContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.match(mvasmParser.WLKT)
                pass
            elif token in [mvasmParser.WLKW]:
                localctx = mvasmParser.InstrwlkWContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 55
                self.match(mvasmParser.WLKW)
                pass
            elif token in [mvasmParser.WLK]:
                localctx = mvasmParser.InstrWLKContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 56
                self.match(mvasmParser.WLK)
                self.state = 57
                self.reg()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return mvasmParser.RULE_mem

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MemRelContext(MemContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mvasmParser.MemContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def address(self):
            return self.getTypedRuleContext(mvasmParser.AddressContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemRel" ):
                listener.enterMemRel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemRel" ):
                listener.exitMemRel(self)


    class MemAbsContext(MemContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mvasmParser.MemContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OBRACE(self):
            return self.getToken(mvasmParser.OBRACE, 0)
        def address(self):
            return self.getTypedRuleContext(mvasmParser.AddressContext,0)

        def CBRACE(self):
            return self.getToken(mvasmParser.CBRACE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemAbs" ):
                listener.enterMemAbs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemAbs" ):
                listener.exitMemAbs(self)



    def mem(self):

        localctx = mvasmParser.MemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_mem)
        try:
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mvasmParser.T__0, mvasmParser.DIGIT]:
                localctx = mvasmParser.MemRelContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.address()
                pass
            elif token in [mvasmParser.OBRACE]:
                localctx = mvasmParser.MemAbsContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.match(mvasmParser.OBRACE)
                self.state = 62
                self.address()
                self.state = 63
                self.match(mvasmParser.CBRACE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddressContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(mvasmParser.NumberContext,0)


        def gen_reg(self):
            return self.getTypedRuleContext(mvasmParser.Gen_regContext,0)


        def getRuleIndex(self):
            return mvasmParser.RULE_address

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddress" ):
                listener.enterAddress(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddress" ):
                listener.exitAddress(self)




    def address(self):

        localctx = mvasmParser.AddressContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_address)
        try:
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mvasmParser.DIGIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.number()
                pass
            elif token in [mvasmParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.gen_reg()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Gen_regContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(mvasmParser.DIGIT)
            else:
                return self.getToken(mvasmParser.DIGIT, i)

        def getRuleIndex(self):
            return mvasmParser.RULE_gen_reg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGen_reg" ):
                listener.enterGen_reg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGen_reg" ):
                listener.exitGen_reg(self)




    def gen_reg(self):

        localctx = mvasmParser.Gen_regContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_gen_reg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(mvasmParser.T__0)
            self.state = 73 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 72
                self.match(mvasmParser.DIGIT)
                self.state = 75 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==mvasmParser.DIGIT):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RegContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def gen_reg(self):
            return self.getTypedRuleContext(mvasmParser.Gen_regContext,0)


        def getRuleIndex(self):
            return mvasmParser.RULE_reg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReg" ):
                listener.enterReg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReg" ):
                listener.exitReg(self)




    def reg(self):

        localctx = mvasmParser.RegContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_reg)
        try:
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mvasmParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.gen_reg()
                pass
            elif token in [mvasmParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.match(mvasmParser.T__1)
                pass
            elif token in [mvasmParser.T__2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 79
                self.match(mvasmParser.T__2)
                pass
            elif token in [mvasmParser.T__3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 80
                self.match(mvasmParser.T__3)
                pass
            elif token in [mvasmParser.T__4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 81
                self.match(mvasmParser.T__4)
                pass
            elif token in [mvasmParser.T__5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 82
                self.match(mvasmParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(mvasmParser.DIGIT)
            else:
                return self.getToken(mvasmParser.DIGIT, i)

        def getRuleIndex(self):
            return mvasmParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = mvasmParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 85
                self.match(mvasmParser.DIGIT)
                self.state = 88 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==mvasmParser.DIGIT):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





