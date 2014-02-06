import arithmetic

# basic function takes 3 arguments
# arg1, arg2, and arg3 are the tokenized items from raw input
# operators is a dictionary that maps tokenized raw input operator
# to arithmetic function.

def basic(arg1, arg2, arg3):
    operators = {
        "+": arithmetic.add,
        "-": arithmetic.subtract,
        "*": arithmetic.multiply,
        "/": arithmetic.divide,
        "pow": arithmetic.power,
        "mod": arithmetic.mod
    }

    print operators[arg1](int(arg2),int(arg3))

while True:
    userdata = raw_input(">")
    calc = userdata.split(" ")

    if calc[0] == "+" or calc[0] == "-" or calc[0] == "*" or calc[0] == "/" or calc[0] == "pow" or calc[0] == "mod":
        if len(calc) == 3 and str(calc[1]).isdigit() == True and str(calc[2]).isdigit() == True:
            basic(calc[0], calc[1], calc[2])
        else:
            print "Please provide two numbers to calculate."

    elif calc[0] == "square":
        print arithmetic.square(int(calc[1]))

    elif calc[0] == "cube":
        print arithmetic.cube(int(calc[1]))

    elif calc[0] == "q":
        break

    else:
        print "That's not a valid function. Valid functions are \
+, -, *, /, mod, square, cube, pow, or q."

