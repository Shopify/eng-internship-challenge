"""

"""

# Constants
ALPHABET = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' # 'J' is excluded
KEY = 'SUPERSPY'
MESSAGE = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'

def main():
    """
    The main function that decrypts a message using the Playfair cipher and prints the decrypted text.

    This function takes no parameters.

    Returns:
        None
    """

    # Decrypt message
    decrypted = decrypt(MESSAGE, KEY)
    final_answer = check(decrypted)

    # Print only the Playfair decrypted text
    print(final_answer)


def decrypt(message, key):

    # Variables
    """
    Decrypts a message using the Playfair cipher algorithm.

    Args:
        message (str): The ciphertext to be decrypted.
        key (str): The key used for decryption.

    Returns:
        str: The decrypted plaintext.

    Raises:
        None

    Examples:
        >>> decrypt("IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV", "SUPERSPY")
        'HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA'
    """
    message_decrypted = ''
    chunk = ''
    counter = 0

    # Clean message and key
    message = clean_message(message)
    key = clean_key(key)

    # Create a 5x5 matrix and load it with unique chars
    matrix = []
    for i in range(5):
        matrix.append(key[i*5:(i+1)*5])


    # Initiate a while loop which continues until the entire message has been decrypted
    while counter < len(message):

        # Break ciphertext into chunks of two chars
        if message[counter] == message[counter+1]:
            chunk = message[counter] + 'X'
            counter += 1
        else:
            chunk = message[counter:counter+2]
            counter += 2

        # Add decrypted chunks to new message
        message_decrypted += decrypt_chunk(chunk, matrix)

    return message_decrypted


def clean_message(message):
    """
    Takes a string `message` and returns a cleaned version of it. If the length of `message` is odd, it appends an 'X' to the end of the string.
    
    :param message: A string to be cleaned.
    :type message: str
    
    :return: A cleaned version of the input string.
    :rtype: str
    """

    # Make MESSAGE even
    if len(message) % 2 == 1:
        message += 'X'

    return message


def clean_key(key):
    """
    A description of the entire function, its parameters, and its return types.
    """
     
    # Normalize the key: and handle 'J'
    key = ''.join(filter(str.isalpha, key)).replace('J', 'I')

    # Create a list of unique characters in the key
    unique_chars = set()
    key_unique = [i for i in key if not (i in unique_chars or unique_chars.add(i))]

    # Create a list of chars unique chars starting with the key and ending with the alphabet
    unique_list = key_unique + [i for i in ALPHABET if i not in unique_chars]

    return unique_list


def decrypt_chunk(chunk, matrix):
    """
    Decrypts a chunk of text using a given matrix based on the Playfair Cipher technique.

    :param chunk: A string representing the chunk of text to decrypt.
    :type chunk: str
    :param matrix: A 5x5 matrix used for decryption.
    :type matrix: List[List[str]]

    :return: A string representing the decrypted chunk of text.
    :rtype: str
    """
    loci = [(i, row.index(chunk[j])) for j in range(2) for i, row in enumerate(matrix) if chunk[j] in row]
    if len(loci) != 2:
        return chunk  # In case of an error or no matches found

    # Unpack loci
    (row0, col0), (row1, col1) = loci

    # Decrypt if letters appear in the same row
    if row0 == row1:
        # Same row, shift columns to the left
        decrypted_chars = [
            matrix[row0][(col0 - 1) % 5],
            matrix[row1][(col1 - 1) % 5]
        ]
    # Decrypt if letters appear in the same column
    elif col0 == col1:
        # Same column: shift rows up
        decrypted_chars = [
            matrix[(row0 - 1) % 5][col0],
            matrix[(row1 - 1) % 5][col1]
        ]
    # Decrypt if exception
    else:
        # Rectangle: swap columns
        decrypted_chars = [matrix[row0][col1], matrix[row1][col0]]

    return ''.join(decrypted_chars)


def find_column_and_row(loci):
    """
    Find the column and row indices of a given location in a 5x5 matrix.

    Parameters:
        loci (int): The location index in the matrix.

    Returns:
        tuple: A tuple containing the column and row indices.
    """
    
    # Calculate quotient
    row = loci // 5

    # Calculate modulo
    column = loci % 5

    return column, row


def check(message):
    """
    A function that ensures the decrypted string is entirely UPPER CASE, excluding spaces, the letter 'X', and special characters.

    Parameters:
        message (str): The input string to be checked.

    Returns:
        str: The modified string meeting the specified conditions.
    """
    
    # Your decrypted string must by entirely UPPER CASE, and not include spaces, the letter "X", or special characters.
    # Ensure you meet all these conditions before outputting the result.
    new_string = ''
    for i in enumerate(message):
        if message[i].isalpha() and message[i].upper() != 'X':
            new_string += message[i].upper()

    return new_string


if __name__ == '__main__':
    main()