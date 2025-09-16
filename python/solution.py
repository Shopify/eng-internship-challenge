class PlayfairCipherSolver():
    
    def generate_key_table(self, keyword:str) -> list[list[str]]:
        """
        Creates 5 x 5 table using the key, according to Playfair cipher rules
        Cipher Version: "I" and "J" are interchangeable, so "J" is removed from alphabet
        """

        ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        keyTable = []
        tableChars = []

        # Add letters of keyword, dropping any duplicates
        for char in keyword.upper().replace("J","I"):
            if char not in tableChars and char.isalpha():
                tableChars.append(char)
        # Add remaining letters of alphabet
        for char in ALPHABET:
            if char not in tableChars:
                tableChars.append(char)

        # Create 5 x 5 table
        for i in range(0, 25, 5):
            keyTable.append(tableChars[i:i+5])

        return keyTable
    
    def split_to_digram(self, message:str) -> list[str]:
        """
        Splits the message into digrams (pairs of two letters)
        """
        messageChars = []
        # Remove non-alphabetic characters and convert to uppercase
        for char in message.upper().replace("J","I"):
            if char.isalpha():
                messageChars.append(char)
        
        # Add padding if necessary
        if len(messageChars) % 2 != 0:
            messageChars.append("X")
        
        # Split into digrams and return
        return [messageChars[i:i+2] for i in range(0, len(messageChars), 2)]
    
    def find_char_position(self, char:str, keyTable:list):
        """
        Finds the (row, col) position of a character in the key table
        """
        for i, row in enumerate(keyTable):
            if char in row:
                return (i, row.index(char))
        return None
    
    def decrypt(self, message:str, keyword:str) -> str:
        """
        Decrypts the message using the keyword
        Final message can be obtained by removing "X" or "Q" that don't make sense, if applicable
        
        'X' is the padding character and removed, based on the test case provided
        """
        keyTable = self.generate_key_table(keyword)
        digrams = self.split_to_digram(message)
        decryptedMessage = []
        
        for digram in digrams:
            # Find (row,col) positions for the two characters in the key table
            char1Pos = self.find_char_position(digram[0], keyTable)
            char2Pos = self.find_char_position(digram[1], keyTable)
            
            # If the characters are in the same row, shift back one position
            if char1Pos[0] == char2Pos[0]:
                decryptedMessage += keyTable[char1Pos[0]][(char1Pos[1]-1)%5] + keyTable[char2Pos[0]][(char2Pos[1]-1)%5]
            # If the characters are in the same column, shift up one position
            elif char1Pos[1] == char2Pos[1]:
                decryptedMessage += keyTable[(char1Pos[0]-1)%5][char1Pos[1]] + keyTable[(char2Pos[0]-1)%5][char2Pos[1]]
            # If the characters form a rectangle, take same rows and opposite columns to get opposite corners
            else:
                decryptedMessage += keyTable[char1Pos[0]][char2Pos[1]] + keyTable[char2Pos[0]][char1Pos[1]]
        
        return "".join(decryptedMessage).replace("X","")

if __name__ == "__main__":
    playfairSolver = PlayfairCipherSolver()
    MESSAGE = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    KEYWORD = "SUPERSPY"
    print(playfairSolver.decrypt(MESSAGE, KEYWORD))