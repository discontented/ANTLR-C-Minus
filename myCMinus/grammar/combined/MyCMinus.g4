grammar MyCMinus;

/*
 Parser Rules
 */

program: statementList ;

statementList:
	statementList SEMI statement
	| statement
	;

// varDecl: vartype ID (EQUALS expression)? SEMI # varDeclaration;

varType: INT | FLOAT | VOID | BOOL | STRING | CHAR # IDtype;

statement:
	assignStatement
	| PRINT expression
	| expression
	| conditionalStat
	| LCURL statementList RCURL
	|
	;

assignStatement: varType ID EQUALS expression;

conditionalStat:
	ifStatement
	| whileStatement
	;

ifStatement:
	IF LPAR expression RPAR statement (ELSE statement)?  ;

whileStatement: WHILE LPAR expression RPAR statementList ;

expression:
	ID LBRAC expression RBRAC									# arrayCall
	| NOT expression											# unaryExp
	| expression (OR | AND) expression							# logicalExp
	| expression (LTHAN | GTHAN | LEQUAL | GEQUAL) expression	# relationExp
	| expression (EQUALTO | NOTEQ) expression					# equalityExp
	| expression (PLUS | MINUS) expression						# arithmeticExp
	| expression (TIMES | DIVIDE) expression					# multExp
	| ID														# idCall
	| NUMBER													# primNum
	| LPAR expression RPAR										# parExp;
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

WS: [ \r\n\t]+ -> skip;