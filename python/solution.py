'''
Author: Manpreet Rajpal 
Program: Encrypts and Decrypts a message using the Playfair Cipher technique 
'''
def cleanAlpha(text):
    #removing all special characters, leaving us with just the alphabet 
    alpha = ""
    for char in text.upper(): 
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            alpha += char 
    return alpha

def generatePlayfairSquare(keyWord): 
    #removed J from the alphabet as it is generally not included in this technique 
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    playfairSquare = []
    playfairSet = set()

    #inseting the keyWord letter by letter in the playfair cipher 
    for char in keyWord: 
        if char not in playfairSet and char in alphabet: 
            playfairSquare.append(char)
            playfairSet.add(char)

    #filling up the rest of the sqaure with the alphabet 
    for char in alphabet: 
        if char not in playfairSet: 
            playfairSquare.append(char)
            playfairSet.add(char)
    
    #creating a 5 by 5 matrix using the the playfairSquare 
    matrix = []

    # Iterate over the range 0 to 25 with a step size of 5
    for i in range(0, 25, 5):
        substring = playfairSquare[i:i + 5]
        # Append the extracted substring to the list
        matrix.append(substring)
    return matrix

def swap(playfairSquare, char):
    for i in range(5):
        for j in range(5): 
            if playfairSquare[i][j] == char: 
                return i, j
    return -1, -1

def decryptMsg(encryptedMsg, keyWord):
    matrix = generatePlayfairSquare(cleanAlpha(keyWord))
    encryptedMsg = cleanAlpha(encryptedMsg)
    decryptedMsg = ""

    for i in range(0, len(encryptedMsg), 2):
        char1 = encryptedMsg[i]
        char2 = encryptedMsg[i+1]
        row1, col1 = swap(matrix, char1)
        row2, col2 = swap(matrix, char2)

        # handling the case for when the pair is in the same row 
        if row1 == row2:
            decryptedMsg += matrix[row1][(col1-1)%5]
            decryptedMsg += matrix[row2][(col2-1)%5]
        # handling the case for when the pair is in the same column
        elif col1 == col2:
            decryptedMsg += matrix[(row1-1)%5][col1]
            decryptedMsg += matrix[(row2-1)%5][col2]
        # handling the case for when the pair is in different row and column
        else:
            decryptedMsg += matrix[row1][col2]
            decryptedMsg += matrix[row2][col1]

    # Making sure that the final decrypted msg does not include 'X'
    return decryptedMsg.replace('X', '')


encryptedMsg = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
keyWord = "SUPERSPY"
print(decryptMsg(encryptedMsg, keyWord))

