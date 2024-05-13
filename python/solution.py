# CREATE 5x5 PLAYFAIR CIPHER MATRIX
def create_matrix(key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    matrix_string = ""
    seen = False
    for char in key + alphabet:
        if char == "I" or char == "J":
            if seen:
                continue
            seen = True
        if char not in matrix_string:
            matrix_string += char
    matrix = [list(matrix_string[i:i + 5]) for i in range(0, 25, 5)]
    return matrix

# FIND THE COORDINATES OF A CHAR IN THE PLAYFAIR CIPHER MATRIX
def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

# DECRYPT THE MESSAGE
def decrypt_playfair(message, key):
    matrix = create_matrix(key)
    decryption = ""
    for i in range(0, len(message), 2):
        char1, char2 = message[i], message[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)
        if row1 == row2:
            decryption += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decryption += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            decryption += matrix[row1][col2] + matrix[row2][col1]

    decryption = decryption.replace("X", "")
    decryption = decryption.replace(" ", "")

    return decryption

'''
Assumptions:
- Message input is valid (all caps, no special characters)
- Key input is valid (all caps, no special characters)
'''
def main():
    encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"

    print(decrypt_playfair(encrypted_message, key))

main()
