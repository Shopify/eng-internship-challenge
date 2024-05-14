def create_matrix(key):
    # remove duplicates and replace 'J' with 'I'
    key = ''.join([k.upper() for k in key if k.isalpha() and k != 'J'])
    seen = set()
    matrix = []
    for char in key:
        if char not in seen:
            seen.add(char)
            matrix.append(char)
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'.replace('J', '')
    for char in alphabet:
        if char not in seen:
            matrix.append(char)
            seen.add(char)
    # Form a 5x5 matrix 
    return [matrix[i * 5:(i + 1) * 5] for i in range(5)]

def decrypt_message(message, key):
    # make the 5x5 matrix from the key
    matrix = create_matrix(key)
    message = ''.join([m for m in message if m.isalpha()]).upper().replace('J', 'I')
    plaintext = ""
    i = 0
    # Process each pair of characters
    while i < len(message) - 1:
        a, b = message[i], message[i + 1]
        row1, col1, row2, col2 = -1, -1, -1, -1
        for r in range(5):
            if row1 != -1 and row2 != -1:
                break
            for c in range(5):
                if matrix[r][c] == a:
                    row1, col1 = r, c
                if matrix[r][c] == b:
                    row2, col2 = r, c
        if row1 == row2:  #  shift characters to the left
            plaintext += matrix[row1][(col1 - 1) % 5]
            plaintext += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  #  shift characters up
            plaintext += matrix[(row1 - 1) % 5][col1]
            plaintext += matrix[(row2 - 1) % 5][col2]
        else:  #  swap the columns
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]
        i += 2
    # Remove any 'X' 
    plaintext = plaintext.replace('X', '')
    return plaintext

if __name__ == "__main__":
    key = "SUPERSPY"
    message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    decrypted_message = decrypt_message(message, key)
    print(decrypted_message)
