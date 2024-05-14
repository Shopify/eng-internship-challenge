def playfair_cipher(key, encrypted):
    # Ensure the key and encrypted text is all UPPER CASE
    key.upper()
    encrypted.upper()
    
    # Dynamically fill grid based on the key provided
    grid, grid_dict = create_grid(key)
    
    # Break the encrypted phrase into pairs of letters
    pairs = [encrypted[i : i + 2] for i in range(0, len(encrypted), 2)]
    
    # For each pair in pairs
    decrypted_pairs = []
    for pair in pairs:
        # Lookup first and second letter in the dict to get the coordinates of each
        first_coords = grid_dict[pair[0]]
        second_coords = grid_dict[pair[1]]
        # Compare the two coordinates, determine which rule applies, update pairs string with new pair string deencrypted
        determine_rule(first_coords, second_coords, decrypted_pairs, grid)
   
    # Collapse the pairs structure into one string
    decrypted = ''.join(decrypted_pairs)
    
    # Ensure the string does not have spaces, the letter "X", or special characters
    decrypted = decrypted.replace(' ', '').replace('X', '')
    decrypted = ''.join(letter for letter in decrypted if letter.isalnum())
    
    # Return the result
    return decrypted
    
    
def create_grid(key):
    # Define variables
    letters = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Locate unique letters in the key
    for l in key:
        if l not in letters:
            letters.append(l)

    # Add the rest of the alphabet to the unique letters, skipping J
    for a in alphabet:
        if a == 'J':
            a = 'I'
        if a not in letters:
            letters.append(a)

    # Turn the letters list into a 2D grid structure
    grid = [[letters[row * 5 + col] for col in range(5)] for row in range(5)]
    
    # Turn the grid into a dictionary of coordinates
    grid_dict = {}
    for i, row in enumerate(grid):
        for j, letter in enumerate(row):
            grid_dict[letter] = (i, j)
    
    # Return the grid and the grid_dict
    return grid, grid_dict


def determine_rule(first_coords, second_coords, decrypted_pairs, grid):
    # 1) ROWS EQUAL
    if first_coords[0] == second_coords[0]:
        # Keep the same row, and move left 1 column for both coordinates
        decrypted_pairs.append(grid[first_coords[0]][first_coords[1] - 1] + grid[second_coords[0]][second_coords[1] - 1])
    # 2) COLUMNS EQUAL
    if first_coords[1] == second_coords[1]:
        # Keep the same column, and move up 1 row for both coordinates
        decrypted_pairs.append(grid[first_coords[0] - 1][first_coords[1]] + grid[second_coords[0] - 1][second_coords[1]]) 
    # 3) NOTHING EQUAL
    if first_coords[0] != second_coords[0] and first_coords[1] != second_coords[1]:
        # Keep the same row, swap column values
        decrypted_pairs.append(grid[first_coords[0]][second_coords[1]] + grid[second_coords[0]][first_coords[1]])


if __name__ == '__main__':
    key = "SUPERSPY"
    encrypted = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    print(playfair_cipher(key, encrypted))