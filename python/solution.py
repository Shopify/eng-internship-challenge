def playfair_matrix(key):
    """
    Generate the playfair matrix, replacing J with I
    key: The secret to key to create the matrix
    The filtered key without the recurring letters and playfair cypher matrix are returned. 
    """
    # Create empty matrix
    matrix = [['' for _ in range(5)] for _ in range(5)]

    #Convert to upper,
    key = key.upper().replace("J","I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    addedletters = set()
    # Convert key to be an array with the letters in order, to eventually add to the matrix
    convertedkey=[]
    for letter in key:
        if letter not in addedletters and letter in alphabet:
            addedletters.add(letter)
            convertedkey.append(letter)
    for char in alphabet:
        if char not in addedletters:
            convertedkey.append(char)
            addedletters.add(char)
    keyindex=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j]=convertedkey[keyindex]
            keyindex+=1
    return matrix

def decrypt(key, ciphertext):
    """
    Uses the playfair matrix to decrypt the ciphertext given the key
    key: a key used to create the matrix
    ciphertext: The text to be decoded
    """
    matrix = playfair_matrix(key)
    plaintext = []
    letter_to_matrix_position = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            letter_to_matrix_position[matrix[i][j]]=[i,j]

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    
    # Remove spaces and special characters in the ciphertext
    ciphertext = ciphertext.upper()
    ciphertext = [letter for letter in ciphertext if letter in alphabet]

    # Append the uncommon letter X at the end if odd so the ciphertext is even
    if len(ciphertext) % 2 != 0:
        ciphertext.append('X')

    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i+1]
        row_first, col_first = letter_to_matrix_position[char1]
        row_second, col_second = letter_to_matrix_position[char2]
        # We add the next letter to the ciphertext depending on if it's a row, column or rectangle
        if row_first == row_second:
            plaintext.append(matrix[row_first][(col_first - 1) % 5] + matrix[row_second][(col_second - 1) % 5])
        elif col_first == col_second:
            plaintext.append(matrix[(row_first - 1) % 5][col_first] + matrix[(row_second - 1) % 5][col_second])
        else:
            plaintext.append(matrix[row_first][col_second] + matrix[row_second][col_first])
    return ''.join(plaintext).replace("X","")

if __name__ == "__main__":
    key = "SUPERSPY"
    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

    #Decrypt into the plaintext given the key and ciphertext
    plaintext = decrypt(key, ciphertext)
    print(plaintext)