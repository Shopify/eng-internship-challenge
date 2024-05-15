def generate_playfair_key(key):
    """
    This function generates the Playfair key matrix from the provided key.
    It removes duplicates and constructs a 5x5 matrix.
    """
    # Convert the key to uppercase and remove duplicates while maintaining order
    key = "".join(dict.fromkeys(key.upper()))

    # The alphabet for the Playfair cipher, 'J' is commonly excluded
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    # Create a list that will hold the characters for the matrix
    key_matrix = []
    
    # Add characters from the key to the matrix, ensuring no duplicates
    for char in key:
        if char not in key_matrix and char in alphabet:
            key_matrix.append(char)
    
    # Add remaining characters from the alphabet that are not in the key
    for char in alphabet:
        if char not in key_matrix:
            key_matrix.append(char)
    
    # Create the 5x5 matrix
    matrix = []
    for i in range(5):
        row = key_matrix[i*5:(i+1)*5]
        matrix.append(row)
    
    return matrix

def find_position(matrix, char):
    """
    This function finds the position of a character in the matrix.
    It returns the row and column indices.
    """
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None, None

def decrypt_char_pair(matrix, char_pair):
    """
    This function decrypts a pair of characters (char_pair) using the Playfair cipher rules.
    It returns the decrypted char_pair.
    """
    # Find positions of both characters in the char_pair
    row1, col1 = find_position(matrix, char_pair[0])
    row2, col2 = find_position(matrix, char_pair[1])

    # If both characters are in the same row
    if row1 == row2:
        decrypted_char1 = matrix[row1][(col1 - 1) % 5]
        decrypted_char2 = matrix[row2][(col2 - 1) % 5]
    # If both characters are in the same column
    elif col1 == col2:
        decrypted_char1 = matrix[(row1 - 1) % 5][col1]
        decrypted_char2 = matrix[(row2 - 1) % 5][col2]
    # If characters form a rectangle, swap columns
    else:
        decrypted_char1 = matrix[row1][col2]
        decrypted_char2 = matrix[row2][col1]

    return decrypted_char1 + decrypted_char2

def decrypt_playfair(ciphertext, key):
    """
    This function decrypts an entire ciphertext using the Playfair cipher.
    It processes the text in char_pairs and applies decryption rules.
    """
    # removing spaces and converting to uppercase
    ciphertext = ciphertext.upper().replace(' ', '')

    # Remove any 'X' added for padding
    ciphertext = ciphertext.replace('X', '')

    # Generate the Playfair key matrix
    matrix = generate_playfair_key(key)
    plaintext = ""

    #ciphertext
    i = 0
    while i < len(ciphertext):
        # Get the char_pair
        char_pair = ciphertext[i:i+2]

        # If the char_pair is odd len pad with 'X'
        if len(char_pair) < 2:
            char_pair += 'X'

        # Decrypt the char_pair
        decrypted_char_pair = decrypt_char_pair(matrix, char_pair)
        plaintext += decrypted_char_pair

        i += 2 # Move to the next char_pair

    return plaintext

# Main function

if __name__ == "__main__":
    # The key for the Playfair cipher
    key = "SUPERSPY"

    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV" # encrypted message

    decrypted_message = decrypt_playfair(ciphertext, key)  # Decrypt the ciphertext
    
    decrypted_message = decrypted_message.replace('X', '') #remove 'X'

    print(decrypted_message) #output
