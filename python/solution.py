import sys


def generate_key_matrix(key, verbose=False):
    """
    Generate a 5x5 matrix for the Playfair cipher using the key.
    """
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_matrix = []

    for char in key:
        if char not in key_matrix:
            key_matrix.append(char)

    for char in alphabet:
        if char not in key_matrix:
            key_matrix.append(char)

    matrix = [key_matrix[i * 5:(i + 1) * 5] for i in range(5)]

    if verbose:
        print("generated matrix:")
        for row in matrix:
            print(row)
        print()

    return matrix

def find_position(matrix, char):
    """
    Find the position of a character in the matrix.
    """
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def decrypt_cipher(ciphertext, key, verbose=False):
    """
    Decrypt a Playfair cipher using the key.
    """
    matrix = generate_key_matrix(key, verbose)
    plaintext = ""
    i = 0

    while i < len(ciphertext):
        a = ciphertext[i]
        b = ciphertext[i + 1]
        a_row, a_col = find_position(matrix, a)
        b_row, b_col = find_position(matrix, b)

        if a_row == b_row:  # same row
            plaintext += matrix[a_row][(a_col - 1) % 5]
            plaintext += matrix[b_row][(b_col - 1) % 5]
        elif a_col == b_col:  # same column
            plaintext += matrix[(a_row - 1) % 5][a_col]
            plaintext += matrix[(b_row - 1) % 5][b_col]
        else:
            plaintext += matrix[a_row][b_col]
            plaintext += matrix[b_row][a_col]

        if verbose:
            print(f"Decrypting pair: {a}{b} -> {plaintext[-2:]}")

        i += 2
    
    return plaintext.replace('X', '')

if __name__ == "__main__":
    verbose = "DEBUG" in sys.argv

    encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"

    decrypted_message = decrypt_cipher(encrypted_message, key, verbose)

    print(decrypted_message)
