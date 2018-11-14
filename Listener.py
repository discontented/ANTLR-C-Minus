import sys
from antlr4 import *
from gen.MyCMinusParser import MyCMinusParser
from gen.MyCMinusListener import MyCMinusListener


class Listener(MyCMinusListener):

    def enterStatement(self, ctx: MyCMinusParser.StatementContext):
        print(ctx.getText())