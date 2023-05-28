class TokenType:
    """Base class for token types"""

    def __init__(self):
        pass


class OpenParan(TokenType):
    def __str__(self):
        return "OpenParan"


class CloseParan(TokenType):
    def __str__(self):
        return "CloseParan"


class OpenBrace(TokenType):
    def __str__(self):
        return "OpenBrace"


class CloseBrace(TokenType):
    def __str__(self):
        return "CloseBrace"


class Comma(TokenType):
    def __str__(self):
        return "Comma"


class Dot(TokenType):
    def __str__(self):
        return "Dot"


class Minus(TokenType):
    def __str__(self):
        return "Minus"


class Plus(TokenType):
    def __str__(self):
        return "Plus"


class SemiColon(TokenType):
    def __str__(self):
        return "SemiColon"


class Slash(TokenType):
    def __str__(self):
        return "Slash"


class Star(TokenType):
    def __str__(self):
        return "Star"


class Bang(TokenType):
    def __str__(self):
        return "Bang"


class BangEqual(TokenType):
    def __str__(self):
        return "BangEqual"


class Equal(TokenType):
    def __str__(self):
        return "Equal"


class EqualEqual(TokenType):
    def __str__(self):
        return "EqualEqual"


class Greater(TokenType):
    def __str__(self):
        return "Greater"


class GreaterEqual(TokenType):
    def __str__(self):
        return "GreaterEqual"


class Less(TokenType):
    def __str__(self):
        return "Less"


class LessEqual(TokenType):
    def __str__(self):
        return "LessEqual"


class Identifier(TokenType):
    def __str__(self):
        return "Identifier"


class String(TokenType):
    def __str__(self):
        return "String"


class Number(TokenType):
    def __str__(self):
        return "Number"


class And(TokenType):
    def __str__(self):
        return "And"


class Class(TokenType):
    def __str__(self):
        return "Class"


class Else(TokenType):
    def __str__(self):
        return "Else"


class FALSE(TokenType):
    def __str__(self):
        return "FALSE"


class Fun(TokenType):
    def __str__(self):
        return "Fun"


class For(TokenType):
    def __str__(self):
        return "For"


class If(TokenType):
    def __str__(self):
        return "If"


class Null(TokenType):
    def __str__(self):
        return "Null"


class Or(TokenType):
    def __str__(self):
        return "Or"


class Print(TokenType):
    def __str__(self):
        return "Print"


class Return(TokenType):
    def __str__(self):
        return "Return"


class Super(TokenType):
    def __str__(self):
        return "Super"


class This(TokenType):
    def __str__(self):
        return "This"


class TRUE(TokenType):
    def __str__(self):
        return "TRUE"


class Var(TokenType):
    def __str__(self):
        return "Var"


class While(TokenType):
    def __str__(self):
        return "While"


class EOF(TokenType):
    def __str__(self):
        return "EOF"
