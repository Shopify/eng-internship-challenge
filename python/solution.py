from typing import List, Dict, Tuple

ENCRYPTED_MSG = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
CIPHER_KEY = "SUPERSPY"

def playfair_cipher() -> None:
    # Create the cipher table based off given key
    cipher_table = create_cipher_table(CIPHER_KEY)
    letter_map = map_char_to_table_position(cipher_table)
    digrams = split_into_digrams(ENCRYPTED_MSG)
    decrypted_message = decrypt_digrams(digrams, letter_map, cipher_table)
    
    print(f"{decrypted_message}")

def create_cipher_table(key: str) -> List[List[str]]:
    ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ" # exclude J; it is interchangeable with I
    cipher_table = []
    used_letters = set()
    
    # Add letters from the cipher key into the table first
    for letter in key:
        if letter not in used_letters:
            cipher_table.append(letter)
            used_letters.add(letter)
        
    # Add remaining unique letters from alphabet to complete table
    for letter in ALPHABET:
        if letter not in used_letters:
            cipher_table.append(letter)
            used_letters.add(letter)
    
    # Reshape into 5x5 matrix
    cipher_table = [cipher_table[i:i+5] for i in range(0, len(cipher_table), 5)]
    
    return cipher_table

def map_char_to_table_position(table: List[List[str]]) -> Dict[str, Tuple[int, int]]:
    letter_to_position = {}
    
    for i, row in enumerate(table):
        for j, letter in enumerate(row):
            letter_to_position[letter] = (i, j)
            
    return letter_to_position

def split_into_digrams(message: str) -> List[str]:
    """
    Split the message into digrams (pairs of two letters).
    """
    digrams = []
    i = 0
    
    while i < len(message):
        if i + 1 < len(message):
            digram = message[i:i+2]
            digrams.append(digram)
            i += 2 # Step by 2 since we process 2 letters at a time
        else:
            # Handle edge case where message has odd number of letters, should the encrypted message be odd
            # Pad the last letter with an 'X' to maintain digram structure
            digram = message[i] + "X"
            digrams.append(message[i] + "X")
            i += 1 # Step by 1 since we processed the last letter

    return digrams
    
def decrypt_digrams(digrams: List[str], letter_map: Dict[str, Tuple[int, int]], cipher_table: List[List[str]]) -> str:
    decrypted_message = []
    
    for digram in digrams:
        letter_1 = digram[0]
        letter_2 = digram[1]
        
        # Positions of the letters in the cipher table, using tuple unpacking
        letter_1_row, letter_1_col = letter_map[letter_1]
        letter_2_row, letter_2_col = letter_map[letter_2]
        
        # Process the letters based on their positions in the table
        if letter_1_row == letter_2_row:
            decrypted_message.append(process_letter_in_same_row(letter_1_row, letter_1_col, letter_2_col, cipher_table))
        elif letter_1_col == letter_2_col:
            decrypted_message.append(process_letter_in_same_col(letter_1_col, letter_1_row, letter_2_row, cipher_table))
        else:
            decrypted_message.append(process_letter_as_rectangle(letter_1_row, letter_1_col, letter_2_row, letter_2_col, cipher_table))
    
    raw_decrypted_message = "".join(decrypted_message)
    clean_message = raw_decrypted_message.replace("X", "")
    
    return clean_message

def process_letter_in_same_row(row: int, col_1: int, col_2: int, cipher_table: List[List[str]]) -> str:
    # If the letters are in the same row, shift them to the left (decryption), wrap to the right if needed:
    decoded_letter_1 = ""
    decoded_letter_2 = ""
    
    if col_1 == 0:
        # Wrap to the right
        decoded_letter_1 = cipher_table[row][4]
    else:
        decoded_letter_1 = cipher_table[row][col_1 - 1]
        
    if col_2 == 0:
        # Wrap to the right
        decoded_letter_2 = cipher_table[row][4]
    else:
        decoded_letter_2 = cipher_table[row][col_2 - 1]
    
    return decoded_letter_1 + decoded_letter_2

def process_letter_in_same_col(col: int, row_1: int, row_2: int, cipher_table: List[List[str]]) -> str:
    # If the letters are in the same column, shift them up (decryption), wrap to the bottom if needed
    decoded_letter_1 = ""
    decoded_letter_2 = ""
    
    if row_1 == 0:
        # Wrap to the bottom
        decoded_letter_1 = cipher_table[4][col]
    else:
        decoded_letter_1 = cipher_table[row_1 - 1][col]
    if row_2 == 0:
        # Wrap to the bottom
        decoded_letter_2 = cipher_table[4][col]
    else:
        decoded_letter_2 = cipher_table[row_2 - 1][col]
    
    return decoded_letter_1 + decoded_letter_2

def process_letter_as_rectangle(row_1: int, col_1: int, row_2: int, col_2: int, cipher_table: List[List[str]]) -> str:
    # If the letters are in different rows and columns, eg a rectangle, decrypt them by swapping the columns
    decoded_letter_1 = cipher_table[row_1][col_2]
    decoded_letter_2 = cipher_table[row_2][col_1]
    
    return decoded_letter_1 + decoded_letter_2

if __name__ == "__main__":
    playfair_cipher()
