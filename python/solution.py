"""
Shopify Engineering Intern Fall 2024 Technical Challenge: Playfair Cipher
Date: May 14, 2024
Author: Divya Prasad
"""

class PlayfairCipher:
    def __init__(self, key: str, message: str):
        self.key = key.upper()
        self.message = message.upper()
        self.table = self.table_generation()

    def table_generation(self) -> str:
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J is omitted here
        table_str = ""
        used_alphabets = set()  # ensure no duplicates are added
        for char in (
            self.key + alphabet
        ):  # will go through the key first, then the rest of the alphabet
            if char.isalpha() and char not in used_alphabets:
                # Making sure that J is treated like an I here
                if char == "I" or char == "J":
                    used_alphabets.add("J")
                    used_alphabets.add("I")
                else:
                    used_alphabets.add(char)
                table_str += char
        table_returned = table_str[
            0:25
        ]  # only returns the 5x5 matrix (25 letters in total)
        return table_returned

    def row_col_position_getter(self, char: str) -> tuple:
        for i in range(len(self.table)):
            if self.table[i] == char:
                return (i // 5, i % 5)  # returns (row, col)
        return (-1, -1)  # returns -1 to signify not found

    def find_pairs(self) -> list:
        message = self.message.replace(" ", "")  # removes spaces
        pairs = []
        i = 0
        while i < len(message):
            first = message[i]
            if i + 1 < len(message):
                second = message[i + 1]
                if first != second:
                    pairs.append((first, second))
                    i += 2  # moves onto the next pair by increasing it by 2
                else:
                    pairs.append((first, "X"))  # handles duplicates in the input string
                    i += 1
            else:
                pairs.append((first, "X"))  # handles odd length messages
                i += 1

        return pairs

    def decrypter(self, pairs: list) -> str:
        decrypted_message = ""

        for num_1, num_2 in pairs:
            row_1, col_1 = self.row_col_position_getter(num_1)
            row_2, col_2 = self.row_col_position_getter(num_2)

            # Handles case where character is not found in table
            if row_1 == -1 or row_2 == -1 or col_1 == -1 or col_2 == -1:
                decrypted_message += "X"  # Replace with default 'X' character
                continue

            # Case 1: Same row, move left
            if row_1 == row_2:
                decrypted_message += self.table[row_1 * 5 + ((col_1 - 1) % 5)]
                decrypted_message += self.table[row_2 * 5 + ((col_2 - 1) % 5)]
            # Case 2: Same column, move up
            elif col_1 == col_2:
                decrypted_message += self.table[((row_1 - 1) % 5) * 5 + col_1]
                decrypted_message += self.table[((row_2 - 1) % 5) * 5 + col_2]
            # Case 3: Rectangle Swap
            else:
                decrypted_message += self.table[row_1 * 5 + col_2]
                decrypted_message += self.table[row_2 * 5 + col_1]

        # Get rid of extra X's
        decrypted_message = decrypted_message.replace("X", "")
        return decrypted_message


def main():
    key = "SUPERSPY"
    message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    cipher = PlayfairCipher(key, message)
    pairs = cipher.find_pairs()
    decrypted_message = cipher.decrypter(pairs)
    print(decrypted_message)


if __name__ == "__main__":
    main()
