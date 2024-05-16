class PlayfairDecryptor:
    def __init__(self, key):
        """ Initialises the keysquare
            :param key: The key string used to generate the key square.
        """
        self.key_square = self.create_key_square(key)

    def create_key_square(self, key):
            """
        Generates a 5x5 key square based on the provided key.
        :param key: The key string used to generate the key square.
        :return: A list of lists representing the 5x5 key square.
            """
            used_chars = set()
            key_characters = []
            for char in key:
                if char.isalpha() and char.upper() not in used_chars:
                    key_characters.append(char.upper())
                    used_chars.add(char.upper())

            alpha = "ABCDEFGHIKLMNOPQRSTUVWXYZ" #no J

            for char in alpha:
                if char not in used_chars:
                    key_characters.append(char)
            key_square_matrix = []
            for i in range(0, 25, 5):
                key_square_matrix.append(key_characters[i:i + 5])
            return key_square_matrix

    def decrypt_pair(self, pair):

        """
        Decrypts a pair of characters using the key square.
        :param pair: A tuple of two characters to be decrypted.
        :return: The decrypted string of two characters.
        """
        pos = {}
        for row_index in range(5):
            for col_index in range(5):
                char = self.key_square[row_index][col_index]
                pos[char] = (row_index, col_index)

        row1, col1 = pos[pair[0]]
        row2, col2 = pos[pair[1]]

        # if same row
        if row1 == row2:
            left_1 = self.key_square[row1][(col1 - 1) % 5]
            left_2 = self.key_square[row2][(col2 - 1) % 5]
            return left_1 + left_2
        # if same column
        elif col1 == col2:
            up_1 = self.key_square[(row1 - 1) % 5][col1]
            up_2 = self.key_square[(row2 - 1) % 5][col2]
            return up_1 + up_2

        # if rectangle
        else:
            rec_1 = self.key_square[row1][col2]
            rec_2 = self.key_square[row2][col1]
            return rec_1 + rec_2

    def decrypt_message(self, encrypted_message):

        """
        Decrypts an entire message by splitting it into pairs, decrypting each pair,
        and then concatenating the results. Thencleans the message by removing any
        padding characters that are not needed.
        :param encrypted_message: The string of the encrypted message.
        :return: The decrypted and cleaned message.
        """
        # split the message into pairs
        encrypted_pairs = []
        for i in range(0, len(encrypted_message), 2):
            pair = encrypted_message[i:i+2]
            encrypted_pairs.append(pair)

        # decrypt and concatenate 
        decrypted_chars = []
        for pair in encrypted_pairs:
            decrypted_pair = self.decrypt_pair(pair)
            decrypted_chars.append(decrypted_pair)

        decrypted_message = ''.join(decrypted_chars)
        return self.clean_message(decrypted_message)

    def clean_message(self, decrypted_message):
        """
        Cleans the decrypted message by ensuring it is uppercase, free of spaces, the letter 'X',
        'Q', and any special characters. This function only retains alphabetic characters that make
        sense in the context of the decrypted text.
        :param decrypted_message: The decrypted string.
        :return: The cleaned message string.
        """
        cleaned_message = ""
        i = 0
        while i < len(decrypted_message):
            # check if the character is not a special character and not X 
            if decrypted_message[i].isalpha() and decrypted_message[i] not in ('X'):
                # skip 'X' only if  last character or used to separate duplicate letters
                if decrypted_message[i] in ('X') and (i == len(decrypted_message) - 1 or decrypted_message[i - 1] == decrypted_message[i + 1]):
                    i += 1
                else:
                    cleaned_message += decrypted_message[i].upper()
                    i += 1
            else:
                i += 1
        return cleaned_message

if __name__ == '__main__':
    key = "SUPERSPY"
    encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    decryptor = PlayfairDecryptor(key)
    print(decryptor.decrypt_message(encrypted_message))
