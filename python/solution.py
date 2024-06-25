ENCODED_STRING = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
KEYCODE  = "SUPERSPY"
ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

def create_reordered_alphabet(keycode: str, alphabet: str) -> list:
    """
    Create a reordered alphabet based on the keycode.
    
    Args:
    keycode (str): The keycode used to reorder the alphabet.
    alphabet (str): The original alphabet string.
    
    Returns:
    list: A list of characters representing the reordered alphabet.
    """
    reordered = []
    for letter in keycode + alphabet:
        if letter in reordered:
            continue
        reordered.append(letter)
    return reordered


def create_grid_and_mapping(reordered_alphabet: list) -> tuple:
    """
    Create a 5x5 grid and a mapping from letters to their positions in the grid.
    
    Args:
    reordered_alphabet (list): A list of characters representing the reordered alphabet.
    
    Returns:
    tuple: A tuple containing the 5x5 grid (list of lists) and the mapping (dict).
    """
    mapping = {}
    grid = []
    for i in range(5):
        row = []
        for j in range(5):
            letter = reordered_alphabet.pop(0)
            mapping[letter] = (i, j)
            row.append(letter)
        grid.append(row)
    return grid, mapping

def decrypt_pairs(encoded_string: str, grid: list, mapping: dict):
    """
    Decrypt pairs of letters using the grid and mapping.
    
    Args:
    encoded_string (str): The string of encoded letters.
    grid (list of lists): The 5x5 grid of letters.
    mapping (dict): The mapping from letters to their positions in the grid.
    
    Returns:
    list: A list of decrypted characters.
    """
    decrypted_text = []
    for i in range(0, len(encoded_string), 2):
        first_letter = encoded_string[i]
        second_letter = encoded_string[i+1]
        
        i1, j1 = mapping[first_letter]
        i2, j2 = mapping[second_letter]

        if j1 == j2:
            # The two letters are in the same column
            decrypted_text.append(grid[i1 - 1][j1] if i1 > 0 else grid[4][j1])
            decrypted_text.append(grid[i2 - 1][j2] if i2 > 0 else grid[4][j2])
        elif i1 == i2:
            # The two letters are in the same row
            decrypted_text.append(grid[i1][j1 - 1] if j1 > 0 else grid[i1][4])
            decrypted_text.append(grid[i2][j2 - 1] if j2 > 0 else grid[i2][4])
        else:
            # The two letters form are corner in a rectangle
            decrypted_text.append(grid[i1][j2])
            decrypted_text.append(grid[i2][j1])
    
    return decrypted_text

def main():
    """Main function to perform the decryption process."""
    reordered_alphabet = create_reordered_alphabet(KEYCODE, ALPHABET)
    grid, mapping = create_grid_and_mapping(reordered_alphabet)
    decrypted_text = decrypt_pairs(ENCODED_STRING, grid, mapping)
    final_text = "".join(decrypted_text).replace('X', '')
    print(final_text)

if __name__ == "__main__":
    main()