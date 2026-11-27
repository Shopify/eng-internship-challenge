import string

class PlayfairCipher:
    """
    Playfair Cipher class
    
    Attributes:
    key -- the key used for encryption and decryption
    matrix -- the 5x5 matrix used for encryption and decryption
    
    Methods:
    _prepare_key -- prepares the key by removing duplicates and replacing 'J' with 'I'
    _create_matrix -- creates the 5x5 matrix from the key
    _find_position -- finds the position of a letter in the matrix
    decrypt -- decrypts the ciphertext using the Playfair Cipher
    """
    def __init__(self, key):
        self.key = self._prepare_key(key)
        self.matrix = self._create_matrix()

    def _prepare_key(self, key):
        key = key.upper().replace('J', 'I')
        return ''.join(dict.fromkeys(key + string.ascii_uppercase.replace('J', '')))

    def _create_matrix(self):
        return [list(self.key[i:i+5]) for i in range(0, 25, 5)]

    def _find_position(self, letter):
        for i, row in enumerate(self.matrix):
            if letter in row:
                return i, row.index(letter)
        return None

    def decrypt(self, ciphertext):
        """
        Decrypts the ciphertext using the Playfair Cipher
        
        Arguments:
        ciphertext -- the text to be decrypted
        
        Returns:
        plaintext -- the decrypted text
        """
        ciphertext = ciphertext.upper().replace('J', 'I')
        plaintext = ""

        for i in range(0, len(ciphertext), 2):
            a, b = ciphertext[i], ciphertext[i+1]
            row1, col1 = self._find_position(a)
            row2, col2 = self._find_position(b)

            if row1 == row2:
                plaintext += self.matrix[row1][(col1-1)%5] + self.matrix[row2][(col2-1)%5]
            elif col1 == col2:
                plaintext += self.matrix[(row1-1)%5][col1] + self.matrix[(row2-1)%5][col2]
            else:
                plaintext += self.matrix[row1][col2] + self.matrix[row2][col1]

        return plaintext.replace('X', '')

def main():
    key = "SUPERSPY"
    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    
    cipher = PlayfairCipher(key)
    decrypted_text = cipher.decrypt(ciphertext)
    
    print(decrypted_text, end='')

if __name__ == "__main__":
    main()