'''
Shopify Engineering Internship (F24) - Playfair Cipher Solver Submission
Prasanna Thallapalli
June 21st, 2024
'''

def createTable(key):
    '''
    Purpose: creates a 5x5 table containing the key + unique alphabet characters and stores letters with their coordinates in a hashmap

    Input: key (str) given to decrypt the text

    Output: returns a 5x5 list of lists and a hashmap with key:value of char:tuple containing letter:(row, col)
    '''

    # preprocess the key by converting to uppercase and removing 'J' character 
    key = key.upper().replace('J', 'I')
    alphabet = list("ABCDEFGHIKLMNOPQRSTUVWXYZ")

    # appending unique characters from key and alphabet to tableChars list 
    tableChars = []
    for c in key:
        if c not in tableChars:
            tableChars.append(c)
    for c in alphabet:
        if c not in tableChars:
            tableChars.append(c)

    # creating a 5x5 table (25 entries) using tableChars list
    table = [tableChars[i:i + 5] for i in range(0, 25, 5)]

    # creating a hashmap with a char (letter) as the key and a tuple of (row, col) as the value for fast access
    coordsMap = {}
    for i in range(5):
        for j in range(5):
            coordsMap[table[i][j]] = (i, j)

    return table, coordsMap


def decryptText(table, coordsMap, encryptedText):
    '''
    Purpose: facilitates the playfair cipher decryption algorithm, by looping through pairs of letters and decrypting each pair based on row, column and rectangle rules

    Input: table (5x5 list of lists), coordsMap (hashmap of letter:(row,col)), encryptedText (str)

    Output: returns a str representing the decrypted text after running the cipher decryption algorithm 
    '''
    decryptedText = ""

    for i in range(0, len(encryptedText), 2):
        # saving the pair of characters to decrypt: element 1 (e1) and element 2 (e2)
        e1 = encryptedText[i]
        e2 = encryptedText[i + 1]

        # retrieving (row, col) of e1 and e2 from coordsMap
        e1r, e1c = coordsMap[e1]
        e2r, e2c = coordsMap[e2]

        # row rule: replace with the left of each char
        if e1r == e2r:
            decryptedText += table[e1r][(e1c - 1) % 5]
            decryptedText += table[e2r][(e2c - 1) % 5]

        # column rule: replace with the top of each char
        elif e1c == e2c:
            decryptedText += table[(e1r - 1) % 5][e1c]
            decryptedText += table[(e2r - 1) % 5][e2c]

        # rectangle rule: bounding rectangle with both coordinates (replace with same row, opposite columns)
        else:
            decryptedText += table[e1r][e2c]
            decryptedText += table[e2r][e1c]

    return decryptedText


def main():
    encryptedText = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"
    
    table, coordsMap = createTable(key)
    output = decryptText(table, coordsMap, encryptedText)

    # postprocess the decrypted string by removing 'X' and spaces
    output = output.replace('X', '').replace(' ', '')
    print(output)


if __name__ == "__main__":
    main()
