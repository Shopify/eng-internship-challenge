"""Script to decrypt a given string with a given key using the Playfair cipher
"""
def generate_table (key):
    """Function to generate Playfair Cipher table with given key


    Args:
        key (str): Key for generating the table

    Returns:
        list[list[str]]: Playfair table as 5x5 matrix
    """
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M',
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] # We skip the letter J in the alphabet to have 25 letters
    key_chars = []
    for c in key:  # Loop to get all the characters in the key without repetitions
        if c not in key_chars:
            key_chars.append(c)
    filler_chars = []
    for c in alpha: # Loop to fill the rest of the table with the remaning alphabet letters
        if c not in filler_chars and c not in key_chars:
            filler_chars.append(c)
    key_array = key_chars + filler_chars # Merge the list of the key chars and the remaning alphabet letters in one
    cipher_table = []
    while key_array:
        cipher_table.append(key_array[:5]) # Generate a 5x5 matrix to use as our cipher table
        key_array = key_array[5:]

    return cipher_table

def search_char(cipher_table, char):
    """Function to search a given character in the table, returing its indexes

    Args:
        cipher_table (list[list[str]]): Playfair table as 5x5 matrix
        char (str): Character to search

    Returns:
        tuple(int, int): Character's indexes in the Playfair table
    """
    for i in range(5):
        for j in range(5):
            if char == cipher_table[i][j]:
                return i, j

def decrypt_row(cipher_table, chars_x, char1_y, char2_y):
    """Function to apply the Row Rule decrypting a string

    Args:
        cipher_table (list[list[str]]): Playfair table as 5x5 matrix
        chars_x (int): Row index for both character
        char1_y (int): Column index for character 1
        char2_y (int): Column index for character 2

    Returns:
        str: Decrpyted digram
    """
    digram = ""
    if char1_y == 0: # If the character index is 0, loop around the row and gets the last character
        digram = digram + cipher_table[chars_x][4]
    else: # If we don't need to loop around, we get the character to the left of the one we're decrypting
        digram = digram + cipher_table[chars_x][char1_y - 1]
    if char2_y == 0: # Same as character 1
        digram = digram + cipher_table[chars_x][4]
    else:
        digram = digram + cipher_table[chars_x][char2_y - 1]
    return digram # Returns the two letters decrypted

def decrypt_column(cipher_table, chars_y, char1_x, char2_x):
    """Function to apply the Column Rule decrypting a string

    Args:
        cipher_table (list[list[str]]): Playfair table as 5x5 matrix
        chars_y (int): Column index for both charcters
        char1_x (int): Row index for character 1
        char2_x (int): Row index for character 2

    Returns:
        str: Decrpyted digram
    """
    digram = ""
    if char1_x == 0: # If the character index is 0, loop around the column and gets the last character
        digram = digram + cipher_table[4][chars_y]
    else: # If we don't need to loop around, we get the character below the one we're decrypting
        digram = digram + cipher_table[char1_x - 1][chars_y]
    if char2_x == 0: # Same as character 1
        digram = digram + cipher_table[4][chars_y]
    else:
        digram = digram + cipher_table[char2_x - 1][chars_y]
    return digram # Returns the two letters decrypted


def decrypt_rectangle(cipher_table, char1_x, char1_y, char2_x, char2_y):
    """Function to apply the Rectangle Rule decrypting a string

    Args:
        cipher_table (list[list[str]]): Playfair table as 5x5 matrix
        char1_x (int): Row index for character 1
        char1_y (int): Column index for character 1
        char2_x (int): Row index for character 2
        char2_y (int): Column index for character 2

    Returns:
        str: Decrpyted digram
    """
    # We return the characters at the opposite corner and in the same row of the ones we're decrypting
    return cipher_table[char1_x][char2_y] + cipher_table[char2_x][char1_y]

def decrypt_playfair(key, encrypted_string):
    """Function to decrypt a string encrypted with the Playfair cipher with a given key

    Args:
        key (str): Key for generating the table
        encrypted_string (str): String to decrypt using the Playfair cipher

    Returns:
        str: Decrypted string
    """
    cipher_table = generate_table(key) # Generates the Playfair table using the key
    plaintext = ""
    for i in range(0, len(encrypted_string), 2): # We loop the entire encrypted string and we decrypt it digram by digram
        char1_x, char1_y = search_char(cipher_table, encrypted_string[i])
        char2_x, char2_y = search_char(cipher_table, encrypted_string[i + 1])
        if char1_x == char2_x: # If the two characters are in the same row we use the Row Rule
            plaintext = plaintext + decrypt_row(cipher_table, char1_x, char1_y, char2_y)
        elif char1_y == char2_y: # If the two characters are in the same Column we use the Column Rule
            plaintext = plaintext + decrypt_column(cipher_table, char1_y, char1_x, char2_x)
        else: # If the two characters are in different rows and different columns we use the Rectangle Rule
            plaintext = plaintext + decrypt_rectangle(cipher_table, char1_x, char1_y, char2_x, char2_y)
    return plaintext.replace('X', '') # We return the decrypted string, after removing the placeholders "X" for double letters

# We decrypt the string and print the result
print(decrypt_playfair("SUPERSPY", "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"), end="")
