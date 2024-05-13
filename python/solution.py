#createTable creates a 5x5 table containing the key and alphabet
def createTable(key, alphabet):
    tableChars = []
    for i in key:
        if i not in tableChars:
            tableChars.append(i)
    for i in alphabet:
        if i != "J" and i not in tableChars:
            tableChars.append(i)

    table = []
    while tableChars != []:
        table.append(tableChars[:5])
        tableChars = tableChars[5:]

    return table

#search returns the position (row, column) of an element in the table
def search(table, element):
    for i in range(5):
        for j in range(5):
            if table[i][j] == element:
                return i, j

#decryptRules facilitates the playfair cipher decryption algorithm, by looping through pairs of letters and decrypting them based on row, column and rectangle rules
def decryptRules(table, encryptedText):
    decryptedText = ""
    for i in range(0, len(encryptedText), 2):
        e1 = encryptedText[i]
        e2 = encryptedText[i + 1]
        e1r, e1c = search(table, e1)
        e2r, e2c = search(table, e2)
        c1 = ''
        c2 = ''

        #row rule => left of each char
        if e1r == e2r:
            if e1c == 0:
                c1 = table[e1r][4]
            else:
                c1 = table[e1r][e1c - 1]

            if e2c == 0:
                c2 = table[e2r][4]
            else:
                c2 = table[e2r][e2c - 1]

        #column rule => top of each char
        elif e1c == e2c:
            if e1r == 0:
                c1 = table[4][e1c]
            else:
                c1 = table[e1r - 1][e1c]

            if e2r == 0:
                c2 = table[4][e2c]
            else:
                c2 = table[e2r - 1][e2c]

        #rectangle rule
        else:
            c1 = table[e1r][e2c]
            c2 = table[e2r][e1c]

        decryptedText += c1 + c2
    
    return decryptedText

def main():
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    encryptedText = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"
    table = createTable(key, alphabet)
    output = decryptRules(table, encryptedText)

    for i in output:
        if i == 'X' or i == ' ':
            output = output.replace(i, '')
    print(output)

main()
