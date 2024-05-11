def filter(keyString):
    charSet = set()
    filteredKey = []
    for char in keyString:
        if char not in charSet:
            charSet.add(char)
            filteredKey.append(char)
    # Now append the alphabet without repeating letters
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" # drop J from alphabet for 5x5 matrix to fit as per playfair ruling
    for char in alphabet:
        if char not in filteredKey:
            filteredKey.append(char)
    filteredKey = ''.join(filteredKey)
    return filteredKey

def createMatrix(cipherString):
    matrix = []
    for i in range(0, len(cipherString), 5):
        subString = cipherString[i:i+5]
        row = []
        for char in subString:
            row.append(char)
        matrix.append(row)
    return matrix

def locateIndicesOfPair(matrix, char):
    # Need to loop through the entire matrix to find the exact position of each character given  
    for i, row in enumerate(matrix):
        for j, column in enumerate(row):
            if char == column:
                print (char, i , j)
                return i, j

def decryptMsg(encryptedMsg, cipherKey):
    # Construct 5x5 matrix and ensure removal of duplicate letters/non alphabetical letters
    filteredCipher = filter(cipherKey)
    # Create a 5x5 matrix using a 2D array in python    
    matrix = createMatrix(filteredCipher)
    # Now, we need to go through the encrypted message with 2 letters at a time, and using the reverse ruling, we can decrypt the message
    decryptedPairs = []
    for i in range(0, len(encryptedMsg), 2):
        pair = encryptedMsg[i:i+2]
        # Manually, we can just look at the matrix to see rows and column values, but for our implementation we will instead get the exact row and column indices and compare them
        firstChar = pair[0]
        secondChar = pair[1]
        firstRow, firstColumn = locateIndicesOfPair(matrix, firstChar)
        secondRow, secondColumn = locateIndicesOfPair(matrix, secondChar)
                



def main():
    # Variables
    encryptedMsg = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    cipherKey = "SUPERSPY"

    # Plan: The playfair cipher has an encryption and decryption process, from understanding the 
    # encryption process we can proceed to decrypting it.

    # The decryption process begins by grouping up the encrypted message into pairs of letters, then reversing encryption. 
    # We also need to then place the encrypted message into a 5*5 matrix, and utilize the 3 encryption rules to undo the process

    # First manually decrypt the message, then code it. Drop the J and make the matrix with superspy
    # # # # # # 
    # S U P E R                 # IK EW EN EN XL NQ LP ZS LE RU MR HE ER YB OF NE IN CH CV
    # Y A B C D                 # HI PX PO PO TO MO NS TR OS ES QU IP PE DA LI OP HO BI AX
    # F G H I K                 # HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA - decrypted message
    # L M N O Q
    # T V W X Z

    decryptMsg(encryptedMsg, cipherKey)


if __name__ == "__main__":
    main()