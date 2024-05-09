# Constants
ALPHABET = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' # 'J' is excluded
KEY = 'SUPERSPY'
MESSAGE = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'

def main():

    # Decrypt message
    decrypted = decrypt(MESSAGE, KEY)
    
    # Print only the Playfair decrypted text
    print(decrypted)

def decrypt(message, key):

    # Variables
    message_decrypted = ''
    chunk = ''
    counter = 0

    message = clean_message(message)
    key = clean_key(key)

    # Create a 5x5 matrix and load it with unique chars
    matrix = []
    for i in range(5):
         matrix.append(key[i*5:(i+1)*5])

    
    # Initiate a while loop which continues until the entire message has been decrypted
    while counter < len(message):

        # Break ciphertext into chunks of two chars
        chunk += message[counter:counter+1]

        # Add decrypted chunks to new message
        message_decrypted += decrypt_chunk(chunk, message, key, matrix)

        # Update counter by two to account for the chunks of two chars
        counter += 2

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

def decrypt_chunk(chunk, message, key, matrix):
     
    # Compare message chunk to playfair matrix
    # Decrypt if letters appear in the same row
    x = 0
    while x is < len(key):
        if chunk[0] == key[x]:
            loci0 = x
        elif chunk[1] == key[x]:
            loci1 = x
        x += 1

    row0, column0 = find_column_and_row(loci0)
    row1, column1 = find_column_and_row(loci1)

    if row0 == row1:
        matrix[][]
    if column0 == column1:

    else:
    
    # Decrypt if letters appear in the same column
    # Decrypt if exception

    # Your decrypted string must by entirely UPPER CASE, and not include spaces, the letter "X", or special characters. Ensure you meet all these conditions before outputting the result.

     return

def find_column_and_row(loci):
    
    # Calculate quotient
    row = loci // 5

    # Calculate modulo
    column = loci % 5

    return column, row




if __name__ == '__main__':
    main()