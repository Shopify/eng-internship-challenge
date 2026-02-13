#--------------------------
# Playfair Cipher - Paulo Massao Kawakami
#--------------------------

#Define function to deal with duplicates
def removeDuplicatesFromString(aString):
    resultList = []
    for i in aString:
        # print(i)
        if (i in resultList):
            # print("found")
            pass
        else:
            resultList.append(i)
    #list = list(password)
    return(resultList)


#Generate the Playfair cypher table
def generateTable(aPassword):
    #alphabet ignoring J
    modifiedAlphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']
    #transform password into list and merge with the modifiedAlpabet
    uniqueList = removeDuplicatesFromString(list(aPassword) + modifiedAlphabet)
    #define table row by row 5 x 5
    resultSet = []
    for i in range(5):
        row = []
        for j in range(5):
            #apply multiplier by 5 to define a delimiter and next starting point in the uniqueList
            row.append(uniqueList[i*5 + j])
        resultSet.append(row)
    return resultSet


#Set pairs - return a tuple of paired elements
def getPairs(aCode):
    result = []
    i = 1
    while(i < len(aCode)):
        #case duplicated letter, insert X and decrement the iterator by 1
        if(aCode[i-1] == aCode[i]):
            result.append((aCode[i-1], "X"))
            i-= 1
        else:
            result.append((aCode[i-1], aCode[i]))
        i += 2
    #append final pair in case it is uneven
    if(i == len(aCode)):
        result.append((aCode[-1], "X"))
    return result

#Search value - return the position of an element in a table
def searchPosition(aTable, aValue):
    for i in range(len(aTable)):
        for j in range(len(aTable[i])):
            if aTable[i][j] == aValue:
                return (i,j)
    return

#PlayfairCipher - define modes for Encrypt/Decrypt
def playfairCipher(aMessage, aKey, aMode):
    #set parameters
    pairs = getPairs(aMessage)
    cipherTable = generateTable(aKey)
    result = []

    #loop through pairs to get row and column in the cipherTable
    for pair in pairs:  

        #get position from each character in the cipherTable
        position = []
        for element in pair:
            position.append(searchPosition(cipherTable, element)) #call searchPosition to get its reference on the the table

        #apply chiper
        cipheredPair = []
        min = 0
        max = 4

        for i in range(2):
            row = position[i][0]
            col = position[i][1]

            #if same row, apply the to shift columns
            if position[0][0] == position[1][0]:
                #apply direction based on the mode Encrypt or decript
                #encrypt
                if aMode:
                    if col < max:
                        col += 1
                    else:
                        col = min
                #decrypt
                else:
                    if col > min:
                        col -= 1
                    else:
                        col = max

            #if same column, apply the following rule
            elif  position[0][1] == position[1][1]:
                #apply direction based on the mode Encrypt or decript
                #encrypt
                if aMode:
                    if row < max:
                        row += 1
                    else:
                        row = min
                #decrypt    
                else:
                    if row > min:
                        row -= 1
                    else:
                        row = max

            #in case none of the above, apply rectangle rule - Mode does not affect this, as it is swapping
            else:
                if i == 0:
                    col = position[1][1]
                else:
                    col = position[0][1]

            #append to pair
            cipheredPair.append(cipherTable[row][col])
        
        #append to result list
        result.append(cipheredPair)

    #Deal with decrypting

    return result

#displayResult
def showMessage(aMessage):
    resultMessage = ""
    for i in range(len(aMessage)):
        for j in range(2):
            #solve the X for duplicates or filler
            if len(resultMessage) > 0:
                if ((resultMessage[-1] == "X" and resultMessage[len(resultMessage)-2] == aMessage[i][j])):
                    resultMessage = resultMessage[:len(resultMessage)-1]
            resultMessage += aMessage[i][j]
    #solve message ending with X
    if resultMessage[-1] == "X":
        resultMessage = resultMessage[:len(resultMessage)-1]
    return resultMessage
    
#Testing
# password = ("playfair example").upper().replace(" ", "")
# message = ("hide the gold in the tree stump").upper().replace(" ", "")
# resultMessage = playfairCipher(message,password,1)
# #encrypted
# displayMessage = showMessage(resultMessage)
# print(displayMessage)
# #decripted
# resultMessage = playfairCipher(displayMessage,password,0)
# displayMessage = showMessage(resultMessage)
# print(displayMessage)

message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
password = ("SUPERSPY").upper().replace(" ", "")
resultMessage = playfairCipher(message,password,0)
displayMessage = showMessage(resultMessage)
print(displayMessage)