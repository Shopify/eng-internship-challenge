#Main decryption function
def decrypt():
    word = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"

    #Create key without duplicate letters
    newKey = ""
    for char in key:
        if char not in newKey:
            newKey += char

    #Create alphabet with remaining letters
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    newalpha = ""
    for char in alphabet:
        if not(char in newKey):
            newalpha+=char

    index = 0
    index2 = 0
    max = len(newKey)

    #Make key matrix
    matrixKey = [[0 for _ in range(5)] for _ in range(5)]
    for i in range(0, 5):
        for j in range(0, 5):
            if (index < max):
                matrixKey[i][j] = newKey[index]
                index+=1
            else:
                matrixKey[i][j] = newalpha[index2]
                index2+=1

    #Split into digraphs
    digraphList = []
    i = 0
    while i < len(word):
        currentLetter = word[i]
        nextLetter = word[i+1]
        digraphList.append([currentLetter, nextLetter])
        i+=2
    
    #Decrypt
    encryptedWord = ""
    for i in range(0, len(digraphList)):
        #Same col
        if sameCol(digraphList[i], matrixKey):
            encryptedWord += getNextCharCol(digraphList[i][0], matrixKey)
            encryptedWord += getNextCharCol(digraphList[i][1], matrixKey)
        #Same row
        elif sameRow(digraphList[i], matrixKey):
            encryptedWord += getNextCharRow(digraphList[i][0], matrixKey)
            encryptedWord += getNextCharRow(digraphList[i][1], matrixKey)
        #Otherwise
        else:
            char1 = digraphList[i][0]
            char2 = digraphList[i][1]
            row1 = getRow(char1, matrixKey)
            row2 = getRow(char2, matrixKey)
            col1 = getCol(char1, matrixKey)
            col2 = getCol(char2, matrixKey)
            encryptedWord += matrixKey[row1][col2]
            encryptedWord += matrixKey[row2][col1]

    #Get rid of other chars
    final = ""
    for char in encryptedWord:
        if not char == "X" and not char == " ":
            final += char

    return final

#HELPER FUNCTIONS

#Finds if two chars are in the same column
def sameCol(list, matrix):
    firstCharIndex = getCol(list[0], matrix)
    secondCharIndex = getCol(list[1], matrix)
    return firstCharIndex == secondCharIndex

#Finds if two chars are in the same row
def sameRow(list, matrix):
    firstCharIndex = -1
    secondCharIndex = -1
    for i in range(0,5):
        for j in range(0, 5):
            if list[0] == matrix[i][j]:
                firstCharIndex = i
            if list[1] == matrix[i][j]:
                secondCharIndex = i
    return firstCharIndex == secondCharIndex

#Returns the char in the previous column
def getNextCharCol(char, matrix):
    charCol = getCol(char, matrix)
    charRow = getRow(char, matrix)

    if charRow - 1 < 0:
        return matrix[4][charCol]
    else:
        return matrix[charRow-1][charCol]

#Returns the char in the previous row        
def getNextCharRow(char, matrix):
    charCol = getCol(char, matrix)
    charRow = getRow(char, matrix)
    if charCol - 1 < 0:
        return matrix[charRow][4]
    else:
        return matrix[charRow][charCol-1]

#Gets column of the char in the matrix           
def getCol(char, matrix):
    for i in range(0, 5):
        for j in range(0, 5):
            if char == matrix[i][j]:
                return j

#Gets the row of the char in the matrix         
def getRow(char, matrix):
    for i in range(0, 5):
        for j in range(0, 5):
            if char == matrix[i][j]:
                return i

#Main
if __name__ == '__main__':
    result = decrypt()
    print(result)