def create_digram_pairs(ciphertext):
    # Use list comprehension to create a list with digram pairs
    pairs = [ciphertext[i:i + 2] for i in range(0, len(ciphertext), 2)]
    return pairs


def create_table(suspected_key):
    # Remove duplicates by converting to a dict and create empty table
    suspected_key = ''.join(dict.fromkeys(suspected_key.upper()))
    key_table = ""

    # Populate table with key's unique characters
    for char in suspected_key:
        key_table += char

    # Populate table with the rest of the alphabet (Keeping J inside I)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in key_table:
            key_table += char

    # Convert table (string) into a 5x5 matrix
    key_matrix = [list(key_table[i:i + 5]) for i in range(0, 25, 5)]

    return key_matrix


def reverse_cipher(table, pairs):
    decrypted_message = ""
    # Iterate through each digram pair
    for pair in pairs:
        # Define the first and second letters in the pair
        letter1, letter2 = pair

        # Find the positions of both letters in the key table
        row1, col1 = find_position(letter1, table)
        row2, col2 = find_position(letter2, table)

        # If they are in the same row, replace each with the letter to its left
        if row1 == row2:
            decrypted_pair = table[row1][(col1 - 1) % 5] + table[row2][(col2 - 1) % 5]

        # If they are in the same column, replace each with the letter above it
        elif col1 == col2:
            decrypted_pair = table[(row1 - 1) % 5][col1] + table[(row2 - 1) % 5][col2]

        # If they form a rectangle, replace each letter with the one in its own row but in the other letter’s column
        else:
            decrypted_pair = table[row1][col2] + table[row2][col1]

        decrypted_message += decrypted_pair

        # Remove all instances of X in the final decrypted message
        decrypted_message = decrypted_message.replace("X", "")

    return decrypted_message


def find_position(letter, key_table):
    # Navigate through matrix and find the positions of the letters
    for i in range(5):
        for j in range(5):
            if key_table[i][j] == letter:
                return i, j


if __name__ == '__main__':
    secret_cipher = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    digram_pairs = create_digram_pairs(secret_cipher)

    key = "SUPERSPY"
    five_by_five_table = create_table(key)

    plaintext = reverse_cipher(five_by_five_table, digram_pairs)
    print(plaintext)
