def decrypt_cipher(encrypted_phrase, key):
    '''
    This method decrypts the encrypted phrase by breaking the phrase into pairs and decrypting 
    each pair
    '''
    matrix = make_matrix(key) # Create the 5x5 matrix

    # Create an array which is the encrypted text broken into pairs
    pairs = [encrypted_phrase[i:i+2] for i in range(0, len(encrypted_phrase), 2)]
    
    decrypted_word = ""

    # Loop through each pair and decrypt it. Append the decrypted pair to the result string
    for i in pairs:
        decrypted_word += decrypt_two_letters(i, matrix)

    # Delete the X's which are used to complete pairs or split up repeating words
    decrypted_word = decrypted_word.replace("X", "")

    return decrypted_word

def make_matrix(key):
    '''
    This method creates the 5x5 matrix the cipher uses using the key.
    '''
    # Upper case key and removing "J" to fit alaphabet
    key = key.upper().replace("J", "")

    # Create a dictionary with the key letters first then the alphabet. This will remove duplicate letters 
    matrix_letters = "".join(dict.fromkeys(key + "ABCDEFGHIKLMNOPQRSTUVWXYZ"))

    # Create 5x5 matrix and populating with the matrix letters
    matrix = [list(matrix_letters[i:i+5]) for i in range(0, 25, 5)]
    
    return matrix

def decrypt_two_letters(pair, matrix):
    '''
    This method determines which rule to use when decrypting the pair, then returning the
    decrypted method.
    '''
    # Unpack the row and column of the letters
    row1, col1 = find_coordinates(pair[0], matrix)
    row2, col2 = find_coordinates(pair[1], matrix)

    # Letters are in the same row
    if row1 == row2:
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    # Letters are in the same column
    elif col1 == col2:
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2] 
    # If letters are not in same row or column, preform the rectange method
    else:
        return matrix[row1][col2] + matrix[row2][col1] 

def find_coordinates(letter, matrix):
    '''
    This method finds the row and column of a letter in the matrix.
    '''

    # Loop through every letter until the correct one is found
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == letter:
                return [row, col]


if __name__ == "__main__":
    print(decrypt_cipher("IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV", "SUPERSPY"))