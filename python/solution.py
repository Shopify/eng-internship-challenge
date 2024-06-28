"""
Shopify Engineering Internship Playfair Cypher
Hussein Elguindi
June 28, 2024
"""

from string import ascii_uppercase
from abc import ABC, abstractmethod
from typing import Any, Final, Generator
from itertools import chain


class Cipher(ABC):
    """
    An abstract base class defining the basis of cipher implementations
    
    Methods:
        encrypt: accepts a plaintext string and returns the ciphertext
        decrypt: accepts a ciphertext string and returns the plaintext
    """
    @abstractmethod
    def encrypt(self, plaintext: str) -> str:
        pass

    @abstractmethod
    def decrypt(self, ciphertext: str) -> str:
        pass


class PlayfairCipher(Cipher):
    """
    Implements the Cipher base class for the Playfair cypher scheme

    Methods:
        encrypt: accepts plaintext and returns the Playfair ciphertext
        decrypt: accepts Playfair ciphertext and returns the plaintext
    """
    def __init__(self, cipher_key: str, dimension: int = 5):
        """
        Initializes a new Playfair cipher object

        Attributes:
            cipher_key: a string consisting of only uppercase ASCII letters
            dimension: an optional integer defining the side lengths of the cipher key table
        """
        if not cipher_key.isalpha() or not cipher_key.isupper():
            return ValueError("cipher key must consist of only uppercase ASCII letters")

        # An uncommon character (used to separate identical part digrams)
        # Must not appear in decrypted plaintext
        self.__none_char: Final[str] = "X"
        # A pair of characters that should be treated identically
        self.__identical_chars: Final[tuple[str, str]] = ("I", "J")

        self.__alphabet: Final[str] = ascii_uppercase
        self.__cipher_key: Final[str] = cipher_key
        self.__dimension: Final[int] = dimension

        self.__table: list[str]
        self.__adjacency: dict[str, tuple[int, int]]
        self.__build_table()

    def __build_table(self):
        """
        Builds the cipher key table and adjacency map to be used for encryption/decryption
        """
        # The key table
        self.__table = [""] * (self.__dimension**2)
        # Stores (row, col) indices of each char in the key table (to optimize searching during encryption/decryption)
        self.__adjacency = {}

        # Populate the table with the cipher key, followed by the alphabet, without repeated characters
        table_index = 0
        for char in chain(self.__cipher_key, self.__alphabet):
            # The table is filled
            if table_index >= len(self.__table):
                break

            # The character was repeated
            if char in self.__adjacency:
                continue

            # Only one of the identical characters can appear
            a, b = self.__identical_chars
            if (char == a and b in self.__adjacency
                or char == b and a in self.__adjacency
            ):
                continue

            self.__table[table_index] = char
            # Convert index into (row, col)
            self.__adjacency[char] = divmod(table_index, self.__dimension)
            table_index += 1

    def __digrams(self, text: str) -> Generator[tuple[str, str], Any, None]:
        """
        A generator function yielding consecutive digrams from a string

        Args:
            text: any string
        """
        i = 0
        while i < len(text) - 1:
            a, b = text[i], text[i + 1]

            # Separate pairs with identical characters using an uncommon character
            if a == b:
                yield (a, self.__none_char)
                # Only increment by 1 to handle the other character in the pair
                i += 1
                continue

            yield (a, b)
            i += 2

        # If the text length is odd, the digram is the last character and an uncommon character
        if len(text) % 2 == 1:
            yield (text[-1], self.__none_char)

    def __transform_digram(self, a: str, b: str, diff: int) -> str:
        """
        Applies transformations on a digram as described by https://en.wikipedia.org/wiki/Playfair_cipher
        The extent of a transformation can customized using the "diff" attribute

        Attributes:
            a: the first character of the digram
            b: the second character of the digram
            diff: an integer specifying the amount to shift a character when applying a transformation,
                for a standard Playfair cypher, this is often -1 for decrypt and 1 for encrypt
        """
        a_row, a_col = self.__adjacency[a]
        b_row, b_col = self.__adjacency[b]

        # Wraps an index around the key table dimensions
        def wrap(i: int):
            return i % self.__dimension

        # Case 1: the pair appears on the same row
        if a_row == b_row:
            offset = a_row * self.__dimension
            i1, i2 = offset + wrap(a_col + diff), offset + wrap(b_col + diff)

        # Case 2: the pair appears on the same column
        elif a_col == b_col:
            i1, i2 = (
                a_row * self.__dimension + wrap(a_col + diff),
                b_row * self.__dimension + wrap(b_col + diff),
            )

        # Case 3: the pair makes a rectangle on the table
        else:
            # Swap columns (i.e. get opposite corners on the rectangle)
            a_col, b_col = b_col, a_col
            i1, i2 = a_row * self.__dimension + a_col, b_row * self.__dimension + b_col

        return self.__table[i1] + self.__table[i2]

    def encrypt(self, plaintext: str) -> str:
        # This is similar to the decrypt method except the "diff" parameter for transform_digram should be set to 1. That's all!
        # Omitted out for the sake of brevity.
        raise NotImplementedError("not yet implemented!")

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts ciphertext into plaintext according the Playfair cipher scheme

        Attributes:
            ciphertext: a string consisting of ASCII letters
        """
        if not ciphertext.isalpha():
            raise ValueError("ciphertext must consist of ASCII letters")

        ciphertext = ciphertext.upper()

        # Ensure that identical characters are treated identically
        a, b = self.__identical_chars
        if a in self.__adjacency:
            ciphertext = ciphertext.replace(b, a)
        else:
            ciphertext = ciphertext.replace(a, b)

        # Transforming each digram of the ciphertext yields the plaintext
        plaintext = "".join(
            self.__transform_digram(a, b, diff=-1)
            for a, b in self.__digrams(ciphertext)
        )
        # The plaintext is guaranteed to consist of only uppercase ASCII letters
        return plaintext.replace(self.__none_char, "")


def main():
    cipher_key = "SUPERSPY"
    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

    cipher: Cipher = PlayfairCipher(cipher_key)
    plaintext = cipher.decrypt(ciphertext)
    print(plaintext)

if __name__ == "__main__":
    main()
