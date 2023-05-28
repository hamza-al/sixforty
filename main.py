import sys
from scanner import Scanner


class SixForty():
    def __init__(self):
        self.hadError = False
        self.args = sys.argv[1:]

    def main(self):

        if len(self.args) > 1:
            print('Usage: hmz [script]')
            sys.exit(64)

        elif len(self.args) == 1:
            self.runFile(self.args[0])

        else:

            self.repl()

    def runFile(self, file):
        with open(file, 'r') as file:
            content = file.read()
            self.run(content)

    def repl(self):
        while True:
            line = input("> ")
            if line is None:
                break
            self.run(line)

    def run(self, cmd):
        scanner = Scanner(cmd)
        tokens = scanner.scanTokens()
        for token in tokens:
            print(f'{token}\n')

    def error(self, line, msg):
        self.report(line, "", msg)

    def report(self, line, where, msg):
        print(f'[line {line}]{where}: {msg}')


if __name__ == '__main__':
    main = SixForty()
    main.main()
