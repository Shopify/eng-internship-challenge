from collections import deque, OrderedDict


class SpyCityCodeCracker:
    """
    SpyCityCodeCracker Class contains all the necessary functions to decrypt the encrypted message.
    Note: You might notice a lot of type checking in my functions, I do that, so I catch expected type mismatch
          errors early on while writing code.

    Let's Get to Spy City!
    """
    def __init__(self, cipherKey: str, encryptedMessage: str):
        self.cipherKey = cipherKey.upper()
        self.encryptedMessage = encryptedMessage.upper()

    def createKeyTable(self) -> list[list[str]]:
        """
        Sanitized Key filters redundant characters and puts them in a queue for ease of popping key values into
        the matrix, followed by the remaining alphabet

        Note: I did not account for J, since the message does not contain the letter J, and a lot of cipher key tables
        choose to omit it or use it interchangeably with the letter I.
        """
        sanitizedKey = deque(OrderedDict.fromkeys(self.cipherKey.upper()))
        alphabet = deque(
            chr(char) for char in range(ord('A'), ord('Z') + 1) if (char != ord('J') and chr(char) not in sanitizedKey))
        cipherMatrix = [[] for _ in range(5)]
        for i in range(25):
            if sanitizedKey:  # i // 5 -> controls the column index without overflowing from 0 to 4
                cipherMatrix[i // 5].append(sanitizedKey.popleft())
                continue
            cipherMatrix[i // 5].append(alphabet.popleft())

        return cipherMatrix

    def pairEncryptedMessage(self) -> list[str]:
        """
        Every encrypted message has even length since they are encrypted in pairs, and it would later be
        easier to use and debug these pairs while finding their decrypted letter pairs.
        """
        pairs = []
        message, length, i = self.encryptedMessage, len(self.encryptedMessage) + 1, 0
        for pair in range(2, length, 2):
            pairs.append(message[i:pair])
            i += 2
        return pairs

    def searchChar(self, char: chr) -> (int, int):
        """
        This function searches a letter in every column of the matrix, and returns the (col, row) index tuple.
        """
        cipherMatrix = self.createKeyTable()
        for col in range(len(cipherMatrix)):
            if char in cipherMatrix[col]:
                return col, cipherMatrix[col].index(char)
        raise ValueError(f"{char} not found in the Cipher Matrix.")

    def decrypt(self) -> str:
        """
        The Decrypting Concept is simple: Reverse the methods use to encrypt the message
        1. Create the Key Table from the Cipher Key and pair up the encrypted message
        2. For every pair:
            a, if they are both on the same column then move their row index to the left by one unit
            b, or they are both on the same row then move their column index to the up by one unit
            c, and if they are neither in the same column nor row, they form a rectangle from the corner of their
               indices, then exchange their rows index, so they move to the opposite horizontal corner.
        Note: if index is in the left corner or bottom, it is moved circularly back to right corner or top respectively.

        3. Filter all 'X's, spaces, or special characters. (I could have created a separate function for serialization
        but creating a function in python has overhead costs and I decided to serialize in the return statement.)
        """
        decryptedString, encryptedPairs, cipherMatrix = "", self.pairEncryptedMessage(), self.createKeyTable()
        for char1, char2 in encryptedPairs:
            colChar1, rowChar1 = self.searchChar(char1)
            colChar2, rowChar2 = self.searchChar(char2)

            if colChar1 == colChar2:  # Same column
                newRowChar1, newRowChar2 = rowChar1 - 1 if rowChar1 - 1 > -1 else 4, rowChar2 - 1 if rowChar2 - 1 > -1 else 4
                decryptedString += f'{cipherMatrix[colChar1][newRowChar1] + cipherMatrix[colChar2][newRowChar2]}'
            elif rowChar1 == rowChar2:  # Same row
                newColChar1, newColChar2 = colChar1 - 1 if colChar1 - 1 > -1 else 4, colChar2 - 1 if colChar2 - 1 > -1 else 4
                decryptedString += f'{cipherMatrix[newColChar1][rowChar1] + cipherMatrix[newColChar2][rowChar2]}'
            else:  # Forms a rectangle
                newRowChar1, newRowChar2 = rowChar2, rowChar1
                decryptedString += f'{cipherMatrix[colChar1][newRowChar1] + cipherMatrix[colChar2][newRowChar2]}'

        # Serialize decrypted string
        return ''.join(char for char in decryptedString if char.isalpha() and char != 'x' and char != 'X').upper()


CIPHER_KEY = "SUPERSPY"
ENCRYPTED_MESSAGE = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
spyCity = SpyCityCodeCracker(CIPHER_KEY, ENCRYPTED_MESSAGE)
DECRYPTED_MESSAGE = spyCity.decrypt()
print(DECRYPTED_MESSAGE)  # Password to the Club
