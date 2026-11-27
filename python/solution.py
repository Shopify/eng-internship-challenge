# Define the alphabet used in the Playfair cipher, excluding 'J'
alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"


def construct_table(secret_key):
    """
    Constructs the 5x5 table used for Playfair cipher encryption and decryption based on the given secret key.

    Parameters:
        secret_key (str): The secret key used to construct the table.

    Returns:
        list: A 5x5 matrix representing the Playfair table.
    """
    # Replace 'J' with 'I' in the secret key
    secret_key = secret_key.replace('J', 'I')
    table = []
    used_chars = set()

    # Populate the table with characters from the secret key and the alphabet, ensuring no duplicates
    for char in secret_key + alphabet:
        if char not in used_chars:
            used_chars.add(char)
            table.append(char)

    # Return the table as a list of lists, each representing a row of 5 characters
    return [table[i:i + 5] for i in range(0, 25, 5)]


def find_position(table, char):
    """
    Finds the position of a character in the Playfair table.

    Parameters:
        table (list): The 5x5 Playfair table.
        char (str): The character to find in the table.

    Returns:
        tuple: A tuple (row, column) representing the position of the character in the table.
    """
    # Iterate through each row of the table to find the character
    for row in range(5):
        if char in table[row]:
            return row, table[row].index(char)


def decrypt_playfair(ciphertext, table):
    """
    Decrypts a ciphertext encrypted with the Playfair cipher using the given table.

    Parameters:
        ciphertext (str): The ciphertext to decrypt.
        table (list): The 5x5 Playfair table used for decryption.

    Returns:
        str: The decrypted plaintext.
    """
    plaintext = ""

    # Process the ciphertext two characters at a time
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i + 1]
        row_a, col_a = find_position(table, a)
        row_b, col_b = find_position(table, b)

        # Apply Playfair cipher decryption rules
        if row_a == row_b:
            # If both characters are in the same row, move left
            plaintext += table[row_a][(col_a - 1) % 5]
            plaintext += table[row_b][(col_b - 1) % 5]
        elif col_a == col_b:
            # If both characters are in the same column, move up
            plaintext += table[(row_a - 1) % 5][col_a]
            plaintext += table[(row_b - 1) % 5][col_b]
        else:
            # If characters form a rectangle, swap columns
            plaintext += table[row_a][col_b]
            plaintext += table[row_b][col_a]

    return plaintext


def execute_decryption(ciphertext, secret_key):
    """
    Executes the decryption process for a given ciphertext and secret key using the Playfair cipher.

    Parameters:
        ciphertext (str): The ciphertext to decrypt.
        secret_key (str): The secret key used to construct the Playfair table.

    Returns:
        str: The decrypted plaintext with 'X' and spaces removed.
    """
    key_table = construct_table(secret_key)
    decrypted_message = decrypt_playfair(ciphertext, key_table)
    return decrypted_message.replace('X', '').replace(' ', '')


if __name__ == '__main__':
    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    secret_key = "SUPERSPY"

    result = execute_decryption(ciphertext, secret_key)
    print(result)
