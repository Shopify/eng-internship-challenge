class PlayfairCipherDecryptor:
    """
    Class used to represent a playfair cipher decryptor for a specific key.
    Assumes 'J' is omitted from table and 'X' is used as a placeholder letter.

    Attributes
    ----------
    key_table_matrix : list[list[char]]
        A list of lists of characters representing the 5x5 key table of characters as a matrix.
    key_table_post : dict[char, tuple[int, int]]
        A dictionary representing the 5x5 key table by mapping each character to its position as a tuple in the table.
    """

    # omit a letter from alphabet to fit in 5x5 table
    # 'J' omitted as standard practice
    ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    def __init__(self, key):
        """ 
        Initializes new decryptor with key table.

        Parameters
        ----------
        key : str
            The key string used to generate the key table.
        """

        self.key_table_matrix, self.key_table_pos = self.create_key_table(key)

    def create_key_table(self, key):
        """
        Generates a 5x5 playfair cipher key table from the provided key.

        Parameters
        ----------
        key : str
            The key string used to generate the key square, containing only alphabetical letters.

        Returns
        -------
        tuple[list[list[char]], dict[char, tuple[int, int]]]
            A tuple of the matrix (list of lists) and dictionary representations of the key table.
        """

        # find order of letters in the table
        used_chars = set()
        ordered_key_chars = []
        for char in key.upper():
            if char not in used_chars:
                ordered_key_chars.append(char)
                used_chars.add(char)

        for char in self.ALPHABET:
            if char not in used_chars:
                ordered_key_chars.append(char)

        # convert list of 25 ordered characters to 5x5 matrix (list of lists)
        key_table_matrix = [list(row) for row in zip(*[iter(ordered_key_chars)]*5)]
        # find mapping of each character to its positions in the matrix
        key_table_pos = {}
        for row in range(5):
            for col in range(5):
                key_table_pos[ordered_key_chars[row * 5 + col]] = (row, col)

        return key_table_matrix, key_table_pos

    def decrypt_digram(self, digram):
        """
        Decrypts a digram using the key table.

        Parameters
        ----------
        digram : tuple[char]
            An encrypted digram as a tuple of two characters.

        Returns
        -------
        str
            The decrypted digram as a string.
        """

        row1, col1 = self.key_table_pos[digram[0]]
        row2, col2 = self.key_table_pos[digram[1]]

        # rule 2: same row shift
        if row1 == row2:
            new1 = self.key_table_matrix[row1][(col1 - 1) % 5]
            new2 = self.key_table_matrix[row2][(col2 - 1) % 5]
            return new1 + new2
        
        # rule 3: same column shift
        elif col1 == col2:
            new1 = self.key_table_matrix[(row1 - 1) % 5][col1]
            new2 = self.key_table_matrix[(row2 - 1) % 5][col2]
            return new1 + new2

        # rule 4: opposite diagonal in rectangle
        else:
            new1 = self.key_table_matrix[row1][col2]
            new2 = self.key_table_matrix[row2][col1]
            return new1 + new2

    def decrypt_message(self, encrypted_message):
        """
        Decrypts a message encrypted with playfair cipher using the key of this decryptor.

        Parameters
        ----------
        encrypted_message : string
            The encrypted message as a string.

        Returns
        -------
        str
            The decrypted message as a string.
        """

        decrypted_message = ""
        for i in range(0, len(encrypted_message), 2):
            # separate into digrams
            encrypted_digram = encrypted_message.upper()[i:i+2]
            # decrypt each digram
            decrypted_digram = self.decrypt_digram(encrypted_digram)
            # append the digram with 'X's removed
            decrypted_message += decrypted_digram.replace('X', '')
        
        return decrypted_message

if __name__ == '__main__':
    key = "SUPERSPY"
    encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    decryptor = PlayfairCipherDecryptor(key)
    print(decryptor.decrypt_message(encrypted_message))