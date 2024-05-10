import re

def find_position(matrix, char):
    """
    Function to return position of character in playfair matrix
    @param matrix: The playfair matrix containing secret key
    @param char: the character to find in the matrix
    @return: Returns the tuple for the specific (row, column) indices
    """
    for i in range(5):
        for j in range(5):
            if char == matrix[i][j]:
                return (i, j)
def filter_string(input_string):
    """ 
    Function to remove all special characters, spaces, and replace 'J's with 'I's
    @param input_string: The input string to clean
    @return: a modified string devoid of all spaces, special characters, and with replaced 'J's
    """
    input_string = input_string.replace("J", "I").replace(" ", "").upper()
    allowed_chars = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    filtered_string = ''.join(char for char in input_string if char in allowed_chars)
    return filtered_string

def create_playfair_matrix(key):
    """
    Function to build a playfair matrix given a secret key
    @param key: the secret key to build the matrix
    @return: a 5x5 matrix of the newly created matrix
    """
    # Remove spaces, and replace "I" with "J", convert to uppercase
    matrix = []
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    # First fill matrix with letters from the key, skip over duplicate letters
    for char in key:
        if char not in matrix:
            matrix.append(char)
    # Then fill matrix with letters from the alphabet string
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
    # Reshape the matrix to 5x5
    matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    return matrix

def decrypt_message(matrix, message):
    """
    Function to use matrix to decode given message.
    @param matrix: Created playfair matrix 
    @param message: Encrypted message to decode
    @return: a decrypted message
    """
    text = ""
    message = filter_string(message)

    # iterate through the message by two, so that we can process it by pairs
    for i in range(0, len(message), 2):
        pair = message[i:i+2]
        # Get the (row, column) tuples for the first two chars
        first_char_pos = find_position(matrix, pair[0])
        second_char_pos = find_position(matrix, pair[1])
        # Case 1: if both characters appear in the same column, get letter above each one,
        # using modulo so that it takes value at the bottommost of the column if we are at the upmost row
        if first_char_pos[1] == second_char_pos[1]:
            text += matrix[(first_char_pos[0] - 1) % 5][first_char_pos[1]] + matrix[(second_char_pos[0] - 1) % 5][second_char_pos[1]]
        # Case 2: if both characters appear in the same row, get letter to the left of each,
        # using modulo to take value at the rightmost of the row if we are at the first column
        elif first_char_pos[0] == second_char_pos[0]:
            text += matrix[first_char_pos[0]][(first_char_pos[1] - 1) % 5] + matrix[second_char_pos[0]][(second_char_pos[1] - 1) % 5]
        # Case 3: if none of the above is true, form rectangle with two chars, and take value at opposite
        # ends of the rectangle
        else:
            text += matrix[first_char_pos[0]][second_char_pos[1]] + matrix[second_char_pos[0]][first_char_pos[1]]
    return text.replace('X', '').upper()

if __name__ == "__main__":
    key = "SUPERSPY"
    matrix = create_playfair_matrix(key)
    encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    decrypted_message = decrypt_message(matrix, encrypted_message)
    
    print(decrypted_message)
