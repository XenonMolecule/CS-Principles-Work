import argparse
from code_instance import Code_Instance

default_file_path = "/Users/MichaelRyan/Documents/GitHub/CS-Principles-Work/human_machine_language/challenges/sort.txt"

# Add in the ability to specify verbose logging
parser = argparse.ArgumentParser()
parser.add_argument("-V", "--verbose", help="enable verbose logging", action="store_true")
parser.add_argument("--file", default = default_file_path, type = open)

args = parser.parse_args()

file = "/Users/MichaelRyan/Documents/GitHub/CS-Principles-Work/human_machine_language/challenges/sort.txt" #sys.argv[0]
code_string = []


with args.file as code_file:
    code_string.append("LINE NUMBERS AREN'T ZERO INDEXED")
    for i,line in enumerate(code_file):
        code_string.append(line)

code = Code_Instance(code_string, args.verbose)
print("\ninitial: " + code.seq_string())
code.evaluate()
print("  final: " + code.seq_string() + "\n")
code.print_summary()
print()
