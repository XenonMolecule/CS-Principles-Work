import random

class Code_Instance(object):

    def gen_seq(self, length):
        list = []
        for i in range(length) :
            list.append(random.randint(1,10))
        return list

    def gen_code_block(self, text):
        params = text.split(" ")
        

    def __init__(self, code_string, seq=self.gen_seq(9)):
        self.code_string = code_string
        self.seq = seq
        self.rpos = 0
        self.lpos = 0
        self.curr_line = 1
        self.stop = False
        self.error = False
        self.error_txt = ""
        self.error_line = 0

    def reset(self):
        self.rpos = 0
        self.lpos = 0
        self.curr_line = 1
        self.stop = False
        self.error = False
        self.error_txt = ""
        self.error_line = 0

    def evaluate(self):
        while(not self.stop and not self.error):
            if(self.curr_line < len(code)):
                code[self.curr_line].evaluate()
            else:
                print("ERROR: Line " + self.curr_line + " is not in the program... did you forget to STOP?")
                return
        if(self.error):
            print("ERROR on Line " + self.error_line + ": " self.error_txt)

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
