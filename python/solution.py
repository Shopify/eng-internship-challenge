import string
from typing import List, Set, Tuple

ROWS = 5
COLUMNS = 5
# The key table is 5x5, so one of the 26 letters in the alphabet must be omitted, typically 'J'
omitted_letter = 'J'
# The ciphertext is decoded in pairs, so if the ciphertext has an odd length, it must be padded to an even length
padding_letter = 'X'
given_ciphertext = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'
given_key = 'SUPERSPY'


def validate_input(s: str) -> str:
    """
    Ensures the input string is in uppercase and contains only alphabetical characters.
    Throws a ValueError if the input is not valid.
    """
    if not s.isalpha() or not s.isupper():
        raise ValueError("Input must be uppercase and contain only alphabetic characters.")
    return s


def remove_duplicates(s: str) -> str:
    """
    Removes duplicate characters from the given string and returns a new string
    consisting only of the unique characters, maintaining their original order.
    """
    seen: Set[str] = set()
    unique_string: List[str] = []
    for char in s:
        if char not in seen:
            unique_string.append(char)
            seen.add(char)
    return ''.join(unique_string)


def get_missing_letters(key: str) -> List[str]:
    """
    Creates a sorted list of the alphabet letters excluding letters in the key and the chosen omitted letter.
    """
    all_letters: Set[str] = set(string.ascii_uppercase)
    excluded: Set[str] = set(key + omitted_letter)
    return sorted(all_letters - excluded)


def create_matrix(key: str) -> List[List[str]]:
    """
    Creates a 5x5 key matrix for the Playfair cipher.
    """
    grid: List[List[str]] = []
    index = 0
    unique_key = remove_duplicates(key)
    missing_letters = get_missing_letters(unique_key)
    all_letters = unique_key + ''.join(missing_letters)

    for i in range(ROWS):
        row: List[str] = []
        for j in range(COLUMNS):
            row.append(all_letters[index])
            index += 1
        grid.append(row)
    return grid


def find_position(letter: str, matrix: List[List[str]]) -> Tuple[int, int]:
    """
    Finds the position of a letter in the matrix.
    """
    for i in range(ROWS):
        for j in range(COLUMNS):
            if matrix[i][j] == letter:
                return i, j
    return -1, -1  # letter not found


def decrypt(ciphertext: str, key) -> str:
    """
    Decrypts a ciphertext encrypted with the Playfair cipher using a predefined key.
    """
    ciphertext = validate_input(ciphertext)
    matrix = create_matrix(validate_input(key))
    plaintext: List[str] = []

    if len(ciphertext) % 2 != 0:
        ciphertext += padding_letter

    for index in range(0, len(ciphertext), 2):
        char1 = ciphertext[index]
        char2 = ciphertext[index + 1]
        char1_row, char1_col = find_position(char1, matrix)
        char2_row, char2_col = find_position(char2, matrix)

        if char1_row == char2_row:
            # letters appear on the same row, shift left by 1
            plaintext.append(matrix[char1_row][(char1_col - 1) % COLUMNS])
            plaintext.append(matrix[char2_row][(char2_col - 1) % COLUMNS])
        elif char1_col == char2_col:
            # letters appear in the same column, shift up by 1
            plaintext.append(matrix[(char1_row - 1) % ROWS][char1_col])
            plaintext.append(matrix[(char2_row - 1) % ROWS][char2_col])
        else:
            plaintext.append(matrix[char1_row][char2_col])
            plaintext.append(matrix[char2_row][char1_col])

    return ''.join(plaintext).replace('X', '')


print(decrypt(given_ciphertext, given_key))
