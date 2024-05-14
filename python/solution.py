def make_matrix(key: str):
    """
    Creates and returns 5x5 Key Square for Playfair Cipher
    """

    mtrx_str = ""
    seen = set()
    for c in key:
        if c == "J":
            c = "I"
        if c not in seen:
            mtrx_str += c
            seen.add(c)

    letters = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    for c in letters:
        if c not in seen:
            mtrx_str += c
            seen.add(c)

    mtrx = [[""] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            mtrx[i][j] = mtrx_str[5 * i + j]

    return mtrx


def decrypt(matrix: list, message: str):
    """
    Decrypts an encrypted message using the Playfair Cipher
    """

    pairs = []
    for i in range(0, len(message), 2):
        pairs.append(message[i : i + 2])

    coordinates = {}

    for i in range(5):
        for j in range(5):
            coordinates[matrix[i][j]] = (i, j)

    decrypted = ""

    for first, second in pairs:
        row1, col1 = coordinates[first]
        row2, col2 = coordinates[second]
        if col1 == col2:
            decrypted += matrix[(row1 - 1) % 5][col1]
            decrypted += matrix[(row2 - 1) % 5][col2]
        elif row1 == row2:
            decrypted += matrix[row1][(col1 - 1) % 5]
            decrypted += matrix[row2][(col2 - 1) % 5]
        else:
            decrypted += matrix[row1][col2]
            decrypted += matrix[row2][col1]

    decrypted = decrypted.replace("X", "")

    return decrypted

if __name__ == "__main__":
    encrypted = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"
    matrix = make_matrix(key)
    decrypted = decrypt(matrix, encrypted)
    print(decrypted)
