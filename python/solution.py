from typing import Tuple, List
class Cipher:

    def __init__(self, key: str, cipherName: str) -> None:
        self.key = key
        self.cipherName = cipherName
        self.gridSize = 5
        self.cipherGrid = None
        self.gridCollection = {}
        self.__buildPlayfairGrid()
        self.__buildGridCollection()

    def __buildPlayfairGrid(self) -> None:
        """ Build 5 x 5 Play fair grid using the key. """

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

    def __buildGridCollection(self) -> None:
        """ Build a dictionary of letters with respect to their grid location. """

        for i in range(len(self.cipherGrid)):
            for j in range(len(self.cipherGrid[0])):
                self.gridCollection[self.cipherGrid[i][j]] = (i, j)


    def decrypt(self, encryptedMessage: str) -> None:
        """
        Decrypt an encrypted message given a key.
        Args:
            encryptedMessage: encrypted message to be decrypted.

        Returns:
            decryptedMessage: decrypted message.
        """

        decryptedMessage = ''
        
        bigrams = self.__buildBigrams(encryptedMessage)
        



    def __buildBigrams(self, text: str) -> List[Tuple[str, str]]:
        """
        Creates bigrams of characters from a text.
        Args:
            text: string to be divided into bigrams of its characters.

        Returns:
            bigrams of text.
        """

        text = text.upper()
        bigrams = []
        i = 0
        while i < len(text) - 1:
            if text[i] == text[i + 1]:
                bigrams.append((text[i], 'X'))
                i += 1
            else:
                bigrams.append((text[i], text[i + 1]))
                i += 2
        # Check if last character was not considered
        if i == len(text) - 1:
            bigrams.append((text[i], 'X'))
        
        return bigrams



if __name__ == '__main__':
    encryptedMessage = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"
    cipherName = "Playfair"

    cipher = Cipher(key=key, cipherName=cipherName)
    print(cipher.gridCollection)
    message = cipher.decrypt(encryptedMessage)
