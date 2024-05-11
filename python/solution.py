ENCRYPTED_MESSAGE = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
CIPHER_KEY = "SUPERSPY"
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
PLAYFAIR_KEY_TABLE_SIZE = 5
# INVALID_KEY_CHARACTERS in a set to have O(1) search complexity
INVALID_KEY_CHARACTERS = set([' ', 'X', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', '{', ']', '}', '|', '\\', ';', ':', '\'', '"', ',', '.', '<', '>', '/', '?', '`'])

def generate_key_table(cipher_key):
    """
    Generate the playfair key table using the provided cipher key.

    Parameters:
    - cipher_key (str): The key used for generating the key table.

    Returns:
    - dict: A dictionary representing the generated key table.
    """
    # Dictionary to store each letter and its position in the table.
    # Utilizing a dictionary ensures O(1) complexity for when accessing a letter's position.
    key_table = {}
    # Set to track used letters to avoid duplicates letters in the key table.
    used_letters = set()
    # Start index of the key table
    i, j = 0, 0
    # Concatenate the key letters and the alphabet into one string to iterate 
    # once over all possible key letters.
    key_letters = cipher_key + ALPHABET
    # Iterate through the key letters to add them to the key table
    for letter in key_letters:
        # Make sure the letter is upper case
        uppercase_letter = letter.upper()
        # If the same letter is already used in the key table matrix or the letter 
        # is an invalid character, we dont add it to the key table
        if uppercase_letter in used_letters or uppercase_letter in INVALID_KEY_CHARACTERS:
            continue
        # Add the letter and its position as a tuple in the key table
        key_table[uppercase_letter] = (i, j)
        # Add the letter to the used letters set and increment the j position 
        # to go to the next position in the matrix
        used_letters.add(uppercase_letter)
        j += 1
        # If the column index j reaches the maximum size (5),
        # we move to the next row of the matrix.
        if j == PLAYFAIR_KEY_TABLE_SIZE:
            i += 1
            j = 0

        # If the row index i reaches the maximum size (5),
        # the key table is complete, and we stop adding letters.
        if i == PLAYFAIR_KEY_TABLE_SIZE:
            break
    return key_table


if __name__ == "__main__":
    key_table = generate_key_table("playfair example")
