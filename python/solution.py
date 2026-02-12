def create_playfair_matrix(keyword):
    # Generate a 5x5 matrix for the Playfair cipher using the keyword
    matrix = []
    seen = set()
    keyword = "".join([char for char in keyword if not (char in seen or seen.add(char))])
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Note: J = I

    # These are characters from the keyword that are inserted into the matrix
    for char in keyword:
        if char not in matrix:
            matrix.append(char)

    # add the remaining alphabet characters also into a matrix
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)

    
    return [matrix[i:i + 5] for i in range(0, len(matrix), 5)]


def preprocess_text(ciphertext):
    # Prepare the text by replacing J with I and forming digraphs
    ciphertext = ciphertext.replace("J", "I")
    pairs = []
    i = 0

    while i < len(ciphertext):
        pair = ciphertext[i]
        if i + 1 < len(ciphertext):
            if ciphertext[i] == ciphertext[i + 1]:
                pair += "X"
                i += 1
            else:
                pair += ciphertext[i + 1]
                i += 2
        else:
            pair += "X"
            i += 1
        pairs.append(pair)

    return pairs


def locate_char(char, matrix):
    # This is used to find the position of the character inside the matrix
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None


def playfair_decrypt(ciphertext, keyword):
    # Here we decrypt the ciphertext using the Playfair cipher with a keyword
    matrix = create_playfair_matrix(keyword)
    pairs = preprocess_text(ciphertext)
    decrypted_text = ""

    for pair in pairs:
        row1, col1 = locate_char(pair[0], matrix)
        row2, col2 = locate_char(pair[1], matrix)

        if row1 == row2:
            decrypted_text += matrix[row1][(col1 - 1) % 5]
            decrypted_text += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted_text += matrix[(row1 - 1) % 5][col1]
            decrypted_text += matrix[(row2 - 1) % 5][col2]
        else:
            decrypted_text += matrix[row1][col2]
            decrypted_text += matrix[row2][col1]

    return decrypted_text


# Here we encrypte the message and the key
ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
keyword = "SUPERSPY"

#test
decrypted_text = playfair_decrypt(ciphertext, keyword)
decrypted_text = decrypted_text.replace("X", "")

#answer:
print(decrypted_text)

