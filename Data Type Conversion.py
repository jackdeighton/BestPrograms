while True:

    def db():
        var1 = int(input("Enter the denary number"))
        var2 = bin(var1)
        print("0" + var2[2:])
    def dh():
        var1 = int(input("Enter the denary number"))
        var2 = hex(var1)
        print(var2[2:])
    def da():
        var1 = int(input("Enter the denary number"))
        var2 = chr(var1)
        print(var2)
    #
    def bd():
        var1 = input("Enter the binary number")
        var1 = int(var1, 2)
        print(var1)
    def bh():
        var1 = input("Enter the binary number")
        var1 = int(var1, 2)
        var2 = hex(var1)
        print(var2[2:])
    def ba():
        var1 = input("Enter the binary number")
        var1 = int(var1, 2)
        var1 = chr(var1)
        print(var1)
    #
    def hd():
        var1 = input("Enter the hexadecimal number")
        var1 = int(var1, 16)
        print(var1)
    def hb():
        var1 = int(input("Enter the hexadecimal number"))
        var1 = int(var1, 16)
        var2 = bin(var1)
        print("0" + var2[2:])
    def ha():
        var1 = input("Enter the hexadecimal number")
        var1 = int(var1, 16)
        var1 = chr(var1)
        print(var1)
    #
    def ad():
        var1 = input("Enter the ASCII character")
        var1 = ord(var1)
        print(var1)
    def ab():
        var1 = input("Enter the ASCII character")
        var1 = ord(var1)
        var1 = bin(var1)
        print(var1)
    def ah():
        var1 = input("Enter the ASCII character")
        var1 = ord(var1)
        var1 = hex(var1)
        print(var1)
    #
    def ASCIIChoose():
        choose = int(input("1. ASCII to Denary\n2. ASCII to Binary\n3. ASCII to Hexidecimal\n"))
        if choose == 1:
            ad()
        elif choose == 2:
            ab()
        elif choose == 3:
            ah()
    def hexChoose():
        choose = int(input("1. Hexidecimal to Denary\n2. Hexidecimal to Binary\n3. Hexidecimal to ASCII\n"))
        if choose == 1:
            hd()
        elif choose == 2:
            hb()
        elif choose == 3:
            ha()
    def binChoose():
        choose = int(input("1. Binary to Denary\n2. Binary to Hexidecimal\n3. Binary to ASCII\n"))
        if choose == 1:
            bd()
        elif choose == 2:
            bh()
        elif choose == 3:
            ba()
    def denChoose():
        choose = int(input("1. Denary to Binary\n2. Denary to Hexidecimal\n3. Denary to ASCII\n"))
        if choose == 1:
            db()
        elif choose == 2:
            dh()
        elif choose == 3:
            da()
    #
    start = int(input("Are you starting with:\n1. Denary\n2. Binary\n3. Hexadecimal\n4. ASCII\n"))
    if start == 1:
        denChoose()
    elif start == 2:
        binChoose()
    elif start == 3:
        hexChoose()
    elif start == 4:
        ASCIIChoose()
