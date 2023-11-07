def minify_program(program):
    minified_program = ""

    for instruction in program:
        if instruction in ["[","]","+","-","<",">",".",","]:
            minified_program += instruction
        
    return minified_program