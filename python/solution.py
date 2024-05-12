







class PlayfairCipher():
    def __init__(self, key:str="", grid_letters:str="ABCDEFGHIKLMNOPQRSTUVWXYZ"): # J is excluded from grid letters
        self.key = key
        self.grid_letters = grid_letters
        self.grid = [] # stores letters
        self.indices = {} # stores indices as values, letters as keys

    def _create_playfair_grid(self, key:str, grid_letters:str):
        # Build the grid using a 1D list
        for c in key + grid_letters: # prepend the key to ensure it is added first
            if len(self.grid) == 25:  # size of grid must be 5 x 5
                break
            if c not in self.indices:
                self.grid.append(c) 
                self.indices[c] = len(self.grid) - 1

    def decrypt(self, message: str) -> str:
        decoded_message = ""  # append decoded chunks to return
        self._create_playfair_grid(self.key, self.grid_letters)

        # process by chunks of two letters
        for i in range(0, len(message), 2):
            chunk = message[i:i+2]
            # row is obtained from the 1D index by integer division of 5, column by remainder
            # note: the 1D index can be reconstructed from row * 5 + col
            row1, col1 = divmod(self.indices[chunk[0]], 5)
            row2, col2 = divmod(self.indices[chunk[1]], 5)
            # scenario 1: same row
            if row1 == row2:
                col1 = (col1 - 1) % 5  # take remainder in case of wrap around
                col2 = (col2 - 1) % 5
            # scenario 2: same column
            elif col1 == col2:
                row1 = (row1 - 1) % 5
                row2 = (row2 - 1) % 5
            # scenario 3: rectangle -> swap the columns to get the opposite corner
            else:
                col1, col2 = col2, col1  # Swap columns
            
            # reconstruct the 1D indices to get the decoded letters
            decoded_message += self.grid[row1 * 5 + col1] + self.grid[row2 * 5 + col2]

        # clean up X's
        return decoded_message.replace("X", "")

if __name__ == "__main__":
    cipher = PlayfairCipher(key="SUPERSPY")
    decoded_message = cipher.decrypt("IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV")
    print(decoded_message)

