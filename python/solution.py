class PlayfairCipherSolver:
    def __init__(self, keyword):
        self.keyword = self._clean_keyword(keyword)
        self.grid = self._generate_playfair_grid()
    
    def _clean_keyword(self, keyword):
        seen = set()
        cleaned = []
        for char in keyword.upper():
            if char not in seen and char != 'J':
                seen.add(char)
                cleaned.append(char)
        return ''.join(cleaned)
    
    def _generate_playfair_grid(self):
        grid = [[None] * 5 for _ in range(5)]
        alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
        filled = set(self.keyword)
        keyword_chars = list(self.keyword)
        
        # Fill grid with the keyword characters
        row, col = 0, 0
        for char in keyword_chars:
            grid[row][col] = char
            col += 1
            if col == 5:
                row += 1
                col = 0
        
        # Fill in the remaining alphabet
        for char in alphabet:
            if char not in filled:
                grid[row][col] = char
                filled.add(char)
                col += 1
                if col == 5:
                    row += 1
                    col = 0
        return grid
    
    def _find_position(self, char):
        for r, row in enumerate(self.grid):
            if char in row:
                return r, row.index(char)
        return None
    
    def decrypt(self, ciphertext):
        plaintext = []
        pairs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
        
        for pair in pairs:
            r1, c1 = self._find_position(pair[0])
            r2, c2 = self._find_position(pair[1])
            
            if r1 == r2:
                plaintext.append(self.grid[r1][(c1 - 1) % 5])
                plaintext.append(self.grid[r2][(c2 - 1) % 5])
            elif c1 == c2:
                plaintext.append(self.grid[(r1 - 1) % 5][c1])
                plaintext.append(self.grid[(r2 - 1) % 5][c2])
            else:
                plaintext.append(self.grid[r1][c2])
                plaintext.append(self.grid[r2][c1])
        
        # Clean the decrypted message by removing 'X' fillers
        return ''.join(plaintext).replace('X', '')
    

# Example usage:
solver = PlayfairCipherSolver('SUPERSPY')
ciphertext = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'
print(solver.decrypt(ciphertext))
