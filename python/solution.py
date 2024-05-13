CIPHER_KEY = "SUPERSPY"
TEST_STRING = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

def groupLetters(text):
    grouped, i = [], 0
    
    while (i < len(text)):
        letterOne = text[i]
        letterTwo = text[i + 1] if (i + 1 < len(text)) else "X"

        if (letterOne == letterTwo):
            grouped.append((letterOne, "X"))
            i += 1
        else:
            grouped.append((letterOne, letterTwo))
            i += 2

    return grouped    

def makeMatrix():
    ROW = COL = 5
    matrix = [['' for i in range(ROW)] for j in range(COL)]
    letterToCoordinate = {}
    keyIndex = alphabetIndex = 0

    for r in range(ROW):
        for c in range(COL):
            if (keyIndex < len(CIPHER_KEY)):
                while (CIPHER_KEY[keyIndex] in letterToCoordinate):
                    keyIndex += 1

                matrix[r][c] = CIPHER_KEY[keyIndex]
                letterToCoordinate[CIPHER_KEY[keyIndex]] = (r, c)
                keyIndex += 1
            else:
                while (ALPHABET[alphabetIndex] in letterToCoordinate):
                    alphabetIndex += 1

                matrix[r][c] = ALPHABET[alphabetIndex]
                letterToCoordinate[ALPHABET[alphabetIndex]] = (r, c)
                alphabetIndex += 1

    return matrix, letterToCoordinate
    
def decrypt(ciphertext):
    matrix, letterToCoordinate = makeMatrix()
    groupedLetters = groupLetters(ciphertext)    
    plaintext = []

    for letterOne, letterTwo in groupedLetters:
        rowOne, colOne = letterToCoordinate[letterOne]
        rowTwo, colTwo = letterToCoordinate[letterTwo]

        if (rowOne == rowTwo):
            if (matrix[rowOne][(colOne - 1) % 5] != "X"):
                plaintext.append(matrix[rowOne][(colOne - 1) % 5])

            if (matrix[rowTwo][(colTwo - 1) % 5] != "X"):
                plaintext.append(matrix[rowTwo][(colTwo - 1) % 5])
        elif (colOne == colTwo):
            if (matrix[(rowOne - 1) % 5][colOne] != "X"):
                plaintext.append(matrix[(rowOne - 1) % 5][colOne])

            if (matrix[(rowTwo - 1) % 5][colTwo] != "X"):
                plaintext.append(matrix[(rowTwo - 1) % 5][colTwo])
        else:
            if (matrix[rowOne][colTwo] != "X"):
                plaintext.append(matrix[rowOne][colTwo])
                
            if (matrix[rowTwo][colOne] != "X"):
                plaintext.append(matrix[rowTwo][colOne])

    return "".join(plaintext)

def main():
    print(decrypt(TEST_STRING))

if __name__ == "__main__":
    main()
 