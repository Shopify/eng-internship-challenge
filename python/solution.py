'''
Program to decrypt a message encrpyted using the Playfair cipher

Jerry Cheng

'''

# These can be changed if we have different input parameters, or if spy city changes their password ;)
encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
key = "SUPERSPY"


def generate_key_table(key):
    # Generate key table in 1D first for simplicity and efficiency
    oneD_key_table = []
    key = key.upper()

    # Add key into key table first
    for char in key:
        if char not in oneD_key_table:
            oneD_key_table.append(char)
    
    # Add remaining letters into key table
    for i in range(65, 91):
        # We only insert one of I or J, since they are combined together in the key table
        #   * This implementation makes it so that I is used instead of J, unless J is in the key.
        #   * This is just a design choice that made the most sense
        if chr(i) == 'I' or chr(i) == 'J':
            if 'I' not in oneD_key_table and 'J' not in oneD_key_table:
                oneD_key_table.append('I')
            continue
        if chr(i) not in oneD_key_table:
            oneD_key_table.append(chr(i))
    
    # Generate 2D key table
    key_table = []
    for i in range(0, 25, 5):
        key_table.append(oneD_key_table[i:i+5])
    return key_table

def find_char_in_key_table(key_table, char):
    for i in range(5):
        for j in range(5):
            if key_table[i][j] == char:
                return i, j
    return -1, -1

def decrypt_message(encrypted_message, key):
    decrypted_message = ""
    key_table = generate_key_table(key)
    
    for i in range(0, len(encrypted_message), 2):
        char1 = encrypted_message[i]
        char2 = encrypted_message[i+1]
        row1, col1 = find_char_in_key_table(key_table, char1)
        row2, col2 = find_char_in_key_table(key_table, char2)

        # If the two characters are in the same row (Rule 2)
        if row1 == row2:
            decrypted_message += key_table[row1][(col1-1)%5]
            decrypted_message += key_table[row2][(col2-1)%5]
        # If the two characters are in the same column (Rule 3)
        elif col1 == col2:
            decrypted_message += key_table[(row1-1)%5][col1]
            decrypted_message += key_table[(row2-1)%5][col2]
        # If the two characters are in different rows and columns (Rule 4)
        else:
            decrypted_message += key_table[row1][col2]
            decrypted_message += key_table[row2][col1]
    
    # Remove any instances of 'X' as it was used as a filler character
    return decrypted_message.replace('X', '')

print(decrypt_message(encrypted_message, key))