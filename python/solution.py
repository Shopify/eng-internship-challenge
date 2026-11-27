
alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
keySquare = [['' for _ in range(5)] for _ in range(5)]
usedChar = set()
def decryption(encryptedMessage, dKey):
    # create square
    result = ''
    idx = 0
    for c in dKey:
        if c not in usedChar:
            row, col = divmod(idx, 5)
            usedChar.add(c)
            keySquare[row][col] = c
            idx += 1
            
    for c in alphabet:
        if c not in usedChar:
            row, col = divmod(idx, 5)
            usedChar.add(c)
            keySquare[row][col] = c
            idx += 1
    #start decrypting
    counter = 0
    while counter < len(encryptedMessage):
        val1 = encryptedMessage[counter]
        counter += 1
        val2 = encryptedMessage[counter]
        counter += 1
        row1, col1 = findPosition(val1)
        row2, col2 = findPosition(val2)
        if row1 == row2:
            if(keySquare[row1][col1-1] != "X"):
                result = result + keySquare[row1][col1-1]
            if(keySquare[row2][col2-1] != "X"):
                result = result + keySquare[row2][col2-1]
        elif col1 == col2:
            if keySquare[row1-1][col1] !="X":
                result = result + keySquare[row1-1][col1]
            if keySquare[row2-1][col2] !="X":    
                result = result + keySquare[row2-1][col2]
        else:
            if keySquare[row1][col2] != "X":
                result = result + keySquare[row1][col2]
            if keySquare[row2][col1] != "X":
                result = result + keySquare[row2][col1]
            
    print(result)
            
        
    
#find position
def findPosition(c):
    for row in range(5):
        for col in range(5):
            if keySquare[row][col] == c:
                return row, col
            
            
            
    

decryption("IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV", "SUPERSPY")