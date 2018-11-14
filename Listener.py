import sys
from antlr4 import *
from gen.MyCMinusParser import MyCMinusParser
from gen.MyCMinusListener import MyCMinusListener


class Listener(MyCMinusListener):
    def __init__(self, output):
        self.output = output

