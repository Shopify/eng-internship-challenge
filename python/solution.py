'''
PlayfairCipher is a class that implements the playfair cipher by taking in the key and
input message outputing the encrypted message.
'''
class PlayfairCipher:

    def __init__(self, key: str, message: str) -> None:
        self.key = key
        self.message = message
        self.tableHash = {} # key: str, value: tuple [int, int]

    '''
    createTable is a function that creates the 5x5 table of characters for the Playfair
    Cipher with the given key.
    Args:
        key (str): given key to be used in creating the table
    Returns: 
        list[list[str]]: the table to be used when encrypting the given text
    '''
    def createTable(self, key: str) -> list[list[str]]:
        usedLetters = set()
        uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        table = []
        rowCount = 0
        
        row = []
        colCount = 0

        for letter in key:
            if letter not in usedLetters:
                row.append(letter)
                self.tableHash[letter] = [rowCount, colCount]
                usedLetters.add(letter)
                colCount += 1
                if colCount == 5:
                    colCount = 0
                    table.append(row)
                    rowCount += 1
                    row = []
        for letter in uppercase_letters:
            if letter not in usedLetters:
                row.append(letter)
                self.tableHash[letter] = [rowCount, colCount]
                colCount += 1
                if colCount == 5:
                    colCount = 0
                    table.append(row)
                    rowCount += 1
                    row = []

        return table
                
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
    def rowRule(self, table: list[list[str]], first_x: int, first_y: int, second_x: int, second_y: int) -> str:
        new1 = ""
        new2 = ""

        if first_y == 0:
            new1 = table[first_x][4] # loop around row
        else:
            new1 = table[first_x][first_y - 1]

        if second_y == 0:
            new2 = table[second_x][4] # loop around row
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
    def colRule(self, table: list[list[str]], first_x: int, first_y: int, second_x: int, second_y: int) -> str:
        new1 = ""
        new2 = ""

        if first_x == 0:
            new1 = table[4][first_y] # loop around column
        else:
            new1 = table[first_x - 1][first_y]

        if second_x == 0:
            new2 = table[4][second_y] # loop around column
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
    def rectRule(self, table: list[list[str]], first_x: int, first_y: int, second_x: int, second_y: int) -> str:
        new1 = table[first_x][second_y]
        new2 = table[second_x][first_y]
        
        return new1 + new2

    '''
    main is the function that combines all the steps, by first creating the table, and parsing through the string two characters
    at a time, and applying the appropriate encryption to the two character strings based on the rules they follow, and finally outputting
    the completed encrypted string.
    '''
    def implementCipher(self):
        table = self.createTable(self.key)
        length = len(self.message)

        encryptedString = ""
        i = 0
        while(i < length):
            if i + 1 < length:
                firstLetter = self.message[i]
                i += 1
                secondLetter = self.message[i]
                if firstLetter == secondLetter:
                    secondLetter = "X"
                else:
                    i += 1

                first_x, first_y = self.tableHash[firstLetter] 
                second_x, second_y = self.tableHash[secondLetter] 

                if first_x == second_x:
                    encryptedString += self.rowRule(table, first_x, first_y, second_x, second_y)
                elif first_y == second_y:
                    encryptedString += self.colRule(table, first_x, first_y, second_x, second_y)
                else:
                    encryptedString += self.rectRule(table, first_x, first_y, second_x, second_y)
                

        
        encryptedString = encryptedString.replace("X", "").replace(" ", "") # remove whitespaces and Xs as required
        encryptedString = ''.join(filter(str.isalnum, encryptedString)) # remove special characters
        print(encryptedString)

if __name__ == '__main__':
    key = "SUPERSPY"
    inputString = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    newCipher = PlayfairCipher(key, inputString)
    newCipher.implementCipher()