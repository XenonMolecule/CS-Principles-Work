# The general Command class which acts as a parent object to the other Commands
class Command(object):
    # Initialize with name, text, and line number
    def __init__(self, name, txt, line_num):
        self.name = name
        self.txt = txt
        self.line_num = line_num

    def __str__(self):
        return self.txt

    # If child doesn't override, throw an error
    def evaluate(self, code_instance):
        print("ERROR: UNDEFINED BEHAVIOR FOR FUNCTION" + self.name)
        self.report_error(code_instance, "Undefined Function Behavior")

    # Run all code to throw an error message and stop program termination
    def report_error(self, code_instance, msg):
        code_instance.error = True
        code_instance.error_txt = msg
        code_instance.error_line = self.line_num
