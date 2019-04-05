from commands.command import Command

# Error class to be created when there is a compiler error in creating the other classes
class Error(Command):
    def __init__(self, text, line_num, message):
        super(Error, self).__init__("ERROR", text, line_num)
        self.message = message

    # The error command should throw an error if it is ever run
    def evaluate(self, code_instance):
        self.report_error(code_instance, self.message)
