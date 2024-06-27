import string


def remove_duplicates_preserve_order(string):
    return "".join(sorted(set(string), key=string.index))


def create_playfair_table(key):
    key_without_duplicates = remove_duplicates_preserve_order(key)

    # Uppercase alphabet exluding 'J'
    playfair_alphabet = string.ascii_uppercase.replace("J", "")

    potential_chars = key_without_duplicates + playfair_alphabet

    # List of table characters that will become the playfair table
    table_chars = remove_duplicates_preserve_order(potential_chars)

    # Unflatten into a 2x2 matrix
    return [table_chars[i : i + 5] for i in range(0, 25, 5)]


# Find a character's coordinates in the playfair table
def char_coordinates(table, char):
    for row in range(5):
        for col in range(5):
            if table[row][col] == char:
                return row, col
    return None


def decrypt_digraph(digraph, table):
    # Get coordinates for each digraph
    # First letter
    row1, col1 = char_coordinates(table, digraph[0])
    # Second letter
    row2, col2 = char_coordinates(table, digraph[1])

    # If the characters are on the same row in the playfair table, return each characters left side neighbour
    if row1 == row2:
        return table[row1][(col1 - 1) % 5] + table[row2][(col2 - 1) % 5]
    # If the characters are on the same column in the playfair table, get each characters top side neighbour
    elif col1 == col2:
        return table[(row1 - 1) % 5][col1] + table[(row2 - 1) % 5][col2]
    # If characters are not in the same row or column of the playfair table, then use the inverse coordinates of the accompanying digraph
    else:
        return table[row1][col2] + table[row2][col1]


def decrypt_playfair(ciphertext, key):
    table = create_playfair_table(key)

    # Split ciphertext into digraphs
    digraphs = [ciphertext[i : i + 2] for i in range(0, len(ciphertext), 2)]

    # The decrypted text
    plaintext = ""
    for digraph in digraphs:
        plaintext += decrypt_digraph(digraph, table)

    return plaintext


if __name__ == "__main__":
    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"
    decrypted_message = (
        decrypt_playfair(ciphertext, key)
        # Ensures decrypt is uppercase
        .upper()
        # Removes any Xs
        .replace("X", "")
        # Removes empty spaces
        .replace(" ", "")
    )

    print(decrypted_message)
