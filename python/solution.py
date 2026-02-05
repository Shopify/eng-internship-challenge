def generate_key_table(key):
    key = ''.join(sorted(set(key), key=key.index)).replace('J', 'I')
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    key_table = []
    used_chars = set(key)

    for char in key:
        key_table.append(char)

    for char in alphabet:
        if char not in used_chars:
            key_table.append(char)

    key_table_5x5 = [key_table[i:i + 5] for i in range(0, 25, 5)]
    return key_table_5x5

def find_position(char, key_table):
    for i, row in enumerate(key_table):
        if char in row:
            return i, row.index(char)
    return None

def decrypt_playfair(cipher_text, key):
    key_table = generate_key_table(key)
    decrypted_text = ""

    pairs = [cipher_text[i:i+2] for i in range(0, len(cipher_text), 2)]

    for pair in pairs:
        row1, col1 = find_position(pair[0], key_table)
        row2, col2 = find_position(pair[1], key_table)

        if row1 == row2:  # Same row
            decrypted_text += key_table[row1][(col1 - 1) % 5]
            decrypted_text += key_table[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column
            decrypted_text += key_table[(row1 - 1) % 5][col1]
            decrypted_text += key_table[(row2 - 1) % 5][col2]
        else:  #Rectangle
            decrypted_text += key_table[row1][col2]
            decrypted_text += key_table[row2][col1]

    return decrypted_text

cipher_text = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
key = "SUPERSPY"

decrypted_text = decrypt_playfair(cipher_text, key)
decrypted_text = decrypted_text.replace('X', '')
print(decrypted_text)
