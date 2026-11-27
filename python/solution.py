import re

#"Attention spy network! You've been assigned a task of the utmost importance! 
# We've received an encrypted message from an agent in the field containing the password to a top secret club for super spies. 
# The encrypted message reads as follows: "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV". 
# We've been told if we can crack this code and give the password to the door-person at the corner of 32nd Street, we will gain access to the illustrious spy club Spy City! 
# We must get inside! However the password has been encrypted with an older system known as a Playfair Cipher. 
# Our agent in the field says the key to the cipher is the string "SUPERSPY". 
# However, for the life of us we cannot crack this code! 
# Devise an application that can solve this encryption, get the password, and join us inside Spy City for what we are sure will be a night to remember!"

# Instructions:
# 1. Fork this repo to your personal Github Account
# 2. Clone your forked repo to begin working on the challenge locally.
# 3. Create a new Branch in your repo where you will be pushing your code to.
# 4. Choose which programming language you wish to complete the challenge with.
#     - Navigate to the folder of that programming language and complete your work in the solution file found inside. ie: ruby/solution.rb
#     - Do not edit the test file in the folder. Tests will only work as intended after you have submitted a PR.
#     - You'll find a separate README.md in that folder with language specific instructions.
# 5. Ensure your application is executable from the command-line by running your solution file.
# 6. Your decrypted string must by entirely UPPER CASE, and not include spaces, the letter "X", or special characters. Ensure you meet all these conditions before outputting the result.
# 7. Your application must output only the decrypted Playfair Cipher string.
#     - ie: BANANAS not The decrypted text is: BANANAS



# Playfair Cipher
def decrypt_playfair_cipher(ciphertext, key):
    # Remove special characters and convert to uppercase
    ciphertext = re.sub('[^A-Z]', '', ciphertext.upper())
    key = re.sub('[^A-Z]', '', key.upper())

    # Generate the Playfair matrix
    matrix = generate_playfair_matrix(key)

    # Decrypt the ciphertext
    plaintext = decrypt(ciphertext, matrix)

    return plaintext


# Find the position of a character in the Playfair matrix
def find_position(char, matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

# Generate the Playfair matrix using the key
def generate_playfair_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    # Replace 'J' with 'I' in the key
    key = key.replace("J", "I") 

    # Append the remaining alphabet to the key 
    key += alphabet  

    # Remove duplicate characters
    key = "".join(dict.fromkeys(key))  

    # Split the key into 5x5 matrix
    matrix = [key[i:i+5] for i in range(0, 25, 5)]  

    return matrix

# Decrypt the ciphertext using the Playfair matrix
def decrypt(ciphertext, matrix):
    # Create return variable
    plaintext = ""

    # Decrypt the ciphertext by looking at bigrams
    for i in range(0, len(ciphertext), 2):
        pair = ciphertext[i:i+2]
        row1, col1 = find_position(pair[0], matrix)
        row2, col2 = find_position(pair[1], matrix)

        # If the characters are in the same row, replace them with the character to their left
        if row1 == row2:
            col1 = (col1 - 1) % 5
            col2 = (col2 - 1) % 5

        # If the characters are in the same column, replace them with the character upwards
        elif col1 == col2:
            row1 = (row1 - 1) % 5
            row2 = (row2 - 1) % 5

        # Otherwise, replace them with the character in the same row but in the opposite column to form a rectangle
        else:
            col1, col2 = col2, col1

        # Append the decrypted characters to the plaintext
        plaintext += matrix[row1][col1] + matrix[row2][col2]

    # Remove X from the output
    plaintext = plaintext.replace("X", "")

    return plaintext

# Set the input and the key
ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
key = "SUPERSPY"

# Decrypt the Playfair cipher
plaintext = decrypt_playfair_cipher(ciphertext, key)
print(plaintext)


