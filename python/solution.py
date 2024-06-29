import string

# Amidst the neon-lit alleys of Spy City, Agent Vulpine Algorithmico braces for the ultimate challenge.

# Cryptonym: Vulpine Algorithmico 
# True Identity: Jake Lance
# Home Base: Toronto, ON
# Current Mission: Decrypt ENCRYPTED_MESSAGE to reveal the password for the secret club at the corner of 32nd Street!


def create_table(key):
    """
    Generate a 5x5 Playfair cipher table based on a given cipher key. I and J are treated as the same character

    Parameters:
    cipher_key (str): The key to generate the cipher table.

    Returns:
    list: A 5x5 table representing the Playfair cipher table. 
    """
    # J ommitted because there can only be 25 characters in the table
    used_chars = set("J") # Historically, I and J have been treated as the same char for Playfair ciphers.
    unique_chars = [char for char in key + string.ascii_uppercase if char not in used_chars and not used_chars.add(char)]
    return [unique_chars[i:i+5] for i in range(0, 25, 5)]

def decrypt_message(digraphs, table):
    """
    Decrypt a message encrypted using a Playfair cipher with a given table.

    Parameters:
    digraphs (list): List of digraphs (pairs of characters) from the encrypted message.
    table (list): A 5x5 table representing the Playfair cipher table.

    Returns:
    str: The decrypted message as a string.
    """
    index = {table[row][col]: (row, col) for row in range(5) for col in range(5)}

    def decrypt_pair(pair):
        # Retrieve the row and column indices of each character in the pair from the location_index dictionary
        row1, col1 = index[pair[0]]
        row2, col2 = index[pair[1]]

        if row1 == row2:
            # If both characters are in the same row:
            # Decrypt by replacing each character with the character to its immediate left
            return table[row1][(col1-1) % 5] + table[row2][(col2-1) % 5]
        elif col1 == col2:
            # If both characters are in the same column:
            # Decrypt by replacing each character with the character immediately above
            return table[(row1-1) % 5][col1] + table[(row2-1) % 5][col2]
        else:
            # If the characters aren't in the same row or same column:
            # Decrypt by swapping characters diagonally opposite to each other within the same row
            return table[row1][col2] + table[row2][col1]

    return ''.join(decrypt_pair(pair) for pair in digraphs)

def create_digraphs(message):
    # Generate digraphs (pairs of characters) from a given message.
    return [message[i:i+2] for i in range(0, len(message), 2)]


ENCRYPTED_MESSAGE = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
CIPHER_KEY = "SUPERSPY"

table = create_table(CIPHER_KEY)
digraphs = create_digraphs(ENCRYPTED_MESSAGE)
decrypted_message = decrypt_message(digraphs, table).replace('X', '')

print(decrypted_message)