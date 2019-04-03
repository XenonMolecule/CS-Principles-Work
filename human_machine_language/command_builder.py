from commands.jump import Jump
from commands.jumpif import JumpIf
from commands.move import Move
from commands.shift import Shift
from commands.stop import Stop
from commands.swap import Swap
from commands.error import Error

class CodeBuilder(object):
    def __init__(self):
        super(CodeBuilder, self).__init__()

    # Construct either one of the JUMP commands
    def build_jumps(self, text, params, line_num):
        # Check for IF to switch it to JUMPIF rather than JUMP
        if(params[4] == "IF"):
            return self.build_jumpif(text, params, line_num)
        else:
            return self.build_jump(text, params, line_num)

    # Construct the JUMP TO LINE command
    def build_jump(self, text, params, line_num):
        # Check that JUMP, TO, and LINE are in the correct positions in the text
        if (not (params[0] == "JUMP" and params[1] == "TO" and params[2] == "LINE")):
            return self.build_error_msg(text, params, line_num, "Syntax Error")
        # Make sure the line number is actually a number
        if (not params[3].isdigit()):
            return self.build_error_msg(text, params, line_num, line_num, params[3] + "is NaN - Ask me to update later if trying LHPOS or something")
        return Jump(text, line_num, int(params[3]))

    # Replace References such as RHPOS and LHPOS with numerical references instead
    def det_number(self, text):
        num_spec = False
        num = 0
        if(text in ["LHPOS","RHPOS","LHCARD","RHCARD"]):
            num_spec = True # The number is special (it is a reference)
            if(text == "LHPOS"):
                num = -1
            elif(text == "RHPOS"):
                num = -2
            elif(text == "LHCARD"):
                num = -3
            else:
                num = -4
        else:
            num = int(text)
        return num, num_spec

    # Construct the JUMP TO LINE IF Command
    def build_jumpif(self, text, params, line_num):
        # -4 = RHCard, -3 = LHCard, -2 = RHPos -1 = LHPos
        # Check if JUMP, TO, LINE, and IF are written in the proper positions
        if (not (params[0] == "JUMP" and params[1] == "TO" and params[2] == "LINE" and params[4] == "IF")):
            return self.build_error_msg(text, params, line_num, "Syntax Error")
        # Check if the line number is a number (doesn't check if it is a reference since
        #   that functionality does not seem super useful, but could be a later addition)
        if (not params[3].isdigit()):
            return self.build_error_msg(text, params, line_num, str(params[3]) + "is NaN - Ask me to update later if trying LHPOS or something")
        # Check if the first comparison is for a digit or a reference
        if(not (params[5].isdigit() or params[5] in ["LHPOS","RHPOS","LHCARD","RHCARD"])):
            # Give the programmer additional advice if they specifically used LH/RH instead of LHCARD or LHPOS
            if(params[5] in ["LH", "RH"]):
                return self.build_error_msg(text, params, line_num, str(params[5]) + " is not a recognized number or reference\n\tDid you mean LHPOS or LHCARD?")
            return self.build_error_msg(text, params, line_num, str(params[5]) + " is not a recognized number or reference")
        # Check if the second comparison is for a digit or a reference
        if(not (params[7].isdigit() or params[7] in ["LHPOS","RHPOS","LHCARD","RHCARD"])):
            # Give the programmer additional advice if they specifically used LH/RH instead of LHCARD or LHPOS
            if(params[7] in ["LH", "RH"]):
                return self.build_error_msg(text, params, line_num, str(params[7]) + " is not a recognized number or reference\n\tDid you mean LHPOS or LHCARD?")
            return self.build_error_msg(text, params, line_num, str(params[7]) + " is not a recognized number or reference")
        # Check to make sure the comparison is either EQ, NE, LT, or GT
        if(not params[6] in ["EQ","NE","LT","GT"]):
            return self.build_error_msg(text, params, line_num, str(params[6]) + " is not a recognized comparator")
        num1, num1_spec = self.det_number(params[5])
        num2, num2_spec = self.det_number(params[7])
        comp_type = ["EQ","NE","LT","GT"].index(params[6])
        return JumpIf(text, line_num, int(params[3]), num1, num2, comp_type, num1_spec, num2_spec)

    # Construct the MOVE TO POSITION
    def build_move(self, text, params, line_num):
        # Check for proper placement of the words MOVE, TO, and POSTION
        if (not (params[0] == "MOVE" and params[2] == "TO" and params[3] == "POSITION")):
            return self.build_error_msg(text, params, line_num, "Syntax Error")
        # Check if the thing to move is actually LH or RH and not something else
        if (not params[1] in ["LH","RH"]):
            return self.build_error_msg(text, params, line_num, "Unrecognized hand side: " + str(params[1]))
        # Check if the position to move to is either a number or a position reference
        if(not (params[4].isdigit() or params[4] in ["LHPOS","RHPOS","LHCARD","RHCARD"])):
            return self.build_error_msg(text, params, line_num, str(params[4]) + " is not a recognized number or reference")
        num, num_spec = self.det_number(params[4])
        right_hand = (params[1] == "RH")
        return Move(text, line_num, right_hand, num, num_spec)

    # Constuct the SHIFT Command
    def build_shift(self, text, params, line_num):
        # Check for proper placement of the words SHIFT, TO, and THE
        if (not (params[0] == "SHIFT" and params[2] == "TO" and params[3] == "THE")):
            return self.build_error_msg(text, params, line_num, "Syntax Error")
        # Check if the thing to shift is actually LH or RH and not something else
        if (not params[1] in ["LH","RH"]):
            return self.build_error_msg(text, params, line_num, "Unrecognized hand side: " + str(params[1]))
        # Check if the shift direction is R or L and not something else
        if (not params[4] in ["R","L"]):
            return self.build_error_msg(text, params, line_num, "Unrecognized direction: " + str(params[4]))
        right_hand = (params[1] == "RH")
        to_right = (params[4] == "R")
        return Shift(text, line_num, right_hand, to_right)

    # Construct the STOP Command
    def build_stop(self, text, params, line_num):
        # Check if the first word is STOP
        if(not params[0] == "STOP"):
            return self.build_error_msg(text, params, line_num, "Syntax Error")
        return Stop(text, line_num)

    # Construct the SWAP Command
    def build_swap(self, text, params, line_num):
        # Check if the first word is SWAP
        if(not params[0] == "SWAP"):
            return self.build_error_msg(text, params, line_num, "Syntax Error")
        return Swap(text, line_num)

    # Default Constructor when the command is Unrecognized
    def build_error(self, text, params, line_num):
        return self.build_error_msg(text, params, line_num, "Unrecognized command: " + str(params[0]))

    # Command type to print out a compiler error
    def build_error_msg(self, text, params, line_num, message):
        return Error(text, line_num, message)

    # Construct a command object from text
    def build_cmd(self, text, line_num):
        text = text.upper()
        params = text.split(" ")
        # Change the constructor based on the first word of the line
        switch = {
            "JUMP": self.build_jumps,
            "MOVE": self.build_move,
            "SHIFT": self.build_shift,
            "STOP": self.build_stop,
            "SWAP": self.build_swap
        }
        # loop through all parameters and save the ones that aren't blank
        params = [param for param in params if param != ""]
        build = switch.get(params[0],lambda: self.build_error)
        return build(text, params, line_num)
