def create_playfair_matrix(key):
    """Function to construct Playfair cipher matrix (5x5) from the provided key
    Parameters:
        key (str): keyword used to generate the cipher matrx
    Returns:
        list of list of str: 5x5 matrix used for the Playfair cipher
    """
    # Remove duplicates from key while maintaining order and replace J with I
    key = ''.join(sorted(set(key), key=key.index)).replace('J', 'I') 
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' # Alphabet without J
    matrix = [] # List to hold the matrix
    used_chars = set() # Set to track used characters

    # Add unique characters to the matrix
    for char in key: 
        if char not in used_chars: 
            matrix.append(char) 
            used_chars.add(char)

    # Add remaining letters to the matrix
    for char in alphabet: 
        if char not in used_chars: 
            matrix.append(char) 
            used_chars.add(char)

    # Convert the flat list into a 5x5 matrix
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    """Function to find the position of character in the Playfair cipher matrix
    Parameters:
        matrix (list of list of str): 5x5 Playfair cipher matrix
        char (str): character to locate in the matrix
    Returns:
        tuple of int: The row and column indices of the character
    """
    for i, row in enumerate(matrix):
        if char in row:
            return (i, row.index(char))
    return None

def decrypt_pair(matrix, a, b):
    """Function to decrypt a pair of characters using the Playfair cipher rules
    Parameters:
        matrix (list of list of str): 5x5 Playfair cipher matrix
        a (str): first character in the pair
        b (str): second character in the pair
    Returns:
        str: The decrypted pair of characters
    """
    row_a, col_a = find_position(matrix, a)
    row_b, col_b = find_position(matrix, b)

    if row_a == row_b:
        # If same row -> move each character one position to the left
        decrypted_a = matrix[row_a][(col_a - 1) % 5]
        decrypted_b = matrix[row_b][(col_b - 1) % 5]
    elif col_a == col_b:
        # If same column -> move each character one position up
        decrypted_a = matrix[(row_a - 1) % 5][col_a]
        decrypted_b = matrix[(row_b - 1) % 5][col_b]
    else:
        # Rectangle -> swap the columns of the characters
        decrypted_a = matrix[row_a][col_b]
        decrypted_b = matrix[row_b][col_a]

    return decrypted_a + decrypted_b

def preprocess_text(ciphertext):
    """Preprocesses the ciphertext by removing non-alphabetic characters 
    and return the cleaned (str) ciphertext
    """
    return ''.join(filter(str.isalpha, ciphertext)).replace('X', '')

def decrypt_playfair(ciphertext, key):
    """Function to decrypt the entire ciphertext using the Playfair cipher
    Parameters:
        ciphertext (str): The encrypted message
        key (str): The keyword used to generate the cipher matrix
    Returns:
        str: The decrypted plaintext
    """
    matrix = create_playfair_matrix(key)
    ciphertext = preprocess_text(ciphertext)
    plaintext = ''

    # Iterate over the ciphertext in pairs of characters
    for i in range(0, len(ciphertext), 2):
        # a: current char, b: next char or X if it is the last one
        a = ciphertext[i]
        b = ciphertext[i+1] if i+1 < len(ciphertext) else 'X'

        # Decrypt the pair and add the result to the plaintext
        plaintext += decrypt_pair(matrix, a, b)

    return plaintext

if __name__ == "__main__":
    # ciphertext and key
    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"

    decrypted_message = decrypt_playfair(ciphertext, key)

    # Output decrypted message
    print(decrypted_message)
