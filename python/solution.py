class PlayFairCipher:
    def __init__(self, key):
        self.key = key.upper().replace(' ', '')
        self.generate_key_table()

    def generate_key_table(self):
        '''Generate the key table by filling it with the key and the remaining letters of the alphabet'''
        table = []
        for char in self.key + 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
            if char not in table:
                table.append(char)
        self.key_table = [table[i:i+5] for i in range(0, 25, 5)]

    def preprocess_text(self, plaintext):
        '''Preprocess the plaintext by splitting it into pairs of letters and adding an 'X' if necessary'''
        pairs = []
        i = 0
        while i < len(plaintext):
            if i == len(plaintext) - 1:
                # If the length of the plaintext is odd, append an 'X' to the end
                pairs.append(plaintext[i] + 'X')
                i += 1
            elif plaintext[i] == plaintext[i + 1]:
                # If the two letters are the same, insert an 'X' between them
                pairs.append(plaintext[i] + 'X')
                i += 1
            else:
                pairs.append(plaintext[i] + plaintext[i + 1])
                i += 2
        return pairs

    def find_position(self, char):
        '''Find the row and column position of a character in the key table'''
        for i, row in enumerate(self.key_table):
            if char in row:
                return i, row.index(char)
    
    def encipher(self, plaintext):
        plaintext = plaintext.upper().replace(' ', '').replace('J', 'I')
        pairs = self.preprocess_text(plaintext)
        ciphertext = ''
        
        # Encipher each pair
        for pair in pairs:
            a, b = pair
            row_a, col_a = self.find_position(a)
            row_b, col_b = self.find_position(b)

            if row_a == row_b:
                ciphertext += self.key_table[row_a][(col_a + 1) % 5]
                ciphertext += self.key_table[row_b][(col_b + 1) % 5]
            elif col_a == col_b:
                ciphertext += self.key_table[(row_a + 1) % 5][col_a]
                ciphertext += self.key_table[(row_b + 1) % 5][col_b]
            else:
                ciphertext += self.key_table[row_a][col_b]
                ciphertext += self.key_table[row_b][col_a]

        return ciphertext
    
    def decipher(self, ciphertext):
        ciphertext = ciphertext.upper().replace(' ', '')
        pairs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
        plaintext = ''

        for pair in pairs:
            a, b = pair
            row_a, col_a = self.find_position(a)
            row_b, col_b = self.find_position(b)

            if row_a == row_b:
                plaintext += self.key_table[row_a][(col_a - 1) % 5]
                plaintext += self.key_table[row_b][(col_b - 1) % 5]
            elif col_a == col_b:
                plaintext += self.key_table[(row_a - 1) % 5][col_a]
                plaintext += self.key_table[(row_b - 1) % 5][col_b]
            else:
                plaintext += self.key_table[row_a][col_b]
                plaintext += self.key_table[row_b][col_a]

        return plaintext.replace('X', '')

def main():
    pfCipher = PlayFairCipher('SUPERSPY')
    plaintext = pfCipher.decipher('IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV')
    print(plaintext, flush=True)

if __name__ == '__main__':
    main()