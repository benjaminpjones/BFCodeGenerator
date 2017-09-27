# python brainfuck interpreter

# 

import sys

rightTape = [0]
leftTape = []

class Tape:
    def __init__(self):
        self.data = dict()

    def __getitem__(self,index):
        if index in self.data:
            return self.data[index]
        else:
            return 0

    def __setitem__(self, index, value):
        self.data[index] = value%256        # (Bytes)

def run_bf_code(code_string, input):
    tape = Tape()
    ptr = 0
    input_index = 0
    input_len = len(input)

    code_len = len(code_string)
    code_index = 0

    while code_index < code_len:

        # increment/decrement
        if code_string[code_index] == '+':
            tape[ptr] += 1
        elif code_string[code_index] == '-':
            tape[ptr] -= 1

        # move pointer
        elif code_string[code_index] == '>':
            ptr += 1
        elif code_string[code_index] == '<':
            ptr -= 1

        # [loop]
        elif code_string[code_index] == '[':
            if tape[ptr] == 0:
                while code_string[code_index] != ']':
                    code_index += 1
        elif code_string[code_index] == ']':
            if tape[ptr] != 0:
                while code_string[code_index] != '[':
                    code_index -= 1

        # input/output
        elif code_string[code_index] == '.':
            sys.stdout.write(chr(tape[ptr]))
            sys.stdout.flush()
        elif code_string[code_index] == ',':
            if input_index < input_len:
                tape[ptr] = ord(input[input_index])
                input_index += 1
            else:
                tape[ptr] = 0

        code_index += 1


code_string = ",[>,]<[.<]"

run_bf_code(code_string, "abcdf")
print