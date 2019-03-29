import random
from command_builder import CodeBuilder
from commands.error import Error

class Code_Instance(object):

    def __init__(self, code_string, seq=[]):
        self.code_string = code_string
        if(len(seq) < 1):
            self.seq = self.gen_seq(9)
        else:
            self.seq = seq
        self.reset()

    def gen_seq(self, length):
        list = []
        for i in range(length) :
            list.append(random.randint(1,10))
        return list

    def reset(self):
        self.rpos = 0
        self.lpos = 0
        self.curr_line = 1
        self.stop = False
        self.error = False
        self.error_txt = ""
        self.error_line = 0

    def evaluate(self):
        self.compile()
        while(not self.stop and not self.error):
            if(self.curr_line < len(self.code) and self.curr_line > 0):
                self.code[self.curr_line].evaluate(self)
            else:
                print("---\nERROR: Line " + str(self.curr_line) + " is not in the program... did you forget to STOP?" + "\n---")
                return
        if(self.error):
            print("---\nERROR on Line " + str(self.error_line) + ": " + self.error_txt + "\n---")

    def seq_string(self):
        output = ""
        for num in self.seq:
            output += str(num)
            if(num < 10):
                output += "  "
            else:
                output += " "
        return output

    def print_seq(self):
        print(self.seq_string())

    def __str__(self):
        return "\n".join(code_string)

    def compile(self):
        compiler = CodeBuilder()
        self.code = []

        for i,line in enumerate(self.code_string):
            if(i == 0):
                self.code.append(Error("ERROR", 0, "Line 0 is not in the program..."))
                continue
            cmd = compiler.build_cmd(line[:-1], i)
            if(not (type(cmd) is Error)):
                self.code.append(cmd)
            else:
                print("---\nCompiler Error on Line " + str(i))
                cmd.evaluate(self)
                return
