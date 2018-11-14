grammar MyCMinus;

/*
 Parser Rules
 */

program: statementList # mainProg;

statementList:
	(statement SEMI)+						# stat;

type_ID: INT | FLOAT | VOID | BOOL | STRING | CHAR # IDtype;

statement:
	type_ID ID (EQUALS expression)?	# varDeclStat
	| PRINT expression				# printStat
	| ID EQUALS expression			# assignment
	| IF LPAR expression RPAR LCURL statementList RCURL (
		ELSE LCURL statementList RCURL
	)? # ifelseStat
	// | RETURN expression? SEMI								# returnStat
	| expression	# expStat
	|				# emptyStat;

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

// RETURN: 'return';

ID: LETTER (DIGIT | LETTER)*;
NUMBER: DIGIT+ ('.' DIGIT+)?;

WS: [ \n\t]+ -> skip;