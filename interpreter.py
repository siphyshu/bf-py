from utils import minify_program

print("""
=====================
BRAINFUCK INTERPRETER
=====================
""")

program = minify_program(input("> "))
size = len(program)
tape = [0]
data_pointer = 0
ins_pointer = 0

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
        print(chr(tape[data_pointer]))
    
    elif instruction == ",":
        tape[data_pointer] = ord(input()[0])

    elif instruction == "[":
        # to be implemented
        pass

    elif instruction == "]":
        # to be implemented
        pass

    ins_pointer += 1