def make_pairs(ciphertext: str) -> list[str]:
    """
    This function makes returns an array containing
    pairs of 2 characters from the ciphertext
    Precondition: ciphertext has an even number of characters
    """
    n = len(ciphertext)
    arr = []
    for i in range(0, n, 2):
        arr.append(ciphertext[i : i + 2])
    return arr


def create_grid(key: str) -> list[list[str]]:
    """
    This function creates a 5x5 grid of the key, according to the
    rules of the playfair cipher
    """

    # create an empty grid using list comprehension
    grid = [["" for i in range(5)] for j in range(5)]

    letters = ""
    for char in key.upper():
        if char not in letters:
            if char == "J":  # omit J as per playfair rules
                letters += "I"
            else:
                letters += char

    length = 0

    # add the remaining letters to the letters string
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in letters:
            letters += char
            length += 1
        if length == 25:
            break

    # put the string into a 5 x 5 grid
    for i in range(25):
        grid[i // 5][i % 5] = letters[i]

    return grid


def search(char: str, grid: list[list[str]]) -> tuple[int, int]:
    """
    This function returns a 2-tuple containing the x and y coordinates of the
    given 'char' in the playfair cipher grid given by 'grid'. Return (-1, -1)
    if char not found
    Precondition: 'grid' is a valid playfair cipher grid (5 x 5)
    """

    # search linearly
    for i in range(5):
        for j in range(5):
            if grid[i][j] == char:
                return (i, j)
    return (-1, -1)


def decipher_same_column(
    first_location: tuple[int, int],
    second_location: tuple[int, int],
    grid: list[list[str]],
) -> str:
    """
    Handles the case when the both the characters in a given pair occur in the
    same column in the cipher grid given by 'grid'. 'first_location' gives the
    coordinates of the first character of the pair and 'second_location' gives
    the coordinates of the second character of the pair
    Precondition: grid is a valid playfair cipher grid (5x5)
    """

    # get x and y coordinates
    x1, y1 = first_location
    x2, y2 = second_location

    # one position up as per playfair rules
    x1 -= 1
    x2 -= 1

    # roll back to the bottom if any of the coordinates becomes -1
    x1 = 4 if x1 < 0 else x1
    x2 = 4 if x2 < 0 else x2

    return grid[x1][y1] + grid[x2][y2]


def decipher_same_row(
    first_location: tuple[int, int],
    second_location: tuple[int, int],
    grid: list[list[str]],
) -> str:
    """
    Handles the case when the both the characters in a given pair occur in the
    same row in the cipher grid given by 'grid'. 'first_location' gives the
    coordinates of the first character of the pair and 'second_location' gives
    the coordinates of the second character of the pair
    Precondition: grid is a valid playfair cipher grid (5x5)
    """

    # get the x and y coordinates
    x1, y1 = first_location
    x2, y2 = second_location

    # one left
    y1 -= 1
    y2 -= 1

    # account for corner case (coordinate becomes -1)
    y1 = 4 if y1 < 0 else y1
    y2 = 4 if y2 < 0 else y2

    return grid[x1][y1] + grid[x2][y2]


def decipher_rectangle_case(
    first_location: tuple[int, int],
    second_location: tuple[int, int],
    grid: list[list[str]],
) -> str:
    """
    Handles the case when the both the characters in a given pair occur in neither
    the same row nor the same column in the cipher grid given by 'grid'.
    'first_location' gives the coordinates of the first character of the pair
    and 'second_location' gives the coordinates of the second character of the pair
    Precondition: grid is a valid playfair cipher grid (5x5)
    """
    x1, y1 = first_location
    x2, y2 = second_location

    # swap the coordinates in a cross multiplication fashion to obtain
    # the opposite vertices of the rectangle
    return grid[x1][y2] + grid[x2][y1]


def remove_character(deciphered: str, char_remove: str) -> str:
    """
    Return a copy of 'deciphered' with 'char_remove' removed
    """

    # linear traversal and omit char_remove
    new = ""
    for char in deciphered:
        if char != char_remove:
            new += char
    return new


def remove_spaces_and_special(ciphertext: str) -> str:
    """
    Return a copy of 'ciphertext' with spaces and special characters removed
    """

    # traverse and only keep alphabets
    new = ""
    for char in ciphertext:
        if char.isalpha():
            new += char

    return new


def decipher(ciphertext: str, key: str) -> str:
    """
    Returns the string obtained by decrypting 'ciphertext' with the playfair
    cipher with key 'key'
    Precondition: 'ciphertext' must have an even number of characters
    """

    # clean the input (remove spaces, special and convert to upper case)
    ciphertext = remove_spaces_and_special(ciphertext.upper())
    key = remove_spaces_and_special(key.upper())

    # make pairs and grid
    grid = create_grid(key)
    pairs = make_pairs(ciphertext)

    # would store the deciphered string
    deciphered = ""

    # traverse the pairs
    for pair in pairs:
        # get the location of the two characters of the current pair
        first_location = search(pair[0], grid)
        second_location = search(pair[1], grid)

        # unpack the coordinates
        x1, y1 = first_location
        x2, y2 = second_location

        if x1 == x2:  # same row
            deciphered += decipher_same_row(first_location, second_location, grid)
        elif y1 == y2:  # same column
            deciphered += decipher_same_column(first_location, second_location, grid)
        else:  # rectangle case
            deciphered += decipher_rectangle_case(first_location, second_location, grid)

    # remove any Xs
    return remove_character(deciphered, "X")


print(decipher("IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV", "SUPERSPY"))
