grammar MyCMinus;

/*
 Parser Rules
 */

program: block # blockLab;

block: LCURL statementList RCURL # statListBlock;

statementList:
	statementList SEMI statement	# statList
	| statement						# singleStat;

// varDecl: vartype ID (EQUALS expression)? SEMI # varDeclaration;

varType: INT | FLOAT | VOID | BOOL | STRING | CHAR # IDtype;

statement:
	assignStatement		# assignStat
	| PRINT expression	# printStat
	| expression		# expStat
	| conditionalStat	# condStat
	|					# emptyStat;

assignStatement: varType ID EQUALS expression # assignment;

conditionalStat:
	ifStatement			# ifCond
	| whileStatement	# whileCond;

ifStatement:
	IF LPAR expression RPAR block				# ifStat
	| IF LPAR expression RPAR block ELSE block	# ifelseStat;

whileStatement: WHILE LPAR expression RPAR block # whileStat;

expression: logical_or_expr # logicalOrExp;

logical_or_expr:
	logical_and_expr						# logicalAnd
	| logical_or_expr OR logical_and_expr	# logicalOrAnd;

logical_and_expr:
	equalityExp							# equalityExpLab
	| logical_and_expr AND equalityExp	# logicalAndEQ;

equalityExp:
	relationExp									# relationEqExp
	| equalityExp (EQUALTO | NOTEQ) relationExp	# eqRelationExp;

relationExp:
	arithmeticExp													# arithmeticExpLab
	| relationExp (LTHAN | GTHAN | LEQUAL | GEQUAL) arithmeticExp	# relAritExp;

arithmeticExp:
	arithmeticExp (PLUS | MINUS) multiplicativeExp	# aritMultExp
	| multiplicativeExp								# multExp;

multiplicativeExp:
	multiplicativeExp (TIMES | DIVIDE) factor	# multFactorExp
	| factor									# factorLab;

factor:
	LPAR expression RPAR	# parExp
	| NUMBER				# numberCall
	| ID					# idCall
	| ID LBRAC NUMBER RBRAC	# arrayCall;

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