def create_playfair_grid(key: str) -> list[list[str]]:
    """Creates a 5 x 5 grid for the playfair cipher.
    
    Parameters
    ----------
    `key`: str
        The key used to make the key-ed grid.

    Returns
    --------
    list[list[str]]
        The grid of characters.
    """

    ROWS = 5
    COLS = 5
    key = key.upper()
    used_chars = set()

    result = []
    for i in range(ROWS):
        row = []
        for j in range(COLS):
            row.append('X')
        result.append(row)


    for c in key:
        if c not in used_chars:
            index = len(used_chars)
            result[index // ROWS][index % COLS] = c
            used_chars.add(c)

    alphabet = [chr(i) for i in range(0x41, 0x5b)]
    for letter in alphabet:
        if letter == 'J': continue 
        if letter not in used_chars:
            index = len(used_chars)
            result[index // ROWS][index % COLS] = letter
            used_chars.add(letter)

    assert len(used_chars) == ROWS * COLS
    assert len(result) == ROWS
    assert all(len(row) == COLS for row in result)
    return result


def find_char_index(char: str, grid: list[list[str]]) -> tuple[int, int]: 
    """Returns the row and column indices of the `char` in the 2D `grid`.

    Parameters
    ----------
    `char`: str
        The target character.
    `grid`: list[list[str]]
        The search space grid where the charcter is to be found.

    Raises
    ------
    `LookupError`:
        If the target character is not in the grid.

    Returns
    -------
    tuple[int, int]:
        The row and column index of the target character in the grid.

    Notes on complexity
    -------------------
    This search, given constrained memory, will always be O(N^2) for an N x N grid. (though it will be O(1)
    since our grid is a fixed size).

    If this ever becomes a bottleneck, you could improve average perfomance by
    using heuristics like starting from the top if the character is in the key,
    the bottom if it's a high letter, or the middle in other cases.

    You could also improve the time complexity to O(1) if you have a space
    complexity of Theta(N*N) to a hash table for each character and its index in
    the grid.
    """

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if char == grid[r][c]:
                return r, c

    # Should never happen ideally
    raise LookupError(f"Cannot find {char} in grid")


def decrypt(ciphertext: str, key: str) -> str:
    """decrypts `ciphertext` encrypted with the Playfair Cipher using `key`.

    Cipher specification: https://web.archive.org/web/20240411155723/https://en.wikipedia.org/wiki/Playfair_cipher

    Parameters
    ----------
    `ciphertext`: str
        The ciphertext to decrypt.
    `key`: str 
        The secret key used in the cipher.

    Returns
    -------
    str:
        The decrypted plaintext.

    """

    grid = create_playfair_grid(key)
    ciphertext = ciphertext.upper()
    ciphertext = ''.join(filter(str.isalpha, ciphertext))
    assert len(ciphertext) % 2 == 0

    plaintext = ''
    for i in range(0, len(ciphertext), 2):
        a_r, a_c = find_char_index(ciphertext[i], grid) 
        b_r, b_c = find_char_index(ciphertext[i + 1], grid)

        if a_r == b_r:
            plaintext += grid[a_r][a_c - 1] + grid[b_r][b_c -1] 
        elif a_c == b_c:
            plaintext += grid[a_r - 1][a_c] + grid[b_r - 1][b_c] 
        else:
            plaintext += grid[a_r][b_c] + grid[b_r][a_c]

    plaintext = plaintext.replace('X', '')
    return plaintext


if __name__ == '__main__':
    ciphertext = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'
    key = 'SUPERSPY'
    print(decrypt(ciphertext, key))

