def matrix_generator(key):
    ''' 
    Generate a 5x5 matrix for the Playfair cipher
    Args: key (str) -- The key to generate the matrix
    Returns: 2D list -- A 5x5 matrix
    '''

    key = key.upper()
    unique = ""
    seen = set()
    for i in key:
        if i not in seen:
            if i == 'J': i = 'I'
            seen.add(i)
            unique += i

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in seen:
            unique += char

    res = []
    for i in range(0, 25, 5):
        res.append(unique[i:i + 5])
    return res


def decrypt_playfair(text, matrix):
    '''
    Decrypt a Playfair cipher
    Args: text (str) -- The encrypted text
          matrix (2D list) -- The matrix used to encrypt the text
    Returns: string -- The decrypted text
    '''

    position = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            ch = matrix[i][j]
            position[ch] = (i, j)

    two_char_diagram = []
    for i in range(0, len(text), 2):
        two_char_diagram.append(text[i:i + 2])

    res = []

    for a, b in two_char_diagram:
        row_a, col_a = position[a]
        row_b, col_b = position[b]

        if row_a == row_b: 
            new_a = matrix[row_a][(col_a - 1) % 5]
            new_b = matrix[row_b][(col_b - 1) % 5]
        elif col_a == col_b: 
            new_a = matrix[(row_a - 1) % 5][col_a]
            new_b = matrix[(row_b - 1) % 5][col_b]
        else: 
            new_a = matrix[row_a][col_b]
            new_b = matrix[row_b][col_a]

        res.extend([new_a, new_b])

    decrypted_text = ""
    for char in res:
        if char != "X":
            decrypted_text += char

    return decrypted_text


if __name__ == '__main__':
    key = "SUPERSPY"
    encrypted_text = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    matrix = matrix_generator(key)
    answer = decrypt_playfair(encrypted_text, matrix)
    print(answer)
