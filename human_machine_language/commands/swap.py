from command import Command

class Swap(Command):
    def __init__(self, text, line_num):
        super(Jump, self).__init__("SWAP", text, line_num)

    def evaluate(self, code_instance):
        temp = code_instance.seq[code_instance.lpos]
        code_instance.seq[code_instance.lpos] = code_instance.seq[code_instance.rpos]
        code_instance.seq[code_instance.rpos] = temp
        code_instance.curr_line += 1
