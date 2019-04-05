from commands.command import Command

class Jump(Command):
    # Build the Jump Command with a line number to jump to
    def __init__(self, text, line_num, line_num_jump):
        super(Jump, self).__init__("JUMP", text, line_num)
        self.line_num_jump = line_num_jump

    def evaluate(self, code_instance):
        # Check if the line number is in the code, then jump to it
        if(self.line_num_jump in range(len(code_instance.code))):
            code_instance.curr_line = self.line_num_jump
        else:
            self.report_error(code_instance, "Index out of bounds of code length: index=" + str(self.line_num_jump))
