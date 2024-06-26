def generate_playfair_key_matrix(key):
    ''' Generate a 5x5 matrix for the Playfair cipher
    :param key: The key to use for the matrix
    :return: A 5x5 matrix for the Playfair cipher
    '''
    
    # The key is used to fill the matrix, then the remaining letters of the alphabet are added
    # J is omitted, and I is replaced with J
    key = key.upper().replace('J', 'I')
    matrix = []

    # Keep track of used characters
    used_chars = set()
    
    # Add key to the matrix
    for char in key:
        if char not in used_chars:
            matrix.append(char)
            # Skip adding the same character again if it's already in the key
            used_chars.add(char)
    
    # Add remaining letters of the alphabet
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # J is omitted
    for char in alphabet:
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)
    
    # This is to create a 5x5 matrix
    key_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]

    # Print matrix for testing
    # for row in key_matrix:
    #     print(row)

    return key_matrix

def find_position(matrix, char):
    ''' Find the position of a character in the matrix
    :param matrix: The matrix to search
    :param char: The character to find
    :return: The row and column of the character in the matrix
    '''

    for row in range(5):
        for column in range(5):
            if matrix[row][column] == char:
                return row, column
    return None

def decrypt_playfair_cipher(ciphertext, key_matrix):
    ''' Decrypt a Playfair cipher
    :param ciphertext: The text to decrypt
    :param key_matrix: The key matrix to use for decryption
    :return: The decrypted text'''
    
    decrypted_text = []
    ciphertext = ciphertext.upper().replace('J', 'I')
    
    for i in range(0, len(ciphertext), 2):
        # A playfair cipher is a digraph cipher, so we process two characters at a time
        a = ciphertext[i]
        b = ciphertext[i+1]

        # Find the positions of each of the characters in the key matrix
        row_a, col_a = find_position(key_matrix, a)
        row_b, col_b = find_position(key_matrix, b)
        
        # If the characters are in the same row, column, or form a rectangle, we decrypt them accordingly to the rule.

        # First option: Two character are same row
        if row_a == row_b:
            # Shift one position to the left or wrap around if at the end of the row
            decrypted_text.append(key_matrix[row_a][(col_a - 1) % 5])
            decrypted_text.append(key_matrix[row_b][(col_b - 1) % 5])
        # Second option: Two characters are same column
        elif col_a == col_b:
            # Shift one position up or wrap around if at the end of the column
            decrypted_text.append(key_matrix[(row_a - 1) % 5][col_a])
            decrypted_text.append(key_matrix[(row_b - 1) % 5][col_b])
        # Rectangle
        else:
            # We take the characters at the same row but at the column of the other character
            decrypted_text.append(key_matrix[row_a][col_b])
            decrypted_text.append(key_matrix[row_b][col_a])
    
    return ''.join(decrypted_text)

# Main decryption process
key = "SUPERSPY"
ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
key_matrix = generate_playfair_key_matrix(key)
password = decrypt_playfair_cipher(ciphertext, key_matrix)

# remove Xs (as required)
password = password.replace('X', '')

# remove spaces (as required)
password = password.replace(' ', '')

#remove special characters (as required)
for char in password:
    if not char.isalnum():
        password = password.replace(char, '')

print(password)

