# Generated from /home/josh/PycharmProjects/python-p4/grammar/ebnf/MyCMinus.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2%")
        buf.write("\u00d3\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16")
        buf.write("\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3$\7$\u00bb\n$\f$\16")
        buf.write("$\u00be\13$\3%\6%\u00c1\n%\r%\16%\u00c2\3%\3%\6%\u00c7")
        buf.write("\n%\r%\16%\u00c8\5%\u00cb\n%\3&\6&\u00ce\n&\r&\16&\u00cf")
        buf.write("\3&\3&\2\2\'\3\2\5\2\7\3\t\4\13\5\r\6\17\7\21\b\23\t\25")
        buf.write("\n\27\13\31\f\33\r\35\16\37\17!\20#\21%\22\'\23)\24+\25")
        buf.write("-\26/\27\61\30\63\31\65\32\67\339\34;\35=\36?\37A C!E")
        buf.write("\"G#I$K%\3\2\5\3\2\62;\4\2C\\c|\5\2\13\f\17\17\"\"\2\u00d6")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\3M\3\2\2\2\5")
        buf.write("O\3\2\2\2\7Q\3\2\2\2\tT\3\2\2\2\13Y\3\2\2\2\r_\3\2\2\2")
        buf.write("\17e\3\2\2\2\21g\3\2\2\2\23i\3\2\2\2\25k\3\2\2\2\27m\3")
        buf.write("\2\2\2\31o\3\2\2\2\33q\3\2\2\2\35s\3\2\2\2\37u\3\2\2\2")
        buf.write("!w\3\2\2\2#y\3\2\2\2%{\3\2\2\2\'}\3\2\2\2)\177\3\2\2\2")
        buf.write("+\u0082\3\2\2\2-\u0085\3\2\2\2/\u0087\3\2\2\2\61\u008a")
        buf.write("\3\2\2\2\63\u008c\3\2\2\2\65\u008f\3\2\2\2\67\u0091\3")
        buf.write("\2\2\29\u0094\3\2\2\2;\u0097\3\2\2\2=\u009b\3\2\2\2?\u00a1")
        buf.write("\3\2\2\2A\u00a6\3\2\2\2C\u00ad\3\2\2\2E\u00b2\3\2\2\2")
        buf.write("G\u00b7\3\2\2\2I\u00c0\3\2\2\2K\u00cd\3\2\2\2MN\t\2\2")
        buf.write("\2N\4\3\2\2\2OP\t\3\2\2P\6\3\2\2\2QR\7k\2\2RS\7h\2\2S")
        buf.write("\b\3\2\2\2TU\7g\2\2UV\7n\2\2VW\7u\2\2WX\7g\2\2X\n\3\2")
        buf.write("\2\2YZ\7y\2\2Z[\7j\2\2[\\\7k\2\2\\]\7n\2\2]^\7g\2\2^\f")
        buf.write("\3\2\2\2_`\7r\2\2`a\7t\2\2ab\7k\2\2bc\7p\2\2cd\7v\2\2")
        buf.write("d\16\3\2\2\2ef\7*\2\2f\20\3\2\2\2gh\7+\2\2h\22\3\2\2\2")
        buf.write("ij\7}\2\2j\24\3\2\2\2kl\7\177\2\2l\26\3\2\2\2mn\7]\2\2")
        buf.write("n\30\3\2\2\2op\7_\2\2p\32\3\2\2\2qr\7=\2\2r\34\3\2\2\2")
        buf.write("st\7.\2\2t\36\3\2\2\2uv\7-\2\2v \3\2\2\2wx\7/\2\2x\"\3")
        buf.write("\2\2\2yz\7,\2\2z$\3\2\2\2{|\7\61\2\2|&\3\2\2\2}~\7?\2")
        buf.write("\2~(\3\2\2\2\177\u0080\7(\2\2\u0080\u0081\7(\2\2\u0081")
        buf.write("*\3\2\2\2\u0082\u0083\7~\2\2\u0083\u0084\7~\2\2\u0084")
        buf.write(",\3\2\2\2\u0085\u0086\7#\2\2\u0086.\3\2\2\2\u0087\u0088")
        buf.write("\7?\2\2\u0088\u0089\7?\2\2\u0089\60\3\2\2\2\u008a\u008b")
        buf.write("\7@\2\2\u008b\62\3\2\2\2\u008c\u008d\7@\2\2\u008d\u008e")
        buf.write("\7?\2\2\u008e\64\3\2\2\2\u008f\u0090\7>\2\2\u0090\66\3")
        buf.write("\2\2\2\u0091\u0092\7>\2\2\u0092\u0093\7?\2\2\u00938\3")
        buf.write("\2\2\2\u0094\u0095\7#\2\2\u0095\u0096\7?\2\2\u0096:\3")
        buf.write("\2\2\2\u0097\u0098\7k\2\2\u0098\u0099\7p\2\2\u0099\u009a")
        buf.write("\7v\2\2\u009a<\3\2\2\2\u009b\u009c\7h\2\2\u009c\u009d")
        buf.write("\7n\2\2\u009d\u009e\7q\2\2\u009e\u009f\7c\2\2\u009f\u00a0")
        buf.write("\7v\2\2\u00a0>\3\2\2\2\u00a1\u00a2\7x\2\2\u00a2\u00a3")
        buf.write("\7q\2\2\u00a3\u00a4\7k\2\2\u00a4\u00a5\7f\2\2\u00a5@\3")
        buf.write("\2\2\2\u00a6\u00a7\7u\2\2\u00a7\u00a8\7v\2\2\u00a8\u00a9")
        buf.write("\7t\2\2\u00a9\u00aa\7k\2\2\u00aa\u00ab\7p\2\2\u00ab\u00ac")
        buf.write("\7i\2\2\u00acB\3\2\2\2\u00ad\u00ae\7e\2\2\u00ae\u00af")
        buf.write("\7j\2\2\u00af\u00b0\7c\2\2\u00b0\u00b1\7t\2\2\u00b1D\3")
        buf.write("\2\2\2\u00b2\u00b3\7d\2\2\u00b3\u00b4\7q\2\2\u00b4\u00b5")
        buf.write("\7q\2\2\u00b5\u00b6\7n\2\2\u00b6F\3\2\2\2\u00b7\u00bc")
        buf.write("\5\5\3\2\u00b8\u00bb\5\3\2\2\u00b9\u00bb\5\5\3\2\u00ba")
        buf.write("\u00b8\3\2\2\2\u00ba\u00b9\3\2\2\2\u00bb\u00be\3\2\2\2")
        buf.write("\u00bc\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bdH\3\2\2")
        buf.write("\2\u00be\u00bc\3\2\2\2\u00bf\u00c1\5\3\2\2\u00c0\u00bf")
        buf.write("\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c2")
        buf.write("\u00c3\3\2\2\2\u00c3\u00ca\3\2\2\2\u00c4\u00c6\7\60\2")
        buf.write("\2\u00c5\u00c7\5\3\2\2\u00c6\u00c5\3\2\2\2\u00c7\u00c8")
        buf.write("\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9")
        buf.write("\u00cb\3\2\2\2\u00ca\u00c4\3\2\2\2\u00ca\u00cb\3\2\2\2")
        buf.write("\u00cbJ\3\2\2\2\u00cc\u00ce\t\4\2\2\u00cd\u00cc\3\2\2")
        buf.write("\2\u00ce\u00cf\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0")
        buf.write("\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d2\b&\2\2\u00d2")
        buf.write("L\3\2\2\2\t\2\u00ba\u00bc\u00c2\u00c8\u00ca\u00cf\3\b")
        buf.write("\2\2")
        return buf.getvalue()


class MyCMinusLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    ELSE = 2
    WHILE = 3
    PRINT = 4
    LPAR = 5
    RPAR = 6
    LCURL = 7
    RCURL = 8
    LBRAC = 9
    RBRAC = 10
    SEMI = 11
    COMMA = 12
    PLUS = 13
    MINUS = 14
    TIMES = 15
    DIVIDE = 16
    EQUALS = 17
    AND = 18
    OR = 19
    NOT = 20
    EQUALTO = 21
    GTHAN = 22
    GEQUAL = 23
    LTHAN = 24
    LEQUAL = 25
    NOTEQ = 26
    INT = 27
    FLOAT = 28
    VOID = 29
    STRING = 30
    CHAR = 31
    BOOL = 32
    ID = 33
    NUMBER = 34
    WS = 35

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'while'", "'print'", "'('", "')'", "'{'", 
            "'}'", "'['", "']'", "';'", "','", "'+'", "'-'", "'*'", "'/'", 
            "'='", "'&&'", "'||'", "'!'", "'=='", "'>'", "'>='", "'<'", 
            "'<='", "'!='", "'int'", "'float'", "'void'", "'string'", "'char'", 
            "'bool'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "WHILE", "PRINT", "LPAR", "RPAR", "LCURL", "RCURL", 
            "LBRAC", "RBRAC", "SEMI", "COMMA", "PLUS", "MINUS", "TIMES", 
            "DIVIDE", "EQUALS", "AND", "OR", "NOT", "EQUALTO", "GTHAN", 
            "GEQUAL", "LTHAN", "LEQUAL", "NOTEQ", "INT", "FLOAT", "VOID", 
            "STRING", "CHAR", "BOOL", "ID", "NUMBER", "WS" ]

    ruleNames = [ "DIGIT", "LETTER", "IF", "ELSE", "WHILE", "PRINT", "LPAR", 
                  "RPAR", "LCURL", "RCURL", "LBRAC", "RBRAC", "SEMI", "COMMA", 
                  "PLUS", "MINUS", "TIMES", "DIVIDE", "EQUALS", "AND", "OR", 
                  "NOT", "EQUALTO", "GTHAN", "GEQUAL", "LTHAN", "LEQUAL", 
                  "NOTEQ", "INT", "FLOAT", "VOID", "STRING", "CHAR", "BOOL", 
                  "ID", "NUMBER", "WS" ]

    grammarFileName = "MyCMinus.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


