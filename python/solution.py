# ASSUMPTION: THE MATRIX FOR THE KEY IS ALREADY CREATED AND THIS APPLICATION WORKS TO SOLVE CIPHERS WITH THIS SPECIFIC SUPER KEY

# Secret key without duplicates: SUPERSPY -> SUPERY, then add all remaining letters to matrix with i represent i/j
matrix = [
    ['S', 'U', 'P', 'E', 'R'],
    ['Y', 'A', 'B', 'C', 'D'],
    ['F', 'G', 'H', 'I', 'K'],
    ['L', 'M', 'N', 'O', 'Q'],
    ['T', 'V', 'W', 'X', 'Z']
]

ciphertext = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'

def decrypt(ciphertext, matrix):

    digraphs = []
    plaintext = ''

    # creating the digraphs
    for i in range(0, len(ciphertext), 2):
        digraphs.append(ciphertext[i:i+2])

    # decrypting each one individually
    for element in digraphs:
        plaintext += decryptPiece(matrix, element)

    # filtering out the x's using a comprehension
    newcipher = "".join([char for char in plaintext if char != 'X'])
    return newcipher



def decryptPiece(matrix, digraph):


    # getting locations of the respective cols and rows
    crow1, ccol1 = location(matrix, digraph[0])
    crow2, ccol2 = location(matrix, digraph[1])


    # 3 cases: same row, same column, same rectangle


    # same row, take the one to the left
    if crow1 == crow2:
        return matrix[crow1][(ccol1 - 1) % 5] + matrix[crow2][(ccol2 - 1) % 5]
    # same col, take up
    elif ccol1 == ccol2:
        return matrix[(crow1 - 1) % 5][ccol1] + matrix[(crow2 - 1) % 5][ccol2]
    else:
        # flip
        return matrix[crow1][ccol2] + matrix[crow2][ccol1]






def location(matrix, char):

    # function to get location of each character, J and I are substitutable
    if char == 'J':
        char = 'I'

    # search
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None



print(decrypt(ciphertext, matrix))