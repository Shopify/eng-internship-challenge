def preprocess_input(input_text):
    # Remove spaces and convert to uppercase
    input_text = input_text.replace(" ", "").upper()
    # Replace 'J' with 'I' (standard Playfair Cipher treatment)
    input_text = input_text.replace("J", "I")
    # Split input into digraphs (pairs of characters)
    digraphs = []
    i = 0
    while i < len(input_text):
        if i == len(input_text) - 1 or input_text[i] == input_text[i + 1]:
            digraphs.append(input_text[i] + 'X')
            i += 1
        else:
            digraphs.append(input_text[i] + input_text[i + 1])
            i += 2
    return digraphs

def create_key_square(key):
    # Create a list of unique characters in the key (without 'J')
    key = key.upper().replace(" ", "").replace("J", "I")
    key_set = []
    for char in key:
        if char not in key_set:
            key_set.append(char)

    # Create key square (5x5 matrix)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # without 'J'
    key_square = []
    for char in key_set:
        if char not in key_square:
            key_square.append(char)
    for char in alphabet:
        if char not in key_square:
            key_square.append(char)
    return key_square

def find_position(key_square, char):
    # Find position of a character in the key square
    index = key_square.index(char)
    row = index // 5
    col = index % 5
    return (row, col)

def decrypt_digraph(key_square, digraph):
    # Decrypt a digraph based on Playfair Cipher rules
    (char1, char2) = digraph[0], digraph[1]
    (row1, col1) = find_position(key_square, char1)
    (row2, col2) = find_position(key_square, char2)

    if row1 == row2:
        return key_square[row1 * 5 + (col1 - 1) % 5] + key_square[row2 * 5 + (col2 - 1) % 5]
    elif col1 == col2:
        return key_square[((row1 - 1) % 5) * 5 + col1] + key_square[((row2 - 1) % 5) * 5 + col2]
    else:
        return key_square[row1 * 5 + col2] + key_square[row2 * 5 + col1]

def decrypt_message(ciphertext, key):
    # Preprocess input and create key square
    digraphs = preprocess_input(ciphertext)
    key_square = create_key_square(key)

    # Decrypt each digraph and concatenate results
    decrypted_message = ""
    for digraph in digraphs:
        decrypted_message += decrypt_digraph(key_square, digraph)

    return decrypted_message

# Example usage:
ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
key = "SUPERSPY"
plaintext = decrypt_message(ciphertext, key)
print(plaintext)