# Generated from /Users/nacho/Documents/python-projects/Bugs-FCM/mvasm.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\23")
        buf.write("X\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21")
        buf.write("\3\21\3\21\5\21P\n\21\3\22\6\22S\n\22\r\22\16\22T\3\22")
        buf.write("\3\22\2\2\23\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23\3\2\5\3\2\62")
        buf.write(";\4\2\f\f\17\17\5\2\f\f\17\17\"\"\2Y\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\3%\3\2\2\2\5\'\3\2\2")
        buf.write("\2\7*\3\2\2\2\t-\3\2\2\2\13\60\3\2\2\2\r\63\3\2\2\2\17")
        buf.write("\66\3\2\2\2\219\3\2\2\2\23<\3\2\2\2\25@\3\2\2\2\27B\3")
        buf.write("\2\2\2\31D\3\2\2\2\33F\3\2\2\2\35H\3\2\2\2\37J\3\2\2\2")
        buf.write("!O\3\2\2\2#R\3\2\2\2%&\7T\2\2&\4\3\2\2\2\'(\7E\2\2()\7")
        buf.write("U\2\2)\6\3\2\2\2*+\7E\2\2+,\7J\2\2,\b\3\2\2\2-.\7F\2\2")
        buf.write("./\7U\2\2/\n\3\2\2\2\60\61\7R\2\2\61\62\7E\2\2\62\f\3")
        buf.write("\2\2\2\63\64\7U\2\2\64\65\7R\2\2\65\16\3\2\2\2\66\67\7")
        buf.write("N\2\2\678\7F\2\28\20\3\2\2\29:\7U\2\2:;\7V\2\2;\22\3\2")
        buf.write("\2\2<=\7O\2\2=>\7Q\2\2>?\7X\2\2?\24\3\2\2\2@A\7.\2\2A")
        buf.write("\26\3\2\2\2BC\7*\2\2C\30\3\2\2\2DE\7+\2\2E\32\3\2\2\2")
        buf.write("FG\7}\2\2G\34\3\2\2\2HI\7\177\2\2I\36\3\2\2\2JK\t\2\2")
        buf.write("\2K \3\2\2\2LM\7\17\2\2MP\7\f\2\2NP\t\3\2\2OL\3\2\2\2")
        buf.write("ON\3\2\2\2P\"\3\2\2\2QS\t\4\2\2RQ\3\2\2\2ST\3\2\2\2TR")
        buf.write("\3\2\2\2TU\3\2\2\2UV\3\2\2\2VW\b\22\2\2W$\3\2\2\2\5\2")
        buf.write("OT\3\b\2\2")
        return buf.getvalue()


class mvasmLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    LD = 7
    ST = 8
    MOV = 9
    COMMA = 10
    OPAR = 11
    CPAR = 12
    OBRACE = 13
    CBRACE = 14
    DIGIT = 15
    NEWLINE = 16
    WS = 17

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'R'", "'CS'", "'CH'", "'DS'", "'PC'", "'SP'", "'LD'", "'ST'", 
            "'MOV'", "','", "'('", "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "LD", "ST", "MOV", "COMMA", "OPAR", "CPAR", "OBRACE", "CBRACE", 
            "DIGIT", "NEWLINE", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "LD", 
                  "ST", "MOV", "COMMA", "OPAR", "CPAR", "OBRACE", "CBRACE", 
                  "DIGIT", "NEWLINE", "WS" ]

    grammarFileName = "mvasm.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


