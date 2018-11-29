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
    finalKillSet = []

    def enterVarDeclStat(self, ctx: MyCMinusParser.VarDeclStatContext):
        labeller(self.killSet, ctx)

    def enterAssignment(self, ctx: MyCMinusParser.AssignmentContext):
        labeller(self.killSet, ctx)

    def printKillSet(self, labels):
        counter = 1
        index = 0
        while (counter <= labels):
            if (index < len(self.killSet)):
                genLabel = self.killSet[index][0]
            else:
                genLabel = -1
            if (genLabel != counter):
                self.finalKillSet.append((counter, "{empty}"))
            else:
                self.finalKillSet.append(self.killSet[index])
                index = index + 1
            counter += 1

        print("kill set: ")
        for i in self.finalKillSet:
            print(i)

class GenListener(MyCMinusListener):
    # [ 1: {x,y}, 2: {null} ]
    genSet = []
    finalGenSet = []

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
            if(isinstance(children, list)):
                for i in children:
                    localID = i.ID().getText()
                    localSet.add(localID)
            else:
                localSet.add(children.ID().getText())
        except:
            pass
        if(len(localSet) > 0):
            self.genSet.append((label, localSet))


    def enterVarDeclStat(self, ctx:MyCMinusParser.VarDeclStatContext):
        # label = ctx.parentCtx.__getattribute__("label")
        label = ctx.__getattribute__("label")
        self.expressionSet(ctx, label)

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

    def enterConditionalStat(self, ctx:MyCMinusParser.ConditionalStatContext):
        label = ctx.__getattribute__("label")
        self.expressionSet(ctx.conditionalStatement().expression(), label)

    def enterAssignment(self, ctx:MyCMinusParser.AssignmentContext):
        label = ctx.__getattribute__("label")
        self.expressionSet(ctx, label)

    def printGenSet(self, labels):
        counter = 1
        index = 0
        while(counter <= labels):
            if (index < len(self.genSet)):
                genLabel = self.genSet[index][0]
            else:
                genLabel = -1
            if (genLabel != counter):
                self.finalGenSet.append(( counter, "{empty}"))
            else:
                self.finalGenSet.append(self.genSet[index])
                index = index + 1
            counter += 1

        print("gen set: ")
        for i in self.finalGenSet:
            print(i)
