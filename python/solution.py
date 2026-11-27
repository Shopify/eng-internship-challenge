
def split_into_digrams(text):
    text = text.upper().replace('J', 'I')
    digrams = []
    i = 0

    while i < len(text):
        # Get the current letter
        current_letter = text[i]

        # Get the next letter if it exists, otherwise use 'X'
        if i + 1 < len(text):
            next_letter = text[i + 1]
        else:
            next_letter = 'X'

        # If both letters are the same, insert 'X' between them
        if current_letter == next_letter:
            digrams.append(current_letter + 'X')
            i += 1
        else:
            digrams.append(current_letter + next_letter)
            i += 2

    # If the length of the text is odd, add 'X' to the last digram
    if len(digrams[-1]) == 1:
        digrams[-1] += 'X'

    return digrams

def generate_key_square(keyword):
    keyword = keyword.upper().replace('J', 'I')
    key_square = []
    used_chars = set()

    for char in keyword:
        if char not in used_chars and char.isalpha():
            key_square.append(char)
            used_chars.add(char)

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # 'J' combined 'I'
    for char in alphabet:
        if char not in used_chars:
            key_square.append(char)
            used_chars.add(char)

    return [key_square[i * 5:(i + 1) * 5] for i in range(5)]


def find_position(letter, key_square):
    for row in range(5):
        for col in range(5):
            if key_square[row][col] == letter:
                return row, col
    return None


def decrypt_pair(pair, key_square):
    row1, col1 = find_position(pair[0], key_square)
    row2, col2 = find_position(pair[1], key_square)

    if row1 == row2:
        return key_square[row1][(col1 - 1) % 5] + key_square[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return key_square[(row1 - 1) % 5][col1] + key_square[(row2 - 1) % 5][col2]
    else:
        return key_square[row1][col2] + key_square[row2][col1]
    

def decrypt_playfair(raw_ciphertext, keyword):
    key_square = generate_key_square(keyword)
    raw_ciphertext = raw_ciphertext.upper().replace('J', 'I')

    ciphertext=""

    for char in raw_ciphertext:
        if char.isalpha():
            ciphertext+=char

    
    plaintext = ""

    i = 0
    while i < len(ciphertext):
        if i + 1 < len(ciphertext):
            pair = ciphertext[i:i+2]
            if pair[0] == pair[1]:
                pair = pair[0] + 'X'
                i -= 1
            decrypted_pair = decrypt_pair(pair, key_square)
        else:
            pair = ciphertext[i] + 'X'
            decrypted_pair = decrypt_pair(pair, key_square)
        plaintext += decrypted_pair
        i += 2

    cleaned_plaintext = ""
    #removes extra placeholders
    i = 0
    while i < len(plaintext):
        if i < len(plaintext) - 1 and plaintext[i] == 'X' and plaintext[i-1] == plaintext[i+1]:
            i += 1
        else:
            cleaned_plaintext += plaintext[i]
            i += 1
     # Remove a trailing 'X' if it was added as a placeholder
    if cleaned_plaintext.endswith('X'):
        cleaned_plaintext = cleaned_plaintext[:-1]

    return cleaned_plaintext









cipher ='IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'
key= 'SUPERSPY'

print(decrypt_playfair(cipher,key))



