import string
from collections import defaultdict
from typing import Dict, List, Set, Tuple


class PlayfairCipher:
    ALPHABET = string.ascii_uppercase
    FILLER_LETTER = 'X'
    ROWS = 5
    COLUMNS = 5
    key_table_dict: Dict[str, Tuple[int, int]] = defaultdict()

    def __init__(self, key: str):
        self.key = ''.join(key.upper().split())

    def validate_input(self, s: str) -> str:
        s = ''.join(s.split())
        if not (s.isalpha() and s.isupper()):
            raise ValueError(
                "Input must only consist of uppercase alphabetical characters")
        return s

    def filter_duplicate_letters(self, string: str, letters_to_omit: Set[str] = set()) -> List[str]:
        '''
        Filters out duplicate letters as well as the letters, if any, in `letters_to_omit`
        from the `string`.
        '''
        return [
            char for char in string
            if not ((char in letters_to_omit) or letters_to_omit.add(char))
        ]

    def generate_key_table(self) -> List[List[str]]:
        '''
        Generates a 5 * 5 table by first populating it with the key stripped of duplicate letters,
        followed by the rest of the alphabet. I and J are treated as the same letter, J is omitted.
        '''
        filtered_key = self.filter_duplicate_letters(self.key)
        letters_to_omit = set(filtered_key).union(set("J"))
        alphabet = self.filter_duplicate_letters(self.ALPHABET, letters_to_omit)
        key_table = []
        row = 0
        col = 0

        for i in range(0, len(filtered_key)):
            row = i // self.ROWS
            col = i % self.COLUMNS
            if col == 0:
                key_table.append([])
            letter = filtered_key[i]
            key_table[row].append(letter)
            self.key_table_dict[letter] = (row, col)

        col = (col + 1) % self.COLUMNS

        for letter in alphabet:
            if col == 0:
                if row == 4:
                    break
                row += 1
                key_table.append([])
            key_table[row].append(letter)
            self.key_table_dict[letter] = (row, col)
            col = (col + 1) % self.COLUMNS

        return key_table

    def locate_digram(self, digram: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        '''
        Returns a tuple of the location of the letters of the digram
        '''
        first_letter, second_letter = digram
        first_letter_coordinates = self.key_table_dict[first_letter]
        second_letter_coordinates = self.key_table_dict[second_letter]
        return first_letter_coordinates, second_letter_coordinates

    def decrypt_cipher(self, ciphertext: str) -> str:
        ciphertext = self.validate_input(ciphertext)

        if len(ciphertext) % 2 != 0:
            ciphertext += self.FILLER_LETTER

        plaintext = ""
        key_table = self.generate_key_table()

        for i in range(0, len(ciphertext), 2):
            digram = ciphertext[i:i + 2]
            letter1_location, letter2_location = self.locate_digram(digram)
            letter1_row, letter1_col = letter1_location
            letter2_row, letter2_col = letter2_location
            if letter1_row == letter2_row:
                plaintext += key_table[letter1_row][(letter1_col - 1) % self.COLUMNS]
                plaintext += key_table[letter2_row][(letter2_col - 1) % self.COLUMNS]
            elif letter1_col == letter2_col:
                plaintext += key_table[(letter1_row - 1) % self.ROWS][letter1_col]
                plaintext += key_table[(letter2_row - 1) % self.ROWS][letter2_col]
            else:
                plaintext += key_table[letter1_row][letter2_col]
                plaintext += key_table[letter2_row][letter1_col]

        return plaintext.replace(self.FILLER_LETTER, '')


cipher = PlayfairCipher("SUPERSPY")
ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
print(cipher.decrypt_cipher(ciphertext))
