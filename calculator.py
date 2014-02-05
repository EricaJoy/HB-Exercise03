import arithmetic

def basic(arg1, arg2, arg3):
    operators = {
        "+": arithmetic.add,
        "-": arithmetic.subtract,
        "*": arithmetic.multiply,
        "pow": arithmetic.power,
        "mod": arithmetic.mod
    }

    print operators[arg1](int(arg2),int(arg3))

while True:
    userdata = raw_input(">")
    calc = userdata.split(" ")

    if calc[0] == "+" or "-" or "*" or "pow" or "mod":
        basic(calc[0], calc[1], calc[2])

    elif calc[0] == "/":
        print arithmetic.divide(float(calc[1]),float(calc[2]))

    elif calc[0] == "square":
        print arithmetic.square(int(calc[1]))

    elif calc[0] == "cube":
        print arithmetic.cube(int(calc[1]))

    elif calc[0] == "q":
        break

    else:
        print "That's not a valid function. Valid functions are"
        "+, -, *, /, mod, square, cube, pow, or q."

