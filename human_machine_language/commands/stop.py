from commands.command import Command

class Stop(Command):
    def __init__(self, text, line_num):
        super(Stop, self).__init__("STOP", text, line_num)

    # Stop the program when run
    def evaluate(self, code_instance):
        code_instance.stop = True
