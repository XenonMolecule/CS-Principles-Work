from commands.command import Command

class Shift(Command):
    def __init__(self, text, line_num, right_side, to_right):
        super(Shift, self).__init__("SHIFT", text, line_num)
        self.right_side = right_side # Right or left hand
        self.to_right = to_right # Move to right or left

    def evaluate(self, code_instance):
        new_val = -1
        # Move proper hand in proper direction
        if(self.right_side):
            if(self.to_right):  # Move right hand right
                code_instance.rpos += 1
            else:               # Move right hand left
                code_instance.rpos -= 1
            new_val = code_instance.rpos
        else:
            if(self.to_right):  # Move left hand right
                code_instance.lpos += 1
            else:               # Move left hand left
                code_instance.lpos -= 1
            new_val = code_instance.lpos
        # Check if the new position of the moved hand is valid before continuing
        if (new_val in range(len(code_instance.seq))):
            code_instance.curr_line += 1
        else:
            self.report_error(code_instance, "Index out of bounds of sequence: index=" +
            str(new_val) + "\n\tLH: " + str(code_instance.lpos) + "\n\tRH: " + str(code_instance.rpos))
