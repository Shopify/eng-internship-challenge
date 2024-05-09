def generate_table(key):
    """
    Generates a 5x5 table for the Playfair cipher using the given key

    args:
        key: str - the key to generate the table from
    return:
        table: dict - a dictionary mapping characters to their position in the table
    """
    if not key.isalpha():
        raise ValueError("Key should contain only alphabetic characters")

    # create a unique list from the key chars, removing duplicates
    unique_key = []
    for char in key:
        if char not in unique_key:
            unique_key.append(char)

    # add the rest of the alphabet to the unique list, excluding 'J'
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in unique_key:
            unique_key.append(char)

    # initialize dict to map characters to their position in a 5x5 look up table
    table = {}

    # fill the table with the unique characters
    for index, char in enumerate(unique_key):
        # calculate the row and column of the character in the 5x5 table
        row, col = divmod(index, 5)
        # store the character and its position in the table
        table[char] = (row, col)
        # store the position and the character in the table
        table[(row, col)] = char

    return table


def print_table(table):
    """
    Helper function to print the 5x5 table

    args:
        table: dict - a dictionary mapping characters to their position in the table
    """
    # fixed table size of 5x5 for Playfair cipher
    size = 5

    for i in range(size):
        for j in range(size):
            # print current letter, followed by a space
            print(table[(i, j)], end=" ")
        print()  # move to the next row

    return


def split_into_pairs(message):
    """
    Splits the message into pairs of characters, adding an 'X' to the last pair if needed

    args:
        message: str - the message to split into pairs
    return:
        pairs: list - a list of pairs of characters
    """
    # split the message into pairs of characters
    pairs = []
    for i in range(0, len(message), 2):
        pair = message[i : i + 2]
        pairs.append(pair)

    # if the last pair has only one character, add an 'X' to it
    if len(pairs[-1]) == 1:
        pairs[-1] += "X"

    return pairs


def decrypt(key, encrypted_message):
    """
    Decrypts the given message using the Playfair cipher

    args:
        key: str - the key to generate the table from
        encrypted_message: str - the message to decrypt
    return:
        decrypted_message: str - the decrypted message
    """
    table = generate_table(key)
    decrypted_message = ""
    pairs_list = split_into_pairs(encrypted_message)

    # iterate over the pairs of characters
    for first, second in pairs_list:
        if first not in table or second not in table:
            raise ValueError("One of the characters are not in the table")
        
        # get the row and column of the characters in the table
        row1, col1 = table[first] # first letter
        row2, col2 = table[second] # second letter

        # rule 1: both letters in same row -> shift one position left
        if row1 == row2:
            decrypted_message += table[(row1, (col1 - 1) % 5)]  # first letter
            decrypted_message += table[(row2, (col2 - 1) % 5)]  # second letter

        # rule 2: both letters in same column -> shift one position up
        elif col1 == col2:
            decrypted_message += table[((row1 - 1) % 5, col1)]  # first letter
            decrypted_message += table[((row2 - 1) % 5, col2)]  # second letter

        # rule 3: form a rectangle -> swap the columns
        else:
            decrypted_message += table[(row1, col2)]  # first letter
            decrypted_message += table[(row2, col1)]  # second letter

    if not decrypted_message.isupper():
        raise ValueError("Decrypted message should be in uppercase")

    return decrypted_message


def clean_message(message, stage):
    """
    Cleans the message by removing X's, special characters, spaces, 
    merging 'I" and 'J', and numbers depending on the stage
    of the cipher (encrypted or decrypted):
        encrypted stage: remove special characters, spaces, and numbers
        decrypted stage: remove X characters

    args:
        message: str - the message to clean
        stage: str - the stage of the cipher (encrypted or decrypted)
    return:
        cleaned_message: str - the cleaned message
    """
    message = message.upper()

    # before decryption, remove special chars, spaces, and numbers
    if stage == "encrypted":
        # playfair cipher merges 'I' & 'J'
        message = message.replace("J", "I")
        # keep only alphabetic characters
        message = "".join([char for char in message if char.isalpha()])

        # add 'X' to the end of the message if it has an odd length
        if len(message) % 2 == 1:
            message += "X"

    # after decryption, remove 'X' characters
    elif stage == "decrypted":
        message = message.replace("X", "")

    # check if message properly cleaned (only alphabetic, uppercase characters)

    
    return message


def validate_inputs(key, message):
    """
    Helper function to validate the key and message inputs after cleaning

    args:
        key: str - the key to validate
        message: str - the message to validate
    """
    if not key:
        raise ValueError("Key cannot be empty")
    if not message:
        raise ValueError("Message cannot be empty")
    if not key.isalpha() or not message.isalpha():
        raise ValueError("Key and message must contain only alphabetic characters")
    if not message.isupper():
        raise ValueError("Message should be in uppercase")
    

def main():
    key = "SUPERSPY"
    encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    
    try:
        cleaned_encrypted_message = clean_message(encrypted_message, "encrypted")
        validate_inputs(key, cleaned_encrypted_message)
        decrypted_message = decrypt(key, cleaned_encrypted_message)
        message = clean_message(decrypted_message, "decrypted")
        print(message)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
