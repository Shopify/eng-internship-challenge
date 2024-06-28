'''
createTable is a function that creates the 5x5 table of characters for the Playfair
Cipher with the given key.
Args:
    key (str): given key to be used in creating the table
Returns: 
    list[list[str]]: the table to be used when encrypting the given text
'''
def createTable(key: str) -> list[list[str]]:
    usedLetters = set()
    uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    table = []
    count = 0
    row = []

    for letter in key:
        if letter not in usedLetters:
            row.append(letter)
            usedLetters.add(letter)
            count += 1
            if count == 5:
                count = 0
                table.append(row)
                row = []
    for letter in uppercase_letters:
        if letter not in usedLetters:
            row.append(letter)
            count += 1
            if count == 5:
                count = 0
                table.append(row)
                row = []

    return table

'''
findIndices is a function that finds the row and column of the given character in the
Playfair Cipher table.
Args:
    table (list[list[str]]): the given Playfair Cipher table
    value (str): the given character to find
Returns:
    tuple[int, int]: the row and column index where the value was found
'''
def findIndices(table: list[list[str]], value: str) -> tuple[int, int]:
    for i in range(5):
        for j in range(5):
            if(table[i][j] == value):
                return i, j
            
'''
rowRule returns the two character string after encrypting the given two character string, assuming
that the given characters follow the row rule in the Playfair Cipher, where they are both in the same
row of the table.
Args:
    table (list[list[str]]): the given Playfair Cipher table
    first_x (int): the row of the first character
    first_y (int): the column of the first character
    second_x (int): the row of the second character
    second_y (int): the column of the second character
Returns:
    str: the two character string after it has been encrypted from the two given characters indices
'''
def rowRule(table: list[list[str]], first_x: int, first_y: int, second_x: int, second_y: int) -> str:
    new1 = ""
    new2 = ""

    if first_y == 0:
        new1 = table[first_x][4]
    else:
        new1 = table[first_x][first_y - 1]

    if second_y == 0:
        new2 = table[second_x][4]
    else:
        new2 = table[second_x][second_y - 1]
    
    return new1 + new2

'''
colRule returns the two character string after encrypting the given two character string, assuming
that the given characters follow the column rule in the Playfair Cipher, where they are both in the same
column of the table.
Args:
    table (list[list[str]]): the given Playfair Cipher table
    first_x (int): the row of the first character
    first_y (int): the column of the first character
    second_x (int): the row of the second character
    second_y (int): the column of the second character
Returns:
    str: the two character string after it has been encrypted from the two given characters indices
'''
def colRule(table: list[list[str]], first_x: int, first_y: int, second_x: int, second_y: int) -> str:
    new1 = ""
    new2 = ""

    if first_x == 0:
        new1 = table[4][first_y]
    else:
        new1 = table[first_x - 1][first_y]

    if second_x == 0:
        new2 = table[4][second_y]
    else:
        new2 = table[second_x - 1][second_y]
    
    return new1 + new2

'''
rectRule returns the two character string after encrypting the given two character string, assuming
that the given characters follow the recatangle rule in the Playfair Cipher, where they aren't in the same
row or the same column.
Args:
    table (list[list[str]]): the given Playfair Cipher table
    first_x (int): the row of the first character
    first_y (int): the column of the first character
    second_x (int): the row of the second character
    second_y (int): the column of the second character
Returns:
    str: the two character string after it has been encrypted from the two given characters indices
'''
def rectRule(table: list[list[str]], first_x: int, first_y: int, second_x: int, second_y: int) -> str:
    new1 = table[first_x][second_y]
    new2 = table[second_x][first_y]
    
    return new1 + new2

'''
main is the function that combines all the steps, by first creating the table, and parsing through the string two characters
at a time, and applying the appropriate encryption to the two character strings based on the rules they follow, and finally outputting
the completed encrypted string.
'''
def main():
    key = "SUPERSPY"
    inputString = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    table = createTable(key)
    length = len(inputString)

    encryptedString = ""
    i = 0
    while(i < length):
        if i + 1 < length:
            firstLetter = inputString[i]
            i += 1
            secondLetter = inputString[i]
            if firstLetter == secondLetter:
                secondLetter = "X"
            else:
                i += 1

            first_x, first_y = findIndices(table, firstLetter)
            second_x, second_y = findIndices(table, secondLetter)

            if first_x == second_x:
                encryptedString += rowRule(table, first_x, first_y, second_x, second_y)
            elif first_y == second_y:
                encryptedString += colRule(table, first_x, first_y, second_x, second_y)
            else:
                encryptedString += rectRule(table, first_x, first_y, second_x, second_y)
            

    
    encryptedString = encryptedString.replace("X", "").replace(" ", "")
    print(encryptedString)

if __name__ == '__main__':
    main()