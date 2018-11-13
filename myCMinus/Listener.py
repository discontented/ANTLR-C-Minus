import sys
from antlr4 import *
from MyCMinusParser import MyCMinusParser
from MyCMinusListener import MyCMinusListener

class Listener(MyCMinusListener):
    def __init__(self, output):
        self.output = output

    def enterMainProg(self):
        print("entered main")


