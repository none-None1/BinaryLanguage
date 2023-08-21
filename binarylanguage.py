import sys, argparse


class BinaryLanguageMachine:
    def __init__(self, program):
        self.a = 0
        self.b = 0
        self.c = 0
        self.program = program

    def run(self, debug=False):
        stack = []
        matches = {}
        for i, j in enumerate(self.program):
            if j == "(":
                stack.append(i)
            if j == ")":
                if not stack:
                    raise Exception("Unmatched )")
                mat = stack.pop()
                matches[mat] = i
                matches[i] = mat
        if stack:
            raise Exception("Unmatched (")
        ip = 0
        while ip < len(self.program):
            cmd = self.program[ip]
            if debug:
                print(
                    "IP: {}    Command: {}    A={} B={} C={}".format(
                        ip, cmd, self.a, self.b, self.c
                    ),
                    file=sys.stderr,
                )
            if cmd == "+":
                self.a += 1
            if cmd == "-":
                self.a -= 1
                if self.a < 0:
                    self.a += 1
            if cmd == "&":
                self.a &= self.b
            if cmd == "|":
                self.a |= self.b
            if cmd == "^":
                self.a ^= self.b
            if cmd == "<":
                self.a <<= self.b
            if cmd == ">":
                self.a >>= self.b
            if cmd == "~":
                self.a, self.b = self.b, self.a
            if cmd == "*":
                self.a, self.b, self.c = self.c, self.a, self.b
            if cmd == ",":
                self.a = ord(sys.stdin.read(1))
            if cmd == ".":
                sys.stdout.write(chr(self.a))
            if cmd == "(":
                if not self.a:
                    ip = matches[ip] - 1
            if cmd == ")":
                if self.a:
                    ip = matches[ip] - 1
            if cmd not in "+-&|^<>~*,.()":
                sys.stdout.write(cmd)
            ip += 1


def main():
    p = argparse.ArgumentParser(description="Official Interpreter of BinaryLanguage")
    p.add_argument("file", help="Program file name")
    p.add_argument("--debug", "-d", help="Debug mode", action="store_true")
    a = p.parse_args()
    with open(a.file, "r") as f:
        code = f.read()
    m = BinaryLanguageMachine(code)
    m.run(a.debug)


if __name__ == "__main__":
    main()
