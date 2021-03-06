from commands.command import Command

class Move(Command):
    def __init__(self, text, line_num, right_side, position, pos_spec):
        super(Move, self).__init__("MOVE", text, line_num)
        self.right_side = right_side
        self.position = position # -4 = RHCard, -3 = LHCard, -2 = RHPos -1 = LHPos only if pos_spec
        self.pos_spec = pos_spec # Whether or not the position is a special reference

    def convNum(self, code_instance, num):
        # -4 = RHCard, -3 = LHCard, -2 = RHPos -1 = LHPos only if num1_spec
        if(not self.pos_spec):
                return num
        if(num == -1): #LHPos
            return code_instance.lpos
        elif(num == -2): #RHPos
            return code_instance.rpos
        elif(num == -3): #LHCard
            return code_instance.seq[code_instance.lpos]
        elif(num == -4): #RHCard
            return code_instance.seq[code_instance.rpos]

    def evaluate(self, code_instance):
        # Determine the position to move the hand to
        position = self.convNum(code_instance, self.position)
        # If the position is a valid reference within the sequence
        if position in range(len(code_instance.seq)):
            # Move the proper hand to that position
            if(self.right_side):
                code_instance.rpos = position
            else:
                code_instance.lpos = position
            # Move onto the next line of code
            code_instance.curr_line += 1
        else:
            self.report_error(code_instance, "Index out of bounds of sequence: index=" + str(position))
