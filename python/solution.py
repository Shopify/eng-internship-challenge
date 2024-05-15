def cleanInput(text):
    # removing spaces, special characters and numbers from input text
    cleantext = ''.join(c for c in text if c.isalpha())

    # Returning text in upper case
    return cleantext.upper()


def createKeyTable(key):
    # Creating key table for the cipher
    keyTable = [['' for l in range(5)] for m in range(5)]
    # Dictionary to help create the key table
    dictA = {chr(l + 65): 0 for l in range(26)}

    # For letters in the key we set their dictionary value to 2.
    # The value for duplicate letters will already be set to 1, so we won't have to worry about them.
    for i in range(len(key)):
        if key[i] != 'J':
            dictA[key[i]] = 2
    # Setting the value for j since we will be replacing it with i
    dictA['J'] = 1

    row, col, k = 0, 0, 0
    # Setting the values for the table from the key since they are the first letters in table
    while k < len(key):
        if dictA[key[k]] == 2:
            dictA[key[k]] -= 1
            keyTable[row][col] = key[k]
            col += 1
            # End of 5x5 row, so we go down to next row
            if col == 5:
                row += 1
                col = 0
        k += 1
    # Setting the values for the rest of the letters in the table that aren't in key

    for k in dictA.keys():
        # checking if letter is j or already in table
        if dictA[k] == 0:
            keyTable[row][col] = k
            col += 1
            if col == 5:
                row += 1
                col = 0
    return keyTable


def searchDigraph(keyTable,a,b):

    digrLoc = [0,0,0,0]

    if a == "J":
        a = "I"
    elif b == "J":
        b = "I"

    for row in range(5):
        for col in range(5):
            # Setting the locations of the diagraph in the key square
            if keyTable[row][col] == a:
                digrLoc[0], digrLoc[1] = row, col
            elif keyTable[row][col] == b:
                digrLoc[2], digrLoc[3] = row, col

    return digrLoc


def decrypt(cipher, keyTable):

    i = 0
    # Searches for digraph location in key table then deciphers the cipher
    while i < len(cipher):
        digraph = searchDigraph(keyTable, cipher[i], cipher[i+1])
        # Same row for letters in digraph
        if digraph[0] == digraph[2]:
            cipher = (cipher[:i]
                      +keyTable[digraph[0]][(digraph[1]-1) % 5] + keyTable[digraph[2]][(digraph[3]-1) % 5] + cipher[i+2:])
        # Same column for letters in digraph
        elif digraph[1] == digraph [3]:
            cipher = (cipher[:i]
                      + keyTable[(digraph[0]-1) % 5][digraph[1]] + keyTable[(digraph[2]-1) % 5][digraph[3]] + cipher[i+2:])
        # Letters form a rectangle
        else:
            cipher = cipher[:i] + keyTable[digraph[0]][digraph[3]] + keyTable[digraph[2]][digraph[1]] + cipher[i+2:]
        i += 2

    return cipher


def decryptCipher(cipher,key):

    key = cleanInput(key)
    cipher = cleanInput(cipher)
    keytable = createKeyTable(key)
    sol = decrypt(cipher,keytable)
    # return decrypted cipher with x's removed and uppercase
    return sol.upper().replace("X","")


def main():
    print(decryptCipher("IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV", "SUPERSPY"))

if __name__ == '__main__':
    main()