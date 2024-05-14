def runDecryption(key, cipherText):
    # decrypt the cipherText with the key using Playfair cipher
    # return the decrypted text
    def getKeyMatrix(key):
        # create the key matrix
        keyMatrix = []
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for i in range(5):
            keyMatrix.append([])
            j = 0
            while j < 5:
                if key != "":
                    if key[0] not in alphabet:  # skip duplicate characters
                        key = key[1:]
                        continue
                    keyMatrix[i].append(key[0])
                    alphabet = alphabet.replace(key[0], "")
                    key = key[1:]
                else:
                    keyMatrix[i].append(alphabet[0])
                    alphabet = alphabet[1:]
                j += 1

        return keyMatrix

    def getCharPosition(matrix, char):
        # get the position of a character in the matrix
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == char:
                    return i, j

    def decryptPair(matrix, pair):
        # decrypt a pair of characters
        row1, col1 = getCharPosition(matrix, pair[0])
        row2, col2 = getCharPosition(matrix, pair[1])
        if row1 == row2:
            return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        if col1 == col2:
            return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        return matrix[row1][col2] + matrix[row2][col1]

    keyMatrix = getKeyMatrix(key)
    plainText = ""
    i = 0
    while i < len(cipherText):
        pair = cipherText[i : i + 2]
        plainText += decryptPair(keyMatrix, pair)
        i += 2

    return plainText.replace("X", "")


if __name__ == "__main__":
    key = "SUPERSPY"
    cipherText = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    print(runDecryption(key, cipherText))
