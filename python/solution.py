def make_table(key,letter_to_coord):
    """
    Create the cipher table that will be used to decrypt the ciphertext
    Pass in letter_to_coord to be able to update it as the function builds the table

    :param str key: Key used to encrypt the ciphertext originally
    :param dict letter_to_coord: Pass a pointer to the dictionary to update letter to coord pairs
    """

    if "J" in key:
        ALPHABET = "ABCDEFGHJKLMNOPQRSTUVWXYZ"
    else:
        ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    table = [['' for _ in range(5)] for _ in range(5)]

    ct = 0
    for i in range(len(table)):
        for j in range(len(table[0])):
            # If there is still a char we can add in the key, check if that character was not added yet
            # Else add all characters in the ALPHABET that are not already in the matrix
            added = False

            while ct < len(key) and key[ct] in letter_to_coord:
                ct += 1

            if ct < len(key):
                table[i][j] = key[ct]
                letter_to_coord[key[ct]] = (i,j)
                added = True

            while not added and ALPHABET[ct-len(key)] in letter_to_coord:
                ct += 1
                
            if not added:
                table[i][j] = ALPHABET[ct-len(key)]
                letter_to_coord[ALPHABET[ct-len(key)]] = (i,j)

    return table

def decrypt(ciphertext,key):
    """
    Decrypt a ciphertext with a given key utilizing the Playfair Cipher
    Learn more at: https://en.wikipedia.org/wiki/Playfair_cipher

    :param str ciphertext: Ciphertext that will be decrypted
    :param str key: Key used to encrypt the ciphertext originally
    """

    # Our inputs are already properly formatted, but incase sanitization is needed
    ciphertext.upper().strip()
    key.upper().strip()
    if len(ciphertext) // 2 == 1: ciphertext.append("X") # X is my chosen insert character
    
    # Keep a map of letter to coord pairs in the matrix for faster lookup time
    letter_to_coord = {}

    table = make_table(key,letter_to_coord)
    ciphertext = list(ciphertext)

    for index in range(0,len(ciphertext),2):
        char1 = ciphertext[index]
        char2 = ciphertext[index+1]
        
        i1,j1 = letter_to_coord[char1]
        i2,j2 = letter_to_coord[char2]

        # If the letters appear on the same row of your table, replace them 
        # with the letters to their immediate left respectively
        if i1 == i2:
            j1 = j1 - 1 if j1 - 1 > -1 else len(table)-1
            j2 = j2 - 1 if j2 - 1 > -1 else len(table)-1

            ciphertext[index] = table[i1][j1]
            ciphertext[index+1] = table[i2][j2]

        # If the letters appear on the same column of your table, replace them 
        # with the letters immediately above respectively 
        elif j1 == j2:
            i1 = i1 - 1 if i1 - 1 > -1 else len(table[0])-1
            i2 = i2 - 1 if i2 - 1 > -1 else len(table[0])-1

            ciphertext[index] = table[i1][j1]
            ciphertext[index+1] = table[i2][j2]

        # If the letters are not on the same row or column, replace them with the letters on the same row 
        # respectively but at the other pair of corners of the rectangle defined by the original pair.
        else:
            j1, j2 = j2, j1

            ciphertext[index] = table[i1][j1]
            ciphertext[index+1] = table[i2][j2]

    # The first rule can only be reversed by dropping any extra instances of the chosen insert letter 
    # — generally "X"s or "Q"s — that do not make sense in the final message when finished.
    res = ""
    for char in ciphertext:
        if char != "X": res += char

    return res

if __name__ == '__main__':
    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"
    print(decrypt(ciphertext,key))