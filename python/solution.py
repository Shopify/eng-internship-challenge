def create_playfair_matrix(key):
    """
    Creates a 5x5 Playfair matrix using the provided key.
    """
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []
    key_unique = []

    # Add key characters to the matrix
    for char in key.upper():
        if char not in key_unique and char in alphabet:
            key_unique.append(char)

    # Add remaining alphabet characters to the matrix
    for char in alphabet:
        if char not in key_unique:
            key_unique.append(char)

    # Create 5x5 matrix
    for i in range(0, 25, 5):
        matrix.append(key_unique[i:i+5])
    return matrix

def preprocess_text(text):
    """
    Prepares the text for decryption:
    - Converts text to uppercase.
    - Replaces 'J' with 'I'.
    - Splits text into digraphs, inserting 'X' between duplicate letters and at the end if necessary.
    """
    text = text.upper().replace("J", "I")
    processed = ""
    i = 0

    while i < len(text):
        processed += text[i]
        if i+1 < len(text) and text[i] == text[i+1]:
            processed += "X"
        elif i+1 < len(text):
            processed += text[i+1]
            i += 1
        i += 1

    if len(processed) % 2 != 0:
        processed += "X"

    return processed

def find_position(matrix, char):
    """
    Finds the row and column of a character in the Playfair matrix.
    """
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def decrypt_digraph(matrix, digraph):
    """
    Decrypts a pair of characters (digraph) using Playfair cipher rules.
    """
    row1, col1 = find_position(matrix, digraph[0])
    row2, col2 = find_position(matrix, digraph[1])

    if row1 == row2:
        return matrix[row1][(col1-1) % 5] + matrix[row2][(col2-1) % 5]
    elif col1 == col2:
        return matrix[(row1-1) % 5][col1] + matrix[(row2-1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def decrypt_playfair_cipher(cipher_text, key):
    """
    Decrypts a Playfair cipher text using the provided key.
    """
    matrix = create_playfair_matrix(key)
    cipher_text = preprocess_text(cipher_text)
    decrypted_text = ""

    for i in range(0, len(cipher_text), 2):
        decrypted_text += decrypt_digraph(matrix, cipher_text[i:i+2])

    return decrypted_text.replace("X", "")

if __name__ == "__main__":
    key = "SUPERSPY"
    cipher_text = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    decrypted_text = decrypt_playfair_cipher(cipher_text, key)
    print(decrypted_text)
