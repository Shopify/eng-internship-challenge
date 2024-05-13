class Playfair:
    def __init__(self, key, encrypted_message):
        """
        Initialize Playfair cipher with a given key and encrypted message.

        Args:
            key (str): The key to use for encryption/decryption.
            encrypted_message (str): The message to be decrypted.

        Attributes:
            key (str): The key used for encryption/decryption.
            encrypted_message (str): The message to be decrypted.
            table_values (str): Combined key and alphabet without 'J'.
            mapping (dict): Mapping of characters to coordinates on a 5x5 grid.
        """
        self.key = key.upper()
        self.encrypted_message = encrypted_message.upper()
        self.table_values = self.generate_table(key)
        self.mapping = self.create_grid_mapping()

    def generate_table(self, key):
        """
        Generate the Playfair cipher table values.

        Args:
            key (str): The key used for encryption/decryption.

        Returns:
            str: Combined key and alphabet without 'J'.
        """
        key = "".join(sorted(set(key), key=key.index))
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        combined_key = key + "".join(sorted(set(alphabet) - set(key)))
        return combined_key

    def create_grid_mapping(self):
        """
        Create a mapping of characters to coordinates on a 5x5 grid.

        Returns:
            dict: Mapping of characters to coordinates.
        """
        table_values = self.table_values
        mapping = {}
        for i, letter in enumerate(table_values):
            row = i // 5
            col = i % 5
            mapping[letter] = (row, col)
        return mapping

    def decrypt(self):
        """
        Decrypt the encrypted message using the Playfair cipher.

        Returns:
            str: The decrypted message.
        """
        encrypted_message = self.encrypted_message

        if len(encrypted_message) % 2 != 0:
            encrypted_message += 'X'
            
        decrypted_message = ""
        mapping = self.mapping

        for i in range(0, len(encrypted_message), 2):
            digraph = encrypted_message[i:i + 2]

            pos1 = mapping.get(digraph[0])
            pos2 = mapping.get(digraph[1])

            if pos1 and pos2:
                new_digraph = ""

                if pos1[0] == pos2[0]: # Same row
                    new_digraph = self.get_char_at(pos1[0], (pos1[1] - 1) % 5) + self.get_char_at(pos2[0], (pos2[1] - 1) % 5)
                elif pos1[1] == pos2[1]: # Same col
                    new_digraph = self.get_char_at((pos1[0] - 1) % 5, pos1[1]) + self.get_char_at((pos2[0] - 1) % 5, pos2[1])
                else: # Form a rectangle
                    new_digraph = self.get_char_at(pos1[0], pos2[1]) + self.get_char_at(pos2[0], pos1[1])

                decrypted_message += new_digraph

        decrypted_message = decrypted_message.replace("X", "")
        return decrypted_message

    def get_char_at(self, row, column):
        """
        Retrieve character from mapping based on row and column.

        Args:
            row (int): The row index.
            column (int): The column index.

        Returns:
            str or None: Character at the given row and column.
        """
        mapping = self.mapping
        for char, (r, c) in mapping.items():
            if r == row and c == column:
                return char
        return None

def main():
    """
    Main function to demonstrate Playfair cipher decryption.
    """
    key = "SUPERSPY"
    encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    playfair = Playfair(key, encrypted_message)
    decrypted_message = playfair.decrypt()
    print(decrypted_message)

if __name__ == '__main__':
    main()

