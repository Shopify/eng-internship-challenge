def create_matrix(key):
    """
    Function to generate the key square. J will be ommited and replaced by I.
    key: The secret to key to create the matrix
    The filtered key without the recurring letters and playfair cypher matrix are returned. 
    """
    key = key.replace(" ", "").upper().replace("J","I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []
    seen = set()
    for char in key:
        if char not in seen and char in alphabet:
            seen.add(char)
            matrix.append(char)
    filtered_key = "".join(matrix)
    for char in alphabet:
        if char not in seen:
            matrix.append(char)
            seen.add(char)

    return filtered_key, [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(char, matrix):
    """
    Function to return the position of a character in the matrix
    char: The character to be found
    matrix: the playfair matrix.
    the position of the character in the matrix is returned.
    """
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def playfair_decrypt(key, ciphertext):
    """
    Function to use the playfair matrix to decode the text
    key: the secret key which will be used to create the matrix
    ciphertext: The text to be decoded
    The
    """
    key, matrix = create_matrix(key)
    plaintext = ""
    
    #Clearing the ciphertext of any spaces and special characters 
    ciphertext = ''.join([c for c in ciphertext.upper() if c in "ABCDEFGHIKLMNOPQRSTUVWXYZ"])

    # Appending an uncommon letter at the end to make it even
    if len(ciphertext) % 2 != 0:
        ciphertext += 'X'

    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i+1]
        row1, col1 = find_position(char1, matrix)
        row2, col2 = find_position(char2, matrix)
        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2] + matrix[row2][col1]
    return plaintext.replace("X","")

# Example usage
if __name__ == "__main__":
    key = "SUPERSPY"
    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    plaintext = playfair_decrypt(key, ciphertext)
    print(f"{plaintext}")