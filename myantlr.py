from antlr4 import *

from Listener import Listener
from gen.MyCMinusLexer import MyCMinusLexer
from gen.MyCMinusParser import MyCMinusParser


def main(argv):
    input = InputStream(argv)
    lexer = MyCMinusLexer(input)
    stream = CommonTokenStream(lexer)
    parser = MyCMinusParser(stream)
    tree = parser.program()

    output = open("output.txt","w")

    # print(Trees.toStringTree(tree, None, parser))

    listener = Listener(output)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
        
    output.close()      

#if __name__ == '__main__':
#    main(sys.argv)

main("""
{
    int x = 0;
    if(x==0){
        print x;
    }
}
""")