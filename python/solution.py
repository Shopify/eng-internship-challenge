
# generates the 5x5 table used in the cypher
# returns: list of str
# assuming I and J are interchangable
def generate_table(keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    table_str = ""
    table = []
    letters = set()

    keyword = "".join([c.upper() for c in keyword if c.isalpha()]) # remove non-letters + uppercase

    word = keyword + alphabet
    for c in word:
        if c == 'J': c = 'I'
        if c not in letters:
            table_str += c
            letters.add(c)
    
    # put it in list
    for i in range(0, 25, 5):
        table.append(table_str[i:i+5])

    return table


# generates the dictionary as letter : position in table
# returns: dict
def getPosDict(table):
    pos = {}
    for i in range(len(table)):
        for j in range(len(table[i])):
            pos[table[i][j]] = (i, j)
    return pos


# gets the decrpyted string from an encrypted string and keyword
# returns: str
# assumes the encrypted string is valid
def decrypt(encrypted_str, keyword):
    table = generate_table(keyword)
    pos = getPosDict(table)
    encrypted_str = "".join([c.upper() for c in encrypted_str if c.isalpha()]) # remove nonletters + upper case
    decrypted_msg = ""

    for i in range(0, len(encrypted_str), 2):
        a, b = encrypted_str[i], encrypted_str[i+1]
        (row_a, col_a), (row_b, col_b) = pos[a], pos[b]

        if row_a == row_b:      # case 1: a & b are on the same row => move one index left
            decrypted_pair = table[row_a][col_a-1] + table[row_b][col_b-1]
        elif col_a == col_b:    # case 2: a & b are on the same col => move one index up
            decrypted_pair = table[row_a-1][col_a] + table[row_b-1][col_b]
        else:                   # case 3: a & b in different row & col => move them to opposite
            decrypted_pair = table[row_a][col_b] + table[row_b][col_a]
        
        if decrypted_pair[1] == 'X': decrypted_pair = decrypted_pair[0] # remove X
        decrypted_msg += decrypted_pair
    
    return decrypted_msg


if __name__ == "__main__":
    encrypted_msg = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    keyword = "SUPERSPY"

    print(decrypt(encrypted_msg, keyword))

