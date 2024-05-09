# Constants
ALPHABET = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' # 'J' is excluded
KEY = 'SUPERSPY'
MESSAGE = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'

def main():

    # Decrypt message
    decrypted = decrypt(MESSAGE, KEY)

    final_answer = check(decrypted)
    
    # Print only the Playfair decrypted text
    print(final_answer)


def decrypt(message, key):

    # Variables
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

    # Make MESSAGE even
    if len(message) % 2 == 1:
        message += 'X'

    return message


def clean_key(key):
     
    # Normalize the key: and handle 'J'
    key = ''.join(filter(str.isalpha, key)).replace('J', 'I')

    # Create a list of unique characters in the key
    unique_chars = set()
    key_unique = [i for i in key if not (i in unique_chars or unique_chars.add(i))]

    # Create a list of chars unique chars starting with the key and ending with the alphabet
    unique_list = key_unique + [i for i in ALPHABET if i not in unique_chars]

    return unique_list


def decrypt_chunk(chunk, matrix):
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
    
    # Calculate quotient
    row = loci // 5

    # Calculate modulo
    column = loci % 5

    return column, row


def check(message):
    
    # Your decrypted string must by entirely UPPER CASE, and not include spaces, the letter "X", or special characters. Ensure you meet all these conditions before outputting the result.
    new_string = ''
    for i in range(len(message)):
        if message[i].isalpha() and message[i].upper() != 'X':
            new_string += message[i].upper()

    return new_string


if __name__ == '__main__':
    main()