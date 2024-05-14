def matrix(key):
    #Ensure key is in upper case and replace all 'J' with 'I'
    key = key.upper()
    key = key.replace("J","I")

    #Create alphabet without 'J' and empty list
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []

    #Iterate through each character in key and append to matrix only if it is already not in the list
    for char in key:
        if char not in matrix:
            matrix.append(char)

    #Iterate through each character in alphabet and append to matrix only if it is already not in the list
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)

    #Create a 5x5 grid using matrix
    playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    return playfair_matrix

def position(matrix, char):
    #Iterate through each row in the matrix alongside the index
    for i, row in enumerate(matrix):
        #If character is in the row, return the index of the row and it's index within the row
        if char in row:
            return i, row.index(char)

def decrypt(encrypted_text, key):
    #Create 5x5 grid using key
    key_matrix = matrix(key)
    #Ensure encrypted text is all in upper case
    encrypted_text = encrypted_text.upper()
    #Create empty decrypted text
    decrypted_text = ""

    #Iterate through the encrypted text 2 characters at a time
    for i in range(0, len(encrypted_text), 2):
        #Store two characters in c1 and c2 respectively from encrypted text
        c1 = encrypted_text[i]
        c2 = encrypted_text[i + 1]
        #Get row and columns of c1 and c2 in the key matrix
        row1, col1 = position(key_matrix, c1)
        row2, col2 = position(key_matrix, c2)

        #If c1 and c2 are in the same row, take the letter to the left of each one, wrapping if necessary
        if row1 == row2:
            decrypted_text += key_matrix[row1][(col1 - 1) % 5] + key_matrix[row1][(col2 - 1) % 5]
        #If c1 and c2 are in the same column, take the letter above each one, wrapping if necessary
        elif col1 == col2: 
            decrypted_text += key_matrix[(row1 - 1) % 5][col1] + key_matrix[(row2 - 1) % 5][col2]
        #If neither are true, create a rectangle with the two letters and take the letters on the horizontal opposite corners
        else: 
            decrypted_text += key_matrix[row1][col2] + key_matrix[row2][col1]

    #Remove all 'X' characters before returning
    return decrypted_text.replace("X", "")

encrypted_text = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
key = "SUPERSPY"
decrypted_text = decrypt(encrypted_text, key)
print(decrypted_text)
