# Playfair Cipher Decryption Implementation

# Function to clean and prepare the key matrix/grid
def prepareKeyMatrix(key):
    # Remove duplicates and replace 'J' with 'I'
    seenChars = set()
    cleanedKey = []
    for char in key.upper().replace('J', 'I'):
        if char not in seenChars and char.isalpha():
            seenChars.add(char)
            cleanedKey.append(char)
    
    # Add the rest of the alphabet
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    for char in alphabet:
        if char not in seenChars:
            cleanedKey.append(char)
    
    # Create a 5x5 matrix
    matrix = [cleanedKey[i * 5:(i + 1) * 5] for i in range(5)]
    return matrix

# Function to find the row and column of a character in the matrix
def findPosition(matrix, char):
    for rowIndex, row in enumerate(matrix):
        if char in row:
            return (rowIndex, row.index(char))
    return None

# Function to decrypt the Playfair ciphertext
def decryptPlayfairCipher(ciphertext, key):
    matrix = prepareKeyMatrix(key)
    # Clean and prepare the ciphertext
    filteredCiphertext = ''.join([c for c in ciphertext.upper() if c in 'ABCDEFGHIKLMNOPQRSTUVWXYZ'])

    # Check if we need to pad the ciphertext to ensure even length
    if len(filteredCiphertext) % 2 != 0:
        filteredCiphertext += 'X'

    # Decrypt each digraph
    decryptedText = ''
    i = 0

    while i < len(filteredCiphertext):
        char1 = filteredCiphertext[i]
        char2 = filteredCiphertext[i + 1] if (i + 1) < len(filteredCiphertext) else 'X'

        r1, c1 = findPosition(matrix, char1)
        r2, c2 = findPosition(matrix, char2)

        if r1 == r2:
            # Same row: move to the left
            decryptedText += matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:
            # Same column: move up
            decryptedText += matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
        else:
            # Rectangle: swap columns
            decryptedText += matrix[r1][c2] + matrix[r2][c1]

        i += 2

    return decryptedText.replace('X', '').upper()

# Given data
ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
key = "SUPERSPY"

# Decrypt the message
decryptedMessage = decryptPlayfairCipher(ciphertext, key)
print(decryptedMessage)
