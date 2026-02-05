# solution.py

def generate_playfair_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J is usually omitted
    key = "".join(sorted(set(key), key=lambda x: key.index(x)))  # remove duplicates while preserving order
    matrix = []
    used_chars = set()

    for char in key:
        if char not in used_chars:
            used_chars.add(char)
            matrix.append(char)

    for char in alphabet:
        if char not in used_chars:
            used_chars.add(char)
            matrix.append(char)

    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def find_position(char, matrix):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def decrypt_playfair(ciphertext, key):
    matrix = generate_playfair_matrix(key)
    plaintext = []

    # Process pairs of characters
    for i in range(0, len(ciphertext), 2):
        char1 = ciphertext[i]
        char2 = ciphertext[i + 1]

        row1, col1 = find_position(char1, matrix)
        row2, col2 = find_position(char2, matrix)

        if row1 == row2:
            # Same row
            plaintext.append(matrix[row1][(col1 - 1) % 5])
            plaintext.append(matrix[row2][(col2 - 1) % 5])
        elif col1 == col2:
            # Same column
            plaintext.append(matrix[(row1 - 1) % 5][col1])
            plaintext.append(matrix[(row2 - 1) % 5][col2])
        else:
            # Rectangle swap
            plaintext.append(matrix[row1][col2])
            plaintext.append(matrix[row2][col1])

    return "".join(plaintext)

if __name__ == "__main__":
    key = "SUPERSPY"
    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    decrypted_message = decrypt_playfair(ciphertext, key)
    
    # Remove 'X' and ensure uppercase without spaces
    decrypted_message = decrypted_message.replace('X', '').upper()
    print(decrypted_message)
