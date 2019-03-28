class Command(object):
    def __init__(self, name="Command", txt="txt", line_num):
        self.name = name
        self.txt = txt
        self.line_num = line_num

    def __str__(self):
        return self.txt

    def evaluate(self, code_instance):
        print("ERROR: UNDEFINED BEHAVIOR FOR FUNCTION" + self.name)

    def report_error(self, code_instance, msg):
        code_instance.error = True
        code_instance.error_txt = msg
        code_instance.error_line = line_num
