'''
This program decrypts a message encrypted with a Playfair cipher and the key
"SUPERSPY". The decrypted message will be printed out.

The decrypted string will be entirely upper case, not include spaces,
the letter "X", or special characters.
'''


class PlayfairCipherSolver:
    def __init__(self, key):
        # Stores the coordinates of each letter in the key table
        self.coordinates = {}
        # Initialize the key table with 5 empty rows and columns
        self.key_table = [[''] * 5 for _ in range(5)]
        # Generate the key table and populate the coordinates dict
        self._generate_key_table(key)

    def _generate_key_table(self, key):
        '''
        Generates the 5 * 5 table that is used by the Playfair cipher.
        The table is filled in starting from the top row, from left to right.
        It is first filled with the letters in the key, while ignoring
        duplicate letters. The rest of the table is filled with the remaining
        alphabet letters in order, omitting "J".
        '''
        alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

        # Ensure the key is upper case, and has no spaces
        key = key.upper().replace(' ', '')
        # Concatenate the key to the alphabet
        combined = key + alphabet
        # Remove duplicate letters from the combined string
        combined = ''.join(dict.fromkeys(combined))

        # Current index of combined string
        idx = 0

        # Fill in the table with the combined string
        for i in range(5):
            for j in range(5):
                letter = combined[idx]
                self.key_table[i][j] = letter
                self.coordinates[letter] = (i, j)
                idx += 1

    def decrypt(self, encrypted_msg):
        '''
        To decrypt, we first break down the encrypted string into pairs of
        letters.
        Then, we follow the following rules:
          1. If the letters appear on the same row of the key table, replace
             each one with the letter to its immediate left.
          2. If the letters appear on the same column of the key table, replace
             each one with the letter immediately above.
          3. Else, replace them with the letters on the same row but at the
             opposite corner of the rectangle defined by this pair of letters.
          4. At the end, drop any instances of "X".
        '''
        decrypted_msg = ''
        pairs = [encrypted_msg[i:i+2] for i in range(0, len(encrypted_msg), 2)]
        for pair in pairs:
            # Row and column index of the first letter in the pair
            row1, col1 = self.coordinates[pair[0]]
            # Row and column index of the second letter in the pair
            row2, col2 = self.coordinates[pair[1]]

            if row1 == row2:  # Rule 1
                decrypted_msg += self.key_table[row1][(col1 - 1) % 5]
                decrypted_msg += self.key_table[row2][(col2 - 1) % 5]
            elif col1 == col2:  # Rule 2
                decrypted_msg += self.key_table[(row1 - 1) % 5][col1]
                decrypted_msg += self.key_table[(row2 - 1) % 5][col2]
            else:  # Rule 3
                decrypted_msg += self.key_table[row1][col2]
                decrypted_msg += self.key_table[row2][col1]

        decrypted_msg = decrypted_msg.replace('X', '')  # Rule 4

        return decrypted_msg


if __name__ == '__main__':
    encrypted_msg = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'
    key = 'SUPERSPY'
    decrypted_msg = PlayfairCipherSolver(key).decrypt(encrypted_msg)
    # Print decrypted message
    print(decrypted_msg)
