"""
Solution to the PlayFair Cipher Shopify Eng Internship Challenge

Author: Peter
Date: Friday, May 10, 2024
"""

# imports
import subprocess
from collections import defaultdict

# typing imports
from typing import Tuple, List, Final

class PlayFair:
    def __init__(self, key: str):
        """
        Initializes the Playfair class to handle encryption/decryption and matrix building

        Constants:
            alphabet (str): alphabet in uppercase
            rows (int): number of rows of the encryption matrix
            cols (int): number of columns of the encryption matrix

            indicies (defaultdict[str, tuple[int, int]]): location of char in matrix (allows for O(log(n)) lookup)
            matrix (List[List[str]]): 2D array of the encryption matrix
        """

        # constants
        self.alphabet: Final[str] = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.rows: Final[int] = 5
        self.cols: Final[int] = 5

        # encryption matrix and indicies dictionary
        # store the indicies of the character so that for n -> infinity, it is much more optimized than looping through the matrix to find the index
        self.indicies = defaultdict(lambda: (0, 0))
        self.matrix: List[List[str]] = [["" for _ in range(self.cols)] for _ in range(self.rows)]

        # builds the matrix
        self.__build_matrix(key=key)

    def __print_matrix(self) -> None:
        """
        Print the matrix for debugging

        Args:
            None

        Returns:
            None
        """

        # print the rows one by one for readability
        for row in self.matrix:
            print(row)

    def __increment_pointer(self, i, j: int) -> Tuple[int, int]:
        """
        Increments the current position in the matrix

        Args:
            i, j (int, int): the current index of the pointer in the matrix

        Returns:
            new_i, new_j (int, int): the new index of the pointer or -1, -1 if it reaches the end
        """

        # at the end of the matrix
        if i == self.rows - 1 and j == self.cols - 1:
            return -1, -1

        # at the end of the row, but has more rows beneath
        if j == self.cols - 1:
            return i+1, 0

        # at the middle of a row
        return i, j+1

    def __diagraminate(self, text: str) -> List[str]:
        """
        Convert a text into a list of digrams

        Args:
            text (str): the text to convert

        Returns:
            digrams (List[str]): the list of digrams
        """

        # conver the text to uppercase
        text = text.upper()

        # length of the text
        length = len(text)

        # list to store digrams
        digrams = []

        # index to increment
        index = 0

        while index <= length - 2:
            # the current digram to process
            digram = text[index:index+2]

            # if it is the same, then add an X and remove decrement i by one
            # special case to handle I and J
            if digram[0] == digram[1] or digram[0] == 'I' and digram[1] == 'J' or digram[0] == 'J' and digram[1] == 'I':
                digrams.append(digram[0] + 'X')
                index -= 1

            # if it is not the same then append it to the list
            else:
                digrams.append(digram)

            # increment the index by two
            index += 2

        # edge case for cases with odd leftover
        if index < length:
            digrams.append(text[index] + 'X')

        # return the list of digrams
        return digrams

    def __build_matrix(self, key: str) -> None:
        """
        Builds the playfair encryption matrix

        Args:
            key (str): the encryption key

        Returns:
            matrix (List[list[str]]): encryption matrix
        """

        # covert key to all capital
        key = key.upper()

        # remove all the spaces
        key = key.replace(' ', '')

        # initial coordinates of the pointer
        x, y = 0, 0

        # iterate through each character of the key
        for char in key:
            # if the char is already in the matrix, continue
            if char in self.indicies:
                continue

            # special case to handle I, J as they are treated as the same
            if char == 'I' and 'J' in self.indicies or char == 'J' and 'I' in self.indicies:
                continue

            # if it is not already in the matrix, set the current coordinates to the char
            self.matrix[x][y] = char

            # add this location into the dictionary
            self.indicies[char] = (x, y)

            # move the pointer forward
            x, y = self.__increment_pointer(i=x, j=y)

            # if you already reached the end of the matrix, break
            if x == -1 and y == -1:
                break

        for char in self.alphabet:
            # if the char is already in the matrix, continue
            if char in self.indicies:
                continue

            # special case to handle I, J as they are treated as the same
            if char == 'I' and 'J' in self.indicies or char == 'J' and 'I' in self.indicies:
                continue

            # if it is not already in the matrix, set the current coordinates to the char
            self.matrix[x][y] = char

            # set the indicies in the dictionary
            self.indicies[char] = (x, y)

            # move the pointer forward
            x, y = self.__increment_pointer(i=x, j=y)

            # if you already reached the end of the matrix, break
            if x == -1 and y == -1:
                break

        # ensure it reaches the end
        assert(x == -1 and y == -1)

        # self.__print_matrix()

    def encrypt(self, text: str) -> str:
        """
        Encrypt any text with the built encryption matrix

        Args:
            text (str): the text to encrypt

        Returns:
            encrypted_text (str): the encrypted text
        """

        # remove all spaces in text
        text = text.replace(' ', '')

        # get the digrams of the text
        digrams = self.__diagraminate(text=text)

        # encrypted string that will be returned
        encrypted = ""

        # loop through the digrams
        for digram in digrams:
            # get the two characters in the digram
            first, second = digram[0], digram[1]

            # check which I or J is picked in the matrix
            if first == 'I' and 'I' not in self.indicies:
                first = 'J'
            if first == 'J' and 'J' not in self.indicies:
                first = 'I'

            # get the indicies of the two chars in the matrix
            first_x, first_y = self.indicies[first]
            second_x, second_y = self.indicies[second]

            # case 1: both chars are on the same row
            if first_x == second_x:
                # shift the chars to the right
                encrypted += self.matrix[first_x][(first_y + 1) % self.cols] + self.matrix[second_x][(second_y + 1) % self.cols]

            # case 2: both chars are in the same column
            elif first_y == second_y:
                # shift the chars down
                encrypted += self.matrix[(first_x + 1) % self.rows][first_y] + self.matrix[(second_x + 1) % self.rows][second_y]

            # case 3: both chars are in different rows and columns
            elif first_x != second_x and first_y != second_y:
                # get the opposite corner character
                encrypted += self.matrix[first_x][second_y] + self.matrix[second_x][first_y]

            # case 4: if both rows and columns are equal then we have ran into an issue
            else:
                raise Exception("Cannot have same row and column, error with digramminate")

        # return the encrypted string
        return encrypted

    def decrypt(self, encrypted: str) -> str:
        """
        Decrypt an encrypted text with the built encryption matrix

        Args:
            encrypted (str): the encrypted text to decrypt

        Returns:
            text (str): the decrypted text
        """

        # remove space in the encrypted text
        encrypted = encrypted.replace(' ', '')

        # check to make sure the encrypted text has an even length
        assert(len(encrypted) % 2 == 0)

        # split into chunks of two (no edge case handling required here, guaranteed to be even length)
        digrams = [encrypted[i:i+2] for i in range(0, len(encrypted), 2)]

        # decrypted string that will be returned
        decrypted = ""

        # loop through each digram
        for digram in digrams:
            # get the two characters in the digram
            first, second = digram[0], digram[1]

            # get the indicies of the two chars in the matrix
            first_x, first_y = self.indicies[first]
            second_x, second_y = self.indicies[second]

            # case 1: both chars are on the same row
            if first_x == second_x:
                # shift the chars to the right
                # as we need to handle negative indicies, instead of -1 do +4
                decrypted += self.matrix[first_x][(first_y + 4) % self.cols] + self.matrix[second_x][(second_y + 4) % self.cols]

            # case 2: both chars are in the same column
            elif first_y == second_y:
                # shift the chars up
                # as we need to handle negative indicies, instead of -1 do +4
                decrypted += self.matrix[(first_x + 4) % self.rows][first_y] + self.matrix[(second_x + 4) % self.rows][second_y]

            # case 3: both chars are in different rows and columns
            elif first_x != second_x and first_y != second_y:
                # get the opposite corner character
                decrypted += self.matrix[first_x][second_y] + self.matrix[second_x][first_y]

            # case 4: if both rows and columns are equal then we have ran into an issue
            else:
                raise Exception("Cannot have same row and column, error with digramminate")

        # remove the char X in the decrypted string
        decrypted = decrypted.replace('X', '')

        # final checks
        assert ' ' not in decrypted and 'X' not in decrypted

        # return the decrypted string
        return decrypted

if __name__ == "__main__":
    # basic test
    basic = PlayFair(key='playfair example')
    encrypted = basic.encrypt(text='hide the gold in the tree stump')

    assert encrypted == 'BMODZBXDNABEKUDMUIXMMOUVIF'

    # run the pytests
    # result = subprocess.run(['pytest'], cwd='test', text=True, capture_output=True)

    key = "SUPERSPY"
    cipher = PlayFair(key=key)

    # sample test
    encrypted_text = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    decrypted_text = cipher.decrypt(encrypted=encrypted_text)

    expected_output = 'HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA'
    assert decrypted_text == expected_output

    print(decrypted_text)
