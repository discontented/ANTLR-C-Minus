grammar MyCMinus;

/*
 Parser Rules
 */

program: (functionDecl | varDecl)+ # mainProg;

varDecl: type ID (EQUALS expression)? SEMI # varDeclaration;

type: INT | FLOAT | VOID | BOOL | STRING | CHAR # IDtype;

functionDecl:
	type ID LPAR parameters? RPAR block # functionDeclaration;

parameters: parameter (COMMA parameter)* # parameterList;

parameter: type ID # funcPar;

block: LCURL (statement)* RCURL # blockStat;

statement:
	varDecl SEMI									# varDeclStat
	| PRINT expression SEMI							# printStat
	| ID EQUALS expression SEMI						# assignment
	| IF LPAR expression RPAR block (ELSE block)?	# ifelseStat
	| RETURN expression? SEMI						# returnStat
	| expression SEMI								# expStat
	| SEMI											# emptyStat;

expression:
	ID LPAR exprList? RPAR										# funcCall
	| ID LBRAC expression RBRAC									# arrayCall
	| NOT expression											# unaryExp
	| expression (OR | AND) expression							# logicalExp
	| expression (LTHAN | GTHAN | LEQUAL | GEQUAL) expression	# relationExp
	| expression (EQUALTO | NOTEQ) expression					# equalityExp
	| expression (PLUS | MINUS) expression						# arithmeticExp
	| expression (TIMES | DIVIDE) expression					# multExp
	| ID														# IDcall
	| NUMBER													# primNum
	| LPAR expression RPAR										# parExp;

exprList: expression (COMMA expression)* # expressionList;

/*
 lexer rules
 */

fragment DIGIT: [0-9];
fragment LETTER: [a-zA-Z];

IF: 'if';
ELSE: 'else';
WHILE: 'while';
PRINT: 'print';

LPAR: '(';
RPAR: ')';
LCURL: '{';
RCURL: '}';
LBRAC: '[';
RBRAC: ']';

SEMI: ';';
COMMA: ',';
PLUS: '+';
MINUS: '-';
TIMES: '*';
DIVIDE: '/';
EQUALS: '=';

AND: '&&';
OR: '||';
NOT: '!';

EQUALTO: '==';
GTHAN: '>';
GEQUAL: '>=';
LTHAN: '<';
LEQUAL: '<=';
NOTEQ: '!=';

INT: 'int';
FLOAT: 'float';
VOID: 'void';
STRING: 'string';
CHAR: 'char';
BOOL: 'bool';

RETURN: 'return';

ID: LETTER (DIGIT | LETTER)*;
NUMBER: DIGIT+ ('.' DIGIT+)?;

WS: [ \n\t]+ -> skip;