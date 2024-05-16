def find_letter_index(matrix, letter):
    # Find the position of a letter in the Playfair matrix
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == letter:
                return i, j
    # If the letter is not found, return None
    return None, None

def decrypt_pair(pair, matrix):
    letter1, letter2 = pair
    row1, col1 = find_letter_index(matrix, letter1)
    row2, col2 = find_letter_index(matrix, letter2)
    decrypted_pair = ''
    if row1 == row2:  # If same row, change each letter to the letter at its immediate left and append
        decrypted_pair += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:  # If same column, change each letter to the letter above it and append
        decrypted_pair += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:  # if not in the same row or column i.e rectangle, change each letter to the letter on the opposite edge of the rectangle and append
        decrypted_pair += matrix[row1][col2] + matrix[row2][col1]
    return decrypted_pair

def decrypt_message(message, matrix):
    decrypted_message = '' # Initialise decrypted message
    # Divide message into pairs  and decrypt them using decrypt_pair()
    for i in range(0, len(message), 2):
        decrypted_message += decrypt_pair(message[i:i+2], matrix)
    return decrypted_message

key = "SUPERSPY"
alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
matrix = []  # Initialize a list of letters used in decryption

# Get all the letters of the key ensuring none is repeated
for letter in key:
    if letter not in matrix:
        matrix.append(letter)

# Get all the letters of the alphabet ensuring none is repeated
for letter in alphabet:
    if letter not in matrix:
        matrix.append(letter)

# Reshape the matrix into a 5x5 playfair matrix
playfair_matrix = []
for i in range(0, 25, 5):
    playfair_matrix.append(matrix[i:i+5])

# Decrypt the message
decrypted_message = decrypt_message(message, playfair_matrix)
print(decrypted_message.upper().replace("X", ""))
