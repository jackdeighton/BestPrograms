##Vernham Cypher##
###Message
while True:#Loops
    from operator import xor#imports the xor logic gate
    fileAccumalator = 0
    binMessage = []
    mergedString = ""
    mergedList = []
    message = input("Enter the Letter to be Encoded...\n")#takes the letter to be encrypted
    message = " ".join(message)
    message = message.split()
    for i in message:
        a = ord(i)
        a = bin(a)
        a = (a[2:])
        a = str(a)
        binMessage.append(a)
    ###One Time Pad
    binPad = []
    oneTimePad = input("Enter the One-Time-Pad...\n")
    oneTimePad = " ".join(oneTimePad)
    oneTimePad = oneTimePad.split()
    for x in oneTimePad:
        b = ord(x)
        b = bin(b)
        b = (b[2:])
        b = str(b)
        binPad.append(b)
    ###Merging
    count = 0
    count1 = 0
    joined = []
    for each in binMessage:
        list1Item = (binMessage[count])
        list2Item = (binPad[count])
        for z in range(0,7):
            list1Itema = int(list1Item[count1])
            list2Itema = int(list2Item[count1])
            joined.append(xor(list1Itema, list2Itema))
            count1 += 1
        count += 1
        mergedString = "".join(map(str, joined))
        mergedInt = int(mergedString, 2)
        mergedASCII = chr(mergedInt)
        ###File write
        file = open("EncryptedBinary.txt", "a")
        file.write(mergedString + "\n")
        file.close()
        file2 = open("EncryptedASCII.txt", "a")
        file2.write(mergedASCII + "\n")
        file2.close()
