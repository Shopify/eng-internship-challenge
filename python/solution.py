def generate_key_matrix(key):
    key_set = set()
    key_matrix = [['' for _ in range(5)] for _ in range(5)]
    row = 0
    col = 0

    for letter in key:
        if letter not in key_set:
            key_set.add(letter)
            key_matrix[row][col] = letter
            col += 1
            if col == 5:
                col = 0
                row += 1
    
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    for letter in alphabet:
        if letter != 'J' and letter not in key_set:
            key_matrix[row][col] = letter
            col += 1
            if col == 5:
                col = 0
                row += 1

    return key_matrix


def filter_out_x(text):
    filtered_text = text.replace('X', '')
    return filtered_text
    
def find_position(matrix, letter):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == letter:
                return i, j

def decrypt(ciphertext, matrix):
    plaintext = ""

    i = 0
    while i < len(ciphertext):
        char1 = ciphertext[i]
        char2 = ciphertext[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2] + matrix[row2][col1]

        i += 2

    plaintext = filter_out_x(plaintext)

    return plaintext

encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
key_matrix = generate_key_matrix("SUPERSPY")
decrypted_message = decrypt(encrypted_message, key_matrix)
print(decrypted_message)