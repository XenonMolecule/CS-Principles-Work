import random
from command_builder import CodeBuilder
from commands.error import Error

class Code_Instance(object):

    def __init__(self, code_string, verbose=False, seq=[]):
        self.code_string = code_string
        if(len(seq) < 1):
            self.seq = self.gen_seq(9)
        else:
            self.seq = seq
        self.verbose = verbose
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
                if(self.verbose):
                    print("---")
                    print(str(self.curr_line) + ": " + self.code_string[self.curr_line])
                    self.print_seq()
                    self.print_hands()

            else:
                print("---\nERROR: Line " + str(self.curr_line) + " is not in the program... did you forget to STOP?" + "\n---")
                return
        if(self.error):
            print("---\nERROR on Line " + str(self.error_line) + ": " + self.error_txt + "\n\t" + self.code_string[self.error_line][:-1] + "\n---")

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

    def print_hands(self):
        padding1 = ""
        padding2 = ""
        if(self.lpos == self.rpos):
            padding1 = " " * (self.lpos * 3)
            print(padding1 + "LR")
        elif(self.lpos < self.rpos):
            padding1 = " " * (self.lpos * 3)
            padding2 = " " * (((self.rpos-self.lpos) * 3) - 2)
            print(padding1 + "LH" + padding2 + "RH")
        else:
            padding1 = " " * (self.rpos * 3)
            padding2 = " " * (((self.lpos-self.rpos) * 3) - 2)
            print(padding1 + "RH" + padding2 + "LH")

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
