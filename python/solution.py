# Playfair Cipher Solver
# Sabrina Umeri
# May 9, 2024


# Function to prepare the text: 
def generateFormattedText(text):
    # Convert to uppercase
    # Remove special characters
    text = ''.join(filter(str.isalpha, text.upper()))
    # Replace 'J' with 'I'
    text = text.replace('J', 'I')
    return text

# Function to generate the "Key Square"
def generateKey(key):
    key = generateFormattedText(key)
    # Create a square matrix (5x5) without repeating characters
    square = ''
    # Looping through each character in the Key
    for char in key:
        if char not in square and char != ' ':
            square += char
    # Defining the alphabet while excluding the letter 'J'
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' 
    # For loop to add the remaining characters from the alphabet until the key is complete.
    for char in alphabet:
        if char not in square:
            square += char
    return square

# Function that creates pairs for characters 
def generatePairs(char):
    pairs = []
    i = 0
    # Loops through the text
    while i < len(char):
        # If two characters next to eachother are the same or if there's only one character left, add 'X' as the second character
        if i == len(char) - 1 or char[i] == char[i + 1]:
            pairs.append(char[i] + 'X')
            i += 1
        # If two characters next to eachother are different, add them as a pair
        else:
            pairs.append(char[i] + char[i + 1])
            i += 2
    return pairs

# Function for decrypting
def decrypt(text, key):
    #Creating the key square
    keySquare = generateKey(key)
    # Text preparatino for decrypting
    text = generateFormattedText(text)
    #Pairs of characters for decrypting
    pairs = generatePairs(text)
    #defining decrypted text variable to blank string to be used
    decryptedMsg = ''
    # Loop through each pair of characters
    for pair in pairs:
        # Row & Column for first character of the pair
        row1, col1 = divmod(keySquare.index(pair[0]), 5)
        # Row & Column for second character of the pair
        row2, col2 = divmod(keySquare.index(pair[1]), 5)
        # Characters are in the same row, replace them with the ones to the left.
        if row1 == row2:
            decryptedMsg += keySquare[row1 * 5 + (col1 - 1) % 5]
            decryptedMsg += keySquare[row2 * 5 + (col2 - 1) % 5]
        # Characters are in the same column, replace them with the ones above.
        elif col1 == col2:
            decryptedMsg += keySquare[((row1 - 1) % 5) * 5 + col1]
            decryptedMsg += keySquare[((row2 - 1) % 5) * 5 + col2]
        # If a rectangle is formed, replace characters on the same row, opposite columns
        else:
            decryptedMsg += keySquare[row1 * 5 + col2]
            decryptedMsg += keySquare[row2 * 5 + col1]
    # Return and remove any 'X' characters from the decryption
    return decryptedMsg.replace('X', '')


# Encrypted Message given in the instructions
text = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
# Key to the cipher given in the instructions
key = "SUPERSPY"

# Using the decryption function with the "Text" & "Key" given above
decryptedMsg = decrypt(text, key)
# Printing the final decrypted message.
print(decryptedMsg)

#When the fear of long words IS a long word :P

