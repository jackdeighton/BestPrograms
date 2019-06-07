numberEntered = True
numbersList =[]
while numberEntered == True:
    numbersList.append(int(input("What is your number")))
    carryOn = input("Do you want to add another number?(y)/(n)")
    if carryOn == "y":
        numberEntered = True
    elif carryOn == "n":
        numberEntered = False
haveNumbersSwapped = True
print("The starting list is", numbersList)
while haveNumbersSwapped == True:
    haveNumbersSwapped = False
    for index in range(0,len(numbersList)-1):
        firstNumber = numbersList[index]
        secondNumber = numbersList[index+1]
        if firstNumber > secondNumber:
            numbersList[index]=secondNumber
            numbersList[index+1]=firstNumber
            haveNumbersSwapped = True
print("Sort Completed!\nHere is your sorted list:")
print(numbersList)
