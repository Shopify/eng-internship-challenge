# Creates the string representing the matrix
# createMatrix: String -> String
def createMatrix(Key):
    keyAndAlphabet = Key.upper() + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    matrixString = ""
    used = set()
    for letter in keyAndAlphabet:
        # Ensures that letter has not been used and that the letter is not a special character.
        if letter not in used and letter.isalpha():
            if letter == 'I' or letter == 'J':
                used.add('I')
                used.add('J')
            else:
                used.add(letter)
            matrixString += letter
    return matrixString

# Returns the row and column of which char would be located in the matrix
# getPosition: Char String -> Int Int
def getPosition(char, matrixString):
    index = 0
    Length = len(matrixString)
    for i in range(Length):
        if matrixString[i] == char:
            index = i
            break
    return index // 5, index % 5

# Returns the decrypted text after going through the decryption process for the Playfair Cipher.
# decryptionPlayfairCipher: String String -> String
def decryptionPlayfairCipher(ciphertext, key):
    matrixStr = createMatrix(key)
    plaintext = ""
    Length = len(ciphertext)
    for i in range (0, Length, 2):
        rowOne, colOne = getPosition(ciphertext[i], matrixStr)
        rowTwo, colTwo = getPosition(ciphertext[i + 1], matrixStr)
        if rowOne == rowTwo:
            plaintext += matrixStr[(rowOne * 5) + ((colOne - 1) % 5)] + matrixStr[(rowTwo * 5) + ((colTwo - 1) % 5)]
        elif colOne == colTwo:
            plaintext += matrixStr[5 * ((rowOne - 1) % 5) + colOne] + matrixStr[5 * ((rowTwo - 1) % 5) + colTwo]
        else:
            plaintext += matrixStr[(rowOne * 5 + colTwo)] + matrixStr[rowTwo * 5 + colOne]
        
        plaintext = plaintext.replace(" ", "")
        plaintext = plaintext.replace("X", "")

    return plaintext

key = "SUPERSPY"
encryptedText = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
print(decryptionPlayfairCipher(encryptedText, key))