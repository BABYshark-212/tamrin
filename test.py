while True:
    n1 = int(input("tool: "))
    n2 = int(input("arz: "))
    if n1 > 0 and n2 > 0:
        s = ("*" * n1)
        for i in range(0,n2):
            print(s)
    ay = input("agane?(y/n)")
    if ay == "n":
        exit()