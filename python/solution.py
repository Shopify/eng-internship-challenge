def generate_matrix(key):
    """
    Return a 5x5 matrix with given key using Playfair cipher rule (https://en.wikipedia.org/wiki/Playfair_cipher)

    :param key:
    :return: 2-d 5x5 array
    """
    normalized = ''
    seen = set()
    for char in key.upper():
        if char.isalpha() and char not in seen:
            if char == 'J':
                char = 'I'
            seen.add(char)
            normalized += char

    # Populate the rest with non-duplicate char in the alphabet
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # no J
    full_key = normalized + ''.join([ch for ch in alphabet if ch not in seen])

    # Create a 5x5 matrix
    key_matrix = [full_key[i:i + 5] for i in range(0, 25, 5)]
    return key_matrix


def decrypt_playfair(text, key):
    """
    Given an encrypted text and a key, using Playfair cipher and return the upper-cased decrypted text

    :param text: encrypted text
    :param key: key for 5x5 matrix
    :return: a string containing decrypted text
    """
    key_matrix = generate_matrix(key)
    letter_pos = {ch: (i, j) for i, row in enumerate(key_matrix) for j, ch in enumerate(row)}

    # Digrams
    digrams = [text[i:i + 2] for i in range(0, len(text), 2)]

    decrypted_text = []

    # Decrypt each digram
    for a, b in digrams:
        row_a, col_a = letter_pos[a]
        row_b, col_b = letter_pos[b]

        if row_a == row_b:  # Same row
            new_a = key_matrix[row_a][(col_a - 1) % 5]
            new_b = key_matrix[row_b][(col_b - 1) % 5]
        elif col_a == col_b:  # Same column
            new_a = key_matrix[(row_a - 1) % 5][col_a]
            new_b = key_matrix[(row_b - 1) % 5][col_b]
        else:  # Rectangle
            new_a = key_matrix[row_a][col_b]
            new_b = key_matrix[row_b][col_a]

        decrypted_text.extend([new_a, new_b])

    # Only return non X and alpha character in decrypted text
    result = ''.join([char for char in decrypted_text if char != "X" and char.isalpha()])

    return result.upper()


if __name__ == '__main__':
    key = "SUPERSPY"
    encrypted = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    print(decrypt_playfair(encrypted, key))
