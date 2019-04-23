from commands.command import Command

class Swap(Command):
    def __init__(self, text, line_num):
        super(Swap, self).__init__("SWAP", text, line_num)

    # Swap the cards under both hands when run
    def evaluate(self, code_instance):
        temp = code_instance.seq[code_instance.lpos] # temporarily store one card
        code_instance.seq[code_instance.lpos] = code_instance.seq[code_instance.rpos] # Swap
        code_instance.seq[code_instance.rpos] = temp # reset right hand to old left value
        code_instance.curr_line += 1
        code_instance.swap_count += 1
