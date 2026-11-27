"""
Playfair Cipher Decryption

This program implements a Playfair cipher decryption algorithm. It takes an encrypted message
and a key, creates a Playfair matrix, decrypts the message using Playfair cipher rules,
and outputs a decrypted string in uppercase with 'X', spaces, and special characters removed.
"""

def create_matrix(key):
    """
    Create a 5x5 Playfair cipher matrix from the given key.
    
    Args:
    key (str): The key to use for creating the matrix.
    
    Returns:
    list: A 5x5 matrix of characters.
    """
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' # minus J
    combined_key = key.upper() + alphabet

    # Remove duplicate letters while preserving order
    unique_key = ''
    seen_letters = set()
    for letter in combined_key:
        if letter not in seen_letters:
            unique_key += letter
            seen_letters.add(letter)

    # Create the 5x5 matrix
    matrix = []
    for i in range(0, 25, 5):
        row = list(unique_key[i:i+5])
        matrix.append(row)

    return matrix

def find_position(matrix, letter):
    """
    Find the position of a letter in the Playfair matrix.
    
    Args:
    matrix (list): The 5x5 Playfair matrix.
    letter (str): The letter to find.
    
    Returns:
    tuple: The (row, column) position of the letter.
    """
    for row_index in range(len(matrix)):
        current_row = matrix[row_index]
        if letter in current_row:
            column_index = current_row.index(letter)
            return row_index, column_index
    
    print(f"Warning: Letter '{letter}' not found in the matrix.")
    return -1, -1  # This should never happen in a correct Playfair matrix

def get_letter(matrix, row, col):
    """Get letter from matrix at given row and column."""
    return matrix[row][col]

def shift_left(matrix, row, col):
    """Get the letter to the left, wrapping around if necessary."""
    new_col = (col - 1) % 5
    return get_letter(matrix, row, new_col)

def shift_up(matrix, row, col):
    """Get the letter above, wrapping around if necessary."""
    new_row = (row - 1) % 5
    return get_letter(matrix, new_row, col)

def decrypt_pair(matrix, pair):
    """
    Decrypt a pair of letters using the Playfair cipher rules.
    
    Args:
    matrix (list): The 5x5 Playfair matrix.
    pair (str): A pair of letters to decrypt.
    
    Returns:
    str: The decrypted pair of letters.
    """
    first_letter, second_letter = pair[0], pair[1]
    row1, col1 = find_position(matrix, first_letter)
    row2, col2 = find_position(matrix, second_letter)
    
    if row1 == row2:
        decrypted_first = shift_left(matrix, row1, col1)
        decrypted_second = shift_left(matrix, row2, col2)
    elif col1 == col2:
        decrypted_first = shift_up(matrix, row1, col1)
        decrypted_second = shift_up(matrix, row2, col2)
    else:
        decrypted_first = get_letter(matrix, row1, col2)
        decrypted_second = get_letter(matrix, row2, col1)
    
    return decrypted_first + decrypted_second

def playfair_decrypt(ciphertext, key):
    """
    Decrypt the entire ciphertext using the Playfair cipher.
    
    Args:
    ciphertext (str): The encrypted message.
    key (str): The key for decryption.
    
    Returns:
    str: The decrypted message.
    """
    matrix = create_matrix(key)
    plaintext = ""
    i = 0
    while i < len(ciphertext):
        plaintext += decrypt_pair(matrix, ciphertext[i:i+2])
        i += 2
    return plaintext

def clean_text(text):
    """
    Clean the decrypted text by removing non-alphabetic characters and 'X'.
    
    Args:
    text (str): The text to clean.
    
    Returns:
    str: The cleaned text.
    """
    uppercase_text = text.upper()
    cleaned_chars = []
    
    for char in uppercase_text:
        if char.isalpha() and char != 'X':
            cleaned_chars.append(char)
    
    cleaned_text = ''.join(cleaned_chars)
    return cleaned_text

# Main execution
if __name__ == "__main__":
    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"
    
    decrypted = playfair_decrypt(ciphertext, key)
    cleaned_decrypted = clean_text(decrypted)
    
    print(cleaned_decrypted)