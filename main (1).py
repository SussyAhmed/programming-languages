import sys


class Program:


    def __init__(self):

        self.filename = sys.argv[1]
        self.file     = open(self.filename, "r").read()
        self.file     = self.file.replace("\n", " ")
        self.file     = self.file.replace("\r", "")
        self.file     = self.file.replace("\t", "")
        self.file     = self.file.split(" ")

        self.stack     = []
        self.variables = {}
        self.functions = {}
        self.mainfunc  = []



    def push(self, element):
        self.stack.append(element)

    def dump(self):
        for elt in self.stack: print(elt)
        self.stack = []

    def var(self):
        name  = self.stack.pop()
        value = self.stack.pop()
        self.variables[name] = value

    def do(self):
        todo = self.stack.pop()
        condition = self.stack.pop()
        self.run_function(self.functions[int(todo)]) if condition else None

    def loop(self):
        times = int(self.stack.pop())
        todo  = self.stack.pop()
        for i in range(times):
            self.run_function(todo)



    def add(self):
        num1 = self.stack.pop()
        num2 = self.stack.pop()
        self.push(int(num1) + int(num2))

    def sub(self):
        num1 = self.stack.pop()
        num2 = self.stack.pop()
        self.push(int(num1) - int(num2))

    def mul(self):
        num1 = self.stack.pop()
        num2 = self.stack.pop()
        self.push(int(num1) * int(num2))

    def div(self):
        num1 = self.stack.pop()
        num2 = self.stack.pop()
        self.push(int(num1) / int(num2))

    def bigger(self):
        num1 = int(self.stack.pop())
        num2 = int(self.stack.pop())
        self.push(True) if num1 >  num2 else self.push(False)

    def smaller(self):
        num1 = int(self.stack.pop())
        num2 = int(self.stack.pop())
        self.push(True) if num1 <  num2 else self.push(False)
        
    def equal(self):
        num1 = int(self.stack.pop())
        num2 = int(self.stack.pop())
        self.push(True) if num1 == num2 else self.push(False)
        
    def bigger_equal(self):
        num1 = int(self.stack.pop())
        num2 = int(self.stack.pop())
        self.push(True) if num1 >= num2 else self.push(False)
        
    def smaller_equal(self):
        num1 = int(self.stack.pop())
        num2 = int(self.stack.pop())
        self.push(True) if num1 <= num2 else self.push(False)



    def run_function(self, function):
        for command in function:
            for key, value in self.variables.items():
                if key in command:
                    command = value
            for key, value in self.functions.items():
                if f"[{key}]" in command:
                    self.run_function(self.functions[key])
            if   command == "dump":     self.dump()
            elif command == "var":      self.var()
            elif command == "do":       self.do()
            elif command == "loop":     self.loop()
            elif command == "+":        self.add()
            elif command == "-":        self.sub()
            elif command == "*":        self.mul()
            elif command == "/":        self.div()
            elif command == ">":        self.bigger()
            elif command == "<":        self.smaller()
            elif command == "==":       self.equal()
            elif command == ">=":       self.bigger_equal()
            elif command == "<=":       self.smaller_equal()
            else               :        self.push(command)


    def separate_functions(self):

        func_mode  = False
        main_mode  = False
        func_count = 0

        for command in self.file:

            if command == "FUNC:":
                func_count += 1
                func_mode   = True
                self.functions[func_count] = []
            if func_mode and command != "END":
                if command != "" and command != "FUNC:":
                    self.functions[func_count].append(command)
            if func_mode and command == "END":
                func_mode = False

            if command == "MAIN:":
                main_mode = True
            if main_mode and command != "END":
                if command != "" and command != "MAIN:":
                    self.mainfunc.append(command)
            if main_mode and command == "END":
                func_mode = False






program = Program()
program.separate_functions()
program.run_function(program.mainfunc)