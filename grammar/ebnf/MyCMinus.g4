grammar MyCMinus;

/*
 Parser Rules
 */

program: statementList ;

statementList:
	(statement SEMI)*
	;

varType: INT | FLOAT | VOID | BOOL | STRING | CHAR ;

statement:
    varType ID                      #varSingleDecl
	| varType ID EQUALS expression	# varDeclStat
	| ID EQUALS expression			# assignment
	| PRINT expression				# printStat
	| conditionalStatement          # conditionalStat
	| expression	                # expStat
	| LCURL statementList RCURL     # block
	;

conditionalStatement:
	IF LPAR expression RPAR statement (ELSE statement)?     #ifStatement
	| WHILE LPAR expression RPAR statement                  #whileStatement
	;

expression:
	ID LPAR exprList? RPAR										# funcCall
	| ID LBRAC expression RBRAC									# arrayCall
	| NOT expression											# unaryExp
	| expression (OR | AND) expression							# logicalExp
	| expression (LTHAN | GTHAN | LEQUAL | GEQUAL) expression	# relationExp
	| expression (EQUALTO | NOTEQ) expression					# equalityExp
	| expression (PLUS | MINUS) expression						# arithmeticExp
	| expression (TIMES | DIVIDE) expression					# multExp
	| ID														# idCall
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

ID: LETTER (DIGIT | LETTER)*;
NUMBER: DIGIT+ ('.' DIGIT+)?;

WS: [ \r\n\t]+ -> skip;