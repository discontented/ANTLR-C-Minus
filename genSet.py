from gen.MyCMinusParser import MyCMinusParser
from gen.MyCMinusListener import MyCMinusListener

class KillListener(MyCMinusListener):
    # [ 1: {x,y}, 2: {null} ]
    killSet = []

    def enterVarDeclStat(self, ctx: MyCMinusParser.VarDeclStatContext):
        self.killSet.append(set(ctx.ID().getText()))

    def enterAssignment(self, ctx: MyCMinusParser.AssignmentContext):
        self.killSet.append(set(ctx.ID().getText()))

    def printKillSet(self):
        print("kill set: ")
        for i in range(len(self.killSet)):
            print(self.killSet[i])


class GenListener(MyCMinusListener):
    # [ 1: {x,y}, 2: {null} ]
    genSet = []

    # def enterIdCall(self, ctx: MyCMinusParser.IdCallContext):
    #     self.genSet.append(set(ctx.ID().getText()))

    # def enterAssignment(self, ctx:MyCMinusParser.AssignmentContext):
    #     exp = ctx.expression().idCall()
    #     print(exp)
    #     # if(exp.ID()):
    #     #     self.genSet.append(set(exp.ID().getText()))

    def enterMultExp(self, ctx:MyCMinusParser.MultExpContext):
        if(ctx.expression()):
            id = self.enterIdCall(ctx.expression())
            print(id)

    def enterIdCall(self, ctx:MyCMinusParser.IdCallContext):
        return ctx.getText()

    def printGenSet(self):
        print("gen set: ")
        for i in range(len(self.genSet)):
            print(self.genSet[i])
