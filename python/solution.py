import argparse
DEFAULT_MESSAGE = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
DEFAULT_KEY = "SUPERSPY"

def create_table(cipher_key):
    """
    creates a 5x5 character table from the key provided

    key: the key to be used to create the table
    """
    table_chars = "".join(dict.fromkeys(cipher_key + "ABCDEFGHIKLMNOPQRSTUVWXYZ"))
    return [table_chars[i:i+5] for i in range(0, 25, 5)]

def create_coordinates_map(table):
    """
    returns a dictionary mapping each character to their coordinates in the table

    table: the 5x5 character table
    """
    return {table[i][j]: (i, j) for i in range(5) for j in range(5)}

def pairer(encrypted_message):
    """
    returns a list of pairs of 2 characters each from the encrypted message

    encrypted_message: the encrypted message
    """
    # if the length of the encrypted message is odd, add an 'X' character to make it even
    if len(encrypted_message) % 2 != 0:
        encrypted_message += "X"
    return [(encrypted_message[i], encrypted_message[i+1]) for i in range(0, len(encrypted_message), 2)]
    
def decrypt(table, coordinates_map, pairs):
    """
    returns the decrypted message from the pairs of characters

    table: the 5x5 character table
    coordinates_map: a dictionary mapping each character to their coordinates in the table
    pairs: a list of pairs of 2 characters each from the encrypted message
    """
    decrypted_message = ''
    for p in pairs:
        # get the coordinates of the characters in the table
        (rowA, colA), (rowB, colB) = coordinates_map[p[0]], coordinates_map[p[1]]
        # if the characters are in the same row, replace them with the characters to their left, with wrap around
        if rowA == rowB:
            decrypted_message += table[rowA][(colA - 1) % 5] + table[rowB][(colB - 1) % 5]
        # elif the characters are in the same column, replace them with the characters above them, with wrap around
        elif colA == colB:
            decrypted_message += table[(rowA - 1) % 5][colA] + table[(rowB - 1) % 5][colB]
        # else the characters are in different rows and columns, so replace them with the characters in the same row but at the column of the other character
        else:
            decrypted_message += table[rowA][colB] + table[rowB][colA]
        
    # remove any 'X' characters from the decrypted message
    # there should not be spaces or special characters in the decrypted message as the table only contains uppercase alphabetical characters
    return decrypted_message.replace('X', '')

def main(message = None, key = None):
    # Define the encrypted message and key
    # Remove any non-alphabetical characters from the message and key while converting them to uppercase
    encrypted_message = ''.join([i for i in message.upper() if i.isalpha()]) if message else DEFAULT_MESSAGE
    # additionally, replace 'J' characters with 'I' in the key
    cipher_key = ''.join([i for i in key.upper().replace("J", "I") if i.isalpha()]) if key else DEFAULT_KEY
    # Create the table and coordinates map
    table = create_table(cipher_key)
    coordinates_map = create_coordinates_map(table)
    # Pair the characters in the encrypted message
    pairs = pairer(encrypted_message)
    # Decrypt the encrypted message and print the result
    return decrypt(table, coordinates_map, pairs)


if __name__ == '__main__':
    # create an argument parser
    parser = argparse.ArgumentParser(description='Decrypt a message using the Playfair cipher')
    # two optional arguments, message and key
    parser.add_argument('message', nargs='?', help='the encrypted message to be decrypted')
    parser.add_argument('key', nargs='?', help='the key to be used to decrypt the message')
    args = parser.parse_args()
    print(main(args.message, args.key))