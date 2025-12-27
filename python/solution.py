#!/usr/bin/env python3

def sanitize(s):
    if not isinstance(s, str) or not s:
        raise ValueError("Input must be a non-empty string.")
    
    clean_string = s.upper().replace('J', 'I')
    clean_string = ''.join([char for char in clean_string if char.isalpha()])

    if not clean_string:
        raise ValueError("Not enough valid characters in input.")
    
    return clean_string

def generate_grid(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" # Omit 'J'
    key = sanitize(key)
    print(key)
    key_grid = []
    
    for char in key:
        if char not in key_grid:
            key_grid.append(char)
    
    for char in alphabet:
        if char not in key_grid:
            key_grid.append(char)
    
    grid = [key_grid[i:i+5] for i in range(0, len(key_grid), 5)]
    
    return grid

def decrypt_message(message, grid):
    decrypted = ""

    message = sanitize(message) # Clean message to avoid errors

    # Constraints: remove 'X', remove special chars, remove spaces
    # Edgecases: must wrap around edges if necessary

    for digraph_point in range(0, len(message), 2):
        letter1, letter2 = message[digraph_point], message[digraph_point+1]

        letter1_row = -1
        letter1_col = -1
        letter2_row = -1
        letter2_col = -1
        
        for rIndex, row in enumerate(grid):
            if letter1 in row:
                letter1_row = rIndex
                letter1_col = row.index(letter1)
            if letter2 in row:
                letter2_row = rIndex
                letter2_col = row.index(letter2)
        
        if letter1_row == letter2_row:
            # print(f"Same row: {letter1} and {letter2}")
            decrypted_digraph = grid[letter1_row][(letter1_col-1) % len(row)] + grid[letter2_row][(letter2_col-1) % len(row)] # Implemented wrap logic although technically not necessary with negative indexing
            decrypted += decrypted_digraph
        elif letter1_col == letter2_col:
            # print(f"Same column: {letter1} and {letter2}")
            decrypted_digraph = grid[(letter1_row-1) % len(grid)][letter1_col] + grid[(letter2_row-1) % len(grid)][letter2_col] # Implemented wrap logic although technically not necessary with negative indexing
            decrypted += decrypted_digraph
        else:
            # print(f"Rectangle: {letter1} and {letter2}")
            decrypted_digraph = grid[letter1_row][letter2_col] + grid[letter2_row][letter1_col]
            decrypted += decrypted_digraph
            
    decrypted = decrypted.replace("X", "")
    decrypted = ''.join([char for char in decrypted if char.isalpha()])
    return decrypted

def main():
    message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"
    
    grid = generate_grid(key)
    # grid = [
    #     ['S','U','P','E','R'],
    #     ['Y','A','B','C','D'],
    #     ['F','G','H','I','K'],
    #     ['L','M','N','O','Q'],
    #     ['T','V','W','X','Z']
    # ]
    
    decrypted_message = decrypt_message(message, grid)
    print(decrypted_message)
    return decrypted_message

main()