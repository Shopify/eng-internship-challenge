
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


def main():
    encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"

if __name__ == "__main__":
    main()

