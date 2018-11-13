# Generated from MyCMinus.g4 by ANTLR 4.5.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyCMinusParser import MyCMinusParser
else:
    from MyCMinusParser import MyCMinusParser

# This class defines a complete generic visitor for a parse tree produced by MyCMinusParser.

class MyCMinusVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyCMinusParser#mainProg.
    def visitMainProg(self, ctx:MyCMinusParser.MainProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#statList.
    def visitStatList(self, ctx:MyCMinusParser.StatListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#stat.
    def visitStat(self, ctx:MyCMinusParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#type_ID.
    def visitType_ID(self, ctx:MyCMinusParser.Type_IDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#varDeclStat.
    def visitVarDeclStat(self, ctx:MyCMinusParser.VarDeclStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#printStat.
    def visitPrintStat(self, ctx:MyCMinusParser.PrintStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#assignment.
    def visitAssignment(self, ctx:MyCMinusParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#ifelseStat.
    def visitIfelseStat(self, ctx:MyCMinusParser.IfelseStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#expStat.
    def visitExpStat(self, ctx:MyCMinusParser.ExpStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#emptyStat.
    def visitEmptyStat(self, ctx:MyCMinusParser.EmptyStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#varDeclaration.
    def visitVarDeclaration(self, ctx:MyCMinusParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#relationExp.
    def visitRelationExp(self, ctx:MyCMinusParser.RelationExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#arithmeticExp.
    def visitArithmeticExp(self, ctx:MyCMinusParser.ArithmeticExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#unaryExp.
    def visitUnaryExp(self, ctx:MyCMinusParser.UnaryExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#equalityExp.
    def visitEqualityExp(self, ctx:MyCMinusParser.EqualityExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#parExp.
    def visitParExp(self, ctx:MyCMinusParser.ParExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#IDcall.
    def visitIDcall(self, ctx:MyCMinusParser.IDcallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#multExp.
    def visitMultExp(self, ctx:MyCMinusParser.MultExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#funcCall.
    def visitFuncCall(self, ctx:MyCMinusParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#primNum.
    def visitPrimNum(self, ctx:MyCMinusParser.PrimNumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#logicalExp.
    def visitLogicalExp(self, ctx:MyCMinusParser.LogicalExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#arrayCall.
    def visitArrayCall(self, ctx:MyCMinusParser.ArrayCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#expressionList.
    def visitExpressionList(self, ctx:MyCMinusParser.ExpressionListContext):
        return self.visitChildren(ctx)



del MyCMinusParser