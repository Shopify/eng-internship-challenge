# Author:           Martin Atanacio
# Date:             11th May 2024
# Description:      This program decrypts a message encrypted using the Playfair 
#                   cipher algorithm. 5x5 matrix is created based on the key and
#                   the modified alphabet. The message is then split into digrams
#                   and decrypted using the matrix and the dictionary of letter positions.


# J and I are equivalent in Playfair cipher, thus, J is removed from the alphabet
MODIFIED_ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

# Create a 5x5 matrix based on the key and the modified alphabet
# Returns the matrix and a dictionary of letter positions
def create_matrix(key) -> tuple[list[list[str]], dict[str, tuple[int, int]]]:
    unique_letters = set() # set to keep track of unique letters in the matrix
    matrix = [['' for _ in range(5)] for _ in range(5)] # 5x5 matrix
    letter_to_position = {} # dictionary to record the position of each letter in the matrix
    row = col = 0 # start at the top-left corner of the matrix

    # iterate through the key and the modified alphabet
    for letter in (key + MODIFIED_ALPHABET):
        if letter == 'J': # J and I are equivalent, so use I instead of J
            letter = 'I'
            
        if letter not in unique_letters: # if unique letter, add to matrix
            matrix[row][col] = letter # add letter to matrix
            unique_letters.add(letter) # add letter to unique letters
            letter_to_position[letter] = (row, col) # record the position of the letter
            col = (col + 1) % 5 # move to the next column, wrapping if necessary
            
            if col == 0: # if at the end of the row, move to the next row
                row += 1

    # return the matrix and the dictionary of letter positions
    return matrix, letter_to_position

# Splits an input message into digrams (pairs of two letters)
# Returns a list of digrams
def message_to_digrams(message) -> list[str]:
    return [message[i: i + 2] for i in range(0, len(message), 2)]

# Decrypts a list of digrams using the Playfair cipher algorithm
# Returns a list of decrypted digrams
def decrypt_digrams(digrams, matrix, letter_to_position) -> list[str]:
    decrypted_digrams = ['' for _ in range(len(digrams))] # store the decrypted digrams
    
    # iterate through each digram
    for i, digram in enumerate(digrams): 
        first_letter, second_letter = digram[0], digram[1] # get the two letters in the digram
        row1, col1 = letter_to_position[first_letter] # get the position of the first letter
        row2, col2 = letter_to_position[second_letter] # get the position of the second letter
        
        # if the letters are in the same row, shift them to the left
        if row1 == row2:
            # shift the letters to the left, wrapping if necessary
            decrypted_digrams[i] = matrix[row1][(col1 - 1) % 5] + \
                matrix[row2][(col2 - 1) % 5]
            
        # if the letters are in the same column, shift them up
        elif col1 == col2:
            # shift the letters up, wrapping if necessary
            decrypted_digrams[i] = matrix[(row1 - 1) % 5][col1] + \
                matrix[(row2 - 1) % 5][col2]
            
        # if the letters form a rectangle, use the opposite corners
        else:
            # use the opposite corners of the rectangle
            decrypted_digrams[i] = matrix[row1][col2] + matrix[row2][col1]

    # return the list of decrypted digrams
    return decrypted_digrams

# Decrypts an encrypted message using the Playfair cipher algorithm
# Returns the decrypted message
def decrypt_message(encrypted_message, key) -> str:

    # remove spaces and convert to uppercase for both message and key
    encrypted_message = encrypted_message.upper().replace(' ', '')
    key = key.upper().replace(' ', '')

    # create matrix and dictionary of letter positions
    matrix, letter_to_position = create_matrix(key)

    # split the encrypted message into digrams
    digrams = message_to_digrams(encrypted_message)

    # decrypt the digrams using the matrix and dictionary
    decrypted_digrams = decrypt_digrams(digrams, matrix, letter_to_position)

    # return the decrypted message, removing any 'X' characters
    return ''.join(decrypted_digrams).replace('X', '')

# Main function
def main():
    ENCRYPTED_MESSAGE = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    KEY = "SUPERSPY"
    
    # expected output: "HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA"
    print(decrypt_message(ENCRYPTED_MESSAGE, KEY))

# Run the main function
if __name__ == "__main__":
    main()