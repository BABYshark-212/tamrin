while True:
    a = int(input("first num: "))
    b = str(input("operator: "))
    c = int(input("second num: "))
    d = float
    match b:
        case "+":
            d = a+c
        case "-":
            d = a-c
        case "×" | "*":
            d = a*c
        case "/" | "÷":
            d = a/c
        case "√":
            d = c**(1/a)
        case "^":
            d = a**c
    if d == int(d):
        d = int(d)
    print(d)
    if input("exit?(y/n) ") == "y":
        exit()