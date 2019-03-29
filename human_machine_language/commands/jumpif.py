from commands.command import Command

class JumpIf(Command):
    def __init__(self, text, line_num, line_num_jump, num1, num2, comp_type, num1_spec, num2_spec):
        super(JumpIf, self).__init__("JUMP IF", text, line_num)
        self.line_num_jump = line_num_jump
        self.num1 = num1 # -4 = RHCard, -3 = LHCard, -2 = RHPos -1 = LHPos only if num1_spec
        self.num2 = num2 # -4 = RHCard, -3 = LHCard, -2 = RHPos -1 = LHPos only if num2_spec
        self.comp_type = comp_type # 0 = eq, 1 = ne, 2 = lt, 3 = gt
        self.num1_spec = num1_spec
        self.num2_spec = num2_spec

    def compeq(self, code_instance, n1, n2):
        return n1 == n2

    def compne(self, code_instance, n1, n2):
        return n1 != n2

    def complt(self, code_instance, n1, n2):
        return n1 < n2

    def compgt(self, code_instance, n1, n2):
        return n1 > n2

    def comperror(self, code_instance, n1, n2):
        self.report_error(code_instance, "INVALID COMPARISON TYPE")
        return False

    # num is either num1 or num2, and num_num is 1 or 2 to indicate which one
    def convNum(self, code_instance, num, num_num):
        # -4 = RHCard, -3 = LHCard, -2 = RHPos -1 = LHPos only if num1_spec
        if(num_num == 1):
            if(not self.num1_spec):
                return num
        else:
            if(not self.num2_spec):
                return num
        if(num == -1):
            return code_instance.lpos
        elif(num == -2):
            return code_instance.rpos
        elif(num == -3):
            return code_instance.seq[code_instance.lpos]
        elif(num == -4):
            return code_instance.seq[code_instance.rpos]

    def evaluate(self, code_instance):
        switch = {
            0:self.compeq,
            1:self.compne,
            2:self.complt,
            3:self.compgt
        }
        comp = switch.get(self.comp_type, lambda: self.comperror)

        if(comp(code_instance, self.convNum(code_instance, self.num1, 1), self.convNum(code_instance, self.num2, 2))):
            self.jump(code_instance)
        else:
            code_instance.curr_line += 1


    def jump(self, code_instance):
        if(self.line_num_jump in range(len(code_instance.code))):
            code_instance.curr_line = self.line_num_jump
        else:
            self.report_error(code_instance, "Index out of bounds of code length: index=" + self.line_num_jump)
