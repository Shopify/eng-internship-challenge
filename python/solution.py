"""
Abhinav Balasubramanian

Assumptions:
- i/j are interchangable

"""

class PlayfairCipher:
    
    def __init__(self, cipher_key : str) -> None:
    
        self.key = cipher_key
        self.mapping, self.table = self.construct_mapping(cipher_key)

    # By doing some extra processing during initialization, we can make lookups more efficient
    def construct_mapping(self, cipher_key: str):
        
        row, col = 0, 0
        table = [['' for i in range(5)] for j in range(5)]
        included = set()

        for letter in cipher_key:

            if letter not in included:

                included.add(letter)
                table[row%5][col%5] = letter
                col += 1
                if col % 5 == 0: 
                    row += 1
        
        letters = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

        for letter in letters:
            
            if letter not in included:

                included.add(letter)
                table[row % 5][col % 5] = letter
                col += 1
                if col % 5 == 0 : 
                    row += 1
        
        letterToPosition = {}
        for row in range(5):
            for col in range(5):
                letterToPosition[table[row][col]] = [row, col]
        
        return letterToPosition, table

    # O(1) lookups
    def position(self, letter : str) -> tuple[int, int]:
        return self.mapping[letter]

    def decrypt_digram(self, digram: str) -> str:
        
        c1 = digram[0]
        c2 = digram[1] 
        
        row1, col1 = self.mapping[c1]
        row2, col2 = self.mapping[c2]

        # Row Rule
        if row1 == row2:
            c1 = self.table[row1][(col1 - 1) % 5]
            c2 = self.table[row2][(col2 - 1) % 5]
        
        # Column Rule
        elif col1 == col2:
            c1 = self.table[(row1 - 1) % 5][col1]
            c2 = self.table[(row2 - 1) % 5][col2]
        
        # Rectangle Rule
        else:
            c1 = self.table[row1][col2]
            c2 = self.table[row2][col1]
            
        if c2 == 'X':
            return c1
        
        return c1 + c2
        
    def decrypt(self, encrypted_string: str) -> str: 
        
        decrypted_string = ""

        for p in range(0, len(encrypted_string), 2):

            decrypted_digram = self.decrypt_digram(encrypted_string[p: p+2])

            decrypted_string += decrypted_digram
 
        return decrypted_string
    
        
cipher_key = "SUPERSPY"

solver = PlayfairCipher(cipher_key)

encrypted_string = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

print(solver.decrypt(encrypted_string))



