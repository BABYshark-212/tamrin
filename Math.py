import re
while True:
    try:
        expr = input("math: ")

        # فقط عدد، اعشار، عملگرها، پرانتز و فاصله مجاز است
        if not re.fullmatch(r'[\d\s.+\-*/()]+', expr):
            raise ValueError("wrang input!")

        result = eval(expr)

        if result == int(result):
            result = int(result)

        print("res: ", result)

        if input("Exit?(y,n): ") == "y":
            exit(0)

    except Exception as e:
        print("Error: ", e)