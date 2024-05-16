#Solution for Shopify Technical Challenge
import string

class Solution:
    #function to create playfair table using a key
    def create_table(self, key: str):
        #initialize the table as a 2x2 matrix
        table = [[''] * 5 for _ in range(5)]

        #initialize dictionary to retrieve positions of letters
        position = {}

        #uppercase key:
        key = key.upper()

        #remove 'special characters' (nonalpha)
        key = ''.join(char for char in key if char.isalpha())

        #replace 'J's with 'I's in the key
        key = key.replace("J", "I")

        #remove duplicates from key
        key = "".join(dict.fromkeys(key))

        #generate uppercase alphabet and without 'J'
        alphabet = string.ascii_uppercase.replace('J', '')

        #remove chars from alphabet that are already in key
        remaining_alphabet = ''.join(char for char in alphabet if char not in key)

        #fill the table with chars from the key and remaining alphabet
        table_letters = key + remaining_alphabet
        for i in range(5):
            for j in range(5):
                letter = table_letters[i * 5 + j]
                table[i][j] = letter
                position[letter] = (i, j)

        return table, position


    #function to decrypt the message
    def decrypt(self, message: str, key: str):
        #initialize string to store decrypted message
        password = ''

        #create table and position map:
        table, position = self.create_table(key)

        #check if message has odd length, append "X"
        if len(message) % 2 != 0:
            message += 'X'

        #decrypt message:
        for i in range(0, len(message), 2):
            #get letter pair:
            letter1 = message[i]
            letter2 = message[i + 1]

            #get letter1, letter2 positions:
            row1, col1 = position[letter1]
            row2, col2 = position[letter2]

            #rule 1 - same row:
            if row1 == row2:
                password += table[row1][(col1 - 1) % 5] + table[row2][(col2 - 1) % 5]
            #rule 2 - same column:
            elif col1 == col2:
                password += table[(row1 - 1) % 5][col1] + table[(row2 - 1) % 5][col2]
            #rule 3 - different row and column:
            else:
                password += table[row1][col2] + table[row2][col1]

        #return password without 'X's:
        return password.replace('X', '')

solution = Solution()
print(solution.decrypt("IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV", "SUPERSPY"))