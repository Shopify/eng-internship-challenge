# Playfair cipher
class Solution:
    ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    TABLE_SIZE = 5

    def __init__(self, cipher):
        self.cipher = cipher
        self.letterToIndex, self.indexToLetter = {}, {}

        self.__build_table()

    # Decipher the code
    def decipher(self, code):
        segments = [code[i:i+2] for i in range(0, len(code), 2)]
        output = ""

        for segment in segments:
            output += self.__decipher_segment(segment)

        return output

    '''
    Private Methods
    '''

    # Populate the table with the cipher and then the alphabet
    def __build_table(self):
        row, col = self.__add_letters(self.cipher, 0, 0)
        self.__add_letters(self.ALPHABET, row, col)

    # Decipher a segment of the code
    def __decipher_segment(self, segment):
        row1, col1 = self.letterToIndex[segment[0]]
        row2, col2 = self.letterToIndex[segment[1]]

        if row1 == row2:
            result = self.__get_letter(row1, col1 - 1) + self.__get_letter(row2, col2 - 1)
        elif col1 == col2:
            result = self.__get_letter(row1 - 1, col1) + self.__get_letter(row2 - 1, col2)
        else:
            result = self.__get_letter(row1, col2) + self.__get_letter(row2, col1)

        if 'X' in result:
            result = result.replace('X', '')

        return result

    # Get the letter at a given row and column
    def __get_letter(self, row, col):
        row = row % self.TABLE_SIZE
        col = col % self.TABLE_SIZE

        return self.indexToLetter[(row, col)]
            
    # Add letters of a string into the table, and return the next index to be inserted at
    def __add_letters(self, text, row, col):
        for letter in text:
            if letter not in self.letterToIndex:
                self.indexToLetter[(row, col)] = letter
                self.letterToIndex[letter] = (row, col)

                col += 1
                if col >= self.TABLE_SIZE:
                    col = 0
                    row += 1
                    
        return (row, col)


CODE = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
CIPHER = "SUPERSPY"
sol = Solution(CIPHER)
print(sol.decipher(CODE))