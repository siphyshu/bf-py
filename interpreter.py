from utils import get_loop_positions, minify_program

print("""
=====================
BRAINFUCK INTERPRETER
=====================
""")

program = minify_program(input("> "))
loop_positions = get_loop_positions(program)
size = len(program)

tape = [0]
data_pointer = 0
ins_pointer = 0

input_buffer = []

while ins_pointer < size:
    instruction = program[ins_pointer]

    if instruction == "+":
        tape[data_pointer] += 1
        if tape[data_pointer] == 256:
            tape[data_pointer] = 0

    elif instruction == "-":
        tape[data_pointer] -= 1
        if tape[data_pointer] == -1:
            tape[data_pointer] = 0

    elif instruction == ">":
        data_pointer += 1
        if data_pointer == len(tape):
            tape.append(0)

    elif instruction == "<":
        data_pointer -= 1
        if data_pointer < 0:
            data_pointer = 0

    elif instruction == ".":
        print(chr(tape[data_pointer]), end="")
    
    elif instruction == ",":
        if len(input_buffer) == 0:
            input_buffer = list(input() + "\n")

        tape[data_pointer] = ord(input_buffer.pop(0))

    elif instruction == "[":
        if tape[data_pointer] == 0:
            ins_pointer = loop_positions[ins_pointer]

    elif instruction == "]":
        if tape[data_pointer] != 0:
            ins_pointer = loop_positions[ins_pointer]

    ins_pointer += 1