import re
import sys
from collections import OrderedDict

class PlayfairCipher:
    def __init__(self, keyword):
        self.keyword = self.clean_keyword(keyword)
        self.matrix = self.generate_matrix()

    #remove duplicate letters and non-alphabetic characters that may appear
    def clean_keyword(self, keyword):
        clean_keyword = "".join(OrderedDict.fromkeys(re.sub(r'[^a-zA-Z]', '', keyword.upper())))
        return clean_keyword
    
    #generate playfair matrix
    def generate_matrix(self):
        matrix = [['' for _ in range (5)] for _ in range(5)]
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" #removing J in cipher to allow it to fit

        #fill in the keyword provided
        index = 0
        for letter in self.keyword:
            row, col = divmod(index, 5)
            matrix[row][col] = letter
            index += 1
        
        #remainder letters
        for letter in alphabet:
            if letter not in self.keyword:
                row, col = divmod(index, 5)
                matrix[row][col] = letter
                index += 1
        return matrix

    def find_positions(self, letter):
        for i in range(5):
            for j in range(5):
                if self.matrix[i][j] == letter:
                    return i, j

    def decrypt(self, message):
        message = re.sub(r'[^a-zA-Z]', '', message.upper()) 
        decrypted_message = ""

        for i in range(0, len(message), 2):
            if i == len(message) - 1:
                message += 'X'
            letter1, letter2 = message[i], message[i+1]    

            row1, col1 = self.find_positions(letter1)
            row2, col2 = self.find_positions(letter2)

            if row1 == row2:
                decrypted_message += self.matrix[row1][(col1 - 1) % 5]
                decrypted_message += self.matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_message += self.matrix[(row1 - 1) % 5][col1]
                decrypted_message += self.matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_message += self.matrix[row1][col2]
                decrypted_message += self.matrix[row2][col1]

        decrypted_message = re.sub(r'X', '', decrypted_message)
        decrypted_message = decrypted_message.upper()
        
        return decrypted_message 

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 solution.py <encrypted_message>")
        sys.exit(1)

    keyword = "SUPERSPY"
    encrypted_message = sys.argv[1]

    cipher = PlayfairCipher(keyword)
    decrypted_message = cipher.decrypt(encrypted_message)

    decrypted_message = re.sub(r'[^A-Z]', '', decrypted_message)

    print(decrypted_message)