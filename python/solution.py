# prepare key for playfair cipher
def prepare_key(key):
    # remove space and convert to uppercase
    key = key.replace(" ", "").upper()
    # replace 'J' with 'I'
    key = key.replace("J", "I")
    # remove duplicates
    key = "".join(dict.fromkeys(key))
    # replaced 'J' with 'I' so 'J' is not present in alphabet
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    # remove key characters from alphabet
    for char in key:
        alphabet = alphabet.replace(char, "")
    # return the remaining alphabet characters along with the key
    return key + alphabet

# generate playfair cipher
def generate_tableau(key):
    # prepare key
    key = prepare_key(key)
    # generate 5x5 tableau
    tableau = [list(key[i:i+5]) for i in range(0,25,5)]
    return tableau

# find position of character in playfair cipher
def position(tableau, char):
    # iteration through the tableau
    for i in range(5):
        for j in range(5):
            # if character is found, return the position
            if tableau[i][j] == char:
                return i, j

# decrypt a pair of characters using the playfair cipher
def decrypt_pair(tableau, pair):
    # positions of both characters
    row_1, col_1 = position(tableau, pair[0])
    row_2, col_2 = position(tableau, pair[1])
    # decrypt the pair
    if row_1 == row_2:
        return tableau[row_1][(col_1-1) % 5] + tableau[row_2][(col_2-1) % 5]
    elif col_1 == col_2:
        return tableau[(row_1 - 1) % 5][col_1] + tableau[(row_2-1) % 5][col_2]
    else:
        return tableau[row_1][col_2] + tableau[row_2][col_1]

# decrypt a message using the playfair cipher
def decrypt_message(ciphertext, key):
    # generate the playfair tableau
    tableau = generate_tableau(key)
    plaintext = ""
    # process the ciphertext
    ciphertext = ciphertext.upper().replace(" ", "").replace("J", "I")
    # split text into characters
    pairs = [ciphertext[i:i + 2] for i in range(0, len(ciphertext), 2)]
    # decrypt each pair and append to the plaintext
    for pair in pairs:
        plaintext += decrypt_pair(tableau, pair)
    # remove any 'X' characters
    plaintext = plaintext.replace('X', '')
    return plaintext

# main function
if __name__ == "__main__":
    encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    cipher_key = "SUPERSPY"
    decrypted_message = decrypt_message(encrypted_message, cipher_key)
    print(decrypted_message)