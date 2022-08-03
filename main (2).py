global variables
global functions
variables = {}
functions = {}


def get_data() -> list[str]:
    import sys
    filename = sys.argv[1]
    filecontents = open(filename, "r").read()
    filecontents = filecontents.replace("\n", "")
    filecontents = filecontents.replace(" ", "")
    filecontents = filecontents.replace("_", " ")
    filecontents = filecontents.split(";")
    commands = []
    for elt in filecontents:
        if len(elt) > 0:
            commands.append(elt)
    return commands


def run(commands=get_data()) -> None:
    for cmd in commands:
        printed = False
        for k, v in variables.items():
            if f"[{k}]" in cmd:
                cmd = cmd.replace(f"[{k}]", v)
        for k, v in functions.items():
            if f"[{k}]" in cmd:
                run(functions[k])
        if cmd[0:5] == "print":
            cmd = cmd.replace("print", "")
            printed = True
        if cmd[0:3] == "var":
            cmd = cmd.replace("var", "")
            n, v = cmd.split("=")
            variables[n] = v
        if cmd[0:5] == "input":
            cmd = cmd.replace("input", "")
            n, c = cmd.split(">")
            v = input(c)
            variables[n] = v
        if "+" in cmd:
            n1, n2 = cmd.split("+")
            cmd = str(int(n1)+int(n2))
        if "-" in cmd:
            n1, n2 = cmd.split("-")
            cmd = str(int(n1)-int(n2))
        if "*" in cmd:
            n1, n2 = cmd.split("*")
            cmd = str(int(n1)*int(n2))
        if "/" in cmd:
            n1, n2 = cmd.split("/")
            cmd = str(int(n1)/int(n2))
        if printed:
            print(cmd)
        if cmd[0:4] == "loop":
            cmd = cmd.replace("loop", "")
            condition, consequence = cmd.split("do")
            if "<" in condition:
                a, b = condition.split("<")
                if a < b:
                    accepted = True
                else:
                    accepted = False
            if ">" in condition:
                a, b = condition.split(">")
                if a > b:
                    accepted = True
                else:
                    accepted = False
            if "<=" in condition:
                a, b = condition.split("<=")
                if a <= b:
                    accepted = True
                else:
                    accepted = False
            if ">=" in condition:
                a, b = condition.split(">=")
                if a >= b:
                    accepted = True
                else:
                    accepted = False
            if "==" in condition:
                a, b = condition.split("==")
                if a == b:
                    accepted = True
                else:
                    accepted = False
            while not accepted:
                consequence = consequence.split("$")
                run(consequence)

        if cmd[0:4] == "func":
            cmd = cmd.replace("func", "")
            n, v = cmd.split(":")
            v = v.split("$")
            functions[n] = v
        if cmd[0:2] == "if":
            accepted = False
            cmd = cmd.replace("if", "")
            condition, consequence = cmd.split(">>")
            if "<" in condition:
                a, b = condition.split("<")
                if a < b:
                    accepted = True
                else:
                    accepted = False
            if ">" in condition:
                a, b = condition.split(">")
                if a > b:
                    accepted = True
                else:
                    accepted = False
            if "<=" in condition:
                a, b = condition.split("<=")
                if a <= b:
                    accepted = True
                else:
                    accepted = False
            if ">=" in condition:
                a, b = condition.split(">=")
                if a >= b:
                    accepted = True
                else:
                    accepted = False
            if "==" in condition:
                a, b = condition.split("==")
                if a == b:
                    accepted = True
                else:
                    accepted = False
            if accepted:
                consequence = consequence.split("$")
                run(consequence)


run()
