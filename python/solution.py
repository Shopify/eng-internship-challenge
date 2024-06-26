# alphabet defined with the omission of the letter J
alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

def createMatrix(keyword):
    """
    Generates 5x5 matrix based on a given keyword

    Args:
        keyword (str): keyword used to generate Playfair matrix

    Returns:
        list of lists (matrix): 5x5 matrix representing cipher matrix
    """
    # replace any instances of J with I and filter special characters
    keyword = ''.join(filter(str.isalpha, keyword.upper().replace('J', 'I')))
    used = set()
    matrix = []

    # populating the matrix with the keyword + no duplicate letters
    for char in keyword:
        if char not in used and char.isalpha():
            used.add(char)
            matrix.append(char)
    
    # adding the remaining alphabet to the matrix
    for char in alphabet:
        if char not in used:
            used.add(char)
            matrix.append(char)
    
    # return the list as a 5x5 matrix
    return [matrix[i*5: (i+1)*5] for i in range(5)]


def findPos(matrix, char):
    """
    Finds position (row, col) of a character in the cipher matrix

    Args:
        matrix (list of lists): cipher matrix
        char (str): character to be found in matrix

    Returns:
        tuple or None: if found, returns (row, column) of the character 
    """
    for row, line in enumerate(matrix):
        if char in line:
            return row, line.index(char)
    return None


def decryptPair(matrix, pair): 
    """
    Decrypts a pair of characters using cipher rules

    Args:
        matrix (list of lists): cipher matrix
        pair (str): pair of characters to be deciphered 

    Returns:
        str: the deciphered pair
    """
    row1, col1 = findPos(matrix, pair[0])
    row2, col2 = findPos(matrix, pair[1])

    if row1 == row2:
        return matrix[row1][(col1-1) % 5] + matrix[row2][(col2-1) % 5]
    elif col1 == col2:
        return matrix[(row1-1) % 5][col1] + matrix[(row2-1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]
    

def decipher(cipher, keyword):
    """
    Main decipher function where cipher message is decrypted using cipher rules

    Args:
        cipher (str): message to be deciphered
        keyword (str): keyword used to generate cipher matrix

    Returns:
        str: the deciphered message without any X's, spaces and special characters
    """
    # special characters in keyword or cipher message is filtered 
    keyword = ''.join(filter(str.isalpha, keyword.upper().replace('J', 'I')))
    cipher = ''.join(filter(str.isalpha, cipher.upper().replace('J', 'I')))
    matrix = createMatrix(keyword)
    message = []

    # decrypt message in pairs 
    for i in range(0, len(cipher), 2):
        cipherPair = cipher[i:i+2]
        message.append(decryptPair(matrix, cipherPair))

    # deciphered pairs are joined into a single string
    messageString = ''.join(message)
    
    # message is filtered to omit X and eliminate whitespaces
    filteredMessage = messageString.replace('X','').replace(' ','')

    return filteredMessage

def main():
    keyword = "SUPERSPY"
    cipher = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    message = decipher(cipher, keyword)
    print(message)

if __name__ == '__main__':
    main()