# Brittaney Nicole Davis (Nico)
# 5/14/2024
# Technical Assessment Challenge - Playfair Cipher Solver

import string
import unittest


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

    for x in range(5):
        row = ['' for x in range(5)]
        matrix.append(row)

    passkey = passkey.replace('J', 'I')

    # begin adding chars to matrix
    used_chars = set()
    row, col = 0, 0

    for char in passkey:
        if char not in used_chars:
            matrix[row][col] = char
            used_chars.add(char)
            col += 1
            if col == 5:
                col = 0
                row += 1

    # add remaining chars
    for char in string.ascii_uppercase:
        if char != 'J' and char not in used_chars:
            matrix[row][col] = char
            used_chars.add(char)
            col += 1
            if col == 5:
                col = 0
                row += 1

    return matrix


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

    decrypted = []
    msg_upper = ""

    # sift for letters only, then set to upper
    for letter in message:
        if letter.isalpha():
            msg_upper += letter.upper()

    # set original message to uppercase version
    message = msg_upper

    position_dict = matrix_position(matrix)

    # obtain character pairs
    for i in range(0, len(message), 2):
        char_1 = message[i]
        char_2 = message[i + 1]

        row_1, col_1 = position_dict[char_1]
        row_2, col_2 = position_dict[char_2]

        if row_1 == row_2:
            decrypted.append(matrix[row_1][(col_1 - 1) % 5])
            decrypted.append(matrix[row_2][(col_2 - 1) % 5])
        elif col_1 == col_2:
            decrypted.append(matrix[(row_1 - 1) % 5][col_1])
            decrypted.append(matrix[(row_2 - 1) % 5][col_2])
        else:
            decrypted.append(matrix[row_1][col_2])
            decrypted.append(matrix[row_2][col_1])

    return ''.join(decrypted)


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

    # establish rows and columns via length
    matrix_rows = len(matrix)
    matrix_columns = len(matrix[0])

    # map matrix position via character(s)
    for i in range(matrix_rows):
        for j in range(matrix_columns):
            letter = matrix[i][j]
            position_dict[letter] = (i, j)

    # map each letter to the proper position
    for letter in string.ascii_uppercase:
        if letter != 'J' and letter not in position_dict:
            position_dict[letter] = (-1, -1)

    return position_dict
