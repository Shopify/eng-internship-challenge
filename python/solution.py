class PlayfairDecryptor:
    def __init__(self, key, ciphertext):
        self.key = key.upper()
        self.ciphertext = ciphertext.upper()
        self.__key_table, self.__char_to_position = self.create_key_table()

    def create_key_table(self):
        """
        Returns a 5x5 key table and a mapping of characters to their positions within the `key_table`.
        """
        char_set = set()  # Set to keep track of characters already added to the key table
        char_array = []  # Temporary array to store characters in the key table
        key = self.key.replace('J', 'I')

        # Add characters from the key to the char_array
        for char in key:
            if char not in char_set:
                char_array.append(char)
                char_set.add(char)
        
        # Add remaining characters in alphabet to the char_array
        for ascii_val in range(65, 91):
            char = chr(ascii_val)
            if char == 'J':  # Skip 'J' as it is replaced by 'I'
                continue
            if char not in char_set:
                char_array.append(char)
                char_set.add(char)

        # Create the key table and hash map from `char_array`
        key_table = [char_array[i * 5: (i + 1) * 5] for i in range(5)]
        char_to_position = {char_array[i]: (i // 5, i % 5) for i in range(25)}
        
        return key_table, char_to_position
    
    def decrypt(self):
        """
        Decrypts the playfair ciphertext using the precomputed key 
        table `key_table` and position hash map `char_to_position`
        """
        decrypted_text = '' 

        for i in range(0, len(self.ciphertext), 2):
            char1, char2 = self.ciphertext[i], self.ciphertext[i + 1]
            row1, col1 = self.__char_to_position[char1]
            row2, col2 = self.__char_to_position[char2]

            if row1 == row2:
                # Same row: Replace with letters immediately to the left of the current letters
                decrypted_char1 = self.__key_table[row1][(col1 - 1) % 5]
                decrypted_char2 = self.__key_table[row2][(col2 - 1) % 5]
            elif col1 == col2:
                # Same column: Replace with letters immediately above the current letters
                decrypted_char1 = self.__key_table[(row1 - 1) % 5][col1]
                decrypted_char2 = self.__key_table[(row2 - 1) % 5][col2]
            else:
                # Form a rectangle: Swap columns and keep the same rows
                decrypted_char1 = self.__key_table[row1][col2]
                decrypted_char2 = self.__key_table[row2][col1]

            # Append the decrypted characters to the decrypted text (Handle 'X' scenario)
            decrypted_text += decrypted_char1 if decrypted_char2 == 'X' else decrypted_char1 + decrypted_char2

        return decrypted_text

if __name__ == "__main__":
    key = "SUPERSPY"
    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    decryptor = PlayfairDecryptor(key, ciphertext)
    print(decryptor.decrypt())
