
import sys
from antlr4 import *
from MyCMinusLexer import MyCMinusLexer
from MyCMinusParser import MyCMinusParser
from MyCMinusListener import MyCMinusListener
from Listener import Listener

def main(argv):
    input = InputStream(argv)
    lexer = MyCMinusLexer(input)
    stream = CommonTokenStream(lexer)
    parser = MyCMinusParser(stream)
    tree = parser.program()

    output = open("output.txt","w")
    
    listener = Listener(output)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
        
    output.close()      

#if __name__ == '__main__':
#    main(sys.argv)