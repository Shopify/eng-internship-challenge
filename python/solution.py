# Author: Puneet Kaur
# Date: June 28, 2024
# File containing the solution to the Playfair Cipher from the Shopify Engineering Internship Technical Assessment Challenge in Python. 

def generate_key_square(key):
    '''
    Generate the 5x5 key square matrix used for the Playfair cipher.

    :param key: The key string used to generate the key square.
    :return: 5x5 matrix (list of lists) representing the key square.
    '''
    # Remove duplicate characters from the key
    key = ''.join(sorted(set(key), key=key.index))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J is excluded
    key_square = []
    
    # Add key characters to the key square
    used_chars = set()
    for char in key:
        if char not in used_chars:
            key_square.append(char)
            used_chars.add(char)

    # Add remaining alphabet characters to the key square
    for char in alphabet:
        if char not in used_chars:
            key_square.append(char)
            used_chars.add(char)

    # Convert list to 5x5 matrix
    key_matrix = [key_square[i:i + 5] for i in range(0, 25, 5)]
    return key_matrix


def find_position(char, key_matrix):
    '''
    Find the position of a character in the key square matrix.

    :param char: The character to find.
    :param key_matrix: The 5x5 matrix representing the key square.
    :return: Tuple of (row, column) positions of the character.
    '''
    for i, row in enumerate(key_matrix):
        if char in row:
            return i, row.index(char)
    return None

def decrypt_digraph(digraph, key_matrix):
    '''
    Decrypt a pair of characters (digraph) using the Playfair cipher rules.

    :param digraph: A pair of characters to decrypt.
    :param key_matrix: The 5x5 matrix representing the key square.
    :return: Decrypted pair of characters.
    '''
    char1, char2 = digraph
    row1, col1 = find_position(char1, key_matrix)
    row2, col2 = find_position(char2, key_matrix)

    if row1 == row2:
        # Same row: move left in the row
        return key_matrix[row1][(col1 - 1) % 5] + key_matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        # Same column: move up in the column
        return key_matrix[(row1 - 1) % 5][col1] + key_matrix[(row2 - 1) % 5][col2]
    else:
        # Rectangle: swap columns
        return key_matrix[row1][col2] + key_matrix[row2][col1]

def preprocess_ciphertext(ciphertext):
    '''
    Preprocess the ciphertext to remove non-alphabet characters and convert to uppercase.

    :param ciphertext: The encrypted message.
    :return: Cleaned and processed ciphertext.
    '''
    cleaned_text = ''.join(filter(str.isalpha, ciphertext.upper()))
    return cleaned_text

def decrypt_playfair_cipher(ciphertext, key):
    '''
    Decrypt the entire ciphertext using the Playfair cipher and the provided key.

    :param ciphertext: The encrypted message.
    :param key: The key string used to generate the key square.
    :return: Decrypted message.
    '''
    key_matrix = generate_key_square(key)
    prepared_text = preprocess_ciphertext(ciphertext)
    digraphs = [prepared_text[i:i + 2] for i in range(0, len(prepared_text), 2)]

    decrypted_text = ''
    for digraph in digraphs:
        if len(digraph) == 2:
            decrypted_text += decrypt_digraph(digraph, key_matrix)

    decrypted_text = decrypted_text.replace('X', '')
    return decrypted_text

if __name__ == "__main__":
    # Input the encrypted message and key
    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"

    # Decrypt the ciphertext using Playfair Cipher
    decrypted_message = decrypt_playfair_cipher(ciphertext, key)

    # Output the decrypted message in uppercase without spaces
    print(decrypted_message)
