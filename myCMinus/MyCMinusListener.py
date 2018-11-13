# Generated from MyCMinus.g4 by ANTLR 4.5.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyCMinusParser import MyCMinusParser
else:
    from MyCMinusParser import MyCMinusParser

# This class defines a complete listener for a parse tree produced by MyCMinusParser.
class MyCMinusListener(ParseTreeListener):

    # Enter a parse tree produced by MyCMinusParser#mainProg.
    def enterMainProg(self, ctx:MyCMinusParser.MainProgContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#mainProg.
    def exitMainProg(self, ctx:MyCMinusParser.MainProgContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#statList.
    def enterStatList(self, ctx:MyCMinusParser.StatListContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#statList.
    def exitStatList(self, ctx:MyCMinusParser.StatListContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#stat.
    def enterStat(self, ctx:MyCMinusParser.StatContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#stat.
    def exitStat(self, ctx:MyCMinusParser.StatContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#type_ID.
    def enterType_ID(self, ctx:MyCMinusParser.Type_IDContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#type_ID.
    def exitType_ID(self, ctx:MyCMinusParser.Type_IDContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#varDeclStat.
    def enterVarDeclStat(self, ctx:MyCMinusParser.VarDeclStatContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#varDeclStat.
    def exitVarDeclStat(self, ctx:MyCMinusParser.VarDeclStatContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#printStat.
    def enterPrintStat(self, ctx:MyCMinusParser.PrintStatContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#printStat.
    def exitPrintStat(self, ctx:MyCMinusParser.PrintStatContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#assignment.
    def enterAssignment(self, ctx:MyCMinusParser.AssignmentContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#assignment.
    def exitAssignment(self, ctx:MyCMinusParser.AssignmentContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#ifelseStat.
    def enterIfelseStat(self, ctx:MyCMinusParser.IfelseStatContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#ifelseStat.
    def exitIfelseStat(self, ctx:MyCMinusParser.IfelseStatContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#expStat.
    def enterExpStat(self, ctx:MyCMinusParser.ExpStatContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#expStat.
    def exitExpStat(self, ctx:MyCMinusParser.ExpStatContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#emptyStat.
    def enterEmptyStat(self, ctx:MyCMinusParser.EmptyStatContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#emptyStat.
    def exitEmptyStat(self, ctx:MyCMinusParser.EmptyStatContext):
        pass


    # Enter a parse tree produced by MyCMinusParser#varDeclaration.
    def enterVarDeclaration(self, ctx:MyCMinusParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#varDeclaration.
    def exitVarDeclaration(self, ctx:MyCMinusParser.VarDeclarationContext):
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


    # Enter a parse tree produced by MyCMinusParser#IDcall.
    def enterIDcall(self, ctx:MyCMinusParser.IDcallContext):
        pass

    # Exit a parse tree produced by MyCMinusParser#IDcall.
    def exitIDcall(self, ctx:MyCMinusParser.IDcallContext):
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


