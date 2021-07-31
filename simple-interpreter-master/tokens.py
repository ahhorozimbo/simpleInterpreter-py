from enum import Enum

class TokenType(Enum):
    Sum = 1
    Sub = 2
    Div = 3
    Mult = 4
    OpenParen = 5
    CloseParen = 6
    Eol = 7
    Equal = 8
    Var = 9
    Print = 10
    Int = 11
    Float = 12
    Invalid = -1
class Token:
    def __init__(self, typeToken, attributeToken=None):
        self.type = typeToken
        self.attribute = attributeToken
