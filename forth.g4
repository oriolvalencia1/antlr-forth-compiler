
grammar forth;

root : expr+ ;

expr :  defFunction   # deffunction
    | NUM             # numero
    | opArithmetic    # arithmetic
    | opStack         # stack
    | opBoolean       # boolean
    | callFunction    # callfunction
    ;

opArithmetic : ('+'|'-'|'*'|'/'|'mod') ;

opStack : ('swap'|'2swap'|'dup'|'2dup'|'over'|'2over'|'rot'|'drop'|'2drop'|'.s'|'.') ;
    
opBoolean : ('and'|'or'|'not'|'<>'|'=='|'>'|'<'|'>='|'<=') ;

defFunction : ':' ID statement+ ';' ;

block : statement* ;

statement : expr
    | condIf
    | condIfElse
    ;

condIf :'if' block 'endif' ;                   
condIfElse :'if' block 'else' block 'endif' ;  

callFunction : ID ;

ID : [a-z]+ ;

NUM : '-'? [0-9]+ ;
WS : [ \t\n\r]+ -> skip ;