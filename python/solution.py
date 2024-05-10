from string import ascii_uppercase
from collections import defaultdict
from typing import List, Dict, Tuple

def remove_duplicates(message: str) -> List[str]:
    """
    Remove duplicates from a message and return a list of unique letters.

    Parameters:
        message (str): The input message from which duplicates are to be removed.

    Returns:
        List[str]: A list of unique letters without duplicates.
    """
    letter_set: set[str] = set()
    result: List[str] = []
    for letter in message:
        if letter not in letter_set:
            result.append(letter)
            letter_set.add(letter)
    return result

def create_playfair_array(key_string: str) -> List[List[str]]:
    """
    Create a 5x5 Playfair array from a key string.

    Parameters:
        key_string (str): The key string to construct the Playfair array.

    Returns:
        List[List[str]]: A 5x5 Playfair array.
    """
    sorted_key_without_duplicates: List[str] = remove_duplicates(key_string)
    sorted_alphabet_uppercase: set[str] = set(ascii_uppercase)
    sorted_alphabet_uppercase.remove("J")

    for letter in sorted_key_without_duplicates:
        if letter in sorted_alphabet_uppercase:
            sorted_alphabet_uppercase.remove(letter)

    size_of_key: int = len(sorted_key_without_duplicates)
    DIMENSION: int = 5
    letter_array: List[List[str]] = [["0"] * DIMENSION for _ in range(DIMENSION)]

    for i in range(size_of_key):
        row: int = i // DIMENSION
        col: int = i % DIMENSION
        letter_array[row][col] = sorted_key_without_duplicates[i]

    sorted_alphabet_uppercase = list(sorted_alphabet_uppercase)
    sorted_alphabet_uppercase.sort()

    for i in range(size_of_key, DIMENSION * DIMENSION):
        row: int = i // DIMENSION
        col: int = i % DIMENSION
        letter_array[row][col] = sorted_alphabet_uppercase[i - size_of_key]

    return letter_array

def create_letter_map(letter_array: List[List[str]]) -> Dict[str, Tuple[int, int]]:
    """
    Create a mapping of letters to their coordinates in the Playfair array.

    Parameters:
        letter_array (List[List[str]]): The Playfair array.

    Returns:
        Dict[str, Tuple[int, int]]: A dictionary mapping each letter to its coordinates (row, column) in the array.
    """
    letter_map: Dict[str, Tuple[int, int]] = defaultdict(tuple)
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            letter: str = letter_array[i][j]
            letter_map[letter] = (i, j)
    return letter_map

def decrypt_message(encrypted_message: str, letter_map: Dict[str, Tuple[int, int]], playfair_array: List[List[str]]) -> str:
    """
    Decrypt the encrypted message using the Playfair array and letter map.

    Parameters:
        encrypted_message (str): The encrypted message to be decrypted.
        letter_map (Dict[str, Tuple[int, int]]): The mapping of letters to their coordinates in the Playfair array.
        playfair_array (List[List[str]]): The Playfair array used for decryption.

    Returns:
        str: The decrypted message.
    """
    decrypted_message: str = ""
    i: int = 0
    while i < len(encrypted_message):
        letter1: str = encrypted_message[i]
        if i + 1 < len(encrypted_message):
            letter2: str = encrypted_message[i + 1]
        else:
            letter2: str = 'X'

        x_coord1, y_coord1 = letter_map[letter1]
        x_coord2, y_coord2 = letter_map[letter2]

        if x_coord1 == x_coord2:
            if y_coord1 == 0:
                y_coord1 = DIMENSION - 1
            else:
                y_coord1 -= 1
            if y_coord2 == 0:
                y_coord2 = DIMENSION - 1
            else:
                y_coord2 -= 1
        elif y_coord1 == y_coord2:
            if x_coord1 == 0:
                x_coord1 = DIMENSION - 1
            else:
                x_coord1 -= 1
            if x_coord2 == 0:
                x_coord2 = DIMENSION - 1
            else:
                x_coord2 -= 1
        else:
            y_coord1, y_coord2 = y_coord2, y_coord1

        decrypted_message += playfair_array[x_coord1][y_coord1]
        decrypted_message += playfair_array[x_coord2][y_coord2]

        i += 2

    # Remove any extra "X"s that were added during encryption
    decrypted_message = decrypted_message.replace("X", "").upper()
    return decrypted_message

# The encrypted message received from the agent
ENCRYPTED_MESSAGE: str = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

# The key string provided by the agent
KEY_STRING: str = "SUPERSPY"

# The dimension of the Playfair array (5x5 in this case)
DIMENSION: int = 5

def main() -> None:
    """
    Main function to decrypt the message.
    """
    playfair_array: List[List[str]] = create_playfair_array(KEY_STRING)
    letter_map: Dict[str, Tuple[int, int]] = create_letter_map(playfair_array)
    decrypted_message: str = decrypt_message(ENCRYPTED_MESSAGE, letter_map, playfair_array)
    print(decrypted_message)

if __name__ == "__main__":
    main()
