grammar MyCMinus;

/*
 Parser Rules
 */

program: block ;

block: LCURL statementList RCURL
    ;

statementList:
	statementList SEMI statement
	| statement
	;

// varDecl: vartype ID (EQUALS expression)? SEMI # varDeclaration;

varType: INT | FLOAT | VOID | BOOL | STRING | CHAR
;

statement:
	assignStatement
	| PRINT expression
	| expression
	| conditionalStat
	|
	;

assignStatement: varType ID EQUALS expression;

conditionalStat:
	ifStatement
	| whileStatement
	;

ifStatement:
	IF LPAR expression RPAR block
	| IF LPAR expression RPAR block ELSE block
	;

whileStatement: WHILE LPAR expression RPAR block ;

expression: logical_or_expr ;

logical_or_expr:
	logical_and_expr
	| logical_or_expr OR logical_and_expr
	;

logical_and_expr:
	equalityExp
	| logical_and_expr AND equalityExp
	;

equalityExp:
	relationExp
	| equalityExp (EQUALTO | NOTEQ) relationExp
	;

relationExp:
	arithmeticExp
	| relationExp (LTHAN | GTHAN | LEQUAL | GEQUAL) arithmeticExp
	;

arithmeticExp:
	arithmeticExp (PLUS | MINUS) multiplicativeExp
	| multiplicativeExp
	;

multiplicativeExp:
	multiplicativeExp (TIMES | DIVIDE) factor
	| factor
	;

factor:
	LPAR expression RPAR
	| NUMBER
	| ID
	| ID LBRAC NUMBER RBRAC
	;

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