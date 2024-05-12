ENCRYPTED_MESSAGE = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
CIPHER_KEY = "SUPERSPY"
ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ" # omit J to reduce the alphabet to fit
PLAYFAIR_KEY_TABLE_SIZE = 5
# INVALID_KEY_CHARACTERS in a set to have O(1) search complexity
INVALID_KEY_CHARACTERS = set([' ', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', '{', ']', '}', '|', '\\', ';', ':', '\'', '"', ',', '.', '<', '>', '/', '?', '`'])

def generate_key_table(cipher_key):
    """
    Generate the playfair key table using the provided cipher key.

    Parameters:
    - cipher_key (str): The key used for generating the key table.

    Returns:
    - dict: A dictionary representing the generated key table.
    """
    # Dictionary representing the generated key table.
    # It consists of two keys:
    # - "letters": Stores each letter and its position in the table as a dictionary.
    #   Utilizing a dictionary ensures O(1) complexity for accessing a letter's position.
    # - "positions": Represents a 5x5 matrix where each element is a letter.
    #   Utilizing a 5x5 matrix ensures O(1) complexity for accessing a letter with its position.
    key_table = {
        "letters": {},
        "positions": [['' for _ in range(PLAYFAIR_KEY_TABLE_SIZE)] for _ in range(PLAYFAIR_KEY_TABLE_SIZE)]
    }
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
        # Add the letter and its position as a tuple in the key table dictionary
        key_table["letters"][uppercase_letter] = (i, j)
        # Add the letter and its position as a tuple in the key table matrix
        key_table["positions"][i][j] = uppercase_letter
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

def break_encrypted_message_into_digrams(encrypted_message):
    """
    Breaks the encrypted message into digrams (pairs of consecutive characters).

    Parameters:
    - encrypted_message (str): The encrypted message to be broken into digrams.

    Returns:
    - list of str: A list containing the digrams extracted from the encrypted message.
    """
    # Check if the encrypted message has an even number of characters
    if len(encrypted_message) % 2 != 0:
        raise ValueError("Encrypted message length must be even")
    
    # Initialize an empty list to store digrams
    digrams = []
    
    # Iterate through the encrypted message by pairs of characters
    for i in range(0, len(encrypted_message) - 1, 2):
        digram = encrypted_message[i:i+2]  # Extract a digram
        digrams.append(digram)    # Add the digram to the list
    
    return digrams

def letters_on_same_row(key_table, first_letter_pos, second_letter_pos):
    """
    Decrypts and returns the swapped digram letters as a tuple, based on the Playfair cipher's same-row rule.

    Parameters:
    - key_table (dict): The key table dictionary.
    - first_letter_pos (tuple of int): The position of the first letter in the key table (row, column).
    - second_letter_pos (tuple of int): The position of the second letter in the key table (row, column).

    Returns:
    - tuple of str: The decrypted swapped letters as a tuple, following the same-row rule of the Playfair cipher.
    """
    # Get the immediate left letter for each encrypted letter
    first_letter_swap = key_table["positions"][first_letter_pos[0]][get_immediate_previous_index(first_letter_pos[1])]
    second_letter_swap = key_table["positions"][second_letter_pos[0]][get_immediate_previous_index(second_letter_pos[1])]
    return (first_letter_swap, second_letter_swap)

def letters_on_same_column(key_table, first_letter_pos, second_letter_pos):
    """
    Decrypts and returns the swapped digram letters as a tuple, based on the Playfair cipher's same-column rule.

    Parameters:
    - key_table (dict): The key table dictionary.
    - first_letter_pos (tuple of int): The position of the first letter in the key table (row, column).
    - second_letter_pos (tuple of int): The position of the second letter in the key table (row, column).

    Returns:
    - tuple of str: The decrypted swapped letters as a tuple, following the same-column rule of the Playfair cipher.
    """
    # Get the immediate upper letter for each encrypted letter
    first_letter_swap = key_table["positions"][get_immediate_previous_index(first_letter_pos[0])][first_letter_pos[1]]
    second_letter_swap = key_table["positions"][get_immediate_previous_index(second_letter_pos[0])][second_letter_pos[1]]
    return (first_letter_swap, second_letter_swap)

def get_immediate_previous_index(index):
    """
    Returns the immediate previous index position (int) of the key table line (immediate left) or column (immediately upward).

    Parameters:
    - index (int): The index of the key table line or column (0 to 4).

    Returns:
    - int: The immediate previous index position.
    """
    index -= 1
    if index < 0:
        index += 5
    decrypt_index = (index) % 5
    return decrypt_index

def decrypt_digrams(key_table, digrams):
    decrypted_digrams = []
    for digram in digrams:
        first_letter, second_letter = digram
        first_letter_pos = key_table["letters"][first_letter]
        second_letter_pos = key_table["letters"][second_letter]
        # Letters are in the same row
        if first_letter_pos[0] == second_letter_pos[0]:
            first_letter_swap, second_letter_swap = letters_on_same_row(key_table, first_letter_pos, second_letter_pos)
        # Letters are in the same column
        elif first_letter_pos[1] == second_letter_pos[1]:
            first_letter_swap, second_letter_swap = letters_on_same_column(key_table, first_letter_pos, second_letter_pos)
        else:
            # TODO implement the rectangle swap
            pass
        decrypted_digram = first_letter_swap + second_letter_swap
        decrypted_digrams.append(decrypted_digram)
    return decrypted_digrams


if __name__ == "__main__":
    key_table = generate_key_table(CIPHER_KEY)
    digrams = break_encrypted_message_into_digrams(ENCRYPTED_MESSAGE)
    decrypted_digrams = decrypt_digrams(key_table, digrams)
    print(decrypted_digrams)