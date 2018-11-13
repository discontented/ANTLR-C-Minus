import sys
from antlr4 import *
from MyCMinusParser import MyCMinusParser
from MyCMinusListener import MyCMinusListener


class Listener(MyCMinusListener):
    def __init__(self, output):
        self.output = output

    def enterSingleStat(self, ctx:MyCMinusParser.SingleStatContext):
        print("statement " + ctx.getText())

    def enterStatList(self, ctx:MyCMinusParser.StatListContext):
        print("stat list " + ctx.getText())

