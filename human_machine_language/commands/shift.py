from commands.command import Command

class Shift(Command):
    def __init__(self, text, line_num, right_side, to_right):
        super(Shift, self).__init__("SHIFT", text, line_num)
        self.right_side = right_side
        self.to_right = to_right

    def evaluate(self, code_instance):
        new_val = -1
        if(self.right_side):
            if(self.to_right):
                code_instance.rpos += 1
            else:
                code_instance.rpos -= 1
            new_val = code_instance.rpos
        else:
            if(self.to_right):
                code_instance.lpos += 1
            else:
                code_instance.lpos -= 1
            new_val = code_instance.lpos
        if (new_val in range(len(code_instance.seq))):
            code_instance.curr_line += 1
        else:
            self.report_error(code_instance, "Index out of bounds of sequence: index=" +
            str(new_val) + "\n\tLH: " + str(code_instance.lpos) + "\n\tRH: " + str(code_instance.rpos))
