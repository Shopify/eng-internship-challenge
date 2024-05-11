# Consturct string of chars that will fill grid
def construct_key_string(key):
    key_string = ''
    s = set() # set of seen characters to avoid duplicates

    for c in key:
        if c not in s:
            key_string += c
            s.add(c)

    # iterate through alphabet using unicode representation
    for i in range(26):
        char = chr(65+i)
        if char not in s and char != 'J': # omitting 'J'
            key_string += char
            s.add(char)

    return key_string

# Creates Polybius square for cipher
def construct_grid(key_string):
    # initialize 5x5 grid for cipher
    cipher_grid = [['' for i in range(5)] for j in range(5)]
    # map to find position of character in cipher in O(1)
    letter_position_map = {}
    k = 0

    for i in range(5):
        for j in range(5):
            cipher_grid[i][j] = key_string[k]
            letter_position_map[key_string[k]] = (i, j)
            k += 1

    return (cipher_grid, letter_position_map)


# Decipher input text with cipher key
def decipher(text, key):
    key_string = construct_key_string(key)
    polybius, letter_map = construct_grid(key_string)
    # digram pairs
    i, j = 0, 1

    res = ''

    while i < len(text):
        # position of characters
        char1 = letter_map[text[i]]
        char2 = letter_map[text[j]]
        # same row
        if char1[0] == char2[0]:
            res += polybius[char1[0]][char1[1]-1]
            res += polybius[char2[0]][char2[1]-1]
        # same column
        elif char1[1] == char2[1]:
            res += polybius[char1[0]-1][char1[1]]
            res += polybius[char2[0]-1][char2[1]]
        # different row and column
        else:
            res += polybius[char1[0]][char2[1]]
            res += polybius[char2[0]][char1[1]]

        i += 2
        j += 2
    
    return res.replace('X', '')


if __name__ == "__main__":
    cipher_key = 'SUPERSPY'
    cipher_text = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'
    print(decipher(cipher_text, cipher_key))