'''
Shopify Eng Internship Challenge Playfair Cipher Solution
Author: Nicholas Chew
'''

class PlayfairCipherSolver:

    # Playfair Cipher Alphabet constant (modified to exclude 'J')
    ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    
    def __init__(self, keyword: str, dimension: int = 5) -> None:
        """
        Initialize the PlayfairCipherSolver with a given keyword and dimension.
        
        Args:
            keyword (str): The keyword used to create the cipher table.
            dimension (int): The dimension of the cipher table (default 5x5).
        """
        # Initialize keyword, replacing 'J' with 'I'
        self.keyword = keyword.upper().replace('J', 'I')

        # Set the dimension of the cipher table (default 5x5)
        self.dimension = dimension

        # Build the Playfair Cipher table
        self.cipher_table = self._build_cipher_table(self.keyword)

        # Map characters to their positions for efficient lookup
        self.character_positions = self._map_character_positions()

    def _build_cipher_table(self, keyword: str) -> list[list[str]]:
        """
        Build the Playfair Cipher table using the keyword.
        
        Args:
            keyword (str): The keyword used to create the cipher table.
        
        Returns:
            list[list[str]]: The 2D list representing the cipher table.
        """
        unique_characters = set()
        keyword_characters = []

        # Add keyword characters to the table and avoid duplicates
        for character in keyword:
            if character not in unique_characters:
                unique_characters.add(character)
                keyword_characters.append(character)

        # Add remaining alphabet characters to the table
        for character in PlayfairCipherSolver.ALPHABET:
            if character not in unique_characters:
                unique_characters.add(character)
                keyword_characters.append(character)

        # Form the table based on the dimension 
        cipher_table = []
        for i in range(self.dimension):
            start_index = i * self.dimension
            end_index = (i + 1) * self.dimension
            row = keyword_characters[start_index:end_index]
            cipher_table.append(row)
        
        return cipher_table

    def _map_character_positions(self) -> dict[str, tuple[int, int]]:
        """
        Map each character to its position in the cipher table.
        
        Returns:
            dict[str, tuple[int, int]]: A dictionary mapping characters to their positions.
        """
        character_positions = {}

        # Map each character to its position in the table
        for row in range(self.dimension):
            for col in range(self.dimension):
                character = self.cipher_table[row][col]
                character_positions[character] = (row, col)

        return character_positions

    def _find_position(self, character: str) -> tuple[int, int]:
        """
        Find the position of a character in the cipher table.
        
        Args:
            character (str): The character to find.
        
        Returns:
            tuple[int, int]: The row and column of the character in the table.
        """
        return self.character_positions[character]

    def _decrypt_pair(self, first_character: str, second_character: str) -> str:
        """
        Decrypt a pair of characters using Playfair Cipher rules.
        
        Args:
            first_character (str): The first character of the pair.
            second_character (str): The second character of the pair.
        
        Returns:
            str: The decrypted pair of characters.
        """
        row1, col1 = self._find_position(first_character)
        row2, col2 = self._find_position(second_character)

        # Decrypt according to Playfair Cipher rules
        if row1 == row2:
            # Shift left characters in the same row
            decrypted_first = self.cipher_table[row1][(col1 - 1) % self.dimension]
            decrypted_second = self.cipher_table[row2][(col2 - 1) % self.dimension]

        elif col1 == col2:
            # Shift up characters in the same column
            decrypted_first = self.cipher_table[(row1 - 1) % self.dimension][col1]
            decrypted_second = self.cipher_table[(row2 - 1) % self.dimension][col2]

        else:
            # Swap columns when characters form a rectangle
            decrypted_first = self.cipher_table[row1][col2]
            decrypted_second = self.cipher_table[row2][col1]

        return decrypted_first + decrypted_second

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypt the entire ciphertext using Playfair Cipher rules.
        
        Args:
            ciphertext (str): The ciphertext to decrypt.
        
        Returns:
            str: The decrypted plaintext.
        """
        ciphertext = ciphertext.upper().replace('J', 'I')

        # Pad with 'X' if the ciphertext length is odd
        if len(ciphertext) % 2 != 0:
            ciphertext += 'X'

        # Assemble the decrypted text by iterating over pairs of characters
        decrypted_text = ""
        for i in range(0, len(ciphertext), 2):
            first_character = ciphertext[i]
            second_character = ciphertext[i + 1]
            decrypted_text += self._decrypt_pair(first_character, second_character)

        # Remove 'X' padding from decrypted_text
        decrypted_text = decrypted_text.replace('X', '')

        return decrypted_text
    

if __name__ == "__main__":

    # Test case 1
    keyword1 = "PLAYFAIREXAMPLE"
    encrypted_text1 = "BMODZBXDNABEKUDMUIXMMOUVIF"
    playfair_cipher_solver1 = PlayfairCipherSolver(keyword1, 5)
    decrypted_text1 = playfair_cipher_solver1.decrypt(encrypted_text1)
    expected_output1 = "HIDETHEGOLDINTHETREESTUMP"
    assert decrypted_text1 == expected_output1

    # Test case 2
    keyword2 = "SUPERSPY"
    encrypted_text2 = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    playfair_cipher_solver2 = PlayfairCipherSolver(keyword2, 5)
    decrypted_text2 = playfair_cipher_solver2.decrypt(encrypted_text2)
    expected_output2 = "HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA"
    assert decrypted_text2 == expected_output2

    print(decrypted_text2)