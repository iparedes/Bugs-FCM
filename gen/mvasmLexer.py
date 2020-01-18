# Generated from /Users/nacho/Documents/python-projects/Bugs-FCM/mvasm.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\25")
        buf.write("d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\23\5\23\\\n\23\3\24\6\24_\n\24\r\24\16\24`\3\24")
        buf.write("\3\24\2\2\25\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25\3")
        buf.write("\2\5\3\2\62;\4\2\f\f\17\17\5\2\f\f\17\17\"\"\2e\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\3)\3\2\2\2\5+\3\2\2\2\7.\3\2\2\2\t\61")
        buf.write("\3\2\2\2\13\64\3\2\2\2\r\67\3\2\2\2\17:\3\2\2\2\21=\3")
        buf.write("\2\2\2\23@\3\2\2\2\25D\3\2\2\2\27H\3\2\2\2\31L\3\2\2\2")
        buf.write("\33N\3\2\2\2\35P\3\2\2\2\37R\3\2\2\2!T\3\2\2\2#V\3\2\2")
        buf.write("\2%[\3\2\2\2\'^\3\2\2\2)*\7T\2\2*\4\3\2\2\2+,\7E\2\2,")
        buf.write("-\7U\2\2-\6\3\2\2\2./\7E\2\2/\60\7J\2\2\60\b\3\2\2\2\61")
        buf.write("\62\7F\2\2\62\63\7U\2\2\63\n\3\2\2\2\64\65\7R\2\2\65\66")
        buf.write("\7E\2\2\66\f\3\2\2\2\678\7U\2\289\7R\2\29\16\3\2\2\2:")
        buf.write(";\7N\2\2;<\7F\2\2<\20\3\2\2\2=>\7U\2\2>?\7V\2\2?\22\3")
        buf.write("\2\2\2@A\7O\2\2AB\7Q\2\2BC\7X\2\2C\24\3\2\2\2DE\7R\2\2")
        buf.write("EF\7U\2\2FG\7J\2\2G\26\3\2\2\2HI\7R\2\2IJ\7Q\2\2JK\7R")
        buf.write("\2\2K\30\3\2\2\2LM\7.\2\2M\32\3\2\2\2NO\7*\2\2O\34\3\2")
        buf.write("\2\2PQ\7+\2\2Q\36\3\2\2\2RS\7}\2\2S \3\2\2\2TU\7\177\2")
        buf.write("\2U\"\3\2\2\2VW\t\2\2\2W$\3\2\2\2XY\7\17\2\2Y\\\7\f\2")
        buf.write("\2Z\\\t\3\2\2[X\3\2\2\2[Z\3\2\2\2\\&\3\2\2\2]_\t\4\2\2")
        buf.write("^]\3\2\2\2_`\3\2\2\2`^\3\2\2\2`a\3\2\2\2ab\3\2\2\2bc\b")
        buf.write("\24\2\2c(\3\2\2\2\5\2[`\3\b\2\2")
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
    PSH = 10
    POP = 11
    COMMA = 12
    OPAR = 13
    CPAR = 14
    OBRACE = 15
    CBRACE = 16
    DIGIT = 17
    NEWLINE = 18
    WS = 19

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'R'", "'CS'", "'CH'", "'DS'", "'PC'", "'SP'", "'LD'", "'ST'", 
            "'MOV'", "'PSH'", "'POP'", "','", "'('", "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "LD", "ST", "MOV", "PSH", "POP", "COMMA", "OPAR", "CPAR", "OBRACE", 
            "CBRACE", "DIGIT", "NEWLINE", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "LD", 
                  "ST", "MOV", "PSH", "POP", "COMMA", "OPAR", "CPAR", "OBRACE", 
                  "CBRACE", "DIGIT", "NEWLINE", "WS" ]

    grammarFileName = "mvasm.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


