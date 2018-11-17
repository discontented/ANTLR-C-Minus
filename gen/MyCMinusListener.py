# Generated from C:/Users/jcorn/PycharmProjects/python-p4/grammar/ebnf\MyCMinus.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyCMinusParser import MyCMinusParser
else:
    from MyCMinusParser import MyCMinusParser

# This class defines a complete listener for a parse tree produced by MyCMinusParser.
class MyCMinusListener(ParseTreeListener):

    # Enter a parse tree produced by MyCMinusParser#program.
    def enterProgram(self, ctx:MyCMinusParser.ProgramContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#program.
    def exitProgram(self, ctx:MyCMinusParser.ProgramContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#statementList.
    def enterStatementList(self, ctx:MyCMinusParser.StatementListContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#statementList.
    def exitStatementList(self, ctx:MyCMinusParser.StatementListContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#varType.
    def enterVarType(self, ctx:MyCMinusParser.VarTypeContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#varType.
    def exitVarType(self, ctx:MyCMinusParser.VarTypeContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#varSingleDecl.
    def enterVarSingleDecl(self, ctx:MyCMinusParser.VarSingleDeclContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#varSingleDecl.
    def exitVarSingleDecl(self, ctx:MyCMinusParser.VarSingleDeclContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#varDeclStat.
    def enterVarDeclStat(self, ctx:MyCMinusParser.VarDeclStatContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#varDeclStat.
    def exitVarDeclStat(self, ctx:MyCMinusParser.VarDeclStatContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#assignment.
    def enterAssignment(self, ctx:MyCMinusParser.AssignmentContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#assignment.
    def exitAssignment(self, ctx:MyCMinusParser.AssignmentContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#printStat.
    def enterPrintStat(self, ctx:MyCMinusParser.PrintStatContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#printStat.
    def exitPrintStat(self, ctx:MyCMinusParser.PrintStatContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#conditionalStat.
    def enterConditionalStat(self, ctx:MyCMinusParser.ConditionalStatContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#conditionalStat.
    def exitConditionalStat(self, ctx:MyCMinusParser.ConditionalStatContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#expStat.
    def enterExpStat(self, ctx:MyCMinusParser.ExpStatContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#expStat.
    def exitExpStat(self, ctx:MyCMinusParser.ExpStatContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#block.
    def enterBlock(self, ctx:MyCMinusParser.BlockContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#block.
    def exitBlock(self, ctx:MyCMinusParser.BlockContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#ifStatement.
    def enterIfStatement(self, ctx:MyCMinusParser.IfStatementContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#ifStatement.
    def exitIfStatement(self, ctx:MyCMinusParser.IfStatementContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#whileStatement.
    def enterWhileStatement(self, ctx:MyCMinusParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#whileStatement.
    def exitWhileStatement(self, ctx:MyCMinusParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#relationExp.
    def enterRelationExp(self, ctx:MyCMinusParser.RelationExpContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#relationExp.
    def exitRelationExp(self, ctx:MyCMinusParser.RelationExpContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#arithmeticExp.
    def enterArithmeticExp(self, ctx:MyCMinusParser.ArithmeticExpContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#arithmeticExp.
    def exitArithmeticExp(self, ctx:MyCMinusParser.ArithmeticExpContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#idCall.
    def enterIdCall(self, ctx:MyCMinusParser.IdCallContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#idCall.
    def exitIdCall(self, ctx:MyCMinusParser.IdCallContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#unaryExp.
    def enterUnaryExp(self, ctx:MyCMinusParser.UnaryExpContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#unaryExp.
    def exitUnaryExp(self, ctx:MyCMinusParser.UnaryExpContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#equalityExp.
    def enterEqualityExp(self, ctx:MyCMinusParser.EqualityExpContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#equalityExp.
    def exitEqualityExp(self, ctx:MyCMinusParser.EqualityExpContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#parExp.
    def enterParExp(self, ctx:MyCMinusParser.ParExpContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#parExp.
    def exitParExp(self, ctx:MyCMinusParser.ParExpContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#multExp.
    def enterMultExp(self, ctx:MyCMinusParser.MultExpContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#multExp.
    def exitMultExp(self, ctx:MyCMinusParser.MultExpContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#funcCall.
    def enterFuncCall(self, ctx:MyCMinusParser.FuncCallContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#funcCall.
    def exitFuncCall(self, ctx:MyCMinusParser.FuncCallContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#primNum.
    def enterPrimNum(self, ctx:MyCMinusParser.PrimNumContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#primNum.
    def exitPrimNum(self, ctx:MyCMinusParser.PrimNumContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#logicalExp.
    def enterLogicalExp(self, ctx:MyCMinusParser.LogicalExpContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#logicalExp.
    def exitLogicalExp(self, ctx:MyCMinusParser.LogicalExpContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#arrayCall.
    def enterArrayCall(self, ctx:MyCMinusParser.ArrayCallContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#arrayCall.
    def exitArrayCall(self, ctx:MyCMinusParser.ArrayCallContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#expressionList.
    def enterExpressionList(self, ctx:MyCMinusParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#expressionList.
    def exitExpressionList(self, ctx:MyCMinusParser.ExpressionListContext):
        pass


