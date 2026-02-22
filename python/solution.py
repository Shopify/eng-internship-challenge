
import re

alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
    'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
    'W', 'X', 'Y', 'Z'
]

# Generates the key table for decryption
def GenerateTable(key):

    # create raw table filled with 0's first
    table = [[0 for i in range (5)] for j in range(5)]
    new_key = []

    # fill new_key with unique letters from key 
    for i in range(len(key)):
        if key[i] not in new_key:

            # if the letter is J and I is not in the key, add I instead
            if (key[i] == 'J' or key[i] == 'I') and 'I' not in new_key:
                new_key.append('I')
            else:    
                new_key.append(key[i])

    # fill key with remaining alphabet
    for i in range(26):
        if alphabet[i] not in new_key:

            # if the letter is J and I is not in the key, add I instead
            # 'I' is index 8 of alphabet
            # 'J' is index 9 of alphabet
            if i == 8 or i == 9:
                if 'I' not in new_key:
                    new_key.append('I')
            else:    
                new_key.append(alphabet[i])

    # fill table with key
    index = 0
    for i in range(0,5):
        for j in range(0,5):
            table[i][j] = new_key[index]
            index += 1

    return table

# Gets the index of a ltter in the table (i, j)
def GetIndex(table, letter):
    for i in range(5):
        for j in range(5):
            if table[i][j] == letter:
                return (i, j)
    return None


# Shift left; same row
def ShiftLeft(table, row, col_a, col_b):

    col_a_index = col_a - 1 if col_a - 1 >= 0 else 4
    col_b_index = col_b - 1 if col_b - 1 >= 0 else 4

    return table[row][col_a_index] + table[row][col_b_index]
    

# Shift up; same column
def ShiftUp(table, col, row_a, row_b):
    
    row_a_index = row_a - 1 if row_a - 1 >= 0 else 4
    row_b_index = row_b - 1 if row_b - 1 >= 0 else 4

    return table[row_a_index][col] + table[row_b_index][col]


# Rectangle Rule
def Rectangle(table, col_a, row_a, col_b, row_b):

    # distance between the two columns indices
    distance = abs(col_a - col_b)
    col_a_index = col_a - distance if col_a > col_b else col_a + distance
    col_b_index = col_b - distance if col_b > col_a else col_b + distance

    return table[row_a][col_a_index] + table[row_b][col_b_index]


# Solution function
def Solution():

    # working variables
    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"

    # basic error checking
    if ciphertext == None or len(ciphertext) == 0:
        return None

    # filter to get only uppercase alphabetical characters
    filtered_ciphertext = "".join(re.split("[^a-zA-Z]*", ciphertext)).upper().strip()
    filtered_key = "".join(re.split("[^a-zA-Z]*", key)).upper().strip()

    # get key table
    key_table = GenerateTable(filtered_key)

    # plaintext variable
    plaintext = ""

    # decrypt ciphertext
    for i in range(0, len(filtered_ciphertext), 2):
        pair = list(filtered_ciphertext[i:i+2])

        row_a, col_a = GetIndex(key_table, pair[0])
        row_b, col_b = GetIndex(key_table, pair[1])

        # same row; shift left
        if (row_b == row_a):
            plaintext += ShiftLeft(key_table, row=row_a, col_a=col_a, col_b=col_b)
        
        # same column; shift up
        elif col_a == col_b:
            plaintext += ShiftUp(key_table, col=col_a, row_a=row_a, row_b=row_b)

        # not same row or column; rectangle rule
        else:
            plaintext += Rectangle(key_table, col_a=col_a, row_a=row_a, col_b=col_b, row_b=row_b)
    
    # Remove excess 'X' characters
    return plaintext.translate({ord('X'): None})

print(Solution())






    

