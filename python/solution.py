
from typing import Dict, List, Tuple

# Generate Polybius Square from key given (probably unnecessary, since task only requires to decrypt one key message pair, but why not?)
# We return the square in array form, so we can access the CHAR from (row, col) in O(1)
# We also return the square in dict form, so we can access the (row, col) from CHAR in O(1)
def generate_polybius_square(key: str)-> Tuple[List[List[str]], Dict[str, Tuple[int, int]]]:
    polybius_square = [[0,0,0,0,0] for _ in range(5)]
    polybius_square_map = {}
    pos = 0

    def fillSquare(char, pos):
        row = pos // 5
        col = pos % 5
        # Handle special case of I & J
        if char == "I" or char == "J":
            polybius_square[row][col] = "IJ"
            polybius_square_map["I"] = (row, col)
            polybius_square_map["J"] = (row, col)
        else:
            polybius_square[row][col] = char
            polybius_square_map[char] = (row, col)

    # Fill out characters from key
    for char in key:
        if char in polybius_square_map:
            continue

        fillSquare(char, pos)
        pos += 1

    # Fill up remaining alphabest
    for unicode_char in range(65, 65 + 26):
        char = chr(unicode_char)
        if char in polybius_square_map:
            continue

        fillSquare(char, pos)
        pos += 1

    return polybius_square, polybius_square_map

# Decrypt using playfair cipher as shown in the wiki page:
# https://en.wikipedia.org/wiki/Playfair_cipher#Description
def decrypt_playfair_cipher(message: str, key: str) -> str:
    plaintext = ""
    polybius_square, polybius_square_map = generate_polybius_square(key)

    # Split message into 2 char blocks (message given should be even)
    assert len(message) % 2 == 0
    blocks = [message[i*2:i*2+2] for i in range(len(message) // 2)]
    
    for block in blocks:
        first, second = block
        first_row, first_col = polybius_square_map[first]
        second_row, second_col = polybius_square_map[second]
        # If the letters appear on the same row of your table, replace them with the letters to their immediate left respectively (with wrapping).
        if first_row == second_row:
            plaintext += polybius_square[first_row][first_col - 1 % 5] + polybius_square[second_row][second_col - 1 % 5]
        # If the letters appear on the same column of your table, replace them with the letters immediately above respectively (with wrapping).
        elif first_col == second_col:
            plaintext += polybius_square[first_row - 1 % 5][first_col] + polybius_square[second_row - 1 % 5][second_col]
        # If the letters are not on the same row or column, 
        # replace them with the letters on the same row respectively but at the other pair of corners of the rectangle defined by the original pair. 
        # The order is important – the first letter of the encrypted pair is the one that lies on the same row as the first letter of the plaintext pair.
        else:
            plaintext += polybius_square[first_row][second_col] + polybius_square[second_row][first_col]

    return plaintext


def main():
    encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"

    return decrypt_playfair_cipher(encrypted_message, key)

if __name__ == "__main__":
    main()

