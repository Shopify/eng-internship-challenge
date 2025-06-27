# This dictionary will be used to store the positions of letters in the key square
letter_positions = {}

# This list will be used to store the key square
square = []


def replace_j(key):
    """Replaces all 'J' characters in the key with 'I' characters.

    Args:
        key: The key to be used for encryption.

    Returns:
        A new string with all 'J' characters replaced with 'I' characters.
    """

    value = ""
    for ele in key:
        if ele != "J":
            value += ele
        else:
            value += "I"
    return value


def generateKeySquare(key):
    """Generates a key square from a given key.

    Args:
        key: The key to be used for encryption.

    Returns:
        A tuple containing the key square and a dictionary mapping letters to their positions in the square.
    """

    key_square = []
    temp = []
    col_count = 0
    row_count = 0

    # Create a dictionary to store the positions of letters in the key square
    letter_positions={}

    # Initialize all values to -1
    for i in range(26):
        if chr(65+i) != "J":
            letter_positions[chr(65 + i)] = [-1, -1]  # A = 65, Z = 90

    for i in range(len(key)):
        if key[i] != ' ' and letter_positions[key[i]][0] == -1:
            letter_positions[key[i]][0] = row_count
            letter_positions[key[i]][1] = col_count

            col_count += 1
            temp.append(key[i])

            if col_count == 5:
                key_square.append(temp)
                temp = []
                row_count += 1
                col_count = 0

    # Fill the last row of the key square with remaining letters
    if col_count != 5 and col_count != 0:

        for k in letter_positions:

            if letter_positions[k][0] == -1:
                if col_count == 5:
                    col_count = 0
                    break
                temp.append(k)
                letter_positions[k][0] = row_count
                letter_positions[k][1] = col_count
                col_count += 1
        row_count += 1
        key_square.append(temp)
        temp = []

    # Fill the remaining cells of the key square with the rest of the letters in alphabetical order
    for k in letter_positions:
        if letter_positions[k][0] == -1:
            letter_positions[k][0] = row_count
            letter_positions[k][1] = col_count
            col_count += 1
            temp.append(k)
            if col_count == 5:
                key_square.append(temp)
                temp = []
                row_count += 1
                col_count = 0

    return key_square, letter_positions


def rules(bigram):
    """Decrypts a bigraph (two-letter pair) using the key square.

    Args:
        diagraph: The bigraph to be decrypted.

    Returns:
        The decrypted bigraph.
    """

    position_row1, position_col1 = letter_positions[bigram[0]][0], letter_positions[bigram[0]][1]
    position_row2, position_col2 = letter_positions[bigram[1]][0], letter_positions[bigram[1]][1]

    if position_row1 == position_row2:  # If same row, return chars to the left (mod 5)
        return square[position_row1][(position_col1 - 1) % 5] +square[position_row2][(position_col2 - 1) % 5]
    elif position_col1 == position_col2:  # If same col, return chars below (mod 5)
        return square[(position_row1 - 1) % 5][position_col1] + square[(position_row2 - 1) % 5][position_col2]
    # Else, return chars at opposite positions
    return square[position_row1][position_col2] + square[position_row2][position_col1]

    
    
def decrypt(encrypt_messg):
    """Decrypts a message using the key square.

    Args:
        encrypt_messg: The encrypted message.

    Returns:
        The decrypted message.
    """

    i = 0
    decrypt_msg = ""

    while (i < len(encrypt_messg)):
        if i != len(encrypt_messg) - 1 and encrypt_messg[i] != encrypt_messg[i + 1]:
            decrypt_msg += rules(encrypt_messg[i] + encrypt_messg[i + 1])
            i += 2

        else:
            decrypt_msg += rules(encrypt_messg[i] + "X")
            i += 1

    return decrypt_msg.replace("X", '')


if __name__ == "__main__":

    encrypt_messg = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"
    # Validate key and encrypted message
    if key.isalpha() and encrypt_messg.isalpha():
        
        # Generate the key square and search dictionary
        square, letter_positions = generateKeySquare(replace_j(key))
    
        # Decrypt the message
        decrypted_message = decrypt(replace_j(encrypt_messg))
        
        print(decrypted_message)