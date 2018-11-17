from antlr4 import *

from Listener import Listener
from GraphListener import GraphListener
from genSet import GenListener, KillListener
from Analyzer import Analyzer
from gen.MyCMinusLexer import MyCMinusLexer
from gen.MyCMinusParser import MyCMinusParser
from gen.MyCMinusVisitor import MyCMinusVisitor


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

    genListener = GenListener()
    killListener = KillListener()

    walker.walk(genListener, tree)
    walker.walk(killListener, tree)

    print("--Gen/Kill Set--")
    genListener.printGenSet(listener.label)
    killListener.printKillSet(listener.label)

    # Analysis
    analyzer = Analyzer(listener.label, killListener.finalKillSet, genListener.finalGenSet)
    walker.walk(analyzer, tree)

    print("--Analyzer--")

    analyzer.LVentry()
    # walker.walk(graphListener, tree)
    # graphListener.printNodes()
    analyzer.LVexit()

    print("---------Graph-----------")
    analyzer.print_cfg()


#if __name__ == '__main__':
#    main(sys.argv)

main("input.txt")