def minify_program(program):
    minified_program = ""

    for ins in program:
        if ins in ["[","]","+","-","<",">",".",","]:
            minified_program += ins
        
    return minified_program


def get_loop_positions(program):
    # this is not perfect, need to add checks and edge cases

    loop_stack = []
    loop_positions = {}

    for ind, ins in enumerate(program):
        if ins == "[":
            loop_stack.append(ind)
        elif ins == "]":
            opening_loop_bracket_ind = loop_stack.pop()
            loop_positions[ind] = opening_loop_bracket_ind
            loop_positions[opening_loop_bracket_ind] = ind

    return loop_positions