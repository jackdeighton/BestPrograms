import math
def other():
    a = float(input("what is A?"))
    b = float(input("what is B?"))
    a1 = a*a
    b1 = b*b
    c = a1 + b1
    c1 = math.sqrt(c)
    print(c1)

def hyp():
    c = float(input("what is C?"))
    b = float(input("what is B?"))
    c1 = c*c
    b1 = b*b
    d = c1 - b1
    d1 = math.sqrt(d)
    print(d1)
test = True
while test == True:
    choice = int(input("R u finding \n\aHypotenuse\n or \n\aOther \n\nChoose 1 or 2"))
    if choice == 2:
        other()
    elif choice == 1:
        hyp()
    else:
        print("Try Again...")
    
