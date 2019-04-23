import argparse
from code_instance import Code_Instance

default_file_path = "./challenges/sort.txt"

# Add in the ability to specify verbose logging and file path
parser = argparse.ArgumentParser()
parser.add_argument("-V", "--verbose", help="enable verbose logging", action="store_true")
parser.add_argument("--file", default = default_file_path, type = open)

args = parser.parse_args()

code_string = []

# Read the file in
with args.file as code_file:
    # The code string should start counting from line 1, not line 0
    code_string.append("LINE NUMBERS AREN'T ZERO INDEXED")
    # Save each line to the list
    for i,line in enumerate(code_file):
        code_string.append(line)

# Make an instance of the code parser
code = Code_Instance(code_string, args.verbose)
print("\ninitial: " + code.seq_string())
code.evaluate() # Run the code
if(not code.error):
    print("  final: " + code.seq_string() + "\n")
    code.print_summary() # Print the code summary
    print()
