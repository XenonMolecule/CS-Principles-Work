import sys
from code_instance import Code_Instance

file = "/Users/MichaelRyan/Documents/GitHub/CS-Principles-Work/human_machine_language/hml-challenge.txt" #sys.argv[0]
code_string = []

with open(file) as code_file:
    code_string.append("LINE NUMBERS AREN'T ZERO INDEXED")
    for i,line in enumerate(code_file):
        code_string.append(line)

code = Code_Instance(code_string)
print()
code.print_seq()
print()
code.evaluate()
print()
code.print_seq()
print()
