def xk():
    global k
    x = int(input("What is 'X'?"))
    total = int(k / x)
    print(total)
def yk():
    global k
    y = int(input("What is 'Y'?"))
    total1 = int(k / y)
    print(total1)
print("x = k/y")
k = int(input("What is 'K'?"))
choice = input("Do you have x or y?")
if choice == "x":
    xk()
elif choice == "y":
    yk()
    
