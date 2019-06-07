def increase():
    firstNumber = int(input("Origonal number"))
    secondNumber = int(input("Increase by what"))
    thirdNumber = firstNumber / 100
    fourthNumber = thirdNumber * secondNumber
    fithNumber = fourthNumber + firstNumber
    print(fithNumber)

def decrease():
    firstNumber = int(input("Origonal number"))
    secondNumber = int(input("Decrease by what"))
    thirdNumber = firstNumber / 100
    fourthNumber = thirdNumber * secondNumber
    fithNumber = fourthNumber - firstNumber
    print(fithNumber)
direct = input("Increase(I) or Decrease(D)?")
direct = direct.upper()
if direct == "I":
    increase()
elif direct == "D":
    decrease()
