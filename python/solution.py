
# 5x5 matrix given that the key is "Superspy"
key = [['S', 'U', 'P', 'E', 'R'],
       ['Y', 'A', 'B', 'C', 'D'],
       ['F', 'G', 'H', 'I', 'K'],
       ['L', 'M', 'N', 'O', 'Q'],
       ['T', 'V', 'W', 'X', 'Z']]
    
# Message to decrypt
message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

# Find the position of a letter in the key matrix
def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None, None

# Decrypt the message by reverse engineering the Playfair cypher
def decrypt(message):
    decrypted_message = ""
    for i in range(0, len(message), 2):
        char1, char2 = message[i], message[i+1]
        row1, col1 = find_position(key, char1)
        row2, col2 = find_position(key, char2)
        
        if row1 == row2:
            # Same row: move to the left
            decrypted_message += (key[row1][(col1 - 1) % 5])
            decrypted_message += (key[row2][(col2 - 1) % 5])
        elif col1 == col2:
            # Same column: move up
            decrypted_message += (key[(row1 - 1) % 5][col1])
            decrypted_message += (key[(row2 - 1) % 5][col2])
        else:
            # Rectangle: swap columns
            decrypted_message += (key[row1][col2])
            decrypted_message += (key[row2][col1])
    
    return decrypted_message

# Remove filler x's
# Note: Only do this if the x's do not make sense in the context of the decrypted message
def remove_x(message):
    final_message = ""
    i = 0

    while i < len(message):
        # Remove X if it is the last letter of an even-lengthed message:
        if message[i] == 'X' and len(message) % 2 == 0 and i == len(message) - 1:
            return final_message
        # Remove X if it is in between two identical letters
        if i > 0 and message[i] == 'X' and message[i-1] == message[i+1]:
            i += 1
        else:
            final_message += message[i]
            i += 1
    
    return final_message

# Combines decryption and removal of x's to return the final decrypted message
def decrypt_and_remove_x(message):
    initial_decryption = decrypt(message)
    final_decryption = remove_x(initial_decryption)
    print(final_decryption)
    return final_decryption

decrypt_and_remove_x(message)
