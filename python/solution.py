def generate_table (key):
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M',
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    key_chars = []
    for c in key:
        if c not in key_chars:
            key_chars.append(c)
    filler_chars = []
    for c in alpha:
        if c not in filler_chars and c not in key_chars:
            filler_chars.append(c)
    key_array = key_chars + filler_chars
    cipher_table = []
    while key_array:
        cipher_table.append(key_array[:5])
        key_array = key_array[5:]

    return cipher_table

def search_char(cipher_table, char):
    for i in range(5):
        for j in range(5):
            if char == cipher_table[i][j]:
                return i, j

def decrypt_row(cipher_table, cx, cy1, cy2):
    digram = ""
    if cy1 == 0:
        digram = digram + cipher_table[cx][4]
    else:
        digram = digram + cipher_table[cx][cy1-1]
    if cy2 == 0:
        digram = digram + cipher_table[cx][4]
    else:
        digram = digram + cipher_table[cx][cy2-1]
    return digram

def decrypt_column(cipher_table, cy, cx1, cx2):
    digram = ""
    if cx1 == 0:
        digram = digram + cipher_table[4][cy]
    else:
        digram = digram + cipher_table[cx1-1][cy]
    if cx2 == 0:
        digram = digram + cipher_table[4][cy]
    else:
        digram = digram + cipher_table[cx2-1][cy]
    return digram

def decrypt_rectangle(cipher_table, cx1, cy1, cx2, cy2):
    return cipher_table[cx1][cy2] + cipher_table[cx2][cy1]

def decrypt_playfair(key, encrypted_string):
    cipher_table = generate_table(key)
    plaintext = ""
    for i in range(0, len(encrypted_string), 2):
        cx1, cy1 = search_char(cipher_table, encrypted_string[i])
        cx2, cy2 = search_char(cipher_table, encrypted_string[i + 1])
        if cx1 == cx2:
            plaintext = plaintext + decrypt_row(cipher_table, cx1, cy1, cy2)
        elif cy1 == cy2:
            plaintext = plaintext + decrypt_column(cipher_table, cy1, cx1, cx2)
        else:
            plaintext = plaintext + decrypt_rectangle(cipher_table, cx1, cy1, cx2, cy2)
    return plaintext.replace('X', '')

print(decrypt_playfair("SUPERSPY", "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"))
