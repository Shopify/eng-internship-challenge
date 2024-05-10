def format_key(key):
    """
    Replace 'J' with 'I'.
    Remove duplicate letters.
    """
    key_modified = key.upper().replace("J", "I")
    unique_chars_dict = dict.fromkeys(key_modified)
    new_key = "".join(unique_chars_dict)
    return new_key

def create_matrix(key):
    """
    Creates the 5x5 cipher matrix.
    """
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    matrix = []

    letters = [letter for letter in key]

    # Add remaining letters of the alphabet to the matrix
    unused_letters = [letter for letter in alphabet if letter not in letters]

    letters += unused_letters

    # Create the 5x5 matrix
    for i in range(5):
        row = letters[i * 5: (i + 1) * 5]
        matrix.append(row)

    return matrix

def create_indices(matrix):
    """
    Returns the coordinates of each alphabet letter in the matrix as a hashmap.
    """

    indices = {}
    for i in range(5):
        for j in range(5):
            indices[matrix[i][j]] = (i, j)
    return indices

def decrypt_pair(matrix, pair):
    """
    Decrypt a pair of characters.
    """
    indices = create_indices(matrix)

    row_1, col_1 = indices[pair[0]]
    row_2, col_2 = indices[pair[1]]

    # Using the given decryption rules
    if row_1 == row_2:
        col_1 = (col_1 - 1) % 5
        col_2 = (col_2 - 1) % 5
    elif col_1 == col_2:
        row_1 = (row_1 - 1) % 5
        row_2 = (row_2 - 1) % 5
    else:
        row_1, col_1, row_2, col_2 = row_1, col_2, row_2, col_1

    return matrix[row_1][col_1] + matrix[row_2][col_2]


def decrypt(text, key):
    """
    Decrypt a text.
    """
    key = format_key(key)
    matrix = create_matrix(key)
    sol = ""

    # Decrypt the text in pairs of characters
    for i in range(0, len(text), 2):
        pair = text[i : i + 2]
        decrypted_pair = decrypt_pair(matrix, pair)
        sol += decrypted_pair

    # Remove "X"
    sol = sol.replace("X", "")
    return sol

def main():
    key = 'SUPERSPY'
    text = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'

    print(decrypt(text, key))

if __name__ == '__main__':
    main()