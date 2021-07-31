"""
Grammar:
    # prog ::= stmt EOL lines
    # lines::= prog | ε
    # stmt ::= attr | imp
    # attr  ::= VAR EQ expr
    # imp  ::= PRINT OPEN VAR CLOSE
    # expr ::= fact SUM expr | fact SUB expr | fact
    # fact ::= term MULT fact | term DIV fact | term
    # term ::= OPEN expr CLOSE | NUM | VAR
"""



from tokens import TokenType, Token

class SimpleParser: 
    def __init__(self, lexer):
        self.lexer = lexer
        self.lookahead = lexer.generateTokens()
        self.output = str()

    def prog(self): # prog ::= stmt EOL lines
        self.stmt()
        self.match(self.lookahead)
        self.lines()

    def lines(self): # lines::= prog | ε
        if self.lookahead.type != TokenType.Invalid:
            self.prog()

    def stmt(self): # stmt ::= attr | imp
        if self.lookahead.type == TokenType.Var:
            self.attr()
        elif self.lookahead.type == TokenType.Print:
            self.imp()
        

    def attr(self):# attr  ::= VAR EQ expr
        ref = self.lookahead.attribute  
        self.match(self.lookahead) 
        self.match(self.lookahead)
        resultExpr = self.expr()
        self.lexer.symbolTable[ref] = resultExpr
        
    def imp(self): # attr  ::= VAR EQ expr
        self.match(self.lookahead)  
        self.match(self.lookahead)  
        ref = self.lookahead.attribute
        if ref in self.lexer.symbolTable:
            value = self.lexer.symbolTable[ref]
            print(value)
        else:
            print('Symbol not defined.')
        self.match(self.lookahead)  
        self.match(self.lookahead)  


    def expr(self): # expr ::= fact SUM expr | fact SUB expr | fact
        resultFactor = self.factor()
        if self.lookahead.type == TokenType.Sum:
            self.match(self.lookahead) 
            resultExpr = self.expr()
            return resultFactor + resultExpr
        elif self.lookahead.type == TokenType.Sub:
            self.match(self.lookahead)  
            resultExpr = self.expr()
            return resultFactor - resultExpr
        else:
            return resultFactor

    def factor(self):# fact ::= term MULT fact | term DIV fact | term
    
        result_term = self.term()  
        if self.lookahead.type == TokenType.Mult:
            self.match(self.lookahead)  
            resultFactor = self.factor()
            return result_term * resultFactor
        elif self.lookahead.type == TokenType.Div:
            self.match(self.lookahead)
            resultFactor = self.factor()
            return result_term / resultFactor
        else:
            return result_term

    def term(self): # term ::= OPEN expr CLOSE | NUM | VAR
        if self.lookahead.type == TokenType.OpenParen:
            self.match(self.lookahead)  
            resultExpr = self.expr()   
            self.match(self.lookahead)  
            return resultExpr
        elif self.lookahead.type == TokenType.Var:
            name = self.lookahead.attribute
            self.match(self.lookahead)
            return self.lexer.symbolTable[name]
        elif self.lookahead.type == TokenType.Int:
            value = int(self.lookahead.attribute)
            self.match(self.lookahead)
            return value
        elif self.lookahead.type == TokenType.Float:
            value = float(self.lookahead.attribute)
            self.match(self.lookahead)
            return value

    def match(self, token):
        if (self.lookahead.type == token.type
                and self.lookahead.attribute == token.attribute):
            self.lookahead = self.lexer.generateTokens()
        else:
            print("\n *** Syntax Error! Values do not match. ***\n")
