import string
from typing import List, Tuple, Set

MATRIX_SIZE = 5
OMITTED_LETTER = 'J'
PADDING_LETTER = 'X'
CIPHERTEXT = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'
KEY = 'SUPERSPY'

def sanitize_input(s: str) -> str:
    if not s.isalpha() or not s.isupper():
        raise ValueError("String must be uppercase and contain only alphabetic characters.")
    return s

def deduplicate(s: str) -> str:
    seen = set()
    return ''.join([x for x in s if not (x in seen or seen.add(x))])

def find_remaining_letters(key: str) -> str:
    return ''.join(sorted(set(string.ascii_uppercase) - set(key + OMITTED_LETTER)))

def construct_matrix(key: str) -> List[List[str]]:
    full_key = deduplicate(sanitize_input(key))
    remaining_letters = find_remaining_letters(full_key)
    matrix_content = full_key + remaining_letters
    return [list(matrix_content[i * MATRIX_SIZE:(i + 1) * MATRIX_SIZE]) for i in range(MATRIX_SIZE)]

def locate_letter(letter: str, matrix: List[List[str]]) -> Tuple[int, int]:
    for r in range(MATRIX_SIZE):
        for c in range(MATRIX_SIZE):
            if matrix[r][c] == letter:
                return r, c
    return -1, -1

def playfair_decrypt(ciphertext: str, key: str) -> str:
    ciphertext = sanitize_input(ciphertext)
    if len(ciphertext) % 2 != 0:
        ciphertext += PADDING_LETTER
    matrix = construct_matrix(key)
    plaintext = []

    for i in range(0, len(ciphertext), 2):
        x1, y1 = locate_letter(ciphertext[i], matrix)
        x2, y2 = locate_letter(ciphertext[i + 1], matrix)

        if x1 == x2:
            plaintext.extend([matrix[x1][(y1 - 1) % MATRIX_SIZE], matrix[x2][(y2 - 1) % MATRIX_SIZE]]) # letters are in the same row -> shift left by 1
        elif y1 == y2:
            plaintext.extend([matrix[(x1 - 1) % MATRIX_SIZE][y1], matrix[(x2 - 1) % MATRIX_SIZE][y2]]) # if letters are in the same column -> shift up by 1
        else:
            plaintext.extend([matrix[x1][y2], matrix[x2][y1]])

    return ''.join(plaintext).replace(PADDING_LETTER, '')

decrypted_text = playfair_decrypt(CIPHERTEXT, KEY)
print(decrypted_text)
