class PlayfairCipher:
    """`PlayfairCipher` class to decrypt the encrypted message using Playfair Cipher."""

    def __init__(self, key):
        self.key = key
        self.key_table = self.generate_key_table()

    def generate_key_table(self):
        """Generate the key table for Playfair Cipher."""
        key_table = []
        key_set = set()

        for char in self.key:
            if char not in key_set:
                key_set.add(char)
                key_table.append(char)

        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

        for char in alphabet:
            if char not in key_set:
                key_table.append(char)

        key_table = [key_table[i : i + 5] for i in range(0, 25, 5)]
        return key_table

    def get_position(self, char):
        """Get the position of the character in the key table."""
        for i, row in enumerate(self.key_table):
            if char in row:
                return i, row.index(char)

    def get_char(self, row, col):
        """Get the character from the key table at the given position."""
        return self.key_table[row][col]

    def decrypt(self, encrypted_msg):
        """Decrypt the encrypted message using Playfair Cipher."""
        decrypted_msg = ""
        for i in range(0, len(encrypted_msg), 2):
            char1 = encrypted_msg[i]
            char2 = encrypted_msg[i + 1]

            row1, col1 = self.get_position(char1)
            row2, col2 = self.get_position(char2)

            if row1 == row2:
                decrypted_msg += self.get_char(row1, col1 - 1)
                decrypted_msg += self.get_char(row2, col2 - 1)
            elif col1 == col2:
                decrypted_msg += self.get_char(row1 - 1, col1)
                decrypted_msg += self.get_char(row2 - 1, col2)
            else:
                decrypted_msg += self.get_char(row1, col2)
                decrypted_msg += self.get_char(row2, col1)

        decrypted_msg = decrypted_msg.replace("X", "")

        print(decrypted_msg)


if __name__ == "__main__":

    encrypted_msg = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"

    instance = PlayfairCipher(key)
    instance.decrypt(encrypted_msg)
