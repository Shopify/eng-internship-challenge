def create_matrix(key):
    # Remove duplicate letters, convert to uppercase
    filtered_key = ''.join(sorted(set(key.upper()), key=key.index))
    # Add the remaining letters of the alphabet, excluding 'J'
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    filtered_key += ''.join([char for char in alphabet if char not in filtered_key and char != 'J'])
    # Create the 5x5 matrix
    matrix = [filtered_key[i:i+5] for i in range(0, 25, 5)]
    return matrix

key = "SUPERSPY"
matrix = create_matrix(key)  # Corrected function call
print("Matrix:\n", "\n".join([" ".join(row) for row in matrix]))


#RULES FOR DECRYPTION USING PLAYFAIR CIPHER
# To decrypt using the Playfair Cipher, you need to handle pairs of letters in the ciphertext and apply the following rules based 
#on their positions in the matrix:

# Same Row: If the pair of letters is in the same row, replace each with the letter immediately to its left (wrap around if necessary).
# Same Column: If the pair is in the same column, replace each with the letter directly above it (wrap around if necessary).
# Rectangle: If the pair forms a rectangle, replace each letter with the letter in the same row but from the column of the other 
#letter in the pair.

#creating a helper function to find the position of the letter in the matrix
def find_position(matrix, char):
    for x, row in enumerate(matrix):
        if char in row:
            return (x, row.index(char))
    return None  # In case the character is not found



#create a function to decrypt a pair of letters using the matrix
def decrypt_pair(pair, matrix):
    row1, col1 = find_position(matrix, pair[0])
    row2, col2 = find_position(matrix, pair[1])

    if row1 == row2:
        # Same row, shift left
        col1 = (col1 - 1) % 5
        col2 = (col2 - 1) % 5
    elif col1 == col2:
        # Same column, shift up
        row1 = (row1 - 1) % 5
        row2 = (row2 - 1) % 5
    else:
        # Rectangle, swap columns
        col1, col2 = col2, col1

    return matrix[row1][col1] + matrix[row2][col2]


#This function combines the previous two to decrypt the entire message. The message should be processed in pairs of letters
def decrypt_message(ciphertext, matrix):
    plaintext = ''
    for i in range(0, len(ciphertext), 2):
        plaintext += decrypt_pair(ciphertext[i:i+2], matrix)
    return plaintext


#the key that will be used to decrypt
key = "SUPERSPY"
#the text that needs to be decrypted
ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
#getting the matrix by sending in the key as parameter
matrix = create_matrix(key)
#send the encrypted text and matrix as parameters to get the decrypted text back
decrypted_text = decrypt_message(ciphertext, matrix)

#should give the decrypted text now
print("Decrypted Message:", decrypted_text)