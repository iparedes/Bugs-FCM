# Generated from /Users/nacho/Documents/python-projects/Bugs-FCM/mvasm.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3)")
        buf.write("m\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\7\2\32\n\2")
        buf.write("\f\2\16\2\35\13\2\3\2\3\2\7\2!\n\2\f\2\16\2$\13\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\5\3H\n\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\5\4O\n\4\3\5\3\5\3\5\3\5\3\5\5\5V\n\5\3\6\3\6\5\6Z\n")
        buf.write("\6\3\7\3\7\5\7^\n\7\3\b\3\b\3\t\3\t\5\td\n\t\3\n\3\n\3")
        buf.write("\13\6\13i\n\13\r\13\16\13j\3\13\2\2\f\2\4\6\b\n\f\16\20")
        buf.write("\22\24\2\4\3\2\3\13\3\2\r\23\2v\2\33\3\2\2\2\4G\3\2\2")
        buf.write("\2\6N\3\2\2\2\bU\3\2\2\2\nY\3\2\2\2\f]\3\2\2\2\16_\3\2")
        buf.write("\2\2\20c\3\2\2\2\22e\3\2\2\2\24h\3\2\2\2\26\27\5\4\3\2")
        buf.write("\27\30\7\'\2\2\30\32\3\2\2\2\31\26\3\2\2\2\32\35\3\2\2")
        buf.write("\2\33\31\3\2\2\2\33\34\3\2\2\2\34\36\3\2\2\2\35\33\3\2")
        buf.write("\2\2\36\"\5\4\3\2\37!\7\'\2\2 \37\3\2\2\2!$\3\2\2\2\"")
        buf.write(" \3\2\2\2\"#\3\2\2\2#\3\3\2\2\2$\"\3\2\2\2%&\7\27\2\2")
        buf.write("&\'\5\20\t\2\'(\7 \2\2()\5\6\4\2)H\3\2\2\2*+\7\34\2\2")
        buf.write("+,\5\f\7\2,-\7 \2\2-.\5\b\5\2.H\3\2\2\2/\60\7\30\2\2\60")
        buf.write("\61\5\f\7\2\61\62\7 \2\2\62\63\5\f\7\2\63H\3\2\2\2\64")
        buf.write("\65\7\24\2\2\65\66\5\20\t\2\66\67\7 \2\2\678\5\f\7\28")
        buf.write("H\3\2\2\29:\7\32\2\2:H\5\f\7\2;<\7\31\2\2<H\5\f\7\2=>")
        buf.write("\7\26\2\2>H\7(\2\2?H\7\33\2\2@H\7\36\2\2AH\7\37\2\2BC")
        buf.write("\7\35\2\2CH\5\f\7\2DH\7\25\2\2EF\7(\2\2FH\7%\2\2G%\3\2")
        buf.write("\2\2G*\3\2\2\2G/\3\2\2\2G\64\3\2\2\2G9\3\2\2\2G;\3\2\2")
        buf.write("\2G=\3\2\2\2G?\3\2\2\2G@\3\2\2\2GA\3\2\2\2GB\3\2\2\2G")
        buf.write("D\3\2\2\2GE\3\2\2\2H\5\3\2\2\2IO\5\b\5\2JK\7!\2\2KL\5")
        buf.write("\24\13\2LM\7\"\2\2MO\3\2\2\2NI\3\2\2\2NJ\3\2\2\2O\7\3")
        buf.write("\2\2\2PV\5\n\6\2QR\7#\2\2RS\5\n\6\2ST\7$\2\2TV\3\2\2\2")
        buf.write("UP\3\2\2\2UQ\3\2\2\2V\t\3\2\2\2WZ\5\24\13\2XZ\5\f\7\2")
        buf.write("YW\3\2\2\2YX\3\2\2\2Z\13\3\2\2\2[^\5\20\t\2\\^\5\22\n")
        buf.write("\2][\3\2\2\2]\\\3\2\2\2^\r\3\2\2\2_`\t\2\2\2`\17\3\2\2")
        buf.write("\2ad\5\16\b\2bd\7\f\2\2ca\3\2\2\2cb\3\2\2\2d\21\3\2\2")
        buf.write("\2ef\t\3\2\2f\23\3\2\2\2gi\7&\2\2hg\3\2\2\2ij\3\2\2\2")
        buf.write("jh\3\2\2\2jk\3\2\2\2k\25\3\2\2\2\13\33\"GNUY]cj")
        return buf.getvalue()


class mvasmParser ( Parser ):

    grammarFileName = "mvasm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'R1'", "'R2'", "'R3'", "'R4'", "'R5'", 
                     "'R6'", "'R7'", "'R8'", "'R9'", "'SRF'", "'CS'", "'CH'", 
                     "'DS'", "'PC'", "'SP'", "'SRR'", "'DRS'", "'ADD'", 
                     "'END'", "'JMP'", "'LD'", "'MOV'", "'POP'", "'PSH'", 
                     "'SRCF'", "'ST'", "'WLK'", "'WLKT'", "'WLKW'", "','", 
                     "'('", "')'", "'{'", "'}'", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ADD", "END", "JMP", "LD", 
                      "MOV", "POP", "PSH", "SRCF", "ST", "WLK", "WLKT", 
                      "WLKW", "COMMA", "OPAR", "CPAR", "OBRACE", "CBRACE", 
                      "COLON", "DIGIT", "NEWLINE", "VARIABLE", "WS" ]

    RULE_program = 0
    RULE_instr = 1
    RULE_val = 2
    RULE_mem = 3
    RULE_address = 4
    RULE_reg = 5
    RULE_gen_reg = 6
    RULE_wrt_reg = 7
    RULE_prt_reg = 8
    RULE_number = 9

    ruleNames =  [ "program", "instr", "val", "mem", "address", "reg", "gen_reg", 
                   "wrt_reg", "prt_reg", "number" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    ADD=18
    END=19
    JMP=20
    LD=21
    MOV=22
    POP=23
    PSH=24
    SRCF=25
    ST=26
    WLK=27
    WLKT=28
    WLKW=29
    COMMA=30
    OPAR=31
    CPAR=32
    OBRACE=33
    CBRACE=34
    COLON=35
    DIGIT=36
    NEWLINE=37
    VARIABLE=38
    WS=39

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
            self.state = 25
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 20
                    self.instr()
                    self.state = 21
                    self.match(mvasmParser.NEWLINE) 
                self.state = 27
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 28
            self.instr()
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==mvasmParser.NEWLINE:
                self.state = 29
                self.match(mvasmParser.NEWLINE)
                self.state = 34
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



    class InstrwlkWContext(InstrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mvasmParser.InstrContext
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


    class InstrADDContext(InstrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mvasmParser.InstrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ADD(self):
            return self.getToken(mvasmParser.ADD, 0)
        def wrt_reg(self):
            return self.getTypedRuleContext(mvasmParser.Wrt_regContext,0)

        def COMMA(self):
            return self.getToken(mvasmParser.COMMA, 0)
        def reg(self):
            return self.getTypedRuleContext(mvasmParser.RegContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrADD" ):
                listener.enterInstrADD(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrADD" ):
                listener.exitInstrADD(self)


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


    class InstrWLKTContext(InstrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mvasmParser.InstrContext
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


    class InstrLabelContext(InstrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mvasmParser.InstrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(mvasmParser.VARIABLE, 0)
        def COLON(self):
            return self.getToken(mvasmParser.COLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrLabel" ):
                listener.enterInstrLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrLabel" ):
                listener.exitInstrLabel(self)


    class InstrSRCFContext(InstrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mvasmParser.InstrContext
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


    class InstrEndContext(InstrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mvasmParser.InstrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def END(self):
            return self.getToken(mvasmParser.END, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrEnd" ):
                listener.enterInstrEnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrEnd" ):
                listener.exitInstrEnd(self)


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


    class InstrWLKContext(InstrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mvasmParser.InstrContext
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


    class InstrJMPContext(InstrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mvasmParser.InstrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def JMP(self):
            return self.getToken(mvasmParser.JMP, 0)
        def VARIABLE(self):
            return self.getToken(mvasmParser.VARIABLE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrJMP" ):
                listener.enterInstrJMP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrJMP" ):
                listener.exitInstrJMP(self)



    def instr(self):

        localctx = mvasmParser.InstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instr)
        try:
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mvasmParser.LD]:
                localctx = mvasmParser.InstrLDContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.match(mvasmParser.LD)
                self.state = 36
                self.wrt_reg()
                self.state = 37
                self.match(mvasmParser.COMMA)
                self.state = 38
                self.val()
                pass
            elif token in [mvasmParser.ST]:
                localctx = mvasmParser.InstrSTContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.match(mvasmParser.ST)
                self.state = 41
                self.reg()
                self.state = 42
                self.match(mvasmParser.COMMA)
                self.state = 43
                self.mem()
                pass
            elif token in [mvasmParser.MOV]:
                localctx = mvasmParser.InstrMOVContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                self.match(mvasmParser.MOV)
                self.state = 46
                self.reg()
                self.state = 47
                self.match(mvasmParser.COMMA)
                self.state = 48
                self.reg()
                pass
            elif token in [mvasmParser.ADD]:
                localctx = mvasmParser.InstrADDContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 50
                self.match(mvasmParser.ADD)
                self.state = 51
                self.wrt_reg()
                self.state = 52
                self.match(mvasmParser.COMMA)
                self.state = 53
                self.reg()
                pass
            elif token in [mvasmParser.PSH]:
                localctx = mvasmParser.InstrPSHContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 55
                self.match(mvasmParser.PSH)
                self.state = 56
                self.reg()
                pass
            elif token in [mvasmParser.POP]:
                localctx = mvasmParser.InstrPOPContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 57
                self.match(mvasmParser.POP)
                self.state = 58
                self.reg()
                pass
            elif token in [mvasmParser.JMP]:
                localctx = mvasmParser.InstrJMPContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 59
                self.match(mvasmParser.JMP)
                self.state = 60
                self.match(mvasmParser.VARIABLE)
                pass
            elif token in [mvasmParser.SRCF]:
                localctx = mvasmParser.InstrSRCFContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 61
                self.match(mvasmParser.SRCF)
                pass
            elif token in [mvasmParser.WLKT]:
                localctx = mvasmParser.InstrWLKTContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 62
                self.match(mvasmParser.WLKT)
                pass
            elif token in [mvasmParser.WLKW]:
                localctx = mvasmParser.InstrwlkWContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 63
                self.match(mvasmParser.WLKW)
                pass
            elif token in [mvasmParser.WLK]:
                localctx = mvasmParser.InstrWLKContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 64
                self.match(mvasmParser.WLK)
                self.state = 65
                self.reg()
                pass
            elif token in [mvasmParser.END]:
                localctx = mvasmParser.InstrEndContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 66
                self.match(mvasmParser.END)
                pass
            elif token in [mvasmParser.VARIABLE]:
                localctx = mvasmParser.InstrLabelContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 67
                self.match(mvasmParser.VARIABLE)
                self.state = 68
                self.match(mvasmParser.COLON)
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
        self.enterRule(localctx, 4, self.RULE_val)
        try:
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mvasmParser.T__0, mvasmParser.T__1, mvasmParser.T__2, mvasmParser.T__3, mvasmParser.T__4, mvasmParser.T__5, mvasmParser.T__6, mvasmParser.T__7, mvasmParser.T__8, mvasmParser.T__9, mvasmParser.T__10, mvasmParser.T__11, mvasmParser.T__12, mvasmParser.T__13, mvasmParser.T__14, mvasmParser.T__15, mvasmParser.T__16, mvasmParser.OBRACE, mvasmParser.DIGIT]:
                localctx = mvasmParser.ValmemContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.mem()
                pass
            elif token in [mvasmParser.OPAR]:
                localctx = mvasmParser.ValnumberContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.match(mvasmParser.OPAR)
                self.state = 73
                self.number()
                self.state = 74
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
        self.enterRule(localctx, 6, self.RULE_mem)
        try:
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mvasmParser.T__0, mvasmParser.T__1, mvasmParser.T__2, mvasmParser.T__3, mvasmParser.T__4, mvasmParser.T__5, mvasmParser.T__6, mvasmParser.T__7, mvasmParser.T__8, mvasmParser.T__9, mvasmParser.T__10, mvasmParser.T__11, mvasmParser.T__12, mvasmParser.T__13, mvasmParser.T__14, mvasmParser.T__15, mvasmParser.T__16, mvasmParser.DIGIT]:
                localctx = mvasmParser.MemRelContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.address()
                pass
            elif token in [mvasmParser.OBRACE]:
                localctx = mvasmParser.MemAbsContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.match(mvasmParser.OBRACE)
                self.state = 80
                self.address()
                self.state = 81
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
        self.enterRule(localctx, 8, self.RULE_address)
        try:
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mvasmParser.DIGIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.number()
                pass
            elif token in [mvasmParser.T__0, mvasmParser.T__1, mvasmParser.T__2, mvasmParser.T__3, mvasmParser.T__4, mvasmParser.T__5, mvasmParser.T__6, mvasmParser.T__7, mvasmParser.T__8, mvasmParser.T__9, mvasmParser.T__10, mvasmParser.T__11, mvasmParser.T__12, mvasmParser.T__13, mvasmParser.T__14, mvasmParser.T__15, mvasmParser.T__16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
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
        self.enterRule(localctx, 10, self.RULE_reg)
        try:
            self.state = 91
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mvasmParser.T__0, mvasmParser.T__1, mvasmParser.T__2, mvasmParser.T__3, mvasmParser.T__4, mvasmParser.T__5, mvasmParser.T__6, mvasmParser.T__7, mvasmParser.T__8, mvasmParser.T__9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.wrt_reg()
                pass
            elif token in [mvasmParser.T__10, mvasmParser.T__11, mvasmParser.T__12, mvasmParser.T__13, mvasmParser.T__14, mvasmParser.T__15, mvasmParser.T__16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
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


    class Gen_regContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


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
        self.enterRule(localctx, 12, self.RULE_gen_reg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << mvasmParser.T__0) | (1 << mvasmParser.T__1) | (1 << mvasmParser.T__2) | (1 << mvasmParser.T__3) | (1 << mvasmParser.T__4) | (1 << mvasmParser.T__5) | (1 << mvasmParser.T__6) | (1 << mvasmParser.T__7) | (1 << mvasmParser.T__8))) != 0)):
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


    class Wrt_regContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def gen_reg(self):
            return self.getTypedRuleContext(mvasmParser.Gen_regContext,0)


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
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mvasmParser.T__0, mvasmParser.T__1, mvasmParser.T__2, mvasmParser.T__3, mvasmParser.T__4, mvasmParser.T__5, mvasmParser.T__6, mvasmParser.T__7, mvasmParser.T__8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.gen_reg()
                pass
            elif token in [mvasmParser.T__9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.match(mvasmParser.T__9)
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
        self.enterRule(localctx, 16, self.RULE_prt_reg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << mvasmParser.T__10) | (1 << mvasmParser.T__11) | (1 << mvasmParser.T__12) | (1 << mvasmParser.T__13) | (1 << mvasmParser.T__14) | (1 << mvasmParser.T__15) | (1 << mvasmParser.T__16))) != 0)):
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
        self.enterRule(localctx, 18, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 101
                self.match(mvasmParser.DIGIT)
                self.state = 104 
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





