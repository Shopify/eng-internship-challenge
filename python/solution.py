# Shopify Engineering Internship Technical Assessment Challenge: Playfair Cipher
# Author: Susanna Liao
# Date: May 14, 2024

# Setting up given key and encrypted message
given_key = "SUPERSPY"
encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

def decrypt_playfair(given_key, encrypted_message):
    # Ensuring given key and encrypted message are in uppercase
    given_key = given_key.upper()
    encrypted_message = encrypted_message.upper()
    
    # Eliminating duplicate letters from given key
    key = []
    for i in given_key:
        if i not in key:
            key.append(i)

    # Making list of letters to fill in playfair square, starting with key followed by rest of alphabet (without duplicates)
    playfair_letters = key
    # Note: alphabet has no 'J' because there would be too many letters for 5x5 matrix, so 'I' can be interpreted as 'J' depending on context of decrypted message
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in alphabet:
        if i not in key:
            playfair_letters.append(i)

    # Filling in 5x5 playfair square with playfair letters
    playfair_square = []
    while playfair_letters != []:
        playfair_square.append(playfair_letters[:5])
        playfair_letters = playfair_letters[5:]

    # Defining function to find row of letter
    def searchrow(letter):
        for i in range(5):
            for j in range(5):
                if letter==playfair_square[i][j]:
                    return i # Returns row number of letter
                
    # Defining function to find column of letter
    def searchcol(letter):
        for i in range(5):
            for j in range(5):
                if letter==playfair_square[i][j]:
                    return j # Returns column number of letter

    # Defining function to find modulus 5, considering overflow of letter position when shifting letters across row or col
    def mod5(n):
        if n<0:
            return 4 # Since the only possible value out of bounds would be -1
        else:
            return n


    # Iterating over the encrypted message by splitting it into pairs of characters and evaluating each pair to swap letters accordingly
    decrypted_message = ""
    for i in range(0, len(encrypted_message), 2):
        char1 = encrypted_message[i]
        char2 = encrypted_message[i+1]
        # Case 1: if letters are on same row of playfair square, shift each letter left and add to decrypted message
        if searchrow(char1)==searchrow(char2):
            decrypted_message+=playfair_square[searchrow(char1)][mod5(searchcol(char1)-1)]
            decrypted_message+=playfair_square[searchrow(char2)][mod5(searchcol(char2)-1)]
        # Case 2: if letters are on same column of playfair square, shift each letter up and add to decrypted message
        elif searchcol(char1)==searchcol(char2):
            decrypted_message+=playfair_square[mod5(searchrow(char1)-1)][searchcol(char1)]
            decrypted_message+=playfair_square[mod5(searchrow(char2)-1)][searchcol(char2)]
        # Case 3: if letters form a box shape on playfair square, swap the columns of the characters and add to decrypted message
        else:
            decrypted_message+=playfair_square[searchrow(char1)][searchcol(char2)]
            decrypted_message+=playfair_square[searchrow(char2)][searchcol(char1)]

    # Removing all filler X's from decrypted messsage
    decrypted_message=decrypted_message.replace('X', '')

    return decrypted_message

# Final step :)
print(decrypt_playfair(given_key, encrypted_message))