# Generated from myCminus_og/MyCMinus.g4 by ANTLR 4.5.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyCMinusParser import MyCMinusParser
else:
    from myCMinus.MyCMinusParser import MyCMinusParser

# This class defines a complete generic visitor for a parse tree produced by MyCMinusParser.

class MyCMinusVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyCMinusParser#blockLab.
    def visitBlockLab(self, ctx:MyCMinusParser.BlockLabContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#statListBlock.
    def visitStatListBlock(self, ctx:MyCMinusParser.StatListBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#statList.
    def visitStatList(self, ctx:MyCMinusParser.StatListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#singleStat.
    def visitSingleStat(self, ctx:MyCMinusParser.SingleStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#varType.
    def visitVarType(self, ctx:MyCMinusParser.VarTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#assignStat.
    def visitAssignStat(self, ctx:MyCMinusParser.AssignStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#printStat.
    def visitPrintStat(self, ctx:MyCMinusParser.PrintStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#expStat.
    def visitExpStat(self, ctx:MyCMinusParser.ExpStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#condStat.
    def visitCondStat(self, ctx:MyCMinusParser.CondStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#emptyStat.
    def visitEmptyStat(self, ctx:MyCMinusParser.EmptyStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#assignment.
    def visitAssignment(self, ctx:MyCMinusParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#ifCond.
    def visitIfCond(self, ctx:MyCMinusParser.IfCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#whileCond.
    def visitWhileCond(self, ctx:MyCMinusParser.WhileCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#ifStat.
    def visitIfStat(self, ctx:MyCMinusParser.IfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#ifelseStat.
    def visitIfelseStat(self, ctx:MyCMinusParser.IfelseStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#whileStat.
    def visitWhileStat(self, ctx:MyCMinusParser.WhileStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#logicalOrExp.
    def visitLogicalOrExp(self, ctx:MyCMinusParser.LogicalOrExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#logicalOrAnd.
    def visitLogicalOrAnd(self, ctx:MyCMinusParser.LogicalOrAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#logicalAnd.
    def visitLogicalAnd(self, ctx:MyCMinusParser.LogicalAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#logicalAndEQ.
    def visitLogicalAndEQ(self, ctx:MyCMinusParser.LogicalAndEQContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#equalityExpLab.
    def visitEqualityExpLab(self, ctx:MyCMinusParser.EqualityExpLabContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#relationEqExp.
    def visitRelationEqExp(self, ctx:MyCMinusParser.RelationEqExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#eqRelationExp.
    def visitEqRelationExp(self, ctx:MyCMinusParser.EqRelationExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#arithmeticExpLab.
    def visitArithmeticExpLab(self, ctx:MyCMinusParser.ArithmeticExpLabContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#relAritExp.
    def visitRelAritExp(self, ctx:MyCMinusParser.RelAritExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#aritMultExp.
    def visitAritMultExp(self, ctx:MyCMinusParser.AritMultExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#multExp.
    def visitMultExp(self, ctx:MyCMinusParser.MultExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#factorLab.
    def visitFactorLab(self, ctx:MyCMinusParser.FactorLabContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#multFactorExp.
    def visitMultFactorExp(self, ctx:MyCMinusParser.MultFactorExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#parExp.
    def visitParExp(self, ctx:MyCMinusParser.ParExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#numberCall.
    def visitNumberCall(self, ctx:MyCMinusParser.NumberCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#idCall.
    def visitIdCall(self, ctx:MyCMinusParser.IdCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#arrayCall.
    def visitArrayCall(self, ctx:MyCMinusParser.ArrayCallContext):
        return self.visitChildren(ctx)



del MyCMinusParser