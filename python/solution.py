import re

DEBUG = False

# Create Key Table (modified Polybius Square)
def createKeyTable(cipher_key):
    # remove space and convert to upper case
    cipher_key = cipher_key.replace(" ", "").upper()
    # add letters from A-Z to key (omitting J)
    cipher_key += "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    # remove duplicate letters
    seen = set()
    keyList = [x for x in cipher_key if not (x in seen or seen.add(x))]

    if DEBUG: print("".join(keyList))

    keyTable = [[] for _ in range(5)]

    for i in range(5):
        for _ in range(5):
            keyTable[i].append(keyList.pop(0))
        if DEBUG: print(keyTable[i])
    
    return keyTable


"""
Find the position of the two characters in the key table
Returns the row and column of the two characters
"""
def findPosition(keyTable, a, b):
    ret = [0, 0, 0, 0]
    for i, row in enumerate(keyTable):
        for j, char in enumerate(row):
            if char == a:
                ret[0] = i
                ret[1] = j
            if char == b:
                ret[2] = i
                ret[3] = j
    return ret[0], ret[1], ret[2], ret[3]


"""
Decrypts the cipher text using the key table
Cipher text has to be of even length
Returns the decrypted text
"""
def decryptText(cipher_text, keyTable):
    cipher_text = cipher_text.replace(" ", "").upper()

    if (len(cipher_text) % 2 != 0) or (not cipher_text.isalpha()):
        print("ERROR: Cipher text is invalid")
        return

    ret = cipher_text
    if DEBUG: print(cipher_text)

    for i in range(0, len(cipher_text), 2):
        a = cipher_text[i]
        b = cipher_text[i + 1]

        if DEBUG: print(a, b)
        aRow, aCol, bRow, bCol = findPosition(keyTable, a, b)
        if DEBUG: print(aRow, aCol, bRow, bCol)

        if aRow == bRow:
            aCol = (aCol - 1) % 5
            bCol = (bCol - 1) % 5
        elif aCol == bCol:
            aRow = (aRow - 1) % 5
            bRow = (bRow - 1) % 5
        else:
            aCol, bCol = bCol, aCol
        
        if DEBUG: print(aRow, aCol, bRow, bCol)
        ret = ret[:i] + keyTable[aRow][aCol] + keyTable[bRow][bCol] + ret[i+2:]
    
    # clean up output: remove "X", and special characters
    ret = re.sub(r'[^A-Z]', '', ret).replace("X", "").upper()
    
    print(ret)


def main():
    cipher_key = "SUPERSPY"
    cipher_text = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

    keyTable = createKeyTable(cipher_key)
    decryptText(cipher_text, keyTable)


if __name__ == '__main__':
    main()
    