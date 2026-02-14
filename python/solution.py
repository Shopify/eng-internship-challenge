# AUTHOR: Matthew Low

class Playfair:

    WRAP_COLUMN = 20
    WRAP_ROW = 4

    alphabet = ['A', 'B', 'C', 'D', 'E',
                'F', 'G', 'H', 'I', 'K',
                'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']

    def __init__(self, keyword):
        self.keyword = self.prepKeyword(keyword)
        self.grid = self.makeGrid()

    # Remove duplicate letters from keyword
    def prepKeyword(self, keyword):
        kw_letters = list(keyword)
        res = []

        for letter in kw_letters:
            if letter not in res:
                res.append(letter)
        
        return "".join(res)

    # Create list that will represent cipher grid, keyword first, then rest of alphabet next
    def makeGrid(self):
        kw_letters = list(self.keyword)

        for letter in self.alphabet:
            if letter not in kw_letters:
                kw_letters.append(letter)

        return kw_letters
    
    # For printing grid
    def printGrid(self):
        print(self.grid[0:5])
        print(self.grid[5:10])
        print(self.grid[10:15])
        print(self.grid[15:20])
        print(self.grid[20:25])
    
    # Check if letters in same column
    def sameColumn(self, a, b):
        return (self.grid.index(a) - self.grid.index(b)) % 5 == 0 
    
    # Check if letters in same row
    def sameRow(self, a, b):
        return (self.grid.index(a) // 5 == self.grid.index(b) // 5)
    
    # Get width of box from letters
    def boxWidth(self, a, b):
        return (self.grid.index(b) % 5) - (self.grid.index(a) % 5)
    
    # Get grid entry to left of letter, wrap row if necessary
    def getLeft(self, letter):
        i = self.grid.index(letter)

        if i % 5 == 0:
            return self.grid[i + self.WRAP_ROW]
        else:
            return self.grid[i - 1]

    # Get grid entry above letter, wrap column if necessary
    def getUp(self, letter):
        i = self.grid.index(letter)

        if i // 5 == 0:
            return self.grid[i + self.WRAP_COLUMN]
        else:
            return self.grid[i - 5]

    def decrypt(self, message):
        m_letters = list(message)

        i = 1

        # Decrypt two letters at a time
        while i <= len(m_letters):
            a = m_letters[i - 1]
            b = m_letters[i]

            if self.sameRow(a, b):
                m_letters[i - 1] = self.getLeft(a)
                m_letters[i] = self.getLeft(b)
            elif self.sameColumn(a, b):
                m_letters[i - 1] = self.getUp(a)
                m_letters[i] = self.getUp(b)
            else:
                w = self.boxWidth(a, b)
                m_letters[i - 1] = self.grid[self.grid.index(a) + w]
                m_letters[i] = self.grid[self.grid.index(b) - w]
            
            i += 2

        # Remove any remaining Xs
        for letter in m_letters:
            if letter == 'X':
                m_letters.remove(letter)

        return "".join(m_letters)

# Execution
cipher = Playfair("SUPERSPY")
print(cipher.decrypt("IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"))
