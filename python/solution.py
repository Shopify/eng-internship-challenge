import sys

def create_matrix_lookup(keyword):
    """
    Create a 5x5 matrix and a lookup table for the Playfair cipher.

    Parameters:
    keyword (str): The keyword provided along with the ciphertext.

    Returns:
    tuple: A tuple containing a 5x5 matrix for solving the cipher and a lookup table, 
           which is used to find the position of a char in the matrix in constant time.
    """


    def matrix_append(char):
        """
        Append a character to the matrix and update the lookup table.

        Parameters:
        char (str): The character to append to the matrix.

        Does not return a value, but mutates the matrix and lookup table.
        """
        nonlocal cur_row
        if len(matrix[cur_row]) == 5:
            matrix.append([])
            cur_row += 1

        matrix[cur_row].append(char)
        lookup[char] = (cur_row, len(matrix[cur_row])-1)


    keyword = keyword.upper()
    matrix = [[]]
    lookup = {}
    cur_row = 0

    for char in keyword:
        if char not in lookup and char != 'J':
            matrix_append(char)

        # Break early if we have all the letters in the alphabet
        if len(lookup) == 25:
            break

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in lookup:
            matrix_append(char)

        if len(lookup) == 25:
            break
            
    return matrix, lookup


def playfair_cipher(text, keyword) -> str:
    """
    Decipher a given text using the Playfair cipher with a given keyword.

    Parameters:
    text (str): The text to decipher.
    keyword (str): The keyword provided along with the ciphertext.

    Returns:
    str: The deciphered text. It must be all uppercase and contain no spaces, X's, or special characters.

    Assumptions:
    - The input text does not contain spaces or special characters.
    - We are deciphering using the convention that 'I' and 'J' are merged within the 5x5 matrix,
      thus any J's in an original text will be deciphered into I.
    """
    result = ""

    text = text.upper()
    matrix, lookup = create_matrix_lookup(keyword)

    for i in range(0, len(text), 2):
        char_1 = text[i]
        char_2 = text[i+1] if i+1 < len(text) else 'X'

        row_1, col_1 = lookup[char_1]
        row_2, col_2 = lookup[char_2]

        new_char_1 = ''
        new_char_2 = ''

        # Decode
        if row_1 == row_2:
            new_char_1 = matrix[row_1][(col_1-1)]
            new_char_2 = matrix[row_2][(col_2-1)]
        elif col_1 == col_2:
            new_char_1 = matrix[(row_1-1)][col_1]
            new_char_2 = matrix[(row_2-1)][col_2]
        else:
            new_char_1 = matrix[row_1][col_2]
            new_char_2 = matrix[row_2][col_1]

        if new_char_1 != 'X':
            result += new_char_1
        if new_char_2 != 'X':
            result += new_char_2

    return result
    
def __main__():
    # Allow for command line arguments when testing from additionaltests.test.py
    if len(sys.argv) == 3:
        print(playfair_cipher(sys.argv[1], sys.argv[2]))
    # Default test
    else:
        print(playfair_cipher("IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV", "SUPERSPY"))

if __name__ == "__main__":
    __main__()