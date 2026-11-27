from typing import List

def create_square(key: str) -> List[List[str]]:
    """
    Create a 5x5 Polybius Square

    @param key: The key used to encode the Polybius square
    @return: 5x5 Matrix representation of the generated square
    """
    square = [['']*5 for i in range(5)]

    i, j = 0, 0
    inserted = set()
    #                       J = I
    for c in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c in inserted:
            continue
        square[i][j] = c
        inserted.add(c)
        j += 1
        if j % 5 == 0:
            j = 0
            i += 1

    return square

def find_char(char: str, square: List[List[str]]) -> tuple[int, int]:
    """
    Finds the location of a character inside the Polybius Square

    @param char: The character to search for inside the square
    @param square: The Polybius square generated from the `create_square()` function
    @return: (row, col) location of the character within the square
    """
    for i in range(5):
        for j in range(5):
            if square[i][j] == char:
                return (i,j)
            
def decrypt(ciphertext: str, square: List[List[str]]) -> str:
    """
    Decrypts the input ciphertext https://en.wikipedia.org/wiki/Playfair_cipher

    @param ciphertext: The input ciphertext
    @param square: The Polybius square generated from the `create_square()` function
    @return: Plaintext
    """
    bigraphs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    result = []
    
    for b in bigraphs:
        r1, c1 = find_char(b[0], square)
        r2, c2 = find_char(b[1], square)

        if r1 == r2:
            result.append(square[r1][(c1 - 1) % 5])
            result.append(square[r2][(c2 - 1) % 5])

        elif c1 == c2:
            result.append(square[(r1 - 1) % 5][c1])
            result.append(square[(r2 - 1) % 5][c2])

        else:
            result.append(square[r1][c2])
            result.append(square[r2][c1])

    result = [c for c in result if c != 'X']
    return "".join(result)

if __name__ == "__main__":
    key = "SUPERSPY"
    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

    square = create_square(key)

    print(decrypt(ciphertext, square))
