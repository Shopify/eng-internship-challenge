from typing import Tuple


class PlayFairDecoder:
    """
    This class decodes an encoded string using a Playfair Cipher for a given key
    """

    def __init__(self, key: str) -> None:
        """
        Creates a Playfair Decoder object and the grid used to decode an encoded string

        :param key: the key used to encode a string
        """
        self.key = key.upper()
        self.grid = []
        self._create_grid()

    def _create_grid(self) -> None:
        """
        Creates the grid used to encode/decode a string
        """
        # set I = J, J is also not used in our encoded string
        ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        # set to keep track of characters we have already used in the grid
        seen_chars = set()
        # int to keep track of how many characters we have in a row
        char_count = 0
        # row to add to the gird
        row = []

        # add the characters in the key to the gird first
        for char in self.key:
            # if char_cnt = 4, add row to the grid and create a new empty one
            if char_count == 5:
                self.grid.append(row)
                row = []
                char_count = 0
            # make sure only new chars are added to the grid
            if char not in seen_chars:
                seen_chars.add(char)
                row.append(char)
                char_count += 1

        # add the rest of the alphabet
        for char in ALPHABET:
            if char_count == 5:
                self.grid.append(row)
                row = []
                char_count = 0
            # make sure only new chars are added to the grid
            if char not in seen_chars:
                # note: we do not need to add to seen_chars because the characters in alphabet is already unique
                row.append(char)
                char_count += 1
        self.grid.append(row)

    def decode(self, encoded_string: str) -> str:
        """
        Decodes an encoded string

        :param encoded_string: the encoded string you want to decipher
        :return: the decoded string
        """
        decoded_string = ""

        for i in range(0, len(encoded_string), 2):
            first_char_pos = self._get_char_pos(encoded_string[i])
            second_char_pos = self._get_char_pos(encoded_string[i + 1])

            # determine which encoding rule was used

            # same row
            if first_char_pos[0] == second_char_pos[0]:
                # check if shifted char was at the start of the row
                if first_char_pos[1] == 0:
                    decoded_string += self.grid[first_char_pos[0]][4]
                else:
                    decoded_string += self.grid[first_char_pos[0]][first_char_pos[1] - 1]

                # check if shifted char was at the start of the row
                if second_char_pos[1] == 0:
                    decoded_string += self.grid[second_char_pos[0]][4]
                else:
                    decoded_string += self.grid[second_char_pos[0]][second_char_pos[1] - 1]

            # same column
            elif first_char_pos[1] == second_char_pos[1]:
                # check if shifted char was at the start of the column
                if first_char_pos[0] == 0:
                    decoded_string += self.grid[4][first_char_pos[1]]
                else:
                    decoded_string += self.grid[first_char_pos[0] - 1][first_char_pos[1]]

                # check if shifted char was at the start of the row
                if second_char_pos[0] == 0:
                    decoded_string += self.grid[4][second_char_pos[1]]
                else:
                    decoded_string += self.grid[second_char_pos[0] - 1][second_char_pos[1]]

            # they are on opposite sides of a box
            else:
                decoded_string += self.grid[first_char_pos[0]][second_char_pos[1]]
                decoded_string += self.grid[second_char_pos[0]][first_char_pos[1]]

        # iterate over the decoded string and remove any Xs and return
        return ''.join([char for char in decoded_string if char != 'X'])

    def _get_char_pos(self, target_char: str) -> Tuple[int, int]:
        """
        Returns the position of a char in the encoding/decoding grid

        :param target_char: the char you want the position of
        :return: tuple of the index the char is in the grid
        """
        for i, row in enumerate(self.grid):
            for j, cur_char in enumerate(row):
                if cur_char == target_char:
                    return i, j


if __name__ == '__main__':
    KEY = "SUPERSPY"
    ENCODED_STRING = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    decoder = PlayFairDecoder(KEY)
    print(decoder.decode(ENCODED_STRING))
