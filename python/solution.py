def generate_playfair_table(key):
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    table = []
    key = key.upper().replace('J', 'I')

    # Construct the initial table based on the key
    for char in key:
        if char not in table:
            table.append(char)

    # Fill the rest of the table with remaining letters of the alphabet
    for char in alphabet:
        if char not in table:
            table.append(char)

    # Convert the table list into a 5x5 matrix
    table = [table[i:i+5] for i in range(0, len(table), 5)]
    return table

def decrypt_playfair(ciphertext, table):
    plaintext = ''

    # Decrypt the ciphertext two characters at a time
    for i in range(0, len(ciphertext), 2):
        char1 = ciphertext[i]
        char2 = ciphertext[i+1]

        # Find the positions of the characters in the table
        row1, col1 = [(r, row.index(char1)) for r, row in enumerate(table) if char1 in row][0]
        row2, col2 = [(r, row.index(char2)) for r, row in enumerate(table) if char2 in row][0]

        # Handle the three cases: same row, same column, and rectangle
        if row1 == row2:
            plaintext += table[row1][(col1 - 1) % 5] + table[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += table[(row1 - 1) % 5][col1] + table[(row2 - 1) % 5][col2]
        else:
            plaintext += table[row1][col2] + table[row2][col1]

    # Remove any 'X' characters added during encryption
    plaintext = plaintext.replace('X', '')
    return plaintext

def main():
    key = 'SUPERSPY'
    ciphertext = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'
    table = generate_playfair_table(key)
    decrypted_text = decrypt_playfair(ciphertext, table)
    print(decrypted_text)

if __name__ == '__main__':
    main()
