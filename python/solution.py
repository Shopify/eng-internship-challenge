# Rachelle De Man Solution

# cipher Key and encrypted Message
cipherKey = "SUPERSPY"
encryptedMsg = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"


# Generating the key table
def generateKeyTable(cipherKey):
    # It is defined that the key table is a 5 x 5 matrix where the
    # letters of the keyword are fulled and then the remaining spaces
    # are the rest of the alphabet letters in alphabetical order
    # note that duplicates are dropped

    # We initialize the key table to be the cipher key without repeating letters
    listCipherLetters = sorted(set(cipherKey), key=cipherKey.index)
    # we remove the letters in the cipher key from the alphabet. Note I/J are the same, both represented by I
    listAlphabet = [
        x for x in "ABCDEFGHIKLMNOPQRSTUVWXYZ" if x not in listCipherLetters
    ]
    # we add the cipher letters and rest of alphabet to key table
    keyTable = "".join(listCipherLetters) + "".join(listAlphabet)

    return keyTable


# function to solve encryption
def decrypt(encryptedMsg, keyTable):
    decryptedMsg = ""
    # we will iterate through the encrypted message in pairs
    for i in range(0, len(encryptedMsg), 2):

        # index of the current pair in the key table
        pair1 = keyTable.index(encryptedMsg[i])
        pair2 = keyTable.index(encryptedMsg[i + 1])

        # check if both letters are in the same column
        if pair1 % 5 == pair2 % 5:
            # Take letter above each (with wraparound, so do mod 25 (as 0-24 positions))
            decryptedMsg += keyTable[(pair1 - 5) % 25]  # matrix is x 5 hence subtract 5
            decryptedMsg += keyTable[(pair2 - 5) % 25]

        # check if both letters are in the same row
        elif pair1 // 5 == pair2 // 5:
            # Take letter to the left of each with wraparound
            # To calculate wraparound if the floor division is equal to regular division,
            # it is the leftmost position and hence add 5

            decryptedMsg += keyTable[((pair1 - 1) + (pair1 // 5 == pair1 / 5) * 5) % 25]
            decryptedMsg += keyTable[((pair2 - 1) + (pair2 // 5 == pair2 / 5) * 5) % 25]

        # final case where letters are not same row or column
        else:
            # Take letter that is in the same row but in the column of the other letter
            # pairX // 5 finds row position, * 5 accounts for string offset for proper positioning
            # pairX % 5 finds column position
            decryptedMsg += keyTable[pair1 // 5 * 5 + pair2 % 5]
            decryptedMsg += keyTable[pair2 // 5 * 5 + pair1 % 5]

    # remove buffer x's from solution
    return decryptedMsg.replace("X", "")


# solving the problem
keyTable = generateKeyTable(cipherKey)
solution = decrypt(cipherKey, encryptedMsg, keyTable)
# print solution
print(solution)
