"""
Shopify Engineering Internship Playfair Cipher Solver Submission
Author: Norman Chen
Date: May 10, 2024
"""


class PlayfairSolver:
    """
    Represents an instance of a Playfair cipher solver by storing the cipher key.

    Attributes:
        cipher_key (str): The cipher key
        dimension (int): The dimension of the Playfair cipher table with a default of 5.
        positions (dict[str, tuple[int, int]]): Dictionary mapping letters to (row, column) pairs.
        table (list[list[str]]): Matrix of letters representing the cipher table.

    Methods:
        solve: Solves the inputted encrypted message.
    """

    def __init__(self, cipher_key: str, dimension: int = 5) -> None:
        """
        Initialize a new PlayfairSolver object with a cipher and dimension.

        Args:
            cipher_key (str): The cipher key, which should contain only uppercase letters.
            dimension (int): The dimension of the Playfair cipher table with a default of 5.
        """

        if not isinstance(cipher_key, str) or not (cipher_key.isalpha() and cipher_key.isupper()):
            raise ValueError("cipher key must be only uppercase letters.")
        if not isinstance(dimension, int):
            raise ValueError("dimension must be an integer.")

        self.cipher_key: str = cipher_key
        self.dimension: int = dimension
        self.positions: dict[str, tuple[int, int]] = {}
        self.table: list[list[str]] = [["" for _ in range(self.dimension)] for _ in range(dimension)]
        self.__populate_table()

    def __populate_table(self) -> None:
        """
        Populate the positions and table class fields according to Playfair cipher.

        This implementation chooses to treat "I" and "J" as the same letter, as per https://en.wikipedia.org/wiki/Playfair_cipher.
        """

        key_idx: int = 0
        # letter_idx starts at the ASCII representation of "A"
        letter_idx: int = 65
        row: int = 0
        while row < self.dimension:
            col: int = 0
            while col < self.dimension:
                # table is populated first with letters that aren't used yet from the cipher key
                if key_idx < len(self.cipher_key):
                    if self.cipher_key[key_idx] not in self.positions:
                        self.table[row][col] = self.cipher_key[key_idx]
                        self.positions[self.cipher_key[key_idx]] = (row, col)
                        col += 1
                    key_idx += 1
                # table is then populated with letters that aren't used yet from the alphabet
                else:
                    # get the letter from its ASCII representation
                    letter: str = chr(letter_idx)
                    # add either "I" or "J" in the table, but not both
                    if (letter == "I" and "J" in self.positions) or (letter == "J" and "I" in self.positions):
                        letter_idx += 1
                        continue

                    if letter not in self.positions:
                        self.table[row][col] = letter
                        self.positions[letter] = (row, col)
                        col += 1
                    letter_idx += 1
            row += 1

    def _decrypt_pair(self, pair: str) -> str:
        """
        Decrypt the pair of letters based on their positions in the table.

        Args:
            pair (str): The pair of letters, a string of length 2 to be decrypted.

        Returns:
            A string of length 2 representing the decrypted pair inputted.
        """

        if not isinstance(pair, str) or len(pair) != 2:
            raise ValueError("pair must be a string of length 2.")

        # get the positions of both letters on the table
        (row1, col1) = self.positions[pair[0]]
        (row2, col2) = self.positions[pair[1]]

        # if letters are on the same row, rotate their column position left
        if row1 == row2:
            col1 = col1 - 1 if col1 > 0 else self.dimension - 1
            col2 = col2 - 1 if col2 > 0 else self.dimension - 1
        # if letters are on the same column, rotate their row position up
        elif col1 == col2:
            row1 = row1 - 1 if row1 > 0 else self.dimension - 1
            row2 = row2 - 1 if row2 > 0 else self.dimension - 1
        # if letters are not on the same row nor column, swap columns
        else:
            col1, col2 = col2, col1
        return self.table[row1][col1] + self.table[row2][col2]

    def solve(self, encrypted_message: str) -> str:
        """
        Decrypt the encrypted message with the Playright cipher.

        This implementation chooses to treat "I" and "J" as the same letter, as per https://en.wikipedia.org/wiki/Playfair_cipher.
        This implementation also assumes that "X" is ignored when the message is decrypted.

        Args:
            encrypted_message (str): The encrypted message to be decrypted.

        Returns:
            A decrypted string following the Playfair cipher.
        """

        if not isinstance(encrypted_message, str) or not (encrypted_message.isalpha() and encrypted_message.isupper()) or len(encrypted_message) % 2 == 1:
            raise ValueError("encrypted message can only be uppercase letters of even length.")

        # replace "J" with "I" if "I" is in the table, and vice versa
        if "I" in self.positions:
            encrypted_message = encrypted_message.replace("J", "I")
        else:
            encrypted_message = encrypted_message.replace("I", "J")

        decrypted: str = ""
        for i in range(0, len(encrypted_message), 2):
            pair = encrypted_message[i:i + 2]
            pair = self._decrypt_pair(pair)
            decrypted += pair
        # remove "X" from decrypted string
        decrypted = decrypted.replace("X", "")

        assert decrypted.isalpha() and decrypted.isupper()

        return decrypted


def main():
    encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    cipher_key = "SUPERSPY"

    solver = PlayfairSolver(cipher_key, 5)
    solution = solver.solve(encrypted_message)
    print(solution)


if __name__ == "__main__":
    main()
