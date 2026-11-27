# Function to clean and prepare the key matrix/grid
def prepare_key_matrix(key):
    """
    Cleans and prepares the key matrix/grid for encryption/decryption.

    Parameters:
    key (str): The key used for encryption/decryption.

    Returns:
    matrix (list): The prepared key matrix/grid.
    """
    # Remove duplicates and replace 'J' with 'I'
    seen_chars = set()
    cleaned_key = []
    for char in key.upper().replace('J', 'I'):
        if char not in seen_chars and char.isalpha():
            seen_chars.add(char)
            cleaned_key.append(char)
    
    # Add the rest of the alphabet
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    for char in alphabet:
        if char not in seen_chars:
            cleaned_key.append(char)
    
    # Create a 5x5 matrix
    matrix = [cleaned_key[i * 5:(i + 1) * 5] for i in range(5)]
    return matrix

# Function to find the row and column of a character in the matrix
def find_pos(matrix, char):
    """
    Finds the row and column of a character in the key matrix/grid.

    Parameters:
    matrix (list): The key matrix/grid.
    char (str): The character to find.

    Returns:
    position (tuple): The row and column of the character in the matrix.
                     Returns None if the character is not found.
    """
    for row_index, row in enumerate(matrix):
        if char in row:
            return (row_index, row.index(char))
    return None

# Function to decrypt the Playfair ciphertext
def decrypt_cipher(ciphertext, key):
    """
    Decrypts the Playfair ciphertext using the provided key.

    Parameters:
    ciphertext (str): The ciphertext to decrypt.
    key (str): The key used for encryption/decryption.

    Returns:
    decrypted_text (str): The decrypted plaintext.
    """
    matrix = prepare_key_matrix(key)
    # Clean and prepare the ciphertext
    filtered_ciphertext = ''.join([c for c in ciphertext.upper() if c in 'ABCDEFGHIKLMNOPQRSTUVWXYZ'])

    # Check if we need to pad the ciphertext to ensure even length
    if len(filtered_ciphertext) % 2 != 0:
        filtered_ciphertext += 'X'

    # Decrypt each digraph
    decrypted_text = ''
    i = 0

    while i < len(filtered_ciphertext):
        char1 = filtered_ciphertext[i]
        char2 = filtered_ciphertext[i + 1] if (i + 1) < len(filtered_ciphertext) else 'X'

        row1, col1 = find_pos(matrix, char1)
        row2, col2 = find_pos(matrix, char2)

        if row1 == row2:
            # Same row: move to the left
            decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            # Same column: move up
            decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            # Rectangle: swap columns
            decrypted_text += matrix[row1][col2] + matrix[row2][col1]

        i += 2

    return decrypted_text.replace('X', '').upper()

# Decrypt and print the message
ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
key = "SUPERSPY"

decrypted_message = decrypt_cipher(ciphertext, key)
print(decrypted_message)