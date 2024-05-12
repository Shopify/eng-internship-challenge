import string


def preprocess_input(text, key):

    # Preprocess the input text and key:

    # Remove non-alphabetic characters and convert to uppercase
    text = "".join(char for char in text.upper() if char.isalpha())
    key = "".join(char for char in key.upper() if char.isalpha())

    # Handle duplicate letters in the key
    key = "".join(dict.fromkeys(key))

    return text, key


def generate_matrix(key):
    # Create the matrix and fill with the key
    matrix = [[] for _ in range(5)]
    letters_added = []

    for char in key:
        if char not in letters_added:
            letters_added.append(char)

    # Fill the remaining matrix cells with the rest of the alphabet
    for char in string.ascii_uppercase:
        if char != "J" and char not in letters_added:
            letters_added.append(char)

    # Fill the matrix row by row
    row = col = 0
    for char in letters_added:
        matrix[row].append(char)
        col += 1
        if col > 4:
            col = 0
            row += 1

    return matrix


def decrypt(ciphertext, key):
    # Decrypt the ciphertext using the Playfair Cipher

    # Preprocess the input
    ciphertext, key = preprocess_input(ciphertext, key)

    # Generate the Playfair matrix
    matrix = generate_matrix(key)

    # Split the ciphertext into digraphs
    digraphs = [ciphertext[i : i + 2] for i in range(0, len(ciphertext), 2)]
    if len(ciphertext) % 2 != 0:
        digraphs[-1] += "X"

    plaintext = []
    for digraph in digraphs:
        row1, col1 = next(
            (row, col)
            for row in range(5)
            for col in range(5)
            if matrix[row][col] == digraph[0]
        )
        row2, col2 = next(
            (row, col)
            for row in range(5)
            for col in range(5)
            if matrix[row][col] == digraph[1]
        )

        # Apply the decryption rules
        if row1 == row2:
            plaintext.append(
                matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            )
        elif col1 == col2:
            plaintext.append(
                matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            )
        else:
            plaintext.append(matrix[row1][col2] + matrix[row2][col1])

    # Remove null characters and convert to uppercase
    plaintext = "".join(plaintext).replace("X", "").upper()

    return plaintext


# Messaged received from agent
ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
key = "SUPERSPY"

plaintext = decrypt(ciphertext, key)
print(f"{plaintext}")
