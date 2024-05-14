#Shopify Engineering Internship Technical Assessment Challenge: Playfair Cipher
#Author: Susanna Liao
#Date: May 14, 2024

#setting up given key and encrypted message
given_key = "SUPERSPY"
encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

#function to decrypt message using playfair cipher
def decrypt_playfair(given_key, encrypted_message):
    #eliminating duplicate letters from given key
    key = []
    for i in given_key:
        if i not in key:
            key.append(i.upper()) #ensuring key is uppercase

    #making list of letters to fill in playfair square, starting with key followed by rest of alphabet (without duplicates)
    playfair_letters = []
    #note: alphabet has no 'J' because there would be too many letters for 5x5 matrix, so 'I' can be interpreted as 'J' depending on context of decrypted message
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in key:
        playfair_letters.append(i)
    for i in alphabet:
        if i not in key:
            playfair_letters.append(i)

    #filling in 5x5 playfair square with playfair letters
    playfair_square = []
    while playfair_letters != []:
        playfair_square.append(playfair_letters[:5])
        playfair_letters = playfair_letters[5:]

    #defining function to find row of letter
    def searchrow(letter):
        for i in range(5):
            for j in range(5):
                if letter==playfair_square[i][j]:
                    return i #returns row number of letter
                
    #defining function to find column of letter
    def searchcol(letter):
        for i in range(5):
            for j in range(5):
                if letter==playfair_square[i][j]:
                    return j #returns column number of letter

    #defining function to find modulus 5, considering overflow of letter position when shifting across row or col
    def mod5(n):
        if n<0:
            n+=5
        return n%5


    #iterating over the encrypted message by splitting it into pairs of characters and evaluating each pair to swap letters accordingly
    decrypted_message = ""
    for i in range(0, len(encrypted_message), 2):
        char1 = encrypted_message[i]
        char2 = encrypted_message[i+1]
        #case 1: if letters are on same row of playfair square, shift left and add to decrypted message
        if searchrow(char1)==searchrow(char2):
            decrypted_message+=playfair_square[searchrow(char1)][mod5(searchcol(char1)-1)]
            decrypted_message+=playfair_square[searchrow(char2)][mod5(searchcol(char2)-1)]
        #case 2: if letters are on same column of playfair square, shift up and add to decrypted message
        elif searchcol(char1)==searchcol(char2):
            decrypted_message+=playfair_square[mod5(searchrow(char1)-1)][searchcol(char1)]
            decrypted_message+=playfair_square[mod5(searchrow(char2)-1)][searchcol(char2)]
        #case 3: if letters form a box shape on playfair square, swap the columns of the characters and add to decrypted message
        elif searchcol(char1)!=searchcol(char2) and searchrow(char1)!=searchrow(char2):
            decrypted_message+=playfair_square[searchrow(char1)][searchcol(char2)]
            decrypted_message+=playfair_square[searchrow(char2)][searchcol(char1)]

    #removing all X's from decrypted messsage
    decrypted_message=decrypted_message.replace('X', '')

    return decrypted_message

#final step :)
print(decrypt_playfair(given_key, encrypted_message))