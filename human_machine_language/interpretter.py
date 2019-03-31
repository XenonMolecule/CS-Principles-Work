import sys
import argparse
from code_instance import Code_Instance

parser = argparse.ArgumentParser()
parser.add_argument("-V", "--verbose", help="enable verbose logging", action="store_true")

args = parser.parse_args()

file = "/Users/MichaelRyan/Documents/GitHub/CS-Principles-Work/human_machine_language/challenges/hi-lo.txt" #sys.argv[0]
code_string = []


with open(file) as code_file:
    code_string.append("LINE NUMBERS AREN'T ZERO INDEXED")
    for i,line in enumerate(code_file):
        code_string.append(line)

code = Code_Instance(code_string, args.verbose)
print()
code.print_seq()
print()
code.evaluate()
print()
code.print_seq()
print()
