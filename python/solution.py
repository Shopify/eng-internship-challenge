
class Cipher:

    def __init__(self, key: str, cipher: str) -> None:
        self.key = key
        self.cipher = cipher
        self.gridSize = 5
        self.cipherGrid = None
        self.__buildPlayfairGrid()

    def __buildPlayfairGrid(self) -> None:
        """ Build 5 x 5 Playfair grid using a key. """

        # Remove duplicates from key
        seenCharacters = set()
        processedKey = []
        for char in self.key:
            char = char.upper()
            if char not in seenCharacters:
                processedKey.append(char)
                seenCharacters.add(char)

        # Add letters from the alphabet that are not present in key
        alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
        remainingLetters = [char for char in alphabet if char not in seenCharacters] 
        flattenedGrid = processedKey + remainingLetters

        # Unflatten grid
        self.cipherGrid = [list(flattenedGrid[i: i + self.gridSize]) for i in range(0, self.gridSize * self.gridSize, self.gridSize)]



if __name__ == '__main__':
    encryptedMessage = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"
    cipher = "Playfair"

    cipher = Cipher(key=key, cipher=cipher)
    print(cipher.cipherGrid)
