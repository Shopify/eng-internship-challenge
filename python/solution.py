def create_playfair_grid(key):
    '''
    This function accepts a key and creates the playfair grid based
    off of the key
    '''
    key = key.replace(' ', '').upper()
    key_set = set(key)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".replace('J','')

    keytable_list = []
    for char in key:
        if char not in keytable_list:
            keytable_list.append(char)
    
    keytable = "".join(keytable_list)

    for char in key + alphabet:
        if char not in key_set:
            keytable += char
            key_set.add(char)

    grid = [keytable[i:i+5] for i in range(0, 25, 5)]
    
    return grid

def decrypt(message, key):
    '''
    This function accepts a message and a key and decrypts the 
    message based off the playfair cipher
    '''
    res = ""

    grid = create_playfair_grid(key)
    # add X to end of message for odd length strings
    if len(message) % 2 != 0:
        message += 'X'
        
    pairs = [message[i:i+2] for i in range(0, len(message), 2)]

    for pair in pairs:
        char1 = pair[0]
        char2 = pair[1]

        y1, x1 = 0, 0
        y2, x2 = 0, 0

        for index, row in enumerate(grid):
            if char1 in row:
                y1, x1 = index, row.index(char1)
            if char2 in row:
                y2, x2 = index, row.index(char2)

        # Decrypt the pair based off the inverse of the encryption rules
        if y1 == y2:
            res += grid[y1][(x1 - 1) % 5] + grid[y2][(x2 - 1) % 5]
        elif x1 == x2:
            res += grid[(y1 - 1) % 5][x1] + grid[(y2 - 1) % 5][x2]
        else:
            res += grid[y1][x2] + grid[y2][x1]
    return res

def main():
    encrypted_message = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'
    key = "SUPERSPY"
    result = decrypt(encrypted_message, key).replace('X','').upper()
    print(result)
    return result

main()