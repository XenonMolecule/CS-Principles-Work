from commands.command import Command

class Error(Command):
    def __init__(self, text, line_num, message):
        super(Error, self).__init__("ERROR", text, line_num)
        self.message = message

    def evaluate(self, code_instance):
        self.report_error(code_instance, self.message)
