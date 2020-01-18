# Generated from /Users/nacho/Documents/python-projects/Bugs-FCM/mvasm.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23")
        buf.write("O\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\7\2\24\n\2\f\2\16\2\27\13\2\3\2\3\2\7")
        buf.write("\2\33\n\2\f\2\16\2\36\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3/\n\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\5\4\66\n\4\3\5\3\5\5\5:\n\5\3\6\3\6\6\6>\n\6")
        buf.write("\r\6\16\6?\3\7\3\7\3\7\3\7\3\7\3\7\5\7H\n\7\3\b\6\bK\n")
        buf.write("\b\r\b\16\bL\3\b\2\2\t\2\4\6\b\n\f\16\2\2\2T\2\25\3\2")
        buf.write("\2\2\4.\3\2\2\2\6\65\3\2\2\2\b9\3\2\2\2\n;\3\2\2\2\fG")
        buf.write("\3\2\2\2\16J\3\2\2\2\20\21\5\4\3\2\21\22\7\22\2\2\22\24")
        buf.write("\3\2\2\2\23\20\3\2\2\2\24\27\3\2\2\2\25\23\3\2\2\2\25")
        buf.write("\26\3\2\2\2\26\30\3\2\2\2\27\25\3\2\2\2\30\34\5\4\3\2")
        buf.write("\31\33\7\22\2\2\32\31\3\2\2\2\33\36\3\2\2\2\34\32\3\2")
        buf.write("\2\2\34\35\3\2\2\2\35\3\3\2\2\2\36\34\3\2\2\2\37 \7\t")
        buf.write("\2\2 !\5\f\7\2!\"\7\f\2\2\"#\5\6\4\2#/\3\2\2\2$%\7\n\2")
        buf.write("\2%&\5\f\7\2&\'\7\f\2\2\'(\5\6\4\2(/\3\2\2\2)*\7\13\2")
        buf.write("\2*+\5\f\7\2+,\7\f\2\2,-\5\f\7\2-/\3\2\2\2.\37\3\2\2\2")
        buf.write(".$\3\2\2\2.)\3\2\2\2/\5\3\2\2\2\60\66\5\b\5\2\61\62\7")
        buf.write("\17\2\2\62\63\5\b\5\2\63\64\7\20\2\2\64\66\3\2\2\2\65")
        buf.write("\60\3\2\2\2\65\61\3\2\2\2\66\7\3\2\2\2\67:\5\16\b\28:")
        buf.write("\5\n\6\29\67\3\2\2\298\3\2\2\2:\t\3\2\2\2;=\7\3\2\2<>")
        buf.write("\7\21\2\2=<\3\2\2\2>?\3\2\2\2?=\3\2\2\2?@\3\2\2\2@\13")
        buf.write("\3\2\2\2AH\5\n\6\2BH\7\4\2\2CH\7\5\2\2DH\7\6\2\2EH\7\7")
        buf.write("\2\2FH\7\b\2\2GA\3\2\2\2GB\3\2\2\2GC\3\2\2\2GD\3\2\2\2")
        buf.write("GE\3\2\2\2GF\3\2\2\2H\r\3\2\2\2IK\7\21\2\2JI\3\2\2\2K")
        buf.write("L\3\2\2\2LJ\3\2\2\2LM\3\2\2\2M\17\3\2\2\2\n\25\34.\65")
        buf.write("9?GL")
        return buf.getvalue()


class mvasmParser ( Parser ):

    grammarFileName = "mvasm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'R'", "'CS'", "'CH'", "'DS'", "'PC'", 
                     "'SP'", "'LD'", "'ST'", "'MOV'", "','", "'('", "')'", 
                     "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "LD", "ST", 
                      "MOV", "COMMA", "OPAR", "CPAR", "OBRACE", "CBRACE", 
                      "DIGIT", "NEWLINE", "WS" ]

    RULE_program = 0
    RULE_instr = 1
    RULE_mem = 2
    RULE_address = 3
    RULE_gen_reg = 4
    RULE_reg = 5
    RULE_number = 6

    ruleNames =  [ "program", "instr", "mem", "address", "gen_reg", "reg", 
                   "number" ]

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
    COMMA=10
    OPAR=11
    CPAR=12
    OBRACE=13
    CBRACE=14
    DIGIT=15
    NEWLINE=16
    WS=17

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
            self.state = 19
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 14
                    self.instr()
                    self.state = 15
                    self.match(mvasmParser.NEWLINE) 
                self.state = 21
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 22
            self.instr()
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==mvasmParser.NEWLINE:
                self.state = 23
                self.match(mvasmParser.NEWLINE)
                self.state = 28
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



    def instr(self):

        localctx = mvasmParser.InstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instr)
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mvasmParser.LD]:
                localctx = mvasmParser.InstrLDContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.match(mvasmParser.LD)
                self.state = 30
                self.reg()
                self.state = 31
                self.match(mvasmParser.COMMA)
                self.state = 32
                self.mem()
                pass
            elif token in [mvasmParser.ST]:
                localctx = mvasmParser.InstrSTContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.match(mvasmParser.ST)
                self.state = 35
                self.reg()
                self.state = 36
                self.match(mvasmParser.COMMA)
                self.state = 37
                self.mem()
                pass
            elif token in [mvasmParser.MOV]:
                localctx = mvasmParser.InstrMOVContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.match(mvasmParser.MOV)
                self.state = 40
                self.reg()
                self.state = 41
                self.match(mvasmParser.COMMA)
                self.state = 42
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
        self.enterRule(localctx, 4, self.RULE_mem)
        try:
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mvasmParser.T__0, mvasmParser.DIGIT]:
                localctx = mvasmParser.MemRelContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.address()
                pass
            elif token in [mvasmParser.OBRACE]:
                localctx = mvasmParser.MemAbsContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.match(mvasmParser.OBRACE)
                self.state = 48
                self.address()
                self.state = 49
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
        self.enterRule(localctx, 6, self.RULE_address)
        try:
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mvasmParser.DIGIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.number()
                pass
            elif token in [mvasmParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
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
        self.enterRule(localctx, 8, self.RULE_gen_reg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(mvasmParser.T__0)
            self.state = 59 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 58
                self.match(mvasmParser.DIGIT)
                self.state = 61 
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
        self.enterRule(localctx, 10, self.RULE_reg)
        try:
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mvasmParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.gen_reg()
                pass
            elif token in [mvasmParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.match(mvasmParser.T__1)
                pass
            elif token in [mvasmParser.T__2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.match(mvasmParser.T__2)
                pass
            elif token in [mvasmParser.T__3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 66
                self.match(mvasmParser.T__3)
                pass
            elif token in [mvasmParser.T__4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 67
                self.match(mvasmParser.T__4)
                pass
            elif token in [mvasmParser.T__5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 68
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
        self.enterRule(localctx, 12, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 71
                self.match(mvasmParser.DIGIT)
                self.state = 74 
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





