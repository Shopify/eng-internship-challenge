def create_playfair_matrix(key):
    """
    Generate the Playfair matrix based on the key, replacing 'J' with 'I'.
    """
    key = key.upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []
    letter_to_coords = {}
    for char in key + alphabet:
        if char not in letter_to_coords:
            matrix.append(char)
            letter_to_coords[char] = (len(matrix) - 1, len(matrix[-1]))
    return [matrix[i:i + 5] for i in range(0, len(matrix), 5)]

def decrypt_playfair(ciphertext, key):
    """
    Decrypt the Playfair ciphertext using the provided key.
    """
    matrix = create_playfair_matrix(key)
    plaintext = []
    letter_to_coords = {char: (i, j) for i, row in enumerate(matrix) for j, char in enumerate(row)}

    # Filter ciphertext to only include valid letters
    ciphertext = ''.join(char.upper() for char in ciphertext if char.isalpha())
    ciphertext += 'X' if len(ciphertext) % 2 != 0 else ''

    for i in range(0, len(ciphertext), 2):
        letter1, letter2 = ciphertext[i], ciphertext[i + 1]
        (row1, col1), (row2, col2) = letter_to_coords[letter1], letter_to_coords[letter2]

        if row1 == row2:
            plaintext.append(matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5])
        elif col1 == col2:
            plaintext.append(matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2])
        else:
            plaintext.append(matrix[row1][col2] + matrix[row2][col1])

    return ''.join(plaintext).replace('X', '')

if __name__ == "__main__":
    key = "SUPERSPY"
    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

    plaintext = decrypt_playfair(ciphertext, key)
    print(plaintext)