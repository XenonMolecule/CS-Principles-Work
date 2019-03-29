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

    def build_jumps(self, text, params, line_num):
        if("IF" in params):
            return self.build_jumpif(text, params, line_num)
        else:
            return self.build_jump(text, params, line_num)

    def build_jump(self, text, params, line_num):
        if (not (params[0] == "JUMP" and params[1] == "TO" and params[2] == "LINE")):
            return self.build_error_msg(text, params, line_num, "Syntax Error")
        if (not params[3].isdigit()):
            return self.build_error_msg(text, params, line_num, line_num, params[3] + "is NaN - Ask me to update later if trying LHPOS or something")
        return Jump(text, line_num, int(params[3]))

    def det_number(self, text):
        num_spec = False
        num = 0
        if(text in ["LHPOS","RHPOS","LHCARD","RHCARD"]):
            num_spec = True
            if(text == "LHPOS"):
                num = -1
            elif(text == "RHPOS"):
                num = -2
            elif(text == "LHCARD"):
                num = -3
            else:
                num = -4
        else:
            num1 = int(text)
        return num, num_spec

    def build_jumpif(self, text, params, line_num):
        # -4 = RHCard, -3 = LHCard, -2 = RHPos -1 = LHPos
        if (not (params[0] == "JUMP" and params[1] == "TO" and params[2] == "LINE" and params[4] == "IF")):
            return self.build_error_msg(text, params, line_num, "Syntax Error")
        if (not params[3].isdigit()):
            return self.build_error_msg(text, params, line_num, str(params[3]) + "is NaN - Ask me to update later if trying LHPOS or something")
        if(not (params[5].isdigit() or params[5] in ["LHPOS","RHPOS","LHCARD","RHCARD"])):
            if(params[5] in ["LH", "RH"]):
                return self.build_error_msg(text, params, line_num, str(params[5]) + " is not a recognized number or reference\n\tDid you mean LHPOS or LHCARD?")
            return self.build_error_msg(text, params, line_num, str(params[5]) + " is not a recognized number or reference")
        if(not (params[7].isdigit() or params[7] in ["LHPOS","RHPOS","LHCARD","RHCARD"])):
            return self.build_error_msg(text, params, line_num, str(params[7]) + " is not a recognized number or reference")
        if(not params[6] in ["EQ","NE","LT","GT"]):
            return self.build_error_msg(text, params, line_num, str(params[6]) + " is not a recognized comparator")
        num1, num1_spec = self.det_number(params[5])
        num2, num2_spec = self.det_number(params[7])
        comp_type = ["EQ","NE","LT","GT"].index(params[6])
        return JumpIf(text, line_num, int(params[3]), num1, num2, comp_type, num1_spec, num2_spec)

    def build_move(self, text, params, line_num):
        if (not (params[0] == "MOVE" and params[2] == "TO" and params[3] == "POSITION")):
            return self.build_error_msg(text, params, line_num, "Syntax Error")
        if (not params[1] in ["LH","RH"]):
            return self.build_error_msg(text, params, line_num, "Unrecognized hand side: " + str(params[1]))
        if(not (params[4].isdigit() or params[4] in ["LHPOS","RHPOS","LHCARD","RHCARD"])):
            return self.build_error_msg(text, params, line_num, str(params[4]) + " is not a recognized number or reference")
        num, num_spec = self.det_number(params[4])
        right_hand = (params[1] == "RH")
        return Move(text, line_num, right_hand, num, num_spec)

    def build_shift(self, text, params, line_num):
        if (not (params[0] == "SHIFT" and params[2] == "TO" and params[3] == "THE")):
            return self.build_error_msg(text, params, line_num, "Syntax Error")
        if (not params[1] in ["LH","RH"]):
            return self.build_error_msg(text, params, line_num, "Unrecognized hand side: " + str(params[1]))
        if (not params[4] in ["R","L"]):
            return self.build_error_msg(text, params, line_num, "Unrecognized direction: " + str(params[4]))
        right_hand = (params[1] == "RH")
        to_right = (params[4] == "R")
        return Shift(text, line_num, right_hand, to_right)

    def build_stop(self, text, params, line_num):
        if(not params[0] == "STOP"):
            return self.build_error_msg(text, params, line_num, "Syntax Error")
        return Stop(text, line_num)

    def build_swap(self, text, params, line_num):
        if(not params[0] == "SWAP"):
            return self.build_error_msg(text, params, line_num, "Syntax Error")
        return Swap(text, line_num)

    def build_error(self, text, params, line_num):
        return self.build_error_msg(text, params, line_num, "Unrecognized command: " + str(params[0]))

    def build_error_msg(self, text, params, line_num, message):
        return Error(text, line_num, message + "\n\t" + text)

    def build_cmd(self, text, line_num):
        text = text.upper()
        params = text.split(" ")
        switch = {
            "JUMP": self.build_jumps,
            "MOVE": self.build_move,
            "SHIFT": self.build_shift,
            "STOP": self.build_stop,
            "SWAP": self.build_swap
        }
        params = [param for param in params if param != ""] # remove blanks
        build = switch.get(params[0],lambda: self.build_error)
        return build(text, params, line_num)
