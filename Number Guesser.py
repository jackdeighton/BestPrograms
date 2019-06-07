choice = int(input("what number have you chosen (1 - 20)"))
guess1 = input("is your number 10? (Y)es / (H)igher / (L)ower").upper()
if guess1 == "Y":
    print("done")
    
elif guess1 == "H":
    guess2 = input("is your number 15? (Y)es / (H)igher / (L)ower").upper()
    
    if guess2 == "Y":
        print("done")
        
    elif guess2 == "H":
        guess3 = input("is your number 18? (Y)es / (H)igher / (L)ower").upper()

        if guess3 == "Y":
            print("Done")
        
        elif guess3 == "H":
            guess4 = input("is your number 20? (Y)es / (L)ower").upper()
            
            if guess4 == "Y":
                print("done")

            elif guess4 == "L":
                print("your number is 19")

        elif guess3 == "L":
            guess4 = input("is your number 16? (Y)es / (H)igher").upper()
            
            if guess4 == "Y":
                print("done")

            elif guess4 == "H":
                print("your number is 17")
            
    elif guess2 == "L":
        guess3 = input("is your number 13? (Y)es / (H)igher / (L)ower").upper()

        if guess3 == "Y":
            print("done")

        elif guess3 == "H":
            guess4 = input("your number is 14").upper()
        
        elif guess3 == "L":
            guess4 = input("is your number 11? (Y)es / (H)igher").upper()

            if guess4 == "Y":
                print("done")

            elif guess4 == "H":
                print("your number is 12")

elif guess1 == "L":
    guess2 = input("is your number 5? (Y)es / (H)igher / (L)ower").upper()
    
    if guess2 == "Y":
        print("done")
        
    elif guess2 == "H":
        guess3 = input("is your number 8? (Y)es / (H)igher / (L)ower").upper()
        
        if guess3 == "Y":
            print("done")

        elif guess3 == "H":
            guess4 = input("your number is 9").upper()
        
        elif guess3 == "L":
            guess4 = input("is your number 6? (Y)es / (H)igher").upper()
            
            if guess4 == "Y":
                print("done")

            elif guess4 == "H":
                print("your number is 7")

    elif guess2 == "L":
        guess3 = input("is your number 3? (Y)es / (H)igher / (L)ower").upper()

        if guess3 == "Y":
            print("done")

        elif guess3 == "H":
            guess4 = input("your number is 4").upper()
        
        elif guess3 == "L":
            guess4 = input("is your number 1? (Y)es / (H)igher").upper()
            
            if guess4 == "Y":
                print("done")

            elif guess4 == "H":
                print("your number is 2")
