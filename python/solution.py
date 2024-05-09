class PlayfairCipherSolver:
    def __init__(self, key):
        """
        Initialize cipher with key
        Stores alphabet without 'J' and defines special characters that are not allowed in input
        
        :param key: string to be used as key to generate cipher grid
        """
        self.LETTERS = "ABCDEFGHIKLMNOPQRSTUVWXYZ" # Alphabet without 'J' for 5x5 matrix (25 letters)
        self.SPECIAL = "!@#$%^&*()_+-=[]{}|;':,.<>?/`~" # Special characters that are not allowed
        self.key = self.prepare_key(key) # Process key to meet cipher requirements
        self.grid = self.create_grid() # Create cipher grid using processed key
    
    def prepare_key(self, key):
        """
        Prepares key by removing 'J', spaces, and converting all characters to uppercase
        Ensures key only contains valid characters from defined alphabet
        
        :param key: string key originally provided
        :return: string that has been processed to fit cipher requirements
        """
        return key.replace("J", "I").replace(" ", "").upper()

    def create_grid(self):
        """
        Creates 5x5 grid from processed key, filling in with additional letters from alphabet
        Ensures no repeated letters in grid, and fills from left to right, top to bottom
        
        :return: list of strings representing 5x5 grid
        """
        grid_letters = ""
        for char in self.key:
            if char not in grid_letters:
                grid_letters += char

        for char in self.LETTERS:
            if char not in grid_letters:
                grid_letters += char
        
        return [grid_letters[i * 5:(i + 1) * 5] for i in range(5)]

    def search_grid(self, letter):
        """
        Searches for position of letter in grid
        Returns row and column as tuple where letter is located
        
        :param letter: single character to find in grid
        :return: tuple (row, column) indicating position of letter in grid
        """
        for i in range(5):
            for j in range(5):
                if self.grid[i][j] == letter:
                    return (i, j)
        return None

    def decipher(self, message):
        """
        Deciphers message using Playfair cipher rules
        Handles message adjustments for characters appearing in pairs and adjusts grid look-up based on Playfair rules
        
        :param message: string message to be deciphered
        :return: string representing deciphered message
        """
        if any(char in message for char in self.SPECIAL):
            return
        
        message = message.replace("J", "I").replace(" ", "").upper()
        if len(message) % 2 != 0:
            message += "X"

        result = ""
        for i in range(0, len(message), 2):
            if message[i] == message[i + 1]:
                message = message[:i + 1] + "X" + message[i + 1:]

            a, b = self.search_grid(message[i]), self.search_grid(message[i + 1])

            if a[0] == b[0]:
                result += self.grid[a[0]][(a[1] - 1) % 5] + self.grid[b[0]][(b[1] - 1) % 5]
            elif a[1] == b[1]:
                result += self.grid[(a[0] - 1) % 5][a[1]] + self.grid[(b[0] - 1) % 5][b[1]]
            else:
                result += self.grid[a[0]][b[1]] + self.grid[b[0]][a[1]]

        return result.replace("X", "").replace(" ", "")

if __name__ == '__main__':
    key = "SUPERSPY"
    message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    cipher = PlayfairCipherSolver(key)
    decrypted_message = cipher.decipher(message)
    print(decrypted_message)
