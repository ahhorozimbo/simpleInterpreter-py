from tokens import TokenType, Token

WHITESPACE = ' \n\t'
DIGITS = '0123456789'

class SimpleLexer:
    def __init__(self, text):
        self.current_Char = -1
        entry = open(text, 'r').readlines()
        self.input = str()
        self.symbolTable = dict()
        for i in entry:
            for j in i:
                if j not in WHITESPACE:
                    self.input = self.input + j
    def advance(self):
        if self.current_Char < len(self.input)-1:
            self.current_Char += 1
            return self.input[self.current_Char]
        return ' '
    def verify(self):
        while True:
            a = self.generateTokens()
            print(f'{a.type}, {a.attribute}')
            if a.type == TokenType.Invalid:
                break
    
    def generateTokens(self):
        currentChar = self.advance()
        if currentChar == '+':
            return Token(TokenType.Sum, '+')
        elif currentChar == '-':
            return Token(TokenType.Sub, '-')
        elif currentChar == '*':
            return Token(TokenType.Mult, '*')
        elif currentChar == '/':
            return Token(TokenType.Div, '/')
        elif currentChar == '(':
            return Token(TokenType.OpenParen)
        elif currentChar == ')':
            return Token(TokenType.CloseParen)
        elif currentChar == ';':
            return Token(TokenType.Eol)
        elif currentChar == '=':
            return Token(TokenType.Equal) 
        elif currentChar in DIGITS:
            num = str()
            while True:
                num = num + currentChar
                currentChar = self.advance()
                if not currentChar.isnumeric():
                    self.current_Char -= 1
                    break
            if '.' in num:
                return Token(TokenType.Float, num)
            return Token(TokenType.Int, num)
        elif currentChar == '$':
            var = str()
            while True:
                var = var + currentChar
                currentChar = self.advance()
                if not currentChar.isalnum():
                    self.current_Char -= 1
                    break
            return Token(TokenType.Var, var)
        elif currentChar == 'p':
            cmd = str()
            while True:
                cmd = cmd+ currentChar
                currentChar = self.advance()
                if currentChar == '(':
                    self.current_Char -= 1
                    break
            return Token(TokenType.Print)
        
        else:
            return Token(TokenType.Invalid)
           

    
