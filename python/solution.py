"""
The CreateTable function creates a table for the Playfair cipher based on a given key.
This table is a 1D list of 25 letters which represents a 5x5 matrix.
The key is added to the table first, avoiding duplicates and omitting 'J'.
The rest of the letters are then added to the table.
"""
def createTable(key):
    table = []
    key = key.upper()
    key = key.replace("J", "I")
    rep = set()
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    # Add the key to the table, avoiding duplicates and not including 'J'
    for char in key:
        if char not in rep and char in alphabet:
            rep.add(char)
            table.append(char)

    # Fill the table with the rest of the letters
    for char in alphabet:
        if char not in rep:
            table.append(char)

    return table

"""
The encrypt_playfair function decrypts an encrypted message using the Playfair Cipher.
It takes a message and a key as input and returns the decrypted message.
The decrypted message is built by adding the decrypted pairs.
"""
def decrypt_playfair(message, key):
    table = createTable(key)
    decryptedMessage = ""
    message = message.upper()
    message = message.replace("J", "I")

    # check each pair
    for i in range(0, len(message), 2):
        pair = message[i:i+2]
        pos1 = table.index(pair[0])
        pos2 = table.index(pair[1])
        # Get the row and column of the pair
        row1, col1 = pos1 // 5, pos1 % 5
        row2, col2 = pos2 // 5, pos2 % 5

        # If the letters are in the same row, shift them to the left
        if row1 == row2:
            first = table[row1*5 + (col1 - 1) % 5]
            second = table[row2*5 + (col2 - 1) % 5]
            # check for X, space and special characters
            if first != 'X' and first != ' ' and first.isalnum():
                decryptedMessage += first
            if second != 'X' and second != ' ' and second.isalnum():
                decryptedMessage += second
        # If the letters are in the same column, shift them up
        elif col1 == col2:
            first = table[((row1 - 1) % 5)*5 + col1]
            second = table[((row2 - 1) % 5)*5 + col2]
            if first != 'X' and first != ' ' and first.isalnum():
                decryptedMessage += first
            if second != 'X' and second != ' ' and second.isalnum():
                decryptedMessage += second
        # If the letters are in different rows and columns, swap the columns
        else:
            first = table[row1*5 + col2]
            second = table[row2*5 + col1]
            if first != 'X' and first != ' ' and first.isalnum():
                decryptedMessage += first
            if second != 'X' and second != ' ' and second.isalnum():
                decryptedMessage += second
    #remove all spaces, X's and special characters
    return decryptedMessage

# Decrypt the message
key = "SUPERSPY"
message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
decrypted_message = decrypt_playfair(message, key)
print(decrypted_message)