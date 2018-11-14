# Generated from C:/Users/jcorn/PycharmProjects/python-p4/grammar/og\MyCMinus.g4 by ANTLR 4.7
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


    # Visit a parse tree produced by MyCMinusParser#block.
    def visitBlock(self, ctx:MyCMinusParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#statementList.
    def visitStatementList(self, ctx:MyCMinusParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#varType.
    def visitVarType(self, ctx:MyCMinusParser.VarTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#statement.
    def visitStatement(self, ctx:MyCMinusParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#assignStatement.
    def visitAssignStatement(self, ctx:MyCMinusParser.AssignStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#conditionalStat.
    def visitConditionalStat(self, ctx:MyCMinusParser.ConditionalStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#ifStatement.
    def visitIfStatement(self, ctx:MyCMinusParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#whileStatement.
    def visitWhileStatement(self, ctx:MyCMinusParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#expression.
    def visitExpression(self, ctx:MyCMinusParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#logical_or_expr.
    def visitLogical_or_expr(self, ctx:MyCMinusParser.Logical_or_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#logical_and_expr.
    def visitLogical_and_expr(self, ctx:MyCMinusParser.Logical_and_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#equalityExp.
    def visitEqualityExp(self, ctx:MyCMinusParser.EqualityExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#relationExp.
    def visitRelationExp(self, ctx:MyCMinusParser.RelationExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#arithmeticExp.
    def visitArithmeticExp(self, ctx:MyCMinusParser.ArithmeticExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#multiplicativeExp.
    def visitMultiplicativeExp(self, ctx:MyCMinusParser.MultiplicativeExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyCMinusParser#factor.
    def visitFactor(self, ctx:MyCMinusParser.FactorContext):
        return self.visitChildren(ctx)



del MyCMinusParser