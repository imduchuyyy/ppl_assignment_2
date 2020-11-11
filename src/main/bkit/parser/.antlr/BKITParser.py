# Generated from /home/duchuy/Documents/bachkhoa/PPL/Assignment/ass2/initial/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
        buf.write("\u01d1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\5\3`\n\3\3\4\3\4\5\4d\n\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\6\5\6p\n\6\3\7\3\7\5\7t\n\7\3")
        buf.write("\7\3\7\5\7x\n\7\3\b\3\b\3\b\3\b\5\b~\n\b\3\t\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\5\13\u008c\n\13")
        buf.write("\3\f\3\f\5\f\u0090\n\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\5\17\u00a1\n\17")
        buf.write("\3\20\3\20\3\20\5\20\u00a6\n\20\3\20\3\20\3\20\3\20\3")
        buf.write("\21\3\21\3\21\3\21\5\21\u00b0\n\21\3\22\3\22\5\22\u00b4")
        buf.write("\n\22\3\23\3\23\3\23\3\23\5\23\u00ba\n\23\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u00c5\n\24\3\25")
        buf.write("\3\25\5\25\u00c9\n\25\3\25\3\25\3\25\3\25\3\26\3\26\5")
        buf.write("\26\u00d1\n\26\3\26\5\26\u00d4\n\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\5\27\u00dd\n\27\3\27\5\27\u00e0\n\27\3")
        buf.write("\30\3\30\3\30\3\30\5\30\u00e6\n\30\3\31\3\31\3\31\3\31")
        buf.write("\5\31\u00ec\n\31\3\31\5\31\u00ef\n\31\3\32\3\32\5\32\u00f3")
        buf.write("\n\32\3\32\5\32\u00f6\n\32\3\33\3\33\3\33\3\33\3\33\3")
        buf.write("\33\5\33\u00fe\n\33\3\33\5\33\u0101\n\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\5\34\u0111\n\34\3\35\3\35\3\35\3\35\5\35\u0117\n\35\3")
        buf.write("\35\5\35\u011a\n\35\3\35\3\35\3\35\3\36\3\36\5\36\u0121")
        buf.write("\n\36\3\36\5\36\u0124\n\36\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\37\3\37\3\37\3 \3 \3 \3!\3!\3!\5!\u0134\n!\3!\3!\7!\u0138")
        buf.write("\n!\f!\16!\u013b\13!\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\5#\u0171\n#\3$\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\7$\u017c\n$\f$\16$\u017f\13$\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3%\3%\3%\7%\u0190\n%\f%\16%\u0193\13")
        buf.write("%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\7&\u01a7\n&\f&\16&\u01aa\13&\3\'\3\'\3\'\5\'\u01af\n")
        buf.write("\'\3(\3(\3(\3(\3(\3(\5(\u01b7\n(\3)\3)\3)\3)\3*\3*\3*")
        buf.write("\5*\u01c0\n*\3*\3*\3+\3+\3+\7+\u01c7\n+\f+\16+\u01ca\13")
        buf.write("+\3,\3,\3,\3,\3,\3,\2\5FHJ-\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTV\2\3")
        buf.write("\3\2\26\27\2\u01ee\2X\3\2\2\2\4_\3\2\2\2\6c\3\2\2\2\b")
        buf.write("e\3\2\2\2\no\3\2\2\2\fq\3\2\2\2\16}\3\2\2\2\20\177\3\2")
        buf.write("\2\2\22\u0083\3\2\2\2\24\u008b\3\2\2\2\26\u008d\3\2\2")
        buf.write("\2\30\u0093\3\2\2\2\32\u0097\3\2\2\2\34\u00a0\3\2\2\2")
        buf.write("\36\u00a2\3\2\2\2 \u00af\3\2\2\2\"\u00b3\3\2\2\2$\u00b9")
        buf.write("\3\2\2\2&\u00c4\3\2\2\2(\u00c8\3\2\2\2*\u00ce\3\2\2\2")
        buf.write(",\u00d8\3\2\2\2.\u00e5\3\2\2\2\60\u00e7\3\2\2\2\62\u00f0")
        buf.write("\3\2\2\2\64\u00f7\3\2\2\2\66\u0105\3\2\2\28\u0112\3\2")
        buf.write("\2\2:\u011e\3\2\2\2<\u012a\3\2\2\2>\u012d\3\2\2\2@\u0130")
        buf.write("\3\2\2\2B\u013f\3\2\2\2D\u0170\3\2\2\2F\u0172\3\2\2\2")
        buf.write("H\u0180\3\2\2\2J\u0194\3\2\2\2L\u01ae\3\2\2\2N\u01b6\3")
        buf.write("\2\2\2P\u01b8\3\2\2\2R\u01bc\3\2\2\2T\u01c3\3\2\2\2V\u01cb")
        buf.write("\3\2\2\2XY\5\4\3\2YZ\7\2\2\3Z\3\3\2\2\2[\\\5\6\4\2\\]")
        buf.write("\5\4\3\2]`\3\2\2\2^`\5\6\4\2_[\3\2\2\2_^\3\2\2\2`\5\3")
        buf.write("\2\2\2ad\5\b\5\2bd\5\26\f\2ca\3\2\2\2cb\3\2\2\2d\7\3\2")
        buf.write("\2\2ef\7\24\2\2fg\7\65\2\2gh\5\n\6\2hi\78\2\2i\t\3\2\2")
        buf.write("\2jk\5\f\7\2kl\7\67\2\2lm\5\n\6\2mp\3\2\2\2np\5\f\7\2")
        buf.write("oj\3\2\2\2on\3\2\2\2p\13\3\2\2\2qs\7\3\2\2rt\5\16\b\2")
        buf.write("sr\3\2\2\2st\3\2\2\2tw\3\2\2\2uv\7\31\2\2vx\5\24\13\2")
        buf.write("wu\3\2\2\2wx\3\2\2\2x\r\3\2\2\2yz\5\20\t\2z{\5\16\b\2")
        buf.write("{~\3\2\2\2|~\5\20\t\2}y\3\2\2\2}|\3\2\2\2~\17\3\2\2\2")
        buf.write("\177\u0080\7\63\2\2\u0080\u0081\7;\2\2\u0081\u0082\7\64")
        buf.write("\2\2\u0082\21\3\2\2\2\u0083\u0084\7\3\2\2\u0084\u0085")
        buf.write("\5\16\b\2\u0085\23\3\2\2\2\u0086\u008c\7;\2\2\u0087\u008c")
        buf.write("\7<\2\2\u0088\u008c\t\2\2\2\u0089\u008c\7=\2\2\u008a\u008c")
        buf.write("\5\22\n\2\u008b\u0086\3\2\2\2\u008b\u0087\3\2\2\2\u008b")
        buf.write("\u0088\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008a\3\2\2\2")
        buf.write("\u008c\25\3\2\2\2\u008d\u008f\5\30\r\2\u008e\u0090\5\32")
        buf.write("\16\2\u008f\u008e\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u0091")
        buf.write("\3\2\2\2\u0091\u0092\5\36\20\2\u0092\27\3\2\2\2\u0093")
        buf.write("\u0094\7\17\2\2\u0094\u0095\7\65\2\2\u0095\u0096\7\3\2")
        buf.write("\2\u0096\31\3\2\2\2\u0097\u0098\7\21\2\2\u0098\u0099\7")
        buf.write("\65\2\2\u0099\u009a\5\34\17\2\u009a\33\3\2\2\2\u009b\u009c")
        buf.write("\5\"\22\2\u009c\u009d\7\67\2\2\u009d\u009e\5\34\17\2\u009e")
        buf.write("\u00a1\3\2\2\2\u009f\u00a1\5\"\22\2\u00a0\u009b\3\2\2")
        buf.write("\2\u00a0\u009f\3\2\2\2\u00a1\35\3\2\2\2\u00a2\u00a3\7")
        buf.write("\4\2\2\u00a3\u00a5\7\65\2\2\u00a4\u00a6\5$\23\2\u00a5")
        buf.write("\u00a4\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a7\3\2\2\2")
        buf.write("\u00a7\u00a8\5 \21\2\u00a8\u00a9\7\n\2\2\u00a9\u00aa\7")
        buf.write("\66\2\2\u00aa\37\3\2\2\2\u00ab\u00ac\5&\24\2\u00ac\u00ad")
        buf.write("\5 \21\2\u00ad\u00b0\3\2\2\2\u00ae\u00b0\5&\24\2\u00af")
        buf.write("\u00ab\3\2\2\2\u00af\u00ae\3\2\2\2\u00b0!\3\2\2\2\u00b1")
        buf.write("\u00b4\7\3\2\2\u00b2\u00b4\5\22\n\2\u00b3\u00b1\3\2\2")
        buf.write("\2\u00b3\u00b2\3\2\2\2\u00b4#\3\2\2\2\u00b5\u00b6\5\b")
        buf.write("\5\2\u00b6\u00b7\5$\23\2\u00b7\u00ba\3\2\2\2\u00b8\u00ba")
        buf.write("\5\b\5\2\u00b9\u00b5\3\2\2\2\u00b9\u00b8\3\2\2\2\u00ba")
        buf.write("%\3\2\2\2\u00bb\u00c5\5(\25\2\u00bc\u00c5\5*\26\2\u00bd")
        buf.write("\u00c5\5\64\33\2\u00be\u00c5\58\35\2\u00bf\u00c5\5:\36")
        buf.write("\2\u00c0\u00c5\5<\37\2\u00c1\u00c5\5> \2\u00c2\u00c5\5")
        buf.write("@!\2\u00c3\u00c5\5B\"\2\u00c4\u00bb\3\2\2\2\u00c4\u00bc")
        buf.write("\3\2\2\2\u00c4\u00bd\3\2\2\2\u00c4\u00be\3\2\2\2\u00c4")
        buf.write("\u00bf\3\2\2\2\u00c4\u00c0\3\2\2\2\u00c4\u00c1\3\2\2\2")
        buf.write("\u00c4\u00c2\3\2\2\2\u00c4\u00c3\3\2\2\2\u00c5\'\3\2\2")
        buf.write("\2\u00c6\u00c9\7\3\2\2\u00c7\u00c9\5\22\n\2\u00c8\u00c6")
        buf.write("\3\2\2\2\u00c8\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca")
        buf.write("\u00cb\7\31\2\2\u00cb\u00cc\5D#\2\u00cc\u00cd\78\2\2\u00cd")
        buf.write(")\3\2\2\2\u00ce\u00d0\5,\27\2\u00cf\u00d1\5.\30\2\u00d0")
        buf.write("\u00cf\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d3\3\2\2\2")
        buf.write("\u00d2\u00d4\5\62\32\2\u00d3\u00d2\3\2\2\2\u00d3\u00d4")
        buf.write("\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\u00d6\7\13\2\2\u00d6")
        buf.write("\u00d7\7\66\2\2\u00d7+\3\2\2\2\u00d8\u00d9\7\20\2\2\u00d9")
        buf.write("\u00da\5D#\2\u00da\u00dc\7\23\2\2\u00db\u00dd\5$\23\2")
        buf.write("\u00dc\u00db\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00df\3")
        buf.write("\2\2\2\u00de\u00e0\5 \21\2\u00df\u00de\3\2\2\2\u00df\u00e0")
        buf.write("\3\2\2\2\u00e0-\3\2\2\2\u00e1\u00e2\5\60\31\2\u00e2\u00e3")
        buf.write("\5.\30\2\u00e3\u00e6\3\2\2\2\u00e4\u00e6\5\60\31\2\u00e5")
        buf.write("\u00e1\3\2\2\2\u00e5\u00e4\3\2\2\2\u00e6/\3\2\2\2\u00e7")
        buf.write("\u00e8\7\t\2\2\u00e8\u00e9\5D#\2\u00e9\u00eb\7\23\2\2")
        buf.write("\u00ea\u00ec\5$\23\2\u00eb\u00ea\3\2\2\2\u00eb\u00ec\3")
        buf.write("\2\2\2\u00ec\u00ee\3\2\2\2\u00ed\u00ef\5 \21\2\u00ee\u00ed")
        buf.write("\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\61\3\2\2\2\u00f0\u00f2")
        buf.write("\7\b\2\2\u00f1\u00f3\5$\23\2\u00f2\u00f1\3\2\2\2\u00f2")
        buf.write("\u00f3\3\2\2\2\u00f3\u00f5\3\2\2\2\u00f4\u00f6\5 \21\2")
        buf.write("\u00f5\u00f4\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\63\3\2")
        buf.write("\2\2\u00f7\u00f8\7\16\2\2\u00f8\u00f9\7\61\2\2\u00f9\u00fa")
        buf.write("\5\66\34\2\u00fa\u00fb\7\62\2\2\u00fb\u00fd\7\7\2\2\u00fc")
        buf.write("\u00fe\5$\23\2\u00fd\u00fc\3\2\2\2\u00fd\u00fe\3\2\2\2")
        buf.write("\u00fe\u0100\3\2\2\2\u00ff\u0101\5 \21\2\u0100\u00ff\3")
        buf.write("\2\2\2\u0100\u0101\3\2\2\2\u0101\u0102\3\2\2\2\u0102\u0103")
        buf.write("\7\f\2\2\u0103\u0104\7\66\2\2\u0104\65\3\2\2\2\u0105\u0106")
        buf.write("\7\3\2\2\u0106\u0107\7\31\2\2\u0107\u0108\5D#\2\u0108")
        buf.write("\u0109\3\2\2\2\u0109\u010a\7\67\2\2\u010a\u010b\5D#\2")
        buf.write("\u010b\u0110\7\67\2\2\u010c\u010d\7\3\2\2\u010d\u010e")
        buf.write("\7\31\2\2\u010e\u0111\5D#\2\u010f\u0111\5D#\2\u0110\u010c")
        buf.write("\3\2\2\2\u0110\u010f\3\2\2\2\u0111\67\3\2\2\2\u0112\u0113")
        buf.write("\7\25\2\2\u0113\u0114\5D#\2\u0114\u0116\7\7\2\2\u0115")
        buf.write("\u0117\5$\23\2\u0116\u0115\3\2\2\2\u0116\u0117\3\2\2\2")
        buf.write("\u0117\u0119\3\2\2\2\u0118\u011a\5 \21\2\u0119\u0118\3")
        buf.write("\2\2\2\u0119\u011a\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u011c")
        buf.write("\7\r\2\2\u011c\u011d\7\66\2\2\u011d9\3\2\2\2\u011e\u0120")
        buf.write("\7\7\2\2\u011f\u0121\5$\23\2\u0120\u011f\3\2\2\2\u0120")
        buf.write("\u0121\3\2\2\2\u0121\u0123\3\2\2\2\u0122\u0124\5 \21\2")
        buf.write("\u0123\u0122\3\2\2\2\u0123\u0124\3\2\2\2\u0124\u0125\3")
        buf.write("\2\2\2\u0125\u0126\7\25\2\2\u0126\u0127\5D#\2\u0127\u0128")
        buf.write("\7\r\2\2\u0128\u0129\7\66\2\2\u0129;\3\2\2\2\u012a\u012b")
        buf.write("\7\5\2\2\u012b\u012c\78\2\2\u012c=\3\2\2\2\u012d\u012e")
        buf.write("\7\6\2\2\u012e\u012f\78\2\2\u012f?\3\2\2\2\u0130\u0131")
        buf.write("\7\3\2\2\u0131\u0133\7\61\2\2\u0132\u0134\5D#\2\u0133")
        buf.write("\u0132\3\2\2\2\u0133\u0134\3\2\2\2\u0134\u0139\3\2\2\2")
        buf.write("\u0135\u0136\7\67\2\2\u0136\u0138\5D#\2\u0137\u0135\3")
        buf.write("\2\2\2\u0138\u013b\3\2\2\2\u0139\u0137\3\2\2\2\u0139\u013a")
        buf.write("\3\2\2\2\u013a\u013c\3\2\2\2\u013b\u0139\3\2\2\2\u013c")
        buf.write("\u013d\7\62\2\2\u013d\u013e\78\2\2\u013eA\3\2\2\2\u013f")
        buf.write("\u0140\7\22\2\2\u0140\u0141\5D#\2\u0141\u0142\78\2\2\u0142")
        buf.write("C\3\2\2\2\u0143\u0144\5F$\2\u0144\u0145\7&\2\2\u0145\u0146")
        buf.write("\5F$\2\u0146\u0171\3\2\2\2\u0147\u0148\5F$\2\u0148\u0149")
        buf.write("\7\'\2\2\u0149\u014a\5F$\2\u014a\u0171\3\2\2\2\u014b\u014c")
        buf.write("\5F$\2\u014c\u014d\7)\2\2\u014d\u014e\5F$\2\u014e\u0171")
        buf.write("\3\2\2\2\u014f\u0150\5F$\2\u0150\u0151\7-\2\2\u0151\u0152")
        buf.write("\5F$\2\u0152\u0171\3\2\2\2\u0153\u0154\5F$\2\u0154\u0155")
        buf.write("\7+\2\2\u0155\u0156\5F$\2\u0156\u0171\3\2\2\2\u0157\u0158")
        buf.write("\5F$\2\u0158\u0159\7/\2\2\u0159\u015a\5F$\2\u015a\u0171")
        buf.write("\3\2\2\2\u015b\u015c\5F$\2\u015c\u015d\7(\2\2\u015d\u015e")
        buf.write("\5F$\2\u015e\u0171\3\2\2\2\u015f\u0160\5F$\2\u0160\u0161")
        buf.write("\7*\2\2\u0161\u0162\5F$\2\u0162\u0171\3\2\2\2\u0163\u0164")
        buf.write("\5F$\2\u0164\u0165\7.\2\2\u0165\u0166\5F$\2\u0166\u0171")
        buf.write("\3\2\2\2\u0167\u0168\5F$\2\u0168\u0169\7,\2\2\u0169\u016a")
        buf.write("\5F$\2\u016a\u0171\3\2\2\2\u016b\u016c\5F$\2\u016c\u016d")
        buf.write("\7\60\2\2\u016d\u016e\5F$\2\u016e\u0171\3\2\2\2\u016f")
        buf.write("\u0171\5F$\2\u0170\u0143\3\2\2\2\u0170\u0147\3\2\2\2\u0170")
        buf.write("\u014b\3\2\2\2\u0170\u014f\3\2\2\2\u0170\u0153\3\2\2\2")
        buf.write("\u0170\u0157\3\2\2\2\u0170\u015b\3\2\2\2\u0170\u015f\3")
        buf.write("\2\2\2\u0170\u0163\3\2\2\2\u0170\u0167\3\2\2\2\u0170\u016b")
        buf.write("\3\2\2\2\u0170\u016f\3\2\2\2\u0171E\3\2\2\2\u0172\u0173")
        buf.write("\b$\1\2\u0173\u0174\5H%\2\u0174\u017d\3\2\2\2\u0175\u0176")
        buf.write("\f\5\2\2\u0176\u0177\7%\2\2\u0177\u017c\5H%\2\u0178\u0179")
        buf.write("\f\4\2\2\u0179\u017a\7$\2\2\u017a\u017c\5H%\2\u017b\u0175")
        buf.write("\3\2\2\2\u017b\u0178\3\2\2\2\u017c\u017f\3\2\2\2\u017d")
        buf.write("\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017eG\3\2\2\2\u017f")
        buf.write("\u017d\3\2\2\2\u0180\u0181\b%\1\2\u0181\u0182\5J&\2\u0182")
        buf.write("\u0191\3\2\2\2\u0183\u0184\f\7\2\2\u0184\u0185\7\32\2")
        buf.write("\2\u0185\u0190\5J&\2\u0186\u0187\f\6\2\2\u0187\u0188\7")
        buf.write("\33\2\2\u0188\u0190\5J&\2\u0189\u018a\f\5\2\2\u018a\u018b")
        buf.write("\7\34\2\2\u018b\u0190\5J&\2\u018c\u018d\f\4\2\2\u018d")
        buf.write("\u018e\7\35\2\2\u018e\u0190\5J&\2\u018f\u0183\3\2\2\2")
        buf.write("\u018f\u0186\3\2\2\2\u018f\u0189\3\2\2\2\u018f\u018c\3")
        buf.write("\2\2\2\u0190\u0193\3\2\2\2\u0191\u018f\3\2\2\2\u0191\u0192")
        buf.write("\3\2\2\2\u0192I\3\2\2\2\u0193\u0191\3\2\2\2\u0194\u0195")
        buf.write("\b&\1\2\u0195\u0196\5L\'\2\u0196\u01a8\3\2\2\2\u0197\u0198")
        buf.write("\f\b\2\2\u0198\u0199\7\36\2\2\u0199\u01a7\5L\'\2\u019a")
        buf.write("\u019b\f\7\2\2\u019b\u019c\7\37\2\2\u019c\u01a7\5L\'\2")
        buf.write("\u019d\u019e\f\6\2\2\u019e\u019f\7 \2\2\u019f\u01a7\5")
        buf.write("L\'\2\u01a0\u01a1\f\5\2\2\u01a1\u01a2\7!\2\2\u01a2\u01a7")
        buf.write("\5L\'\2\u01a3\u01a4\f\4\2\2\u01a4\u01a5\7\"\2\2\u01a5")
        buf.write("\u01a7\5L\'\2\u01a6\u0197\3\2\2\2\u01a6\u019a\3\2\2\2")
        buf.write("\u01a6\u019d\3\2\2\2\u01a6\u01a0\3\2\2\2\u01a6\u01a3\3")
        buf.write("\2\2\2\u01a7\u01aa\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8\u01a9")
        buf.write("\3\2\2\2\u01a9K\3\2\2\2\u01aa\u01a8\3\2\2\2\u01ab\u01ac")
        buf.write("\7#\2\2\u01ac\u01af\5N(\2\u01ad\u01af\5N(\2\u01ae\u01ab")
        buf.write("\3\2\2\2\u01ae\u01ad\3\2\2\2\u01afM\3\2\2\2\u01b0\u01b7")
        buf.write("\5\24\13\2\u01b1\u01b7\7\3\2\2\u01b2\u01b7\5P)\2\u01b3")
        buf.write("\u01b7\5\22\n\2\u01b4\u01b7\5R*\2\u01b5\u01b7\5V,\2\u01b6")
        buf.write("\u01b0\3\2\2\2\u01b6\u01b1\3\2\2\2\u01b6\u01b2\3\2\2\2")
        buf.write("\u01b6\u01b3\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b6\u01b5\3")
        buf.write("\2\2\2\u01b7O\3\2\2\2\u01b8\u01b9\7\61\2\2\u01b9\u01ba")
        buf.write("\5D#\2\u01ba\u01bb\7\62\2\2\u01bbQ\3\2\2\2\u01bc\u01bd")
        buf.write("\7\3\2\2\u01bd\u01bf\7\61\2\2\u01be\u01c0\5T+\2\u01bf")
        buf.write("\u01be\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c1\3\2\2\2")
        buf.write("\u01c1\u01c2\7\62\2\2\u01c2S\3\2\2\2\u01c3\u01c8\5\24")
        buf.write("\13\2\u01c4\u01c5\7\67\2\2\u01c5\u01c7\5T+\2\u01c6\u01c4")
        buf.write("\3\2\2\2\u01c7\u01ca\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c8")
        buf.write("\u01c9\3\2\2\2\u01c9U\3\2\2\2\u01ca\u01c8\3\2\2\2\u01cb")
        buf.write("\u01cc\7\3\2\2\u01cc\u01cd\7\63\2\2\u01cd\u01ce\5D#\2")
        buf.write("\u01ce\u01cf\7\64\2\2\u01cfW\3\2\2\2._cosw}\u008b\u008f")
        buf.write("\u00a0\u00a5\u00af\u00b3\u00b9\u00c4\u00c8\u00d0\u00d3")
        buf.write("\u00dc\u00df\u00e5\u00eb\u00ee\u00f2\u00f5\u00fd\u0100")
        buf.write("\u0110\u0116\u0119\u0120\u0123\u0133\u0139\u0170\u017b")
        buf.write("\u017d\u018f\u0191\u01a6\u01a8\u01ae\u01b6\u01bf\u01c8")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'Body'", "'Break'", "'Continue'", 
                     "'Do'", "'Else'", "'ElseIf'", "'EndBody'", "'EndIf'", 
                     "'EndFor'", "'EndWhile'", "'For'", "'Function'", "'If'", 
                     "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
                     "'True'", "'False'", "'EndDo'", "'='", "'+'", "'+.'", 
                     "'-'", "'-.'", "'*'", "'*.'", "'/'", "'/.'", "'%'", 
                     "'!'", "'||'", "'&&'", "'=='", "'!='", "'=/='", "'<'", 
                     "'<.'", "'>'", "'>.'", "'<='", "'<=.'", "'>='", "'>=.'", 
                     "'('", "')'", "'['", "']'", "':'", "'.'", "','", "';'", 
                     "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "ID", "BODY", "BREAK", "CONTINUE", "DO", 
                      "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", 
                      "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", 
                      "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", "ASSIGN", 
                      "ADDOP", "ADDOPDOT", "SUBOP", "SUBOPDOT", "MULOP", 
                      "MULOPDOT", "DIVOP", "DIVOPDOT", "MODOP", "NOTOP", 
                      "OROP", "ANDOP", "EQUALOP", "NOTEQUALOP", "NOTEQUALOPFLOAT", 
                      "LESSOP", "LESSOPDOT", "GREATEROP", "GREATEROPDOT", 
                      "LESSOREQUALOP", "LESSOREQUALOPDOT", "GREATEOREQUALOP", 
                      "GREATEOREQUALOPDOT", "LB", "RB", "LSB", "RSB", "COLON", 
                      "DOT", "COMMA", "SEMI", "LP", "RP", "INTLIT", "FLOATLIT", 
                      "STRINGLIT", "ARRAY", "WS", "COMMENT", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_many_declare = 1
    RULE_declare = 2
    RULE_var_declare = 3
    RULE_ids_list = 4
    RULE_id_declare = 5
    RULE_array_declares = 6
    RULE_array = 7
    RULE_array_id = 8
    RULE_type_list = 9
    RULE_func_declare = 10
    RULE_header_stm = 11
    RULE_paramater_stm = 12
    RULE_paramater_list = 13
    RULE_body_stm = 14
    RULE_statement_list = 15
    RULE_id_var = 16
    RULE_var_declare_list = 17
    RULE_statement = 18
    RULE_assign_statement = 19
    RULE_if_statement = 20
    RULE_if_then_statement = 21
    RULE_else_if_statements = 22
    RULE_else_if_statement = 23
    RULE_else_statement = 24
    RULE_for_statement = 25
    RULE_for_condition = 26
    RULE_while_statement = 27
    RULE_do_while_statement = 28
    RULE_break_statement = 29
    RULE_continue_statement = 30
    RULE_function_call_statement = 31
    RULE_return_statement = 32
    RULE_expressions = 33
    RULE_exp1 = 34
    RULE_exp2 = 35
    RULE_exp3 = 36
    RULE_exp4 = 37
    RULE_operand = 38
    RULE_sub_expression = 39
    RULE_function_call = 40
    RULE_list_expression = 41
    RULE_index_operator = 42

    ruleNames =  [ "program", "many_declare", "declare", "var_declare", 
                   "ids_list", "id_declare", "array_declares", "array", 
                   "array_id", "type_list", "func_declare", "header_stm", 
                   "paramater_stm", "paramater_list", "body_stm", "statement_list", 
                   "id_var", "var_declare_list", "statement", "assign_statement", 
                   "if_statement", "if_then_statement", "else_if_statements", 
                   "else_if_statement", "else_statement", "for_statement", 
                   "for_condition", "while_statement", "do_while_statement", 
                   "break_statement", "continue_statement", "function_call_statement", 
                   "return_statement", "expressions", "exp1", "exp2", "exp3", 
                   "exp4", "operand", "sub_expression", "function_call", 
                   "list_expression", "index_operator" ]

    EOF = Token.EOF
    ID=1
    BODY=2
    BREAK=3
    CONTINUE=4
    DO=5
    ELSE=6
    ELSEIF=7
    ENDBODY=8
    ENDIF=9
    ENDFOR=10
    ENDWHILE=11
    FOR=12
    FUNCTION=13
    IF=14
    PARAMETER=15
    RETURN=16
    THEN=17
    VAR=18
    WHILE=19
    TRUE=20
    FALSE=21
    ENDDO=22
    ASSIGN=23
    ADDOP=24
    ADDOPDOT=25
    SUBOP=26
    SUBOPDOT=27
    MULOP=28
    MULOPDOT=29
    DIVOP=30
    DIVOPDOT=31
    MODOP=32
    NOTOP=33
    OROP=34
    ANDOP=35
    EQUALOP=36
    NOTEQUALOP=37
    NOTEQUALOPFLOAT=38
    LESSOP=39
    LESSOPDOT=40
    GREATEROP=41
    GREATEROPDOT=42
    LESSOREQUALOP=43
    LESSOREQUALOPDOT=44
    GREATEOREQUALOP=45
    GREATEOREQUALOPDOT=46
    LB=47
    RB=48
    LSB=49
    RSB=50
    COLON=51
    DOT=52
    COMMA=53
    SEMI=54
    LP=55
    RP=56
    INTLIT=57
    FLOATLIT=58
    STRINGLIT=59
    ARRAY=60
    WS=61
    COMMENT=62
    ERROR_CHAR=63
    UNCLOSE_STRING=64
    ILLEGAL_ESCAPE=65
    UNTERMINATED_COMMENT=66

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def many_declare(self):
            return self.getTypedRuleContext(BKITParser.Many_declareContext,0)


        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_program




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.many_declare()
            self.state = 87
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declare(self):
            return self.getTypedRuleContext(BKITParser.DeclareContext,0)


        def many_declare(self):
            return self.getTypedRuleContext(BKITParser.Many_declareContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_many_declare




    def many_declare(self):

        localctx = BKITParser.Many_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_many_declare)
        try:
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.declare()
                self.state = 90
                self.many_declare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.declare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self):
            return self.getTypedRuleContext(BKITParser.Var_declareContext,0)


        def func_declare(self):
            return self.getTypedRuleContext(BKITParser.Func_declareContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_declare




    def declare(self):

        localctx = BKITParser.DeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.VAR]:
                self.state = 95
                self.var_declare()
                pass
            elif token in [BKITParser.FUNCTION]:
                self.state = 96
                self.func_declare()
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


    class Var_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ids_list(self):
            return self.getTypedRuleContext(BKITParser.Ids_listContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_var_declare




    def var_declare(self):

        localctx = BKITParser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(BKITParser.VAR)
            self.state = 100
            self.match(BKITParser.COLON)
            self.state = 101
            self.ids_list()
            self.state = 102
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ids_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_declare(self):
            return self.getTypedRuleContext(BKITParser.Id_declareContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def ids_list(self):
            return self.getTypedRuleContext(BKITParser.Ids_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_ids_list




    def ids_list(self):

        localctx = BKITParser.Ids_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ids_list)
        try:
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.id_declare()

                self.state = 105
                self.match(BKITParser.COMMA)
                self.state = 106
                self.ids_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.id_declare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def array_declares(self):
            return self.getTypedRuleContext(BKITParser.Array_declaresContext,0)


        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def type_list(self):
            return self.getTypedRuleContext(BKITParser.Type_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_id_declare




    def id_declare(self):

        localctx = BKITParser.Id_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_id_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(BKITParser.ID)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.LSB:
                self.state = 112
                self.array_declares()


            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ASSIGN:
                self.state = 115
                self.match(BKITParser.ASSIGN)
                self.state = 116
                self.type_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declaresContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array(self):
            return self.getTypedRuleContext(BKITParser.ArrayContext,0)


        def array_declares(self):
            return self.getTypedRuleContext(BKITParser.Array_declaresContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_array_declares




    def array_declares(self):

        localctx = BKITParser.Array_declaresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_array_declares)
        try:
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.array()

                self.state = 120
                self.array_declares()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 122
                self.array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(BKITParser.LSB, 0)

        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def RSB(self):
            return self.getToken(BKITParser.RSB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_array




    def array(self):

        localctx = BKITParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(BKITParser.LSB)
            self.state = 126
            self.match(BKITParser.INTLIT)
            self.state = 127
            self.match(BKITParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_idContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def array_declares(self):
            return self.getTypedRuleContext(BKITParser.Array_declaresContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_array_id




    def array_id(self):

        localctx = BKITParser.Array_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(BKITParser.ID)
            self.state = 130
            self.array_declares()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKITParser.FLOATLIT, 0)

        def TRUE(self):
            return self.getToken(BKITParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKITParser.FALSE, 0)

        def STRINGLIT(self):
            return self.getToken(BKITParser.STRINGLIT, 0)

        def array_id(self):
            return self.getTypedRuleContext(BKITParser.Array_idContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_type_list




    def type_list(self):

        localctx = BKITParser.Type_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_type_list)
        self._la = 0 # Token type
        try:
            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.match(BKITParser.INTLIT)
                pass
            elif token in [BKITParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.match(BKITParser.FLOATLIT)
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 134
                _la = self._input.LA(1)
                if not(_la==BKITParser.TRUE or _la==BKITParser.FALSE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 135
                self.match(BKITParser.STRINGLIT)
                pass
            elif token in [BKITParser.ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 136
                self.array_id()
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


    class Func_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def header_stm(self):
            return self.getTypedRuleContext(BKITParser.Header_stmContext,0)


        def body_stm(self):
            return self.getTypedRuleContext(BKITParser.Body_stmContext,0)


        def paramater_stm(self):
            return self.getTypedRuleContext(BKITParser.Paramater_stmContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_declare




    def func_declare(self):

        localctx = BKITParser.Func_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_func_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.header_stm()
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 140
                self.paramater_stm()


            self.state = 143
            self.body_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Header_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_header_stm




    def header_stm(self):

        localctx = BKITParser.Header_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_header_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(BKITParser.FUNCTION)
            self.state = 146
            self.match(BKITParser.COLON)
            self.state = 147
            self.match(BKITParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Paramater_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def paramater_list(self):
            return self.getTypedRuleContext(BKITParser.Paramater_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_paramater_stm




    def paramater_stm(self):

        localctx = BKITParser.Paramater_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_paramater_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(BKITParser.PARAMETER)
            self.state = 150
            self.match(BKITParser.COLON)
            self.state = 151
            self.paramater_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Paramater_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_var(self):
            return self.getTypedRuleContext(BKITParser.Id_varContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def paramater_list(self):
            return self.getTypedRuleContext(BKITParser.Paramater_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_paramater_list




    def paramater_list(self):

        localctx = BKITParser.Paramater_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_paramater_list)
        try:
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.id_var()

                self.state = 154
                self.match(BKITParser.COMMA)
                self.state = 155
                self.paramater_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.id_var()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def var_declare_list(self):
            return self.getTypedRuleContext(BKITParser.Var_declare_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_body_stm




    def body_stm(self):

        localctx = BKITParser.Body_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_body_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(BKITParser.BODY)
            self.state = 161
            self.match(BKITParser.COLON)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.VAR:
                self.state = 162
                self.var_declare_list()


            self.state = 165
            self.statement_list()
            self.state = 166
            self.match(BKITParser.ENDBODY)
            self.state = 167
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(BKITParser.StatementContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_statement_list




    def statement_list(self):

        localctx = BKITParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_statement_list)
        try:
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.statement()
                self.state = 170
                self.statement_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def array_id(self):
            return self.getTypedRuleContext(BKITParser.Array_idContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_id_var




    def id_var(self):

        localctx = BKITParser.Id_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_id_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 175
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.state = 176
                self.array_id()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declare_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self):
            return self.getTypedRuleContext(BKITParser.Var_declareContext,0)


        def var_declare_list(self):
            return self.getTypedRuleContext(BKITParser.Var_declare_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_declare_list




    def var_declare_list(self):

        localctx = BKITParser.Var_declare_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_var_declare_list)
        try:
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.var_declare()
                self.state = 180
                self.var_declare_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.var_declare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_statement(self):
            return self.getTypedRuleContext(BKITParser.Assign_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(BKITParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(BKITParser.For_statementContext,0)


        def while_statement(self):
            return self.getTypedRuleContext(BKITParser.While_statementContext,0)


        def do_while_statement(self):
            return self.getTypedRuleContext(BKITParser.Do_while_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(BKITParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(BKITParser.Continue_statementContext,0)


        def function_call_statement(self):
            return self.getTypedRuleContext(BKITParser.Function_call_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(BKITParser.Return_statementContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_statement




    def statement(self):

        localctx = BKITParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_statement)
        try:
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.assign_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.if_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 187
                self.for_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 188
                self.while_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 189
                self.do_while_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 190
                self.break_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 191
                self.continue_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 192
                self.function_call_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 193
                self.return_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def expressions(self):
            return self.getTypedRuleContext(BKITParser.ExpressionsContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def array_id(self):
            return self.getTypedRuleContext(BKITParser.Array_idContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_assign_statement




    def assign_statement(self):

        localctx = BKITParser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 196
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.state = 197
                self.array_id()
                pass


            self.state = 200
            self.match(BKITParser.ASSIGN)
            self.state = 201
            self.expressions()
            self.state = 202
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_then_statement(self):
            return self.getTypedRuleContext(BKITParser.If_then_statementContext,0)


        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def else_if_statements(self):
            return self.getTypedRuleContext(BKITParser.Else_if_statementsContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(BKITParser.Else_statementContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_if_statement




    def if_statement(self):

        localctx = BKITParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.if_then_statement()
            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSEIF:
                self.state = 205
                self.else_if_statements()


            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 208
                self.else_statement()


            self.state = 211
            self.match(BKITParser.ENDIF)
            self.state = 212
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_then_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKITParser.IF, 0)

        def expressions(self):
            return self.getTypedRuleContext(BKITParser.ExpressionsContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def var_declare_list(self):
            return self.getTypedRuleContext(BKITParser.Var_declare_listContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_if_then_statement




    def if_then_statement(self):

        localctx = BKITParser.If_then_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_if_then_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(BKITParser.IF)
            self.state = 215
            self.expressions()
            self.state = 216
            self.match(BKITParser.THEN)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.VAR:
                self.state = 217
                self.var_declare_list()


            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.WHILE))) != 0):
                self.state = 220
                self.statement_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_if_statementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def else_if_statement(self):
            return self.getTypedRuleContext(BKITParser.Else_if_statementContext,0)


        def else_if_statements(self):
            return self.getTypedRuleContext(BKITParser.Else_if_statementsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_else_if_statements




    def else_if_statements(self):

        localctx = BKITParser.Else_if_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_else_if_statements)
        try:
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.else_if_statement()
                self.state = 224
                self.else_if_statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.else_if_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_if_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(BKITParser.ELSEIF, 0)

        def expressions(self):
            return self.getTypedRuleContext(BKITParser.ExpressionsContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def var_declare_list(self):
            return self.getTypedRuleContext(BKITParser.Var_declare_listContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_else_if_statement




    def else_if_statement(self):

        localctx = BKITParser.Else_if_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_else_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(BKITParser.ELSEIF)
            self.state = 230
            self.expressions()
            self.state = 231
            self.match(BKITParser.THEN)
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.VAR:
                self.state = 232
                self.var_declare_list()


            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.WHILE))) != 0):
                self.state = 235
                self.statement_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def var_declare_list(self):
            return self.getTypedRuleContext(BKITParser.Var_declare_listContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_else_statement




    def else_statement(self):

        localctx = BKITParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_else_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(BKITParser.ELSE)
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.VAR:
                self.state = 239
                self.var_declare_list()


            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.WHILE))) != 0):
                self.state = 242
                self.statement_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKITParser.FOR, 0)

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def for_condition(self):
            return self.getTypedRuleContext(BKITParser.For_conditionContext,0)


        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def ENDFOR(self):
            return self.getToken(BKITParser.ENDFOR, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def var_declare_list(self):
            return self.getTypedRuleContext(BKITParser.Var_declare_listContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_for_statement




    def for_statement(self):

        localctx = BKITParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(BKITParser.FOR)
            self.state = 246
            self.match(BKITParser.LB)
            self.state = 247
            self.for_condition()
            self.state = 248
            self.match(BKITParser.RB)
            self.state = 249
            self.match(BKITParser.DO)
            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.VAR:
                self.state = 250
                self.var_declare_list()


            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.WHILE))) != 0):
                self.state = 253
                self.statement_list()


            self.state = 256
            self.match(BKITParser.ENDFOR)
            self.state = 257
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_conditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def expressions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpressionsContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpressionsContext,i)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.ID)
            else:
                return self.getToken(BKITParser.ID, i)

        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.ASSIGN)
            else:
                return self.getToken(BKITParser.ASSIGN, i)

        def getRuleIndex(self):
            return BKITParser.RULE_for_condition




    def for_condition(self):

        localctx = BKITParser.For_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_for_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(BKITParser.ID)
            self.state = 260
            self.match(BKITParser.ASSIGN)
            self.state = 261
            self.expressions()
            self.state = 263
            self.match(BKITParser.COMMA)
            self.state = 264
            self.expressions()
            self.state = 265
            self.match(BKITParser.COMMA)
            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 266
                self.match(BKITParser.ID)
                self.state = 267
                self.match(BKITParser.ASSIGN)
                self.state = 268
                self.expressions()
                pass

            elif la_ == 2:
                self.state = 269
                self.expressions()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def expressions(self):
            return self.getTypedRuleContext(BKITParser.ExpressionsContext,0)


        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def var_declare_list(self):
            return self.getTypedRuleContext(BKITParser.Var_declare_listContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_while_statement




    def while_statement(self):

        localctx = BKITParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_while_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(BKITParser.WHILE)
            self.state = 273
            self.expressions()
            self.state = 274
            self.match(BKITParser.DO)
            self.state = 276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.VAR:
                self.state = 275
                self.var_declare_list()


            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.WHILE))) != 0):
                self.state = 278
                self.statement_list()


            self.state = 281
            self.match(BKITParser.ENDWHILE)
            self.state = 282
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def expressions(self):
            return self.getTypedRuleContext(BKITParser.ExpressionsContext,0)


        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def var_declare_list(self):
            return self.getTypedRuleContext(BKITParser.Var_declare_listContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_do_while_statement




    def do_while_statement(self):

        localctx = BKITParser.Do_while_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_do_while_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(BKITParser.DO)
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.VAR:
                self.state = 285
                self.var_declare_list()


            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 288
                self.statement_list()


            self.state = 291
            self.match(BKITParser.WHILE)
            self.state = 292
            self.expressions()
            self.state = 293
            self.match(BKITParser.ENDWHILE)
            self.state = 294
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKITParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_break_statement




    def break_statement(self):

        localctx = BKITParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(BKITParser.BREAK)
            self.state = 297
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKITParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_continue_statement




    def continue_statement(self):

        localctx = BKITParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(BKITParser.CONTINUE)
            self.state = 300
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_call_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def expressions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpressionsContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpressionsContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_function_call_statement




    def function_call_statement(self):

        localctx = BKITParser.Function_call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_function_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(BKITParser.ID)
            self.state = 303
            self.match(BKITParser.LB)
            self.state = 305
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.NOTOP) | (1 << BKITParser.LB) | (1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.STRINGLIT))) != 0):
                self.state = 304
                self.expressions()


            self.state = 311
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 307
                self.match(BKITParser.COMMA)
                self.state = 308
                self.expressions()
                self.state = 313
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 314
            self.match(BKITParser.RB)
            self.state = 315
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def expressions(self):
            return self.getTypedRuleContext(BKITParser.ExpressionsContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_return_statement




    def return_statement(self):

        localctx = BKITParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(BKITParser.RETURN)
            self.state = 318
            self.expressions()
            self.state = 319
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Exp1Context,i)


        def EQUALOP(self):
            return self.getToken(BKITParser.EQUALOP, 0)

        def NOTEQUALOP(self):
            return self.getToken(BKITParser.NOTEQUALOP, 0)

        def LESSOP(self):
            return self.getToken(BKITParser.LESSOP, 0)

        def LESSOREQUALOP(self):
            return self.getToken(BKITParser.LESSOREQUALOP, 0)

        def GREATEROP(self):
            return self.getToken(BKITParser.GREATEROP, 0)

        def GREATEOREQUALOP(self):
            return self.getToken(BKITParser.GREATEOREQUALOP, 0)

        def NOTEQUALOPFLOAT(self):
            return self.getToken(BKITParser.NOTEQUALOPFLOAT, 0)

        def LESSOPDOT(self):
            return self.getToken(BKITParser.LESSOPDOT, 0)

        def LESSOREQUALOPDOT(self):
            return self.getToken(BKITParser.LESSOREQUALOPDOT, 0)

        def GREATEROPDOT(self):
            return self.getToken(BKITParser.GREATEROPDOT, 0)

        def GREATEOREQUALOPDOT(self):
            return self.getToken(BKITParser.GREATEOREQUALOPDOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expressions




    def expressions(self):

        localctx = BKITParser.ExpressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expressions)
        try:
            self.state = 366
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self.exp1(0)
                self.state = 322
                self.match(BKITParser.EQUALOP)
                self.state = 323
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.exp1(0)
                self.state = 326
                self.match(BKITParser.NOTEQUALOP)
                self.state = 327
                self.exp1(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 329
                self.exp1(0)
                self.state = 330
                self.match(BKITParser.LESSOP)
                self.state = 331
                self.exp1(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 333
                self.exp1(0)
                self.state = 334
                self.match(BKITParser.LESSOREQUALOP)
                self.state = 335
                self.exp1(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 337
                self.exp1(0)
                self.state = 338
                self.match(BKITParser.GREATEROP)
                self.state = 339
                self.exp1(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 341
                self.exp1(0)
                self.state = 342
                self.match(BKITParser.GREATEOREQUALOP)
                self.state = 343
                self.exp1(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 345
                self.exp1(0)
                self.state = 346
                self.match(BKITParser.NOTEQUALOPFLOAT)
                self.state = 347
                self.exp1(0)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 349
                self.exp1(0)
                self.state = 350
                self.match(BKITParser.LESSOPDOT)
                self.state = 351
                self.exp1(0)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 353
                self.exp1(0)
                self.state = 354
                self.match(BKITParser.LESSOREQUALOPDOT)
                self.state = 355
                self.exp1(0)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 357
                self.exp1(0)
                self.state = 358
                self.match(BKITParser.GREATEROPDOT)
                self.state = 359
                self.exp1(0)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 361
                self.exp1(0)
                self.state = 362
                self.match(BKITParser.GREATEOREQUALOPDOT)
                self.state = 363
                self.exp1(0)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 365
                self.exp1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def ANDOP(self):
            return self.getToken(BKITParser.ANDOP, 0)

        def OROP(self):
            return self.getToken(BKITParser.OROP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp1



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_exp1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 379
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 377
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 371
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 372
                        self.match(BKITParser.ANDOP)
                        self.state = 373
                        self.exp2(0)
                        pass

                    elif la_ == 2:
                        localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 374
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 375
                        self.match(BKITParser.OROP)
                        self.state = 376
                        self.exp2(0)
                        pass

             
                self.state = 381
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def ADDOP(self):
            return self.getToken(BKITParser.ADDOP, 0)

        def ADDOPDOT(self):
            return self.getToken(BKITParser.ADDOPDOT, 0)

        def SUBOP(self):
            return self.getToken(BKITParser.SUBOP, 0)

        def SUBOPDOT(self):
            return self.getToken(BKITParser.SUBOPDOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp2



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 399
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 397
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                    if la_ == 1:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 385
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 386
                        self.match(BKITParser.ADDOP)
                        self.state = 387
                        self.exp3(0)
                        pass

                    elif la_ == 2:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 388
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 389
                        self.match(BKITParser.ADDOPDOT)
                        self.state = 390
                        self.exp3(0)
                        pass

                    elif la_ == 3:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 391
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 392
                        self.match(BKITParser.SUBOP)
                        self.state = 393
                        self.exp3(0)
                        pass

                    elif la_ == 4:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 394
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 395
                        self.match(BKITParser.SUBOPDOT)
                        self.state = 396
                        self.exp3(0)
                        pass

             
                self.state = 401
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def MULOP(self):
            return self.getToken(BKITParser.MULOP, 0)

        def MULOPDOT(self):
            return self.getToken(BKITParser.MULOPDOT, 0)

        def DIVOP(self):
            return self.getToken(BKITParser.DIVOP, 0)

        def DIVOPDOT(self):
            return self.getToken(BKITParser.DIVOPDOT, 0)

        def MODOP(self):
            return self.getToken(BKITParser.MODOP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp3



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 422
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 420
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                    if la_ == 1:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 405
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 406
                        self.match(BKITParser.MULOP)
                        self.state = 407
                        self.exp4()
                        pass

                    elif la_ == 2:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 408
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 409
                        self.match(BKITParser.MULOPDOT)
                        self.state = 410
                        self.exp4()
                        pass

                    elif la_ == 3:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 411
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 412
                        self.match(BKITParser.DIVOP)
                        self.state = 413
                        self.exp4()
                        pass

                    elif la_ == 4:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 414
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 415
                        self.match(BKITParser.DIVOPDOT)
                        self.state = 416
                        self.exp4()
                        pass

                    elif la_ == 5:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 417
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 418
                        self.match(BKITParser.MODOP)
                        self.state = 419
                        self.exp4()
                        pass

             
                self.state = 424
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOTOP(self):
            return self.getToken(BKITParser.NOTOP, 0)

        def operand(self):
            return self.getTypedRuleContext(BKITParser.OperandContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp4




    def exp4(self):

        localctx = BKITParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_exp4)
        try:
            self.state = 428
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOTOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 425
                self.match(BKITParser.NOTOP)
                self.state = 426
                self.operand()
                pass
            elif token in [BKITParser.ID, BKITParser.TRUE, BKITParser.FALSE, BKITParser.LB, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 427
                self.operand()
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


    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_list(self):
            return self.getTypedRuleContext(BKITParser.Type_listContext,0)


        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def sub_expression(self):
            return self.getTypedRuleContext(BKITParser.Sub_expressionContext,0)


        def array_id(self):
            return self.getTypedRuleContext(BKITParser.Array_idContext,0)


        def function_call(self):
            return self.getTypedRuleContext(BKITParser.Function_callContext,0)


        def index_operator(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_operand




    def operand(self):

        localctx = BKITParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_operand)
        try:
            self.state = 436
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 430
                self.type_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 431
                self.match(BKITParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 432
                self.sub_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 433
                self.array_id()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 434
                self.function_call()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 435
                self.index_operator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sub_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def expressions(self):
            return self.getTypedRuleContext(BKITParser.ExpressionsContext,0)


        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_sub_expression




    def sub_expression(self):

        localctx = BKITParser.Sub_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_sub_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.match(BKITParser.LB)
            self.state = 439
            self.expressions()
            self.state = 440
            self.match(BKITParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def list_expression(self):
            return self.getTypedRuleContext(BKITParser.List_expressionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_function_call




    def function_call(self):

        localctx = BKITParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.match(BKITParser.ID)
            self.state = 443
            self.match(BKITParser.LB)
            self.state = 445
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.STRINGLIT))) != 0):
                self.state = 444
                self.list_expression()


            self.state = 447
            self.match(BKITParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_list(self):
            return self.getTypedRuleContext(BKITParser.Type_listContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def list_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.List_expressionContext)
            else:
                return self.getTypedRuleContext(BKITParser.List_expressionContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_list_expression




    def list_expression(self):

        localctx = BKITParser.List_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_list_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.type_list()
            self.state = 454
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 450
                    self.match(BKITParser.COMMA)
                    self.state = 451
                    self.list_expression() 
                self.state = 456
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LSB(self):
            return self.getToken(BKITParser.LSB, 0)

        def expressions(self):
            return self.getTypedRuleContext(BKITParser.ExpressionsContext,0)


        def RSB(self):
            return self.getToken(BKITParser.RSB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_index_operator




    def index_operator(self):

        localctx = BKITParser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_index_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.match(BKITParser.ID)
            self.state = 458
            self.match(BKITParser.LSB)
            self.state = 459
            self.expressions()
            self.state = 460
            self.match(BKITParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[34] = self.exp1_sempred
        self._predicates[35] = self.exp2_sempred
        self._predicates[36] = self.exp3_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 2)
         




