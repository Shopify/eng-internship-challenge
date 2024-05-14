# Function to generate the key square matrix
def generate_key_square(key):
    key = key.upper().replace("J", "I")  # Convert to uppercase and replace 'J' with 'I'
    key_square = []
    for char in key:
        if char not in key_square:
            key_square.append(char)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in key_square:
            key_square.append(char)
    key_square_str = ''.join(key_square)
    return [key_square_str[i:i+5] for i in range(0, 25, 5)]

# Function to decrypt the ciphertext
def decrypt(ciphertext, key):
    key_square = generate_key_square(key)
    plaintext = ""
    ciphertext = ciphertext.upper().replace("J", "I")  # Convert to uppercase and replace 'J' with 'I'
    i = 0
    while i < len(ciphertext):
        if i == len(ciphertext) - 1 or ciphertext[i] == ciphertext[i + 1]:
            pair = ciphertext[i] + 'X'
            i += 1
        else:
            pair = ciphertext[i:i+2]
            i += 2
        row1, col1 = None, None
        row2, col2 = None, None
        for row in range(5):
            if pair[0] in key_square[row]:
                row1, col1 = row, key_square[row].index(pair[0])
            if pair[1] in key_square[row]:
                row2, col2 = row, key_square[row].index(pair[1])
        if row1 == row2:
            col1 = (col1 - 1) % 5
            col2 = (col2 - 1) % 5
        elif col1 == col2:
            row1 = (row1 - 1) % 5
            row2 = (row2 - 1) % 5
        else:
            col1, col2 = col2, col1
        plaintext += key_square[row1][col1] + key_square[row2][col2]
    return plaintext

# Test the functions
ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
key = "SUPERSPY"
print(decrypt(ciphertext, key))