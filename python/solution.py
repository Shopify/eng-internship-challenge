class PlayfairCipher:
    def __init__(self, key):
        self.ALPHABET = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
        self.key = key
        self.key_table = self.create_key_table()

    def create_key_table(self):
        # create the key table
        key_table = []
        used_letters = set()

        # fill the table with the letters of the key
        for letter in self.key:
            if letter not in used_letters:
                used_letters.add(letter)
                key_table.append(letter)
        
        # fill the remainder of the table with unused letters of the alphabet
        for letter in self.ALPHABET:
            if letter not in used_letters:
                used_letters.add(letter)
                key_table.append(letter)

        return [key_table[i : i + 5] for i in range(0, 25, 5)]

    def decrypt(self, cipher):
        # Decrypt and print the cipher
        plaintext = ''
        for i in range(0, len(cipher), 2):
            # iterate over pairs of letters in the cipher
            a, b = cipher[i], cipher[i+1]
            a_r, a_c, b_r, b_c = 0, 0, 0, 0
            # find locations of the letters in the table
            for r in range(5):
                for c in range(5):
                    if self.key_table[r][c] == a:
                        a_r, a_c = r, c
                    if self.key_table[r][c] == b:
                        b_r, b_c = r, c
            
            # three possible cases for the letters
            # letters are in the same row
            if a_r == b_r:
                plaintext += self.key_table[a_r][(a_c - 1) % 5]
                plaintext += self.key_table[b_r][(b_c - 1) % 5]
            # letters are in the same column
            elif a_c == b_c:
                plaintext += self.key_table[(a_r - 1) % 5][a_c]
                plaintext += self.key_table[(b_r - 1) % 5][b_c]
            # letters are in different rows and columns
            else:
                plaintext += self.key_table[a_r][b_c]
                plaintext += self.key_table[b_r][a_c]

        # remove occurences of 'X' from plaintext
        plaintext = plaintext.replace('X', '')
        print(plaintext)

if __name__ == '__main__':
    cipher = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'
    key = 'SUPERSPY'
    playfair_cipher = PlayfairCipher(key)
    playfair_cipher.decrypt(cipher)
