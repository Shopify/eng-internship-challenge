# Generates a 5x5 matrix of unique letters using the key
def generateMatrix(key):
    matrixVals = ""
    used = set()

    # Remove duplicates from key and add the characters to matrixVals
    for char in key:
        if(char == "J"): #Edge case: Replace J with I
            char = "I"
        if char not in used:
            matrixVals += char
            used.add(char)
    
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  

    # Add the rest of the alphabet
    for char in alphabet:
        if char not in used:
            matrixVals += char
            used.add(char)
    
    # Create 5x5 matrix with matrixVals
    matrix = []
    val_index = 0
    for i in range(5):
        row = []
        for j in range(5):
            row.append(matrixVals[val_index])
            val_index += 1
        matrix.append(row)

    return matrix

# Create pairs of letters from the text
def makePairs(text):
    pairs = []
    for i in range(0, len(text), 2):
        a = text[i]
        b = text[i + 1]
        pairs.append([a, b])
    return pairs

# Create a dictionary that maps each letter to its index in the matrix
# Improves performance by avoiding nested loops to find the index of a letter
def getLetterToIndexMap(matrix):
    letterToIndex = {}
    for i in range(5):
        for j in range(5):
            letterToIndex[matrix[i][j]] = [i, j]
    return letterToIndex

# Decrypt the ciphertext using the key
def decrypt(ciphertext, key):

    # Generate the 5x5 matrix with the key
    matrix = generateMatrix(key)

    # Create a dictionary that maps each letter to its index in the matrix
    letterToIndex = getLetterToIndexMap(matrix)

    # Create pairs of letters from the ciphertext
    cipherTextPairs = makePairs(ciphertext)
    
    plaintext = ""

    # Iterate through each pair of letters in the ciphertext
    for pair in cipherTextPairs:
        a = pair[0]
        b = pair[1]

        # Find the index of each letter in the matrix
        aIndex = letterToIndex[a]
        bIndex = letterToIndex[b]
        
        aRow = aIndex[0]
        aCol = aIndex[1]
        bRow = bIndex[0]
        bCol = bIndex[1]

        # If rows are the same, replace each letter with the letter to its left
        if(aRow == bRow):
            a = matrix[aRow][(aCol - 1) % 5]
            b = matrix[bRow][(bCol - 1) % 5]
        
        # If columns are the same, replace each letter with the letter above it
        elif(aCol == bCol):
            a = matrix[(aRow - 1) % 5][aCol]
            b = matrix[(bRow - 1) % 5][bCol]
        
        # If none of the above, make a rectangle and replace letters with opposite corners
        else:
            a = matrix[aRow][bCol]
            b = matrix[bRow][aCol]
        
        # Remove any "X" characters
        if(a == "X"):
            a = ""
        if(b == "X"):
            b = ""
        
        # Append the decrypted letters to the result
        plaintext += a + b

    return plaintext

# Validate the ciphertext
def validateCiphertext(ciphertext):
    if not ciphertext.isupper() or not ciphertext.isalpha():
        raise ValueError("Ciphertext must be all uppercase letters with no spaces or special symbols.")
    if len(ciphertext) % 2 != 0:
        raise ValueError("Ciphertext must have an even number of letters.")
    if "J" in ciphertext:
        raise ValueError("Current algorithm does not support the letter 'J' in the ciphertext.")
    
# Validate the key
def validateKey(key):
    key = key.upper().replace(" ", "")
    if not key.isalpha():
        raise ValueError("Key must be all letters.")
    return key

# Program starts here
ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
key = "SUPERSPY"

# Validate the input (with following assumptions):
# 1.) ciphertext is valid if it has all uppercase letters, even in length, and does not contain the letter 'J'
# 2.) Key must have letters/spaces only. Spaces are removed and letters are converted to uppercase
validateCiphertext(ciphertext)
key = validateKey(key)

# Decrypt the ciphertext
decrypted_message = decrypt(ciphertext, key)

# Print the decrypted message
print(decrypted_message)