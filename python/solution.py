from typing import List, Tuple, Union
import string


class PlayfairCipher:
    """
    Class for PLayfair Cipher.

    Given an encrypted message and a key, this class will decrypt the message with the decrypt_message() method
    """

    def __init__(self, encrypted_message: str, key: str):
        """
        Constructor

        Args:
            encrypted_message: the encrypted_message as a string
            key: the secret key used for encryption as a string

        Raises:
            ValueError
        """

        # Check types
        if not isinstance(encrypted_message, str):
            raise TypeError(f"encrypted_message must be of type string")

        if not isinstance(key, str):
            raise TypeError(f"key must be of type string")

        str1 = encrypted_message.upper().strip()
        str2 = key.upper().strip()

        temp1 = ""
        for c in str1:
            if ord("A") <= ord(c) <= ord("Z"):
                temp1 += c

        temp2 = ""
        for c in str2:
            if ord("A") <= ord(c) <= ord("Z"):
                if c == "J":
                    temp2 += "I"
                else:
                    temp2 += c

        self._encrypted_message = temp1
        self._key = temp2
        self._board = self._generate_board()

    def _generate_board(self):
        """
        generates a 5x5 board Cipher table as a 2d array
        """

        # intialize the 5x5 board of characters
        board = [["" for _ in range(5)] for _ in range(5)]
        processed_key = self._process_key()

        # add the missing letters in the alphabet and skip the letter J to the processed_key
        for letter in string.ascii_uppercase:
            if letter not in processed_key and letter != "J":
                processed_key += letter

        # convert the processed_key intto the 5x5 board
        count = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = processed_key[count]
                count += 1

        return board

    def _process_key(self) -> str:
        """
        processes the key by removing duplicates
        """

        processed_key = ""
        char_set = set()

        # remove duplicates from the key string
        for c in self._key:
            if c not in char_set:
                processed_key += c
                char_set.add(c)

        return processed_key

    def _decrypt_type(self, char1: str, char2: str) -> int:
        """
        determines the decrypt type

        Args:
            char1: first character
            char2: second character
            board: the cipher table generated from _generate_board()

        Returns:
            1: if char1 and char2 are in the same row
            2: if char1 and char2 are in the same column
            3: otherwise
        """

        char1_location = self._search_board(char=char1)
        char2_location = self._search_board(char=char2)

        if not char1_location or not char2_location:
            raise ValueError(
                f"self._search_board() did not find char1 or char2 in the board"
            )

        # check if char1 and char2 are in the same row
        if char1_location[0] == char2_location[0]:
            return 1

        # check if char1 and char2 are the same column
        elif char1_location[1] == char2_location[1]:
            return 2

        # otherwise char1 and char 2 form a 'box'
        else:
            return 3

    def _search_board(self, char: str) -> Union[Tuple[int, int], None]:
        """
        linear searches the board for the row and column that char1 exists in the board

        Args:
            char: character to search for
            board: the 5x5 board generated from _generate_board()

        Returns:
            tuple(row, col): if char is found
            None: if char is not found
        """

        if not self._board:
            raise ValueError("Board was not created")

        for i in range(len(self._board)):
            for j in range(len(self._board[i])):
                if self._board[i][j] == char:
                    return i, j

        return None

    def _get_decrypted_letters(self, char1: str, char2: str) -> str:
        """
        given char1 and char2, get the decrypted corresponding characters

        Args:
            char1: first character
            char2: second character

        Returns:
            str: string of two characters
        """

        if not self._board:
            raise ValueError("the board was not set up")

        decrypted_letters = ""
        decrypt_type = self._decrypt_type(char1=char1, char2=char2)
        char1_location = self._search_board(char=char1)
        char2_location = self._search_board(char=char2)

        if not char1_location or not char2_location:
            raise ValueError(
                "_get_decrypted_letters(): char1 or char2 could not be found in the board"
            )

        # same row
        if decrypt_type == 1:

            # check if a 'wrap' around is needed. IE column of either character is at 0th index
            if char1_location[1] == 0:
                decrypted_letters += self._board[char1_location[0]][4]
                decrypted_letters += self._board[char2_location[0]][
                    char2_location[1] - 1
                ]
            elif char2_location[1] == 0:
                decrypted_letters += self._board[char1_location[0]
                                                 ][char1_location[1]]
                decrypted_letters += self._board[char2_location[0]][4]
            else:
                decrypted_letters += self._board[char1_location[0]][
                    char1_location[1] - 1
                ]
                decrypted_letters += self._board[char2_location[0]][
                    char2_location[1] - 1
                ]

        # same column
        elif decrypt_type == 2:

            # check if a 'wrap' around is needed. IE row of either character is at 0th index
            if char1_location[0] == 0:
                decrypted_letters += self._board[4][char1_location[1]]
                decrypted_letters += self._board[char2_location[0] - 1][
                    char2_location[1]
                ]
            elif char2_location[0] == 0:
                decrypted_letters += self._board[char1_location[0] - 1][
                    char1_location[1]
                ]
                decrypted_letters += self._board[4][char2_location[1]]
            else:
                decrypted_letters += self._board[char1_location[0] - 1][
                    char1_location[1]
                ]
                decrypted_letters += self._board[char2_location[0] - 1][
                    char2_location[1]
                ]

        # 'box' case
        else:

            decrypted_letters += self._board[char1_location[0]
                                             ][char2_location[1]]
            decrypted_letters += self._board[char2_location[0]
                                             ][char1_location[1]]

        return decrypted_letters

    def decrypt_message(self):
        """
        decrypts the message
        """

        decrypted_message = ""

        # loop through encrypted_message in pairs of characters
        for i in range(0, len(self._encrypted_message), 2):

            pair = self._encrypted_message[i: i + 2]

            # get the decrypted letters
            decrypted_letters = self._get_decrypted_letters(
                char1=pair[0], char2=pair[1]
            )

            # remove Xs
            processed_decrypted_letters = decrypted_letters.replace("X", "")

            # add the decrypted letters to the string
            decrypted_message += processed_decrypted_letters.strip()

        return str(decrypted_message)


if __name__ == "__main__":

    ENCRYPTED_MESSAGE = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    KEY = "SUPERSPY"

    cipher = PlayfairCipher(encrypted_message=ENCRYPTED_MESSAGE, key=KEY)
    print(cipher.decrypt_message())
