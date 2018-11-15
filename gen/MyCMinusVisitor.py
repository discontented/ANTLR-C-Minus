# Generated from C:/Users/jcorn/PycharmProjects/python-p4/grammar/ebnf\MyCMinus.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyCMinusParser import MyCMinusParser
else:
    from MyCMinusParser import MyCMinusParser

# This class defines a complete generic visitor for a parse tree produced by MyCMinusParser.

class MyCMinusVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyCMinusParser#program.
    def visitProgram(self, ctx:MyCMinusParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#statementList.
    def visitStatementList(self, ctx:MyCMinusParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#varType.
    def visitVarType(self, ctx:MyCMinusParser.VarTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#varDeclStat.
    def visitVarDeclStat(self, ctx:MyCMinusParser.VarDeclStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#assignment.
    def visitAssignment(self, ctx:MyCMinusParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#printStat.
    def visitPrintStat(self, ctx:MyCMinusParser.PrintStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#conditionalStat.
    def visitConditionalStat(self, ctx:MyCMinusParser.ConditionalStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#expStat.
    def visitExpStat(self, ctx:MyCMinusParser.ExpStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#block.
    def visitBlock(self, ctx:MyCMinusParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#ifStatement.
    def visitIfStatement(self, ctx:MyCMinusParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#whileStatement.
    def visitWhileStatement(self, ctx:MyCMinusParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#relationExp.
    def visitRelationExp(self, ctx:MyCMinusParser.RelationExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#arithmeticExp.
    def visitArithmeticExp(self, ctx:MyCMinusParser.ArithmeticExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#idCall.
    def visitIdCall(self, ctx:MyCMinusParser.IdCallContext):
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