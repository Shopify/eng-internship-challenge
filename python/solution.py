def generate_key_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" # J is removed
    key_matrix = [[0] * 5 for _ in range(5)]
    seen = set()
    idx = 0
    table_input = key.upper() + alphabet

    for char in table_input:
        if char not in seen:
            seen.add(char)
            key_matrix[idx // 5][idx % 5] = char
            idx += 1

    return key_matrix


def find_letter_position(key_matrix, letter):
    for row in range(5):
        for col in range(5):
            if key_matrix[row][col] == letter:
                return row, col
    return -1, -1


def decrypt_playfair(ciphertext, key):
    plaintext = ""
    key_matrix = generate_key_matrix(key)

    for i in range(0, len(ciphertext), 2):
        row1, col1 = find_letter_position(key_matrix, ciphertext[i])
        row2, col2 = find_letter_position(key_matrix, ciphertext[i + 1])

        if row1 == row2:
            plaintext += key_matrix[row1][(col1 - 1) % 5] + key_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += key_matrix[(row1 - 1) % 5][col1] + key_matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += key_matrix[row1][col2] + key_matrix[row2][col1]

    plaintext = plaintext.replace("X", "")

    return plaintext


def main():
    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"
    print(decrypt_playfair(ciphertext, key))


if __name__ == "__main__":
    main()