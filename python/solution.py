# Brittaney Nicole Davis (Nico)
# 5/14/2024
# Shopify Internship Challenge

# --------------------------------
# matrix creation
# --------------------------------
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
    for cell in range(0, len(passkey), 5):
        matrix.append(list(passkey[cell:cell + 5]))

    return matrix


# keyword = "SUPERSPY"
# matrix_result = [
#     ['S', 'U', 'P', 'E', 'R'],
#     ['S', 'P', 'Y']
# ]
#
# real_matrix = create_matrix(keyword)
#
# print("real:")
# for row in real_matrix:
#     print(row)
#
# print("expected:")
# for row in matrix_result:
#     print(row)
#
# assert create_matrix(keyword) == matrix_result

# --------------------------------
# decryption
# --------------------------------
def decrypt_message(message, matrix):
    """
    A function which decrypts
    a given message, utilizing the
    matrix position in pairs via indexing.
    Returns the message as a string.
    """

    pass


# --------------------------------
# position handling
# --------------------------------
def matrix_position(matrix):
    """
    A function to determine
    the position within the matrix,
    utilizing a map of rows and columns.
    Returns a dictionary of the map.
    """

    position_dict = {}

    # establish rows and columns via
    matrix_rows = len(matrix)
    matrix_columns = len(matrix[0])

    # map matrix position via character(s)
    for i in range(matrix_rows):
        for j in range(matrix_columns):
            letter = matrix[i][j]
            position_dict[letter] = (i, j)

    return position_dict


# test_matrix = [
#     ['A', 'B', 'C', 'D', 'E'],
#     ['F', 'G', 'H', 'I', 'K'],
#     ['L', 'M', 'N', 'O', 'P'],
#     ['Q', 'R', 'S', 'T', 'U'],
#     ['V', 'W', 'X', 'Y', 'Z']
# ]
#
# position_result = {'A': (0, 0), 'B': (0, 1), 'C': (0, 2), 'D': (0, 3), 'E': (0, 4),
#                    'F': (1, 0), 'G': (1, 1), 'H': (1, 2), 'I': (1, 3), 'K': (1, 4),
#                    'L': (2, 0), 'M': (2, 1), 'N': (2, 2), 'O': (2, 3), 'P': (2, 4),
#                    'Q': (3, 0), 'R': (3, 1), 'S': (3, 2), 'T': (3, 3), 'U': (3, 4),
#                    'V': (4, 0), 'W': (4, 1), 'X': (4, 2), 'Y': (4, 3), 'Z': (4, 4)}
#
# real_matrix = matrix_position(test_matrix)
#
# print("real:")
# for row in real_matrix:
#     print(row)
#
# print("expected:")
# for row in position_result:
#     print(row)
#
# assert real_matrix == position_result
#
# print("real vs expected:")
# for key in sorted(real_matrix.keys()):
#     print(f"{key}: {real_matrix[key]} vs {position_result[key]}")
