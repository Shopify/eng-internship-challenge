def create_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" 
    matrix = []
    seen = set()

    # Append the characters from the key
    for char in key.upper():
        if char == 'J':  # Convert 'J' to 'I'
            char = 'I'
        if char not in seen and char in alphabet:
            seen.add(char)
            matrix.append(char)

    # Append the rest of the alphabet
    for char in alphabet:
        if char not in seen:
            seen.add(char)
            matrix.append(char)

    return [matrix[i:i+5] for i in range(0, 25, 5)]

def decrypt_pair(a, b, matrix):
    # Find positions of letters in the matrix
    row1, col1, row2, col2 = -1, -1, -1, -1
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == a:
                row1, col1 = i, j
            if matrix[i][j] == b:
                row2, col2 = i, j

    # Apply decryption rules
    if row1 == row2:  # Same row
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:  # Same column
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:  # Rectangle
        return matrix[row1][col2] + matrix[row2][col1]

def decrypt_message(ciphertext, matrix):
    ciphertext = ciphertext.replace('J', 'I').upper()
    decrypted_text = ""
    i = 0
    while i < len(ciphertext):
        a = ciphertext[i]
        b = ciphertext[i + 1] if i + 1 < len(ciphertext) else 'X'
        decrypted_text += decrypt_pair(a, b, matrix)
        i += 2
    return decrypted_text.replace('X', '')

if __name__ == "__main__":
    key = "SUPERSPY"
    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    matrix = create_matrix(key)
    decrypted_message = decrypt_message(ciphertext, matrix)
    print(decrypted_message)
