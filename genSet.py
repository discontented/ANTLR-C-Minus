from gen.MyCMinusParser import MyCMinusParser
from gen.MyCMinusListener import MyCMinusListener
from gen.MyCMinusLexer import CommonTokenStream
from gen.MyCMinusVisitor import MyCMinusVisitor


def labeller(killGenSet, ctx):
    label = ctx.__getattribute__("label")
    killGenSet.append((label, set(ctx.ID().getText())))

class KillListener(MyCMinusListener):
    # [ 1: {x,y}, 2: {null} ]
    killSet = []

    def enterVarDeclStat(self, ctx: MyCMinusParser.VarDeclStatContext):
        labeller(self.killSet, ctx)

    def enterAssignment(self, ctx: MyCMinusParser.AssignmentContext):
        labeller(self.killSet, ctx)

    def printKillSet(self):
        print("kill set: ")
        counter = 1
        index = 0
        while(counter < 6):
            genLabel = self.killSet[index][0]
            if (genLabel != counter):
                print("%s empty" % counter)
            else:
                print(self.killSet[index])
                index = index + 1
            counter += 1


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

    # def enterMultExp(self, ctx:MyCMinusParser.MultExpContext):
    #     if(ctx.expression()):
    #         id = self.enterIdCall(ctx.expression())
    #         print(id)

    def expressionSet(self, ctx, label):
        # labeller(self, self.genSet, ctx)
        children = ctx.expression()
        localSet = set()

        try:
            for i in children:
                localID = i.ID().getText()
                localSet.add(localID)
        except:
            pass

        self.genSet.append((label, localSet))

    def enterMultExp(self, ctx:MyCMinusParser.MultExpContext):
        label = ctx.parentCtx.__getattribute__("label")
        self.expressionSet(ctx, label)

    def enterArithmeticExp(self, ctx:MyCMinusParser.ArithmeticExpContext):
        label = ctx.parentCtx.__getattribute__("label")
        self.expressionSet(ctx, label)

    # def enterMultExp(self, ctx:MyCMinusParser.MultExpContext):
    #     child = ctx.children
    #     print(child)
    #     for i in range(len(child)):
    #         print(i.enterIdCall())

    def enterIdCall(self, ctx:MyCMinusParser.IdCallContext):
        return ctx.getText()

    def printGenSet(self):
        print("gen set: ")
        counter = 1
        index = 0
        while(counter < 6):
            genLabel = self.genSet[index][0]
            if (genLabel != counter):
                print("%s empty" % counter)
            else:
                print(self.genSet[index])
                index = index + 1
            counter += 1
