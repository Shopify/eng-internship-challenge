TABLE_SIZE = 5 
encrpted_msg = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
key = "SUPERSPY"

key_table = []

# omit "J" or "Q" to reduce the alphabet to fit
key_table = [['S','U','P','E','R'], 
             ['Y','A','B','C','D'], 
             ['F','G','H','I','K'], 
             ['L','M','N','O','Q'], 
             ['T','V','W','X','Z']]

# param: encrypted message
# return: ['AB','CD']
def split_into_pairs(encrpted_msg):
    pairs = []
    for i in range(0, len(encrpted_msg), 2):
        pairs.append(encrpted_msg[i:i+2])
    return pairs

# param: 'AB'
# return: rowA colA rowB colB [1,2,3,4]
def find_row_col(pair):
    row_col = []
    for letter in pair:
        for i in range(TABLE_SIZE):
            for j in range(TABLE_SIZE):
                if key_table[i][j] == letter:
                    row_col.append(i)
                    row_col.append(j)
    return row_col

# param: rowA colA rowB colB [1,2,3,4]
# return: boolean
def same_row(row_col):
    if row_col[0] == row_col[2]:
        return True
    return False

# param: rowA colA rowB colB [1,2,3,4]
# return: boolean
def same_column(row_col):
    if row_col[1] == row_col[3]:
        return True
    return False

# Playfair Cipher
def decrypt(encrpted_msg, key):
    pairs = split_into_pairs(encrpted_msg)
    
    decrypted_msg = ""
    for pair in pairs:
        row_col = find_row_col(pair)
        if same_row(row_col):
            # replace with the letter immediately to the left
            new_pair = key_table[row_col[0]][row_col[1] - 1] + key_table[row_col[2]][row_col[3] - 1]
        elif same_column(row_col):
            # replace with the letter immediately above
            new_pair = key_table[row_col[0] - 1][row_col[1]] + key_table[row_col[2] - 1][row_col[3]]
        else:
            # replace with the letter in the same row but at the other pair's column
            new_pair = key_table[row_col[0]][row_col[3]] + key_table[row_col[2]][row_col[1]]
        decrypted_msg += new_pair

    # remove "X"s (used to seperate repeated letters during encryption)
    decrypted_msg = decrypted_msg.replace("X", "")
    return decrypted_msg

# Answer
print(decrypt(encrpted_msg, key))