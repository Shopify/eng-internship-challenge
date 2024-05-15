# Brittaney Nicole Davis (Nico)
# 5/14/2024
# Shopify Internship Challenge

# a function for creating the matrix
def create_matrix(passkey):
    """
    A function which builds the
    matrix by utilizing the given
    keyword in a 5x5 fashion.
    Returns the matrix as a list.
    """

    matrix = []

    passkey = passkey.replace('J', 'I')

    # build matrix in steps of 5 for 25 total spaces
    for i in range(0, len(passkey), 5):
        matrix.append(passkey[i:i + 5])

    return matrix


keyword = "SUPERSPY"
matrix_result = [
    ['S', 'U', 'P', 'E', 'R'],
    ['P', 'Y', 'A', 'B', 'C']
]

assert create_matrix(keyword) == matrix_result


# a function for decryption
def decrypt_message(message, matrix):
    """
    A function which decrypts
    a given message, utilizing the
    matrix position in pairs via indexing.
    Returns the message as a string.
    """

    pass


# a function for determining the position
def matrix_position(matrix):
    """
    A function to determine
    the position within the matrix,
    utilizing a map of rows and columns.
    Returns a dictionary of the map.
    """

    pass
