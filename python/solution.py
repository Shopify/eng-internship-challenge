# given a key, returns the associated 5x5 matrix for the playfair cipher
def getPlayfairMatrix(key): 
    # replace instances of J with I in key since I = J in the matrix (ie. J is ommitted)
    key = key.replace("J", "I")
    matrix = [[""] * 5 for _ in range(5)]
    rowLen = len(matrix[0])
    currIdx = 0
    visitedLetters = {}
    # iterate through key first
    for c in key: 
        if c in visitedLetters: 
            continue
        visitedLetters[c] = True
        row = currIdx // rowLen
        col = currIdx % rowLen
        matrix[row][col] = c
        currIdx += 1

    
    # iterate through all letters of the alphabet to insert remaining letters (skipping J since I = J)
    ordA = ord("A")
    for i in range(26): 
        asciiCode = ordA + i
        c = chr(asciiCode)
        if c == "J": 
            continue
        if c in visitedLetters: 
            continue
        visitedLetters[c] = True
        row = currIdx // rowLen
        col = currIdx % rowLen
        matrix[row][col] = c
        currIdx += 1
    return matrix


# given a playfair cipher matrix and an encrypted message
# returns the decrypted message
# *** REQUIRES THAT THE ENCRYPTED MESSAGE HAS EVEN LENGTH *** 
# (ie. should have been padded by X before encrypting if odd length message)
def playfairDecrypt(matrix, charToPosition, message): 
    if len(message) % 2 != 0: 
        raise Exception("Encrypted message length must be even!")

    decryptedMessage = ""
    idx = 0
    rowLen = len(matrix)
    colLen = len(matrix[0])

    # iterate through all pairs of letters in message
    while idx < len(message): 
        char1 = message[idx]
        char2 = message[idx+1]
        row1, col1 = charToPosition[char1]
        row2, col2 = charToPosition[char2]

        resRow1 = row1
        resCol1 = col1
        resRow2 = row2
        resCol2 = col2

        # my assumption is that if a pair of letters are the same letter then both the row shift and 
        # the column shift are applied

        # same row, therefore column was shifted
        if row1 == row2: 
            resCol1 = (resCol1 - 1) % colLen
            resCol2 = (resCol2 - 1) % colLen
        # same col, therefore row was shifted
        if col1 == col2: 
            resRow1 = (resRow1 - 1) % rowLen
            resRow2 = (resRow2 - 1) % rowLen
        # rectangle case
        if row1 != row2 and col1 != col2:
            resCol1 = col2
            resCol2 = col1 
        
        decryptedMessage += matrix[resRow1][resCol1] + matrix[resRow2][resCol2]
        idx += 2
    
    decryptedMessage = decryptedMessage.replace("X", "")
    return decryptedMessage

# given a matrix of characters 
# getCharToPosition returns a dictionary with the keys being 
# characters and the values being a tuple of the (rowIdx, colIdx) of
# the character in the matrix
def getCharToPosition(matrix): 
    charToPosition = {}
    for rowIdx in range(len(matrix)): 
        for colIdx in range(len(matrix[rowIdx])): 
            char = matrix[rowIdx][colIdx]
            charToPosition[char] = (rowIdx, colIdx)
    return charToPosition


def main(): 
    encryptedMessage = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"
    matrix = getPlayfairMatrix(key)
    charToPosition = getCharToPosition(matrix)
    decryptedMessage = playfairDecrypt(matrix, charToPosition, encryptedMessage)
    print(decryptedMessage)

if __name__ == '__main__':
    main()