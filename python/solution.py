'''
Code to take an encrypted message (hardcoded in this case) and output the decrypted message using the playfair cipher
Author: Michael Wieszczek
Date: 2024/05/14
'''

keytable = [['S', 'U', 'P', 'E', 'R'],
            ['Y', 'A', 'B', 'C', 'D'],
            ['F', 'G', 'H', 'I', 'K'], #Ommit J and duplicates as custom in a Playfair Cipher
            ['L', 'M', 'N', 'O', 'Q'],
            ['T', 'V', 'W', 'X', 'Z']]

encryptedMessage = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

#Method that takes a character, looks it up on the keytable and returns the row and column
def cordSearch(char):
    for row in range(0, len(keytable), 1):
        for column in range(0, len(keytable), 1):
            if char in keytable[row][column]:
                return(row, column)
    
    print("Cannot find character")

def main():
    decryptedMessage = ""
    
    # Encrypted message checking to see if it exists, and is valid (is a multiple of 2)
    if (len(encryptedMessage) % 2 != 0 ) or (len(encryptedMessage) == 0):
        print("Invalid encryptedMessage")

    for i in range(0, len(encryptedMessage), 2):
        char1 = encryptedMessage[i]
        char2 = encryptedMessage[i+1]
        char1Cords = cordSearch(char1)
        char2Cords = cordSearch(char2)
        #We use modulus 5 for the first 2 cases in case of index going out of bounds of the 5x5 matrix, all operations are the inverse of encryption
        if char1Cords[0] == char2Cords[0]: #Same Row Case
            decryptedMessage += keytable[char1Cords[0]][(char1Cords[1] - 1) % 5]
            decryptedMessage += keytable[char2Cords[0]][(char2Cords[1] - 1) % 5]
        elif char1Cords[1] == char2Cords[1]: #Same Column Case
            decryptedMessage += keytable[(char1Cords[0] - 1) % 5][char1Cords[1]]
            decryptedMessage += keytable[(char2Cords[0] - 1) % 5][char2Cords[1]]
        else:
            decryptedMessage += keytable[char1Cords[0]][char2Cords[1]]
            decryptedMessage += keytable[char2Cords[0]][char1Cords[1]]
    
    '''
    I noticed after writing the code this all could've been simplified with a string.replace('X', '') but the code below will work for
    instances where there are X's included in the cipher, or even if there are consecuitive X's in the original string.

    Note: I believe the decrypted message does not follow the Playfair Ciphers rules, there should be an added X inbetween the 2 consecutive P's
    in the latter part of the word. The decrypted version of the cipher outputs HIPXPOPOTOMONSTROSESQUI(PP)EDALIOPHOBIAX (quotations for clarity)

    '''
    
    parsedMessage = decryptedMessage[0] #Can always guarentee at least 1 character in message due to validation at beginning of method
    for i in range(1, len(decryptedMessage) - 1, 1): #We will do a check for the final X placeholder after the loop, saves checking an if statment
        if not ((decryptedMessage[i] == 'X') & (decryptedMessage[i-1] == decryptedMessage[i+1])): #Get rid of X's seperating consequitive letters
            parsedMessage += decryptedMessage[i]
        #else do nothing
    if decryptedMessage[len(decryptedMessage) - 1] != 'X': #Final X check
        parsedMessage += decryptedMessage[len(decryptedMessage) - 1]
    print(parsedMessage)
            

if __name__ == "__main__":
    main()
        