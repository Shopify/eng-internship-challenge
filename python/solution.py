# Shopify Engineering Internship Challenge
# Playfair Cipher Solver
# Faseeh Irfan
# University of Waterloo Software Engineering

class PlayFairCipher:
    # Constructor, I wanted to generalize this so it can work for different keys.
    # Hence why it takes in the key and message. 
    def __init__(self, key, message):
        self.key = key
        self.message = message
        self.grid = self.gridGen(key)

    # Generated the grid based on the key
    def gridGen(self, key):
        # Excluding J so we can have 5x5 grid,
        # We can technically pick any letter as long as both parties know,
        # but J is most common
        letters = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' 

        # orignally thought about using 2D Lists, but using a single list
        # and using modulo 5 to get the row and col is much simpler
        grid = []
        seen = set()
        # first append the key to beginning of the grid 
        for char in key:
            if char not in seen:
                grid.append(char)
                seen.add(char)
        # then append the rest of the letters
        for char in letters:
            if char not in seen:
                grid.append(char)
                seen.add(char)
        return grid

    def findCharPos(self, char):
        # Returns the Row and Col of the character in the grid
        # Using division and modulo on the index of the character, 
        # since I've implemented the grid as a 1D array
        ind = self.grid.index(char)
        return ind // 5, ind % 5
    
    def findChar(self, r, c):
        # Returns the character at position (r, c) in the grid
        return self.grid[r*5 + c]
    
    def decryptPair(self, pair):
        # Find the positions of the characters in the grid
        r1, c1 = self.findCharPos(pair[0])
        r2, c2 = self.findCharPos(pair[1])

        # check if the pair is in same row or same column
        # using modulo to wrap around the grid
        if r1 == r2: #shift left
            c1 = (c1 - 1) % 5
            c2 = (c2 - 1) % 5
        elif c1 == c2: #shift up
            r1 = (r1 - 1) % 5
            r2 = (r2 - 1) % 5
        else: # if they form a diagonal, swap the columns
            c1, c2 = c2, c1

        decryptedPair = self.findChar(r1, c1) + self.findChar(r2, c2)
        # getting rid of X's in the new pair and return
        return decryptedPair.replace('X', '')
        
    def decryption(self):    
        result = ''

        # loop through the message and decrypt pair by pair, appending to result as we go
        for i in range(0, len(self.message), 2):
            pair = self.message[i:i+2]
            result += self.decryptPair(pair)

        return result
    
if __name__ == "__main__":
    message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"
    cipher = PlayFairCipher(key, message)
    result = cipher.decryption()
    print(result)

