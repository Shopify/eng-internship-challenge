#################
#
# Functions for creating Playfair Cipher
#
#################

# takes a key as an input and generates a cipher string from the given key
# E.g
# input: "SUPERSPY"
# putput: "SUPERYABCDFGHIKLMNOQTVWXZ"
def key_to_cipher_string(key):
    appended_key = key + "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    # set to track the letters seen in the appended key
    seen_letters = set()
    cipher_string = ""

    for char in appended_key:
        # if the letter has not been seen add it to the cipher_string and the seen set
        if char not in seen_letters:
            seen_letters.add(char)
            cipher_string = cipher_string + char

    return cipher_string

# creating cipher square using the given cipher string string
# E.x
# input: "SUPERYABCDFGHIKLMNOQTVWXZ"
# output: 
# [['S', 'U', 'P', 'E', 'R'], 
# ['Y', 'A', 'B', 'C', 'D'], 
# ['F', 'G', 'H', 'I', 'K'], 
# ['L', 'M', 'N', 'O', 'Q'], 
# ['T', 'V', 'W', 'X', 'Z']] 
#
def create_cipher(str):

    if len(str) != 25:
        raise ValueError("Input string must be exactly 25 characters long")
    
    cipher = [[None]*5 for _ in range(5)]

    # Fill the array with characters from the input string
    for i in range(5):
        for j in range(5):
            cipher[i][j] = str[i*5 + j]

    return cipher

#################
#
# Functions to decode the message
#
#################

# Finds the x and y coordinate of the letter l in the cipher
def find_letter(cipher, l):

    for i in range(5):
        for j in range(5):
            if cipher[i][j] == l:
                return i, j
            
    raise ValueError("Cannot find letter in cipher")

# decodes the letters l1, l2 according to the rules of playfair cipher
def decode(cipher, l1, l2):

    if l1 == l2:
        raise ValueError("cannot decode two of the same letter")
    
    # Finding the row and columns of the letters
    l1_x, l1_y = find_letter(cipher, l1)
    l2_x, l2_y = find_letter(cipher, l2)

    if l1_x == l2_x: # Case if the letters are in the same row
        return cipher[l1_x][l1_y - 1], cipher[l2_x][l2_y - 1]
    elif l1_y == l2_y: # Case if the letters are in the same column
        return cipher[l1_x - 1][l1_y], cipher[l2_x - 1][l2_y]
    else: # Case if the letters are in different row and column
        return cipher[l1_x][l2_y], cipher[l2_x][l1_y]

#################
#
# Decoding the message
#
#################

encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
decrypted_message = ""

if len(encrypted_message) % 2 != 0:
        raise ValueError("A properly encrypted message should have even length")

# Finding the cipher square with a given key
Key = "SUPERSPY"
cipher_string = key_to_cipher_string(Key)
#print(cipher_string)
playf_cipher = create_cipher(cipher_string)
#print(playf_cipher)

# decrypting the encrypted message 2 letters at a time
for i in range(0, len(encrypted_message), 2):
    d1, d2 = decode(playf_cipher, encrypted_message[i], encrypted_message[i + 1])
    decrypted_message = decrypted_message + d1 + d2

# removing Xs to show the decrypted message
decrypted_message = decrypted_message.replace("X", '')

print(decrypted_message)
