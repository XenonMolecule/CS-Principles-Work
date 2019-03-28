from command import Command

class Stop(Command):
    def __init__(self, text, line_num):
        super(Jump, self).__init__("STOP", text, line_num)

    def evaluate(self, code_instance):
        code_instance.stop = True
