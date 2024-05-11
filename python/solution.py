
"""
# ***************************************************
# Victor Chan (vschan@uwaterloo.ca)
# May 10th, 2024
# Shopify Engineering Intern Technical Challenge
# Language: Python
# ***************************************************
"""

# CONSTANTS 
ROWS=5
COLS=5

# remove_dups(key) removes any duplicate letters from key
def remove_dups (key=str):
    return "".join(dict.fromkeys(key))


# create_table(key) returns the Playfair cipher table formed
# by the key, for example, if the keyword was "SUPERFLY", this
# function returns: 
# table = [[S U P E R]
#          [Y A B C D]
#          [F G H I K]
#          [L M N O Q]
#          [T V W X Z]]
#
def create_table (key): 

    key = key.upper() 
    key = remove_dups(key)    
    key_char_array = [char for char in key]

    ALPHABET=  [char for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ"]
    ALPHABET = [c for c in ALPHABET if c not in key]

    key_char_array.extend(ALPHABET)

    table = [['0' for i in range(COLS)] for j in range(ROWS)]

    idx = 0 
    for y in range (ROWS):
        for x in range(COLS):
            table[y][x] = key_char_array[idx]
            idx += 1
       
    return table

# find_cord(table, char) returns a tuple representing the 
# xy coordinate of the char in the table
def find_cord (table, char): 
     
     for y in range (ROWS):
        for x in range(COLS):
            if (table[y][x] == char): 
                return (y, x)

# decrypt_playfair(key, encrypted_msg) decrypts the given
# encrypted message based on the key.
def decrypt_playfair(key, encrypted_msg): 
    table = create_table(key)

    #Uppercasing all letters and filtering out all
    # non-letters
    encrypted_msg = encrypted_msg.upper()
    encrypted_msg = [c for c in encrypted_msg if (c >= 'A' and c <= 'Z')]

    msg_len = len(encrypted_msg)
    
    raw_decrypt = ""
    for i in range (0, msg_len, 2): 

        #Consecutative same letters in an encrypted message
        # means two Xs
        if (encrypted_msg[i] == encrypted_msg[i + 1]): 
            raw_decrypt += "XX"
            continue

        
        (y1, x1) = find_cord(table, encrypted_msg[i])
        (y2, x2) = find_cord(table, encrypted_msg[i + 1])

        if (y1 != y2 and x1 != x2): 
            raw_decrypt += table[y1][x2]
            raw_decrypt += table[y2][x1]

        elif (y1 == y2): 
            raw_decrypt += table[y1][ (x1 - 1) % COLS]
            raw_decrypt += table[y2][ (x2 - 1) % COLS]

        else:
            raw_decrypt += table[ (y1 - 1) % ROWS][x1]
            raw_decrypt += table[ (y2 - 1) % ROWS][x2]
     

    decrypted_msg = ""
    for char in raw_decrypt: 

        if (char == 'X' or char < 'A' or char > 'Z'): 
            continue
        decrypted_msg += char

    print(decrypted_msg)

decrypt_playfair("SUPERSPY", "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV")
            







