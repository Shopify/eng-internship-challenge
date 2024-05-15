import re

class PlayFair:

    def generate_matrix(self, key):   
        '''
        Generates a matrix from the letters in the key.

        Parameters:
            self (PlayFair): The PlayFair instance.
            key (string): A key which is used to encrypt or decrypt the message using Playfair Cipher.
        
        Returns:
            result (list): A 5*5 matrix containing the alphabets which will be useful for encrypting and decrypting.
        ''' 
        
        visited_letters = {}  #Initialize an empty dictionary to store already visited letters        
        matrix = []  #Initialize an empty list to store the unique alphabets
        row = 0   
        col = 0   
        
        for letter in key: 
            if letter not in visited_letters:   #Checking whether the current letter is visited or not
                visited_letters[letter] = 1  #Adding current letter to visited letters to avoid it next time
                if col == 0:  
                    matrix.append([])   #Adding row to the matrix as col = 0 indicates we came to the new row 

                matrix[row].append(letter)  #Adding already visited letter to the matrix
                col += 1  #Increasing the value of column index by 1 as we have already appended the letter
                if col == 5:  #Checking whether column index is 5 or not, as it indicates we reach end of the column 
                    row += 1  #we have to start from next row and 0th column
                    col = 0
        

        alphabets = "ABCDEFGHIKLMNOPQRSTUVWXYZ"    #Declaring all the alphabets to append the remaining ones
        for letter in alphabets:  
            if letter not in visited_letters: 
                visited_letters[letter] = 1

                if col == 0:
                    matrix.append([])

                matrix[row].append(letter)
                col += 1   #Increasing the value of column index by 1 as we have already appended the letter
                if col == 5:   #Checking whether column index is 5 or not, as it indicates we reach end of the column
                    row += 1   #We have to start from next row and 0th column
                    col = 0
        
        return matrix


    def pos(self,letter, matrix):
        '''
        Get the value of row and column index from the generated matrix by passing the letter.

        Parameters:
            self (PlayFair): The PlayFair instance.
            letter (character): A letter for which the row and column index value is required.
            matrix (list): The generated matrix using the given key.
        
        Returns:
            [row index, col index]: The value of row and column index for the passed letter.
        '''

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == letter:
                    return [i,j]
                

    def removeX(self,message):
        '''
        Remove 'X' characters from the message according to certain conditions.

        Parameters:
            self (PlayFair): The PlayFair instance.
            message (string): The message from which 'X' characters are to be removed.

        Returns:
            message (string): The message with 'X' characters removed.
        '''

        if message[-1] == "X" and len(message) % 2 == 0:
            message = message[:-1]  # Remove the last character

        # Remove 'X' between two identical letters
        message = re.sub(r'([A-Z])X\1', r'\1\1', message, flags=re.IGNORECASE)  

        return message.upper().strip()


    def generate_plaintext(self,ciphertext, matrix):
        '''
        Generate plaintext from a ciphertext using a given matrix.

        Parameters:
            self (PlayFair): The PlayFair instance.
            ciphertext (string): The ciphertext to be decrypted.
            matrix (list): The matrix used for decryption.

        Returns:
            plaintext (string): The decrypted plaintext.
        '''

        plaintext = ""
        
        for i in range(0, len(ciphertext), 2):   #Iterating over the pair of 2 letters from the generated pairs
            a = self.pos(ciphertext[i], matrix)    #Getting the row and column index for the ith variable
            b = self.pos(ciphertext[i + 1], matrix)   #Getting the row and column index for the (i+1)th variable
            
            if a[0] == b[0]:   #If both the letters are in the same row
                decA = matrix[a[0]][(a[1] - 1) % 5]   #Shift left by one in the row
                decB = matrix[b[0]][(b[1] - 1) % 5]
            elif a[1] == b[1]:   #If both the letters are in the same column
                decA = matrix[(a[0] - 1) % 5][a[1]]   #Shift up by one in the column
                decB = matrix[(b[0] - 1) % 5][b[1]]
            else:   #If both the letter are in the different row and different column
                decA = matrix[a[0]][b[1]]   #Swap columns
                decB = matrix[b[0]][a[1]]
            
            plaintext += decA + decB
        
        return self.removeX(plaintext)



def main():
    '''
    Main function to decrypt a specific ciphertext using a specific key
    '''
    # Define the key and ciphertext
    key = "SUPERSPY"
    cipherText = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

    pf = PlayFair()   #Initializing playfair instance
    matrix = pf.generate_matrix(key)    #Generating matrix using the key
    plainText = pf.generate_plaintext(cipherText, matrix)
    print(plainText)

if __name__ == "__main__":
    main()

