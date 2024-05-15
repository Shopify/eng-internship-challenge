import itertools

ALPHABET_WITHOUT_J = "ABCDEFGHIKLMNOPQRSTUVWXYZ"


class Playfair:
    def __init__(self, key):
        self.grid, self.lookup_table = self.generate_grid(key)

    def generate_grid(self, key):
        """
        Construct playfair grid and look-up table based on given key.
        Look-up table is used to quickly search for a letter position in the grid.
        """
        grid = [[None] * 5 for _ in range(5)]
        lookup_table = dict()
        content = [char for char in itertools.chain(key.upper().replace(" ", ""), ALPHABET_WITHOUT_J)]

        # Remove duplicate (Python 3.6+)
        content = list(dict.fromkeys(content))
        counter = 0

        for i in range(len(grid)):
            for j in range(len(grid)):
                char = content[counter]
                grid[i][j] = char
                lookup_table[char] = (i, j)
                counter += 1
        return grid, lookup_table

    def decrypt_pair(self, char1, char2):
        """
        Decrypt a letter pair
        """
        row1, col1 = self.lookup_table[char1]
        row2, col2 = self.lookup_table[char2]
        if row1 == row2:
            char1_decrypted = self.grid[row1][(col1 - 1) % 5]
            char2_decrypted = self.grid[row2][(col2 - 1) % 5]
        elif col1 == col2:
            char1_decrypted = self.grid[(row1 - 1) % 5][col1]
            char2_decrypted = self.grid[(row2 - 1) % 5][col2]
        else:
            char1_decrypted = self.grid[row1][col2]
            char2_decrypted = self.grid[row2][col1]

        return char1_decrypted, char2_decrypted

    def decrypt(self, message):
        """
        Decrypt the message
        """
        decrypted_msg = []
        for i in range(0, len(message), 2):
            char1, char2 = message[i], message[i + 1]
            char1_decrypted, char2_decrypted = self.decrypt_pair(char1.upper(), char2.upper())
            if char1_decrypted != "X":
                decrypted_msg.append(char1_decrypted)
            if char2_decrypted != "X":
                decrypted_msg.append(char2_decrypted)

        return "".join(decrypted_msg)


if __name__ == "__main__":
    key = "SUPERSPY"
    secret_msg = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    playfair_cipher = Playfair(key)
    decrypted_msg = playfair_cipher.decrypt(secret_msg)
    print(decrypted_msg)
