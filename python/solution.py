def createMatrix(keyphrase):
    cipherMatrix = [['' for _ in range(5)] for _ in range(5)]  # Create a 5x5 matrix
    
    # Adjust the keyphrase, replacing 'J' with 'I', and add the rest of the alphabet
    keyphrase = keyphrase.replace('J', 'I') + 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    
    usedChars = set()  # Keep track of used characters to ensure uniqueness
    row, col = 0, 0
    
    # Fill the matrix with characters from the keyphrase
    for char in keyphrase:
        if char not in usedChars:
            cipherMatrix[row][col] = char
            usedChars.add(char)
            col += 1

            if col == 5:
                row += 1
                col = 0

    return cipherMatrix

def findPosition(matrix, character):
    for rowIdx, row in enumerate(matrix):
        for colIdx, char in enumerate(row):
            if char == character:
                return rowIdx, colIdx

def decryptMessage(ciphertext, keyphrase):
    # Create the Playfair matrix using the keyphrase
    matrix = createMatrix(keyphrase)
    decryptedText = ''
    
    # Replace 'J' with 'I' in the ciphertext
    ciphertext = ciphertext.replace('J', 'I')
    
    # Split the ciphertext into digraphs
    digraphs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    
    # Iterate through each digraph in the ciphertext
    for digraph in digraphs:
        char1, char2 = digraph[0], digraph[1]
        
        # Find the row and column of each character in the matrix
        row1, col1 = findPosition(matrix, char1)
        row2, col2 = findPosition(matrix, char2)
        
        # Decrypt the digraph based on its position in the matrix
        if row1 == row2:  # If both characters are in the same row
            decryptedText += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # If both characters are in the same column
            decryptedText += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:  # If the characters form a rectangle
            decryptedText += matrix[row1][col2] + matrix[row2][col1]
    
    # Remove any 'X' characters from the decrypted text
    decryptedText = decryptedText.replace('X', '')
    
    return decryptedText

# Define the ciphertext and the keyphrase
encryptedMessage = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
keyphrase = "SUPERSPY"

# Decrypt the ciphertext using the keyphrase and print the message
decryptedMessage = decryptMessage(encryptedMessage, keyphrase)
print(decryptedMessage)
