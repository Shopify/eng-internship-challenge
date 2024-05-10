def remove_duplicates(key):
    """Remove duplicate letters from the key and replace 'J' with 'I'."""
    new_key = "".join(dict.fromkeys(key.upper().replace("J", "I")))
    return new_key


def create_matrix(key):
    """Create a 5x5 matrix using the key for the Playfair cipher."""
    matrix = []
    letters_added = []
    key = remove_duplicates(key)

    # Add unique letters from the key to the matrix
    for char in key:
        if char not in letters_added:
            letters_added.append(char)

    # Add remaining letters of the alphabet to the matrix
    remaining_letters = [
        letter for letter in "ABCDEFGHIKLMNOPQRSTUVWXYZ" if letter not in letters_added
    ]
    letters_added.extend(remaining_letters)

    # Create the 5x5 matrix
    for i in range(5):
        row = letters_added[i * 5 : (i + 1) * 5]
        matrix.append(row)

    return matrix


def find_position(matrix, char):
    """Find the position (row, column) of a character in the matrix."""
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None, None


def decrypt_pair(matrix, pair):
    """Decrypt a pair of characters using the Playfair cipher rules."""
    row1, col1 = find_position(matrix, pair[0])
    row2, col2 = find_position(matrix, pair[1])

    # Apply decryption rules based on the positions of the characters
    if row1 == row2:
        col1 = (col1 - 1) % 5
        col2 = (col2 - 1) % 5
    elif col1 == col2:
        row1 = (row1 - 1) % 5
        row2 = (row2 - 1) % 5
    else:
        row1, col1, row2, col2 = row1, col2, row2, col1

    return matrix[row1][col1] + matrix[row2][col2]


def playfair_decrypt(ciphertext, key):
    """Decrypt a ciphertext using the Playfair cipher."""
    matrix = create_matrix(key)
    plaintext = ""

    # Decrypt the ciphertext in pairs
    for i in range(0, len(ciphertext), 2):
        pair = ciphertext[i : i + 2]
        decrypted_pair = decrypt_pair(matrix, pair)
        plaintext += decrypted_pair

    # Remove any 'X' characters added for padding
    plaintext = plaintext.replace("X", "")
    return plaintext


# Example usage
ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
key = "SUPERSPY"
decrypted_text = playfair_decrypt(ciphertext, key)
print(decrypted_text)
