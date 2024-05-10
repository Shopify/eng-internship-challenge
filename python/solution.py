class cipher_solver:
    def __init__(self, key: str):
        self.key = key.upper()

        self.key_table_size = 5
        self.key_table = [
            ["" for _ in range(self.key_table_size)] for _ in range(self.key_table_size)
        ]
        self.key_table_map = {}

        self.generate_key_table()

    def generate_key_table(self):
        """
        Generates:
            1. self.key_table: 2-D array of size self.key_table_size x self.key_table_size.
            2. self.key_table_map: Dictionary mapping each key to its indices in the key table.
        """
        cur_pos = 0
        parsed = set()

        # Fill in the key table with the provided key.
        for char in self.key:
            if char not in parsed:
                cur_row = cur_pos // self.key_table_size
                cur_col = cur_pos % self.key_table_size

                self.key_table[cur_row][cur_col] = char
                self.key_table_map[char] = (cur_row, cur_col)

                cur_pos += 1
                parsed.add(char)

        # Fill in the key table with the rest of the alphabet.
        # Exclude "J"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for char in alphabet:
            if char not in parsed and char != "J":
                cur_row = cur_pos // self.key_table_size
                cur_col = cur_pos % self.key_table_size

                self.key_table[cur_row][cur_col] = char
                self.key_table_map[char] = (cur_row, cur_col)

                cur_pos += 1

        assert cur_pos == 25, "Key table has not been filled properly"

    def shift_row_col(self, row_or_col: int, offset: int):
        """Shifts a given row or column by the offset and returns the result with wraparound.

        Args:
            row_or_col (int): Starting position.
            offset (int): Amount to move by

        Returns:
            int: Resulting position with wraparound.
        """
        assert (
            type(row_or_col) == int and type(offset) == int
        ), "Parameters must be type int."

        row_or_col += offset

        # Negative case
        if row_or_col < 0:
            return (self.key_table_size + row_or_col) % self.key_table_size
        # Positive & zero case
        else:
            return row_or_col % self.key_table_size

    def decrypt(self, encrypted: str):
        """Decrypts an encrypted string.

        Args:
            encrypted (str): Encrypted string to decrypt.

        Returns:
            str: Decrypted string with "X"s, spaces, and special characters removed.
        """
        pairs = [
            [encrypted[i], encrypted[i + 1]] for i in range(0, len(encrypted) - 1, 2)
        ]

        for i, (char_1, char_2) in enumerate(pairs):
            char_1_row, char_1_col = self.key_table_map[char_1]
            char_2_row, char_2_col = self.key_table_map[char_2]

            row_diff = abs(char_1_row - char_2_row)
            col_diff = abs(char_1_col - char_2_col)

            # Case 1: Rectangle
            if row_diff > 0 and col_diff > 0:
                char_1_decrypted = self.key_table[char_1_row][char_2_col]
                char_2_decrypted = self.key_table[char_2_row][char_1_col]
            # Case 2: Row
            elif row_diff == 0 and col_diff > 0:
                char_1_decrypted = self.key_table[char_1_row][
                    self.shift_row_col(char_1_col, -1)
                ]
                char_2_decrypted = self.key_table[char_2_row][
                    self.shift_row_col(char_2_col, -1)
                ]
            # Case 3: Column
            elif row_diff > 0 and col_diff == 0:
                char_1_decrypted = self.key_table[self.shift_row_col(char_1_row, -1)][
                    char_1_col
                ]
                char_2_decrypted = self.key_table[self.shift_row_col(char_2_row, -1)][
                    char_2_col
                ]

            pairs[i] = [char_1_decrypted, char_2_decrypted]

        # Post processing
        result = []
        [result.extend(pair) for pair in pairs]
        result = "".join(result)
        result = result.replace("X", "")
        return result

solver = cipher_solver("SUPERSPY")
print(solver.decrypt("IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"))
