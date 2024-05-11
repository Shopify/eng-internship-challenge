def generate_key_table(key):
    """
    Function to generate a 5x5 Playfair matrix from the given secret key
    @param key: the secret key string used to construct the array
    @return: the newly created 5x5 matrix as a List[List[str]]
    """

    # convert key to uppercase and replace "J" with "I"
    key = key.upper().replace("J", "I")

    # remove spaces from string
    key = key.replace(" ", "")

    # remove duplicates and special characters from key
    keyNoDuplicates = []
    for letter in key:
        if letter not in keyNoDuplicates and letter.isalpha():
            keyNoDuplicates.append(letter)
    
    # alphabet string without J
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    # matrix input string with cleaned key and alphabet 
    matrixInput = keyNoDuplicates

    for letter in alphabet:
        if letter not in matrixInput:
            matrixInput.append(letter)
    
    # generate 5x5 matrix
    matrix = []
    for i in range(0, 25, 5):
        matrix.append(matrixInput[i:i + 5])

    return matrix

def decrypt_pair(pair, matrix, coordinates):
    """
    Function that decrypts a pair of letters using the given Playfair matrix
    @param pair: pair of letters to decrypt
    @param matrix: Playfair matrix used to decrypt the letter pair
    @param coordinates: dictionary of letter coordinates in the matrix 
    @return: decrypted pair of letters as a string
    """

    # get coordinates of letters in pair
    pos1, pos2 = coordinates[pair[0]], coordinates[pair[1]]
    
    # if letters are in the same row of the matrix, replace them with letters to their immediate left
    # wrap around to the right side of the row if a letter in the pair was on the very left of a row
    if pos1[0] == pos2[0]: 
        row = pos1[0]
        new_pos1 = (row, (pos1[1] - 1) % 5)
        new_pos2 = (row, (pos2[1] - 1) % 5)
    # if letters are in the same column of the matrix, replace them with letters immediately above
    # wrap around to the bottom side of the column if a letter in the pair was on top of a column
    elif pos1[1] == pos2[1]:  
        col = pos1[1]
        new_pos1 = ((pos1[0] - 1) % 5, col)
        new_pos2 = ((pos2[0] - 1) % 5, col)
    # if letters are not in the same row or column, swap the first coordinate of each to get the 
    # letters on the same row but at column positions of the other character in the pair
    else:  
        new_pos1 = (pos1[0], pos2[1])
        new_pos2 = (pos2[0], pos1[1])

    # get the letters from the new positions
    decrypted_pair = matrix[new_pos1[0]][new_pos1[1]] + matrix[new_pos2[0]][new_pos2[1]]
    return decrypted_pair

def decrypt_message(matrix, encrypted_message):
    """
    Function that uses given Playfair matrix to decode the encrypted message
    @param matrix: Playfair matrix used to encrypt the message
    @param encrypted_message: encrypted message as string to decrypt
    @return: decrypted message as a string
    """

    # remove any spaces from the encrypted message
    encrypted_message = encrypted_message.replace(" ", "")

    # create map of letter coordinates in key matrix
    coordinates = {}
    for x, row in enumerate(matrix):
        for y, letter in enumerate(row):
            coordinates[letter] = (x, y) 
    
    # split encrypted_message into pairs (digrams)
    pairs = [encrypted_message[i:i+2] for i in range(0, len(encrypted_message), 2)]

    # decrypt each pair
    decrypted_message = ''
    for pair in pairs:
        decrypted_message += decrypt_pair(pair, matrix, coordinates)
    
    # remove X's from decrypted_message
    decrypted_message = decrypted_message.replace("X", "")

    return decrypted_message
    

if __name__ == '__main__':
    """
    main function to decrypt the secret message
    """

    key = "SUPERSPY"
    encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    matrix = generate_key_table(key)
    answer = decrypt_message(matrix, encrypted_message)
    print(answer)

    