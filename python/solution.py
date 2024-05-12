def generate_key_table(key):
    # Cleaning text
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = key.upper().replace("J", "I")
    key = "".join([i for i in key if i.isalnum()])
    key_table = ""

    # Create key table
    for letter in key + alphabet:
        if letter not in key_table:
            key_table += letter

    return key_table

def create_letter_pairs(text):
    # Cleaning text
    text = text.upper().replace("J", "I")
    text = "".join([i for i in text if i.isalnum()])

    # Adding an "X" at the end if the length is odd
    if len(text) % 2 == 1:
        text += "X"

    # Creating pairs
    return [text[i : i + 2] for i in range(0, len(text), 2)]

def decrypt(pair, key_table):
    # Finding the position of the letters in the key table
    x, y = pair
    row_x, col_x = divmod(key_table.index(x), 5)
    row_y, col_y = divmod(key_table.index(y), 5)

    # Applying rule 2
    if row_x == row_y:
        col_x = (col_x - 1) % 5
        col_y = (col_y - 1) % 5

    # Applying rule 3
    elif col_x == col_y:
        row_x = (row_x - 1) % 5
        row_y = (row_y - 1) % 5

    # Applying rule 4
    else:
        col_x, col_y = col_y, col_x

    # Returning the decrypted pair    
    return key_table[row_x * 5 + col_x] + key_table[row_y * 5 + col_y]

def playfair_cipher(text, key):
    # Generating key table and creating pairs
    key_table = generate_key_table(key)
    pairs = create_letter_pairs(text)
    answer = ""

    # Decrypting pairs
    for pair in pairs:
        answer += decrypt(pair, key_table)

    # Returning the answer without any "X"
    return answer.replace('X', '')

if __name__ == "__main__":
    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"

    print(playfair_cipher(ciphertext, key))
