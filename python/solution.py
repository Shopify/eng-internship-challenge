from typing import List, Dict
from constants.solution import ALPHABETS

def generate_playfair_matrix(key: str) -> List[List[str]]:
    """Generate a 5x5 matrix for the Playfair cipher.

    Args:
        key (str): The key to generate the matrix.

    Returns:
        List[List[str]]: A 5x5 matrix.
    """
    key = key.upper().replace('J', 'I')
    unique_chars = []

    for char in key + ALPHABETS:
        if char not in unique_chars:
            unique_chars.append(char)

    return [unique_chars[i:i + 5] for i in range(0, 25, 5)]

def decrypt_character_pair(matrix: List[List[str]], char1: str, char2: str, char_to_row: Dict[str, int], char_to_col: Dict[str, int]) -> str:
    """Decrypt a pair of characters using the Playfair cipher rules.

    Args:
        matrix (List[List[str]]): The matrix used to encrypt the text.
        char1 (str): The first character of the pair.
        char2 (str): The second character of the pair.
        char_to_row (Dict[str, int]): A dictionary mapping characters to their row positions in the matrix.
        char_to_col (Dict[str, int]): A dictionary mapping characters to their column positions in the matrix.

    Returns:
        str: The decrypted pair.
    """
    row1, col1 = char_to_row[char1], char_to_col[char1]
    row2, col2 = char_to_row[char2], char_to_col[char2]

    if row1 == row2:
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def decrypt_playfair_text(encrypted_text: str, matrix: List[List[str]]) -> str:
    """Decrypt a Playfair cipher.

    Args:
        encrypted_text (str): The encrypted text.
        matrix (List[List[str]]): The matrix used to encrypt the text.

    Returns:
        str: The decrypted text.
    """
    character_pairs = [encrypted_text[i:i + 2] for i in range(0, len(encrypted_text), 2)]
    
    # Precompute a character's row and column indices so we don't need to recompute it every time in decrypt_character_pair
    char_to_row: Dict[str, int] = {}  # char: row
    char_to_col: Dict[str, int] = {}  # char: col
    for row in range(5):
        for col in range(5):
            char_to_row[matrix[row][col]] = row
            char_to_col[matrix[row][col]] = col
    
    decrypted_text = ""
    for char1, char2 in character_pairs:
        decrypted_text += decrypt_character_pair(matrix, char1, char2, char_to_row, char_to_col)
            
    return decrypted_text.replace('X', '') 

def decrypt_playfair_cipher(ciphertext: str, key: str) -> str:
    """Main function to decrypt a Playfair cipher using the given key.

    Args:
        ciphertext (str): The encrypted text.
        key (str): The key to generate the matrix.

    Returns:
        str: The decrypted text.
    """
    playfair_matrix = generate_playfair_matrix(key)
    return decrypt_playfair_text(ciphertext, playfair_matrix)


ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
key = "SUPERSPY"

decrypted_message = decrypt_playfair_cipher(ciphertext, key)
print(decrypted_message)
