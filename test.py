w = True
while w:
    #int
    i = 10
    #str(string)
    s = "Hello world"
    #bool
    b = True

    inp = int(input("nomre"))
    if inp < 10:
        print("mardod")
    else:
        print("pass")

    for i in range(0,10):
        print(i)

    #list
    l = ["ali", "mohammad", "hassan"]
    #dict(dictionary)
    d = {"hello":"سلام", "goodbye":"خداحافظ"}
    ay = input("agane?(y/n)")
    if ay == "n":
        w = False