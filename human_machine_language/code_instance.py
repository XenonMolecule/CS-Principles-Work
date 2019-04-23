import random
from command_builder import CodeBuilder
from commands.error import Error

class Code_Instance(object):

    # Initialize a code instance with the code as a string and a sequence and verbose mode
    def __init__(self, code_string, verbose=False, seq=[]):
        self.code_string = code_string
        # IF no sequence provided, then generate one
        if(len(seq) < 1):
            self.seq = self.gen_seq(9)
        else:
            self.seq = seq
        self.verbose = verbose
        # Initialize all instance data
        self.reset()

    # Generate a list of random numbers of provided length
    def gen_seq(self, length):
        list = []
        for i in range(length) :
            list.append(random.randint(1,10))
        return list

    # Reset or initialize instance data
    def reset(self):
        self.rpos = 0       # Right hand position
        self.lpos = 0       # Left hand position
        self.curr_line = 1  # Current line running in code
        self.stop = False   # Whether or not the instance should keep running
        self.error = False  # Whether or not the instance has crashed/should crash
        self.error_txt = "" # Text to display on error
        self.error_line = 0 # Which line number the error is on
        self.lines_run = 0  # Count of how many lines of code ran
        self.swap_count = 0 # Count of how many swaps the code performs
        self.comp_count = 0 # Count of how many comparisons the code has run

    # Run the code instance to completion or runtime error
    def evaluate(self):
        # compile all of the code into the object types for calling
        self.compile()
        # Keep running until stop or error is reached
        while(not self.stop and not self.error):
            # Make sure the current line number is in range of the code
            if(self.curr_line < len(self.code) and self.curr_line > 0):
                # Run the line of code
                self.code[self.curr_line].evaluate(self)
                self.lines_run += 1
                # Print into on what just ran if user in verbose mode
                if(self.verbose):
                    print("---")
                    print(str(self.curr_line) + ": " + self.code_string[self.curr_line])
                    self.print_seq()
                    self.print_hands()

            else:
                print("---\nERROR: Line " + str(self.curr_line) + " is not in the program... did you forget to STOP?" + "\n---")
                return
        if(self.error):
            print("---\nERROR on Line " + str(self.error_line) + ": " + self.error_txt + "\n\t" + self.code_string[self.error_line][:-1] + "\n---")

    # Convert the sequence of numbers into a string with well spaced numbers
    def seq_string(self):
        output = ""
        for num in self.seq:
            output += str(num)
            if(num < 10):
                output += "  "
            else:
                output += " "
        return output

    # Print the string of the stored sequence of numbers
    def print_seq(self):
        print(self.seq_string())

    # Convert the hand positions to a string which when printed lines up perfectly with the sequence string
    def hand_string(self):
        padding1 = ""
        padding2 = ""
        # If the hands are in the same spot print LR instead of LH & RH
        if(self.lpos == self.rpos):
            padding1 = " " * (self.lpos * 3) # calculate hand padding based on position
            return (padding1 + "LR")
        # If the left hand is to the left of the right hand then add left padding first
        elif(self.lpos < self.rpos):
            padding1 = " " * (self.lpos * 3) # left spacing first
            padding2 = " " * (((self.rpos-self.lpos) * 3) - 2) # right spacing second accounting for the "LH"
            return (padding1 + "LH" + padding2 + "RH")
        # IF the right hand is to the left of the left hand then add right padding first
        else:
            padding1 = " " * (self.rpos * 3) # right spacing first
            padding2 = " " * (((self.lpos-self.rpos) * 3) - 2) # left spacing second accounting for the "RH"
            return (padding1 + "RH" + padding2 + "LH")

    # Print the hand positions string which when printed lines up perfectly with the sequence string
    def print_hands(self):
        print(self.hand_string())

    # Print a summary of how the code ran for analysis and comparison with other implementations
    def print_summary(self):
        print("Code Execution Summary")
        print("----------------------")
        print("    Lines of Code: " + str(len(self.code)))
        print("Lines of Code Run: " + str(self.lines_run))
        print("  Comparisons Run: " + str(self.comp_count))
        print("        Swaps Run: " + str(self.swap_count))

    # Print code instance object as lines of code
    def __str__(self):
        return "\n".join(code_string)

    # convert each code string line into a command object using a command builder
    def compile(self):
        compiler = CodeBuilder() # initialize the compiler
        self.code = []

        # loop through each line of code
        for i,line in enumerate(self.code_string):
            # Include an error if somehow the user tries to execute line 0
            if(i == 0):
                self.code.append(Error("ERROR", 0, "Line 0 is not in the program..."))
                continue
            # Build a command from a string (removes \n from the end first)
            cmd = compiler.build_cmd(line[:-1], i)
            # Do not add an error to the code
            if(not (type(cmd) is Error)):
                self.code.append(cmd)
            # Print the compiler error instead
            else:
                print("---\nCompiler Error on Line " + str(i))
                cmd.evaluate(self)
                return
