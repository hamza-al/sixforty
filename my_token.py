from token_type import *


class Token():

    def __init__(self, kind, lexeme, literal, line):
        self.kind = kind
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self):
        return f'kind: {self.kind},\nLexeme: {self.lexeme}\nLiteral: {self.literal}'
