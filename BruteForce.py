passKey = str(input("Define a 4 digit pass key:\n"))
length = len(passKey)
passBreak = False
breaker = "0000"
while passBreak == False:
    breaker = int(breaker) + 1
    breaker = str(breaker)
    if len(breaker) == 1:
        printBreaker = ("000" + breaker)
    elif len(breaker) == 2:
        printBreaker = ("00" + breaker)
    elif len(breaker) == 3:
        printBreaker = ("0" + breaker)
    elif len(breaker) == 4:
        printBreaker = (breaker)
    print(printBreaker)
    if printBreaker == passKey:
        passBreak = True
print("pin is " + printBreaker)
