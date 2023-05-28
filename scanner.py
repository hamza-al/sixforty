from token_type import *
from my_token import Token


class Scanner():
    """docstring for Scanner"""

    def __init__(self, cmd):
        self.cmd = cmd
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1
        self.keywords = {
            "and": And(),
            "class": Class(),
            "else": Else(),
            "false": FALSE(),
            "for": For(),
            "fun": Fun(),
            "if": If(),
            "nil": Null(),
            "or": Or(),
            "print": Print(),
            "return": Return(),
            "super": Super(),
            "this": This(),
            "true": TRUE(),
            "var": Var(),
            "while": While()
        }

    def scanTokens(self):
        char = self.advance()
        if char == '(':
            self.addToken(OpenParan())
        elif char == ')':
            self.addToken(CloseParan())
        elif char == '{':
            self.addToken(OpenBrace())
        elif char == '}':
            self.addToken(CloseBrace())
        elif char == ',':
            self.addToken(Comma())
        elif char == '.':
            if self.isDigit(self.nextChar()):
                self.advance()
                while self.isDigit(self.nextChar()):
                    self.advance()
                self.addToken(Number(), float(
                    self.cmd[self.start: self.current]))
            else:
                self.addToken(Dot())
        elif char == '-':
            self.addToken(Minus())
        elif char == '+':
            self.addToken(Plus())
        elif char == ';':
            self.addToken(SemiColon())
        elif char == '*':
            self.addToken(Star)
        elif char == '!':
            if self.nextIs('='):
                self.addToken(BangEqual())
            else:
                self.addToken(Bang())
        elif char == '=':
            if self.nextIs('='):
                self.addToken(EqualEqual())
            else:
                self.addToken(Equal())
        elif char == '<':
            if self.nextIs('='):
                self.addToken(LessEqual())
            else:
                self.addToken(Less())
        elif char == '>':
            if self.nextIs('='):
                self.addToken(GreaterEqual())
            else:
                self.addToken(Greater())
        elif char == '/':
            if self.nextIs('/'):
                pass
            else:
                self.addToken(Slash())
        elif char in [' ', '\r', '\t']:
            pass
        elif char == '\n':
            self.line += 1
        elif char in ["'", '"']:
            self.string(char)
        else:
            if self.isDigit(char):
                self.number()
            elif self.isAlpha(char):
                self.identifier()
            else:
                print(f'[line {self.line}]: Unexpected Character')
        return self.tokens

    def atEnd(self):
        return self.current >= len(self.cmd)

    def advance(self):
        advanced = self.cmd[self.current]
        self.current += 1
        return advanced

    def addToken(self, token, literal=None):
        text = self.cmd[self.start:self.current]
        self.tokens.append(Token(token, text, literal, self.line))

    def nextIs(self, expected):
        if self.atEnd():
            return False
        if self.cmd[self.current] != expected:
            return False
        self.current += 1
        return True

    def nextChar(self):
        if self.atEnd():
            return '\0'
        else:
            return self.cmd[self.current]

    def nextNextChar(self):
        if self.current + 1 >= len(self.cmd):
            return '\0'
        return self.cmd[self.current + 1]

    def string(self, quote):
        while self.nextChar() != quote and not self.atEnd():
            if self.nextChar() == '\n':
                self.line += 1
            self.advance()
        if self.atEnd():
            print(f'[line {self.line}]: Unterminated string.')
            return
        self.advance()
        value = self.cmd[self.start+1:self.current-1]
        self.addToken(String(), value)

    def isDigit(self, char):
        return char >= '0' and char <= '9'

    def number(self):
        while self.isDigit(self.nextChar()):
            self.advance()
        if self.nextChar() == '.' and self.isDigit(self.nextNextChar()):
            self.advance()
            while self.isDigit(self.nextChar()):
                self.advance()
        self.addToken(Number(), float(self.cmd[self.start: self.current]))

    def isAlpha(self, c):
        return (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or c == '_'

    def isAlphaNumeric(self, c):
        return self.isAlpha(c) or self.isDigit(c)

    def identifier(self):
        while self.isAlphaNumeric(self.nextChar()):
            self.advance()
        text = self.cmd[self.start:self.current]
        if text in self.keywords:
            self.addToken(self.keywords[text])
        else:
            self.addToken(Identifier())
