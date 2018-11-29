import sys
from antlr4 import *
from gen.MyCMinusParser import MyCMinusParser
from gen.MyCMinusListener import MyCMinusListener


class Listener(MyCMinusListener):
    label = 0;

    def labeller(self, ctx):
        self.label += 1
        ctx.__setattr__("label", self.label)

    def enterVarDeclStat(self, ctx:MyCMinusParser.VarDeclStatContext):
        self.labeller(ctx)
        var_type = ctx.varType().getText()
        id = ctx.ID().getText()
        value = ctx.expression()
        if not(value):
            print("%s %s /*block %d" % (var_type, id, self.label))
        else:
            print("%s %s = %s /*block %d" % (var_type, id, value.getText(), self.label))

    # def enterEqualityExp(self, ctx:MyCMinusParser.EqualityExpContext):
    #     self.label += 1
    #     print("%s /* block %d" % (ctx.getText(), self.label))

    def enterConditionalStat(self, ctx:MyCMinusParser.ConditionalStatContext):
        self.labeller(ctx)
        child = ctx.conditionalStatement()
        exp = child.expression()
        print("%s /* block %d" % (exp.getText(), self.label))

    def enterAssignment(self, ctx:MyCMinusParser.AssignmentContext):
        self.labeller(ctx)
        print("%s /* block %d" % (ctx.getText(), self.label))
