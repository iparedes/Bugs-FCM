# Generated from /Users/nacho/Documents/python-projects/Bugs-FCM/mvasm.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\34")
        buf.write("l\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2\7\2")
        buf.write("\34\n\2\f\2\16\2\37\13\2\3\2\3\2\7\2#\n\2\f\2\16\2&\13")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3<\n\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\5\4C\n\4\3\5\3\5\3\5\3\5\3\5\5\5J\n\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\5\6Q\n\6\3\7\3\7\5\7U\n\7\3\b\3\b\5\bY\n\b\3")
        buf.write("\t\3\t\5\t]\n\t\3\n\3\n\6\na\n\n\r\n\16\nb\3\13\3\13\3")
        buf.write("\f\6\fh\n\f\r\f\16\fi\3\f\2\2\r\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\2\3\3\2\4\n\2q\2\35\3\2\2\2\4;\3\2\2\2\6B\3\2\2\2")
        buf.write("\bI\3\2\2\2\nP\3\2\2\2\fT\3\2\2\2\16X\3\2\2\2\20\\\3\2")
        buf.write("\2\2\22^\3\2\2\2\24d\3\2\2\2\26g\3\2\2\2\30\31\5\4\3\2")
        buf.write("\31\32\7\33\2\2\32\34\3\2\2\2\33\30\3\2\2\2\34\37\3\2")
        buf.write("\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36 \3\2\2\2\37\35\3\2")
        buf.write("\2\2 $\5\4\3\2!#\7\33\2\2\"!\3\2\2\2#&\3\2\2\2$\"\3\2")
        buf.write("\2\2$%\3\2\2\2%\3\3\2\2\2&$\3\2\2\2\'(\7\13\2\2()\5\20")
        buf.write("\t\2)*\7\25\2\2*+\5\b\5\2+<\3\2\2\2,-\7\f\2\2-.\5\16\b")
        buf.write("\2./\7\25\2\2/\60\5\n\6\2\60<\3\2\2\2\61\62\7\r\2\2\62")
        buf.write("\63\5\16\b\2\63\64\7\25\2\2\64\65\5\16\b\2\65<\3\2\2\2")
        buf.write("\66\67\7\16\2\2\67<\5\16\b\289\7\17\2\29<\5\16\b\2:<\5")
        buf.write("\6\4\2;\'\3\2\2\2;,\3\2\2\2;\61\3\2\2\2;\66\3\2\2\2;8")
        buf.write("\3\2\2\2;:\3\2\2\2<\5\3\2\2\2=C\7\20\2\2>C\7\21\2\2?C")
        buf.write("\7\22\2\2@A\7\23\2\2AC\5\16\b\2B=\3\2\2\2B>\3\2\2\2B?")
        buf.write("\3\2\2\2B@\3\2\2\2C\7\3\2\2\2DJ\5\n\6\2EF\7\26\2\2FG\5")
        buf.write("\26\f\2GH\7\27\2\2HJ\3\2\2\2ID\3\2\2\2IE\3\2\2\2J\t\3")
        buf.write("\2\2\2KQ\5\f\7\2LM\7\30\2\2MN\5\f\7\2NO\7\31\2\2OQ\3\2")
        buf.write("\2\2PK\3\2\2\2PL\3\2\2\2Q\13\3\2\2\2RU\5\26\f\2SU\5\16")
        buf.write("\b\2TR\3\2\2\2TS\3\2\2\2U\r\3\2\2\2VY\5\20\t\2WY\5\24")
        buf.write("\13\2XV\3\2\2\2XW\3\2\2\2Y\17\3\2\2\2Z]\5\22\n\2[]\7\24")
        buf.write("\2\2\\Z\3\2\2\2\\[\3\2\2\2]\21\3\2\2\2^`\7\3\2\2_a\7\32")
        buf.write("\2\2`_\3\2\2\2ab\3\2\2\2b`\3\2\2\2bc\3\2\2\2c\23\3\2\2")
        buf.write("\2de\t\2\2\2e\25\3\2\2\2fh\7\32\2\2gf\3\2\2\2hi\3\2\2")
        buf.write("\2ig\3\2\2\2ij\3\2\2\2j\27\3\2\2\2\r\35$;BIPTX\\bi")
        return buf.getvalue()


class mvasmParser ( Parser ):

    grammarFileName = "mvasm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'R'", "'CS'", "'CH'", "'DS'", "'PC'", 
                     "'SP'", "'SRR'", "'DRS'", "'LD'", "'ST'", "'MOV'", 
                     "'PSH'", "'POP'", "'SRCF'", "'WLKT'", "'WLKW'", "'WLK'", 
                     "'SRF'", "','", "'('", "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "LD", "ST", "MOV", "PSH", "POP", "SRCF", 
                      "WLKT", "WLKW", "WLK", "SRF", "COMMA", "OPAR", "CPAR", 
                      "OBRACE", "CBRACE", "DIGIT", "NEWLINE", "WS" ]

    RULE_program = 0
    RULE_instr = 1
    RULE_bug_instr = 2
    RULE_val = 3
    RULE_mem = 4
    RULE_address = 5
    RULE_reg = 6
    RULE_wrt_reg = 7
    RULE_gen_reg = 8
    RULE_prt_reg = 9
    RULE_number = 10

    ruleNames =  [ "program", "instr", "bug_instr", "val", "mem", "address", 
                   "reg", "wrt_reg", "gen_reg", "prt_reg", "number" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    LD=9
    ST=10
    MOV=11
    PSH=12
    POP=13
    SRCF=14
    WLKT=15
    WLKW=16
    WLK=17
    SRF=18
    COMMA=19
    OPAR=20
    CPAR=21
    OBRACE=22
    CBRACE=23
    DIGIT=24
    NEWLINE=25
    WS=26

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
            self.state = 27
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 22
                    self.instr()
                    self.state = 23
                    self.match(mvasmParser.NEWLINE) 
                self.state = 29
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 30
            self.instr()
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==mvasmParser.NEWLINE:
                self.state = 31
                self.match(mvasmParser.NEWLINE)
                self.state = 36
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
        def wrt_reg(self):
            return self.getTypedRuleContext(mvasmParser.Wrt_regContext,0)

        def COMMA(self):
            return self.getToken(mvasmParser.COMMA, 0)
        def val(self):
            return self.getTypedRuleContext(mvasmParser.ValContext,0)


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
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mvasmParser.LD]:
                localctx = mvasmParser.InstrLDContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.match(mvasmParser.LD)
                self.state = 38
                self.wrt_reg()
                self.state = 39
                self.match(mvasmParser.COMMA)
                self.state = 40
                self.val()
                pass
            elif token in [mvasmParser.ST]:
                localctx = mvasmParser.InstrSTContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.match(mvasmParser.ST)
                self.state = 43
                self.reg()
                self.state = 44
                self.match(mvasmParser.COMMA)
                self.state = 45
                self.mem()
                pass
            elif token in [mvasmParser.MOV]:
                localctx = mvasmParser.InstrMOVContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 47
                self.match(mvasmParser.MOV)
                self.state = 48
                self.reg()
                self.state = 49
                self.match(mvasmParser.COMMA)
                self.state = 50
                self.reg()
                pass
            elif token in [mvasmParser.PSH]:
                localctx = mvasmParser.InstrPSHContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 52
                self.match(mvasmParser.PSH)
                self.state = 53
                self.reg()
                pass
            elif token in [mvasmParser.POP]:
                localctx = mvasmParser.InstrPOPContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 54
                self.match(mvasmParser.POP)
                self.state = 55
                self.reg()
                pass
            elif token in [mvasmParser.SRCF, mvasmParser.WLKT, mvasmParser.WLKW, mvasmParser.WLK]:
                localctx = mvasmParser.InstrBug_InstrContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 56
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
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mvasmParser.SRCF]:
                localctx = mvasmParser.InstrSRCFContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.match(mvasmParser.SRCF)
                pass
            elif token in [mvasmParser.WLKT]:
                localctx = mvasmParser.InstrWLKTContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.match(mvasmParser.WLKT)
                pass
            elif token in [mvasmParser.WLKW]:
                localctx = mvasmParser.InstrwlkWContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 61
                self.match(mvasmParser.WLKW)
                pass
            elif token in [mvasmParser.WLK]:
                localctx = mvasmParser.InstrWLKContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 62
                self.match(mvasmParser.WLK)
                self.state = 63
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


    class ValContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return mvasmParser.RULE_val

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ValmemContext(ValContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mvasmParser.ValContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def mem(self):
            return self.getTypedRuleContext(mvasmParser.MemContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValmem" ):
                listener.enterValmem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValmem" ):
                listener.exitValmem(self)


    class ValnumberContext(ValContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mvasmParser.ValContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPAR(self):
            return self.getToken(mvasmParser.OPAR, 0)
        def number(self):
            return self.getTypedRuleContext(mvasmParser.NumberContext,0)

        def CPAR(self):
            return self.getToken(mvasmParser.CPAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValnumber" ):
                listener.enterValnumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValnumber" ):
                listener.exitValnumber(self)



    def val(self):

        localctx = mvasmParser.ValContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_val)
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mvasmParser.T__0, mvasmParser.T__1, mvasmParser.T__2, mvasmParser.T__3, mvasmParser.T__4, mvasmParser.T__5, mvasmParser.T__6, mvasmParser.T__7, mvasmParser.SRF, mvasmParser.OBRACE, mvasmParser.DIGIT]:
                localctx = mvasmParser.ValmemContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.mem()
                pass
            elif token in [mvasmParser.OPAR]:
                localctx = mvasmParser.ValnumberContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.match(mvasmParser.OPAR)
                self.state = 68
                self.number()
                self.state = 69
                self.match(mvasmParser.CPAR)
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
        self.enterRule(localctx, 8, self.RULE_mem)
        try:
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mvasmParser.T__0, mvasmParser.T__1, mvasmParser.T__2, mvasmParser.T__3, mvasmParser.T__4, mvasmParser.T__5, mvasmParser.T__6, mvasmParser.T__7, mvasmParser.SRF, mvasmParser.DIGIT]:
                localctx = mvasmParser.MemRelContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.address()
                pass
            elif token in [mvasmParser.OBRACE]:
                localctx = mvasmParser.MemAbsContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.match(mvasmParser.OBRACE)
                self.state = 75
                self.address()
                self.state = 76
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


        def reg(self):
            return self.getTypedRuleContext(mvasmParser.RegContext,0)


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
        self.enterRule(localctx, 10, self.RULE_address)
        try:
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mvasmParser.DIGIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.number()
                pass
            elif token in [mvasmParser.T__0, mvasmParser.T__1, mvasmParser.T__2, mvasmParser.T__3, mvasmParser.T__4, mvasmParser.T__5, mvasmParser.T__6, mvasmParser.T__7, mvasmParser.SRF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
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


    class RegContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def wrt_reg(self):
            return self.getTypedRuleContext(mvasmParser.Wrt_regContext,0)


        def prt_reg(self):
            return self.getTypedRuleContext(mvasmParser.Prt_regContext,0)


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
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mvasmParser.T__0, mvasmParser.SRF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.wrt_reg()
                pass
            elif token in [mvasmParser.T__1, mvasmParser.T__2, mvasmParser.T__3, mvasmParser.T__4, mvasmParser.T__5, mvasmParser.T__6, mvasmParser.T__7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.prt_reg()
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


    class Wrt_regContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def gen_reg(self):
            return self.getTypedRuleContext(mvasmParser.Gen_regContext,0)


        def SRF(self):
            return self.getToken(mvasmParser.SRF, 0)

        def getRuleIndex(self):
            return mvasmParser.RULE_wrt_reg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrt_reg" ):
                listener.enterWrt_reg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrt_reg" ):
                listener.exitWrt_reg(self)




    def wrt_reg(self):

        localctx = mvasmParser.Wrt_regContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_wrt_reg)
        try:
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mvasmParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.gen_reg()
                pass
            elif token in [mvasmParser.SRF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.match(mvasmParser.SRF)
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
        self.enterRule(localctx, 16, self.RULE_gen_reg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(mvasmParser.T__0)
            self.state = 94 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 93
                self.match(mvasmParser.DIGIT)
                self.state = 96 
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


    class Prt_regContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return mvasmParser.RULE_prt_reg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrt_reg" ):
                listener.enterPrt_reg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrt_reg" ):
                listener.exitPrt_reg(self)




    def prt_reg(self):

        localctx = mvasmParser.Prt_regContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_prt_reg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << mvasmParser.T__1) | (1 << mvasmParser.T__2) | (1 << mvasmParser.T__3) | (1 << mvasmParser.T__4) | (1 << mvasmParser.T__5) | (1 << mvasmParser.T__6) | (1 << mvasmParser.T__7))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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
        self.enterRule(localctx, 20, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 100
                self.match(mvasmParser.DIGIT)
                self.state = 103 
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





