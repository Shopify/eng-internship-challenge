def create_key_table(key):
    key = key.upper().replace("J", "I") # convert key to uppercase & replace 'J' w/ 'I'
    key_table = "".join(sorted(set(key), key=lambda x: key.index(x))) # create string w/ unique key characters --> 'SUPERAY'

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" # remaining alphabet letters (excluding J)
    key_table += "".join([char for char in alphabet if char not in key_table])

    return key_table

def find_indices(char, table): # find row & column indices of a given character in key table
    index = table.index(char)
    return index // 5, index % 5

def decrypt_digraph(digraph, table): # find positions of both characters in digraph
    row1, column1 = find_indices(digraph[0], table)
    row2, column2 = find_indices(digraph[1], table)
    
    if row1 == row2:
        return table[row1 * 5 + (column1 - 1) % 5] + table[row2 * 5 + (column2 - 1) % 5] # shift left if characters are same row
    elif column1 == column2:
        return table[((row1 - 1) % 5) * 5 + column1] + table[((row2 - 1) % 5) * 5 + column2] # shift up if characters are same column
    else:
        return table[row1 * 5 + column2] + table[row2 * 5 + column1] # swap columns if characters form rectangle 

def preprocess(text):
    return text.upper().replace("J", "I")

def decrypt_playfair(ciphertext, key):
    key_table = create_key_table(key) # key table
    ciphertext = preprocess(ciphertext)
    
    plaintext = ""
    i = 0

    while i < len(ciphertext): # decrypt cipher text two characters at a time
        digraph = ciphertext[i:i+2]
        if len(digraph) < 2 or digraph[0] == digraph[1]: # handles digraphs w/ identical/single characters --> 'X'
            digraph = digraph[0] + 'X'
            i -= 1
        plaintext += decrypt_digraph(digraph, key_table) # decrypt and append to plaintext 
        i += 2

    return plaintext.replace('X', '') # replace 'X' w/ empty string --> remove 'X'

if __name__ == "__main__":
    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"
    plaintext = decrypt_playfair(ciphertext, key)
    print(plaintext) # give me my solution after all that hard work 
