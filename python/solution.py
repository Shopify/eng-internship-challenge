class PlayfairCipher:
    def __init__(self, key):
        self.key = key
        self.grid = self.generate_playfair_grid()

    def generate_playfair_grid(self):
        '''generate_playfair_grid method creates the playfair grid based on the key passed
        Our grid will be our key followed by the alphabet, with duplicates removed in order'''
        key = self.key.upper().replace("J", "I") # ensure upper case and remove J
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        key += alphabet

        playfair_grid = "" # We will add letters onto this string when not already included (no duplicates)
        for letter in key:
            if letter not in playfair_grid:
                playfair_grid += letter

        # Now, we need to keep track of the position of each character in our grid
        char_positions = {}  # Initialize an empty dict to store each character position
        for i, char in enumerate(playfair_grid):
            row = i // 5 # Floored division for each row
            col = i % 5 # Mod5 for each col
            char_positions[char] = (row, col) # Tuple containing each char's position


        return playfair_grid, char_positions # Returns grid and positions of each character

    def get_char_from_position(self, row, col):
        ''' get_char_from_position method retrieves the character in the grid based on the position (row, col).
           We are using a list to represent our grid, therefore to map our 2D grid index to our 1D list,
           we use row*5 + col to index the grid position.'''
        playfair_grid, _ = self.grid

        return playfair_grid[row*5 + col]


    def decrypt(self, message):
        ''' decrypt method will decrypt a given message and return the decrypted.
        We assume that J is not included and that the number of elements are even since it must have been
        encrypted under the same assumption set. We loop through the message and remove pairs of letter as we
        decrypt them and add them into our decrypted string'''

        # Raise an exception if our message does not meet our expected format
        if len(message) % 2 != 0 or "J" in message:
            raise Exception("Encrypted Message does not meet requirements, contains J or has odd # of elements")

        playfair_grid, char_positions = self.grid # Obtain the grid and the positions of each char
        # Here are some print statements to look at the playfair grid
        # print(playfair_grid[0:5])
        # print(playfair_grid[5:10])
        # print(playfair_grid[10:15])
        # print(playfair_grid[15:20])
        # print(playfair_grid[20:25])
        message = message.upper() # ensure upper case

        decrypted_message = ""
        while len(message) > 0:
            # Characters
            char1 = message[0]
            char2 = message[1]
            # Character positions
            row1, col1 = char_positions[char1]
            row2, col2 = char_positions[char2]

            if col1 == col2: # both char in same column case: Pick item above each char, wrap to bottom if needed

                next_row1 = (row1 - 1) % 5
                next_row2 = (row2 - 1) % 5

                # Add two decrypted letters in same column with next_rows
                decrypted_message += self.get_char_from_position(next_row1, col1) + \
                                     self.get_char_from_position(next_row2, col2)

            elif row1 == row2: # both char in same row case: Pick item left of char, wrap right if needed

                next_col1 = (col1 - 1) % 5
                next_col2 = (col2 - 1) % 5

                # Add two decrypted letters in same row with next_cols
                decrypted_message += self.get_char_from_position(row1, next_col1) + \
                                     self.get_char_from_position(row2, next_col2)

            else: # Different column and row, rectangle case: Swap indexes to get opposite corners of rectangle
                decrypted_message += self.get_char_from_position(row1, col2) + \
                                     self.get_char_from_position(row2, col1)

            # Remove decrypted pair of characters and move onto the next pair
            message = message[2:]

        # Remove X's from end result as required
        decrypted_message = decrypted_message.replace("X","")
        return decrypted_message

# example where key = "superspy", text = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
if __name__ == '__main__':
    cipher = PlayfairCipher("superspy")
    decrpyted_message = cipher.decrypt("IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV")
    print(decrpyted_message)