def mod(a, b):
    return a % b

def create_key_matrix(key):
    """
    Creates a 5x5 key matrix for the Playfair cipher from a given key.
    - Converts key to uppercase.
    - Replaces 'J' with 'I'.
    - Fills the matrix with unique characters from the key,
      then fills the rest with the remaining letters of the alphabet.
    """
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    key = key.upper().replace('J', 'I')
    seen = set()
    matrix = []
    
    # First, add characters from the key to the matrix
    for char in key:
        if char not in seen and char in alphabet:
            matrix.append(char)
            seen.add(char)
    
    # Fill the matrix with the remaining alphabet
    for char in alphabet:
        if char not in seen and char != 'J':
            matrix.append(char)
            seen.add(char)
    
    # Split the list into a 5x5 matrix
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_in_matrix(letter, matrix):
    """
    Finds and returns the row and column index of a letter in the 5x5 matrix.
    Returns None, None if the letter is not found.
    """
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return None, None

def decrypt(text, matrix):
    """
    Decrypts a ciphertext using a Playfair cipher decryption method.
    Assumes the text has been encrypted using the same cipher and key matrix.
    Adjusts text to ensure all characters are valid and adds 'X' for odd length.
    """
    text = text.upper().replace('J', 'I')
    if len(text) % 2 != 0:
        text += 'X'
    
    output = ""
    pos = 0
    while pos < len(text):
        row1, col1 = find_in_matrix(text[pos], matrix)
        row2, col2 = find_in_matrix(text[pos + 1], matrix)
        
        # Check if the letters are in the same row
        if row1 == row2:
            output += matrix[row1][mod(col1 - 1, 5)]
            output += matrix[row2][mod(col2 - 1, 5)]
        # Check if the letters are in the same column
        elif col1 == col2:
            output += matrix[mod(row1 - 1, 5)][col1]
            output += matrix[mod(row2 - 1, 5)][col2]
        # If letters form a rectangle
        else:
            output += matrix[row1][col2]
            output += matrix[row2][col1]
        
        pos += 2
    return output

def clean_decrypted_text(text):
    """
    Cleans the decrypted text by removing 'X' and any invalid characters.
    Ensures the output is only alphabetic characters.
    """
    cleaned_text = ""
    valid_chars = 'ABCDEFGHIKLMNOPQRSTUVWYZ'
    for char in text:
        if char in valid_chars:
            cleaned_text += char
    return cleaned_text

# Main execution

key = "SUPERSPY"
matrix = create_key_matrix(key)
encrypted_text = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
decrypted_text = decrypt(encrypted_text, matrix)
final_text = clean_decrypted_text(decrypted_text)
print(final_text)
