# Define a function to create a 5x5 matrix filled with unique characters from the key
def playfairSetup(key):
    emptyMatrix = [['' for _ in range(5)] for _ in range(5)]  # Create an empty 5x5 matrix
    
    # Replace 'J' with 'I' in the key and append the rest of the alphabet
    key = key.replace('J', 'I') + 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    
    used = set()  # Keep track of used characters to ensure uniqueness
    row = 0
    col = 0
    
    # Fill the matrix with characters from the key
    for char in key:
        if char not in used:

            emptyMatrix[row][col] = char
            used.add(char)
            col += 1

            if col == 5:
                row += 1
                col = 0

    return emptyMatrix



# Define a function to find the row and column of a character in the matrix
def decipherCharacter(matrix, char):

    for i in range(5):
        for j in range(5):

            if matrix[i][j] == char:

                return i, j



# Define a function to decrypt the ciphertext using the Playfair Cipher and the given key
def decryptTheMessage(ciphertext, key):
    # Create the Playfair matrix using the key
    matrix = playfairSetup(key)
    decrypted_text = ''
    
    # Replace 'J' with 'I' in the ciphertext
    ciphertext = ciphertext.replace('J', 'I')
    
    # Split the ciphertext into digraphs
    digraphs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    
    # Iterate through each digraph in the ciphertext
    for digraph in digraphs:
        char1, char2 = digraph[0], digraph[1]
        
        # Find the row and column of each character in the matrix
        row1, col1 = decipherCharacter(matrix, char1)
        row2, col2 = decipherCharacter(matrix, char2)
        
        # Decrypt the digraph based on its position in the matrix
        if row1 == row2:  # If both characters are in the same row
            decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # If both characters are in the same column
            decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:  # If the characters form a rectangle
            decrypted_text += matrix[row1][col2] + matrix[row2][col1]
    
    # Remove any 'X' characters from the decrypted text
    decrypted_text = decrypted_text.replace('X', '')
    
    return decrypted_text

# Define the ciphertext and the key
textMessage = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
key = "SUPERSPY"

# Decrypt the ciphertext using the key and print the message
message = decryptTheMessage(textMessage, key)
print(message)
