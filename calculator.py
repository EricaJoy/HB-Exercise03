import arithmetic


while True:
    userdata = raw_input(">")
    calc = userdata.split(" ")

    if calc[0] == "q":
        break
    elif calc[0] == "+":
        print arithmetic.add(int(calc[1]),int(calc[2]))
    elif calc[0] == "-":
        print arithmetic.subtract(int(calc[1]),int(calc[2]))
    elif calc[0] == "*":
        print arithmetic.multiply(int(calc[1]),int(calc[2]))
    elif calc[0] == "/":
        print arithmetic.divide(float(calc[1]),float(calc[2]))
    elif calc[0] == "square":
        pass
    elif calc[0] == "cube":
        pass
    elif calc[0] == "pow":
        pass
    elif calc[0] == "mod":
        pass
