from antlr4 import *
from forthLexer import forthLexer 
from forthParser import forthParser 
from forthVisitor import forthVisitor 
from stack import Stack
from boolean import Boolean


class EvalVisitor (forthVisitor):
    def __init__(self):
        self.stack = Stack()
        self.functions = {}
        self.current_function_name = None
        self.opsArithmetic = {
            '+':   lambda x,y : x + y,
            '-':   lambda x,y : x - y,
            '*':   lambda x,y : x * y,
            '/': lambda x,y : (Exception("Error: divisió per zero")) if y == 0 else x / y ,
            'mod':   lambda x,y : x % y
        }
        
        self.opsBoolean = {
            'and': lambda x,y : Boolean._and(x,y),
            'or' : lambda x,y : Boolean._or(x,y),
            '>'  : lambda x,y : Boolean.bool2int(x > y),
            '>=' : lambda x,y : Boolean.bool2int(x >= y),
            '<'  : lambda x,y : Boolean.bool2int(x < y),
            '<=' : lambda x,y : Boolean.bool2int(x <= y),
            '==' : lambda x,y : Boolean.bool2int(x == y),
            '<>' : lambda x,y : Boolean.bool2int(x != y)
        }
        
        self.opsStackFront = {
            '.':     self.stack.printOne,
            '.s':    self.stack.printAll,
            'dup':   self.stack.dup,
            '2dup':  self.stack.dup2,
            'over':  self.stack.over,
            '2over': self.stack.over2,
            'rot':   self.stack.rot,
            'drop':  self.stack.drop,
            '2drop': self.stack.drop2,
            'swap':  self.stack.swap,
            '2swap': self.stack.swap2
        }
    def clear(self):
        self.stack.clear()
        
    def visitNumero(self,ctx):
        [numero] = list(ctx.getChildren())
        self.stack.push(int(numero.getText()))
        
    def visitArithmetic(self,ctx):
        n = self.stack.pop()
        m = self.stack.pop()
        self.stack.push(self.opsArithmetic.get(ctx.getText())(m,n))
        
    def visitStack(self,ctx):
        self.opsStackFront.get(ctx.getText())()
        
    def visitBoolean(self,ctx):
        op = ctx.getText()
        if(op == 'not') :
            a = self.stack.pop()
            self.stack.push(Boolean._not(a))
            return
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.push(self.opsBoolean.get(op)(b,a))
    
    def visitDefFunction(self, ctx):
        name = ctx.ID().getText()
        bodies = ctx.statement()         # list+ : returns [list1, list2, ...]
        self.functions[name] = bodies

    def visitBlock(self,ctx):
        for st in ctx.statement():
            self.visit(st)
    
    def visitCallFunction(self, ctx):
        name = ctx.getText()
        prevName = self.current_function_name
        if name == 'recurse':
            if prevName is None:
                raise Exception("Error: 'recurse' used outside of a function")
    
            self.current_function_name = prevName
            for body in self.functions[prevName]:
                self.visit(body)
            self.current_function_name = prevName
            return
    
        if name not in self.functions:
            raise Exception(f"Undefined function: {name}")
    
        self.current_function_name = name
        for body in self.functions[name]:
            self.visit(body)
        self.current_function_name = prevName
        


    def visitCondIf(self, ctx):
        body = ctx.block()          
        if self.stack.popBoolean() == -1:
            self.visit(body)


    def visitCondIfElse(self, ctx):
        bodyIf = ctx.block(0)
        bodyElse = ctx.block(1)   
        if self.stack.popBoolean() == -1:
            self.visit(bodyIf)
        else:
            self.visit(bodyElse)
    

import io
import sys
def interpret(code : str) -> str:
    visitor = EvalVisitor()
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    try:
        input_stream = InputStream(code)
        lexer = forthLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = forthParser(token_stream)
        tree = parser.root()
        visitor.visit(tree)
        return sys.stdout.getvalue().strip()
    finally:
        sys.stdout = old_stdout
