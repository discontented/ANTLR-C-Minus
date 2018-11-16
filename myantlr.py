from antlr4 import *

from Listener import Listener
from GraphListener import GraphListener
from genSet import GenListener, KillListener
from Analyzer import Analyzer
from gen.MyCMinusLexer import MyCMinusLexer
from gen.MyCMinusParser import MyCMinusParser


def main(argv):
    # input = InputStream(argv)
    input = FileStream(argv)
    lexer = MyCMinusLexer(input)
    stream = CommonTokenStream(lexer)
    parser = MyCMinusParser(stream)
    tree = parser.program()

    walker = ParseTreeWalker()
    # print(Trees.toStringTree(tree, None, parser))
    print("--Control Flow Graph--")
    listener = Listener()
    walker.walk(listener, tree)
    analyzer = Analyzer(listener.label)
    # graphListener = GraphListener()
    genListener = GenListener()
    killListener = KillListener()

    walker.walk(genListener, tree)
    walker.walk(killListener, tree)
    genListener.printGenSet()
    killListener.printKillSet()
    # walker.walk(graphListener, tree)
    # graphListener.printNodes()



#if __name__ == '__main__':
#    main(sys.argv)

main("input.txt")