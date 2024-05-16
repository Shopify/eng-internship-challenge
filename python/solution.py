ALPHABETS = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
FILLER_CHARACTER = 'X'
ROWS = 5
COLS = 5

"""
Creates a 5x5 key grid based on provided key and alphabet coordinates
Grid is populated with alphabets from the key first, then with remaining alphabets (repeating occurrences not added)
Args:
    key: The symmetric cipher key string used for generating the key grrd
Returns:
    tuple:
        key_grid: The generated 5x5 grid used for decryption
        alphabet_coordinates: Dictionary that maps each alphabet to its (row,col) coordinates in the key grid
"""
def makeGrid(key: str):
    key_grid = [[0 for _ in range(ROWS)] for _ in range(COLS)]
    key_index = 0
    alphabet_index = 0
    seen_alphabets = set()
    alphabet_coordinates= {}
    for row_index in range(ROWS):
        for col_index in range(COLS):
            if (key_index != len(key)):
                while (key[key_index] in seen_alphabets):
                    key_index += 1
                curr_alphabet = key[key_index]
                key_grid[row_index][col_index] = curr_alphabet
                seen_alphabets.add(curr_alphabet)
                alphabet_coordinates[curr_alphabet] = (row_index, col_index)
                key_index += 1
            else:
                while(ALPHABETS[alphabet_index] in seen_alphabets):
                    alphabet_index += 1
                curr_alphabet = ALPHABETS[alphabet_index]
                key_grid[row_index][col_index] = curr_alphabet
                seen_alphabets.add(curr_alphabet)
                alphabet_coordinates[curr_alphabet] = (row_index, col_index)
                alphabet_index+=1

    return key_grid, alphabet_coordinates

"""
Finds pairs("digrams") in an ecrypted message, adding each pair into the pairs array
Args:
    encrypted_message: Message encrypted with the PlayFair Cipher
Returns:
    pairs_array: A list of character pairs found in the encrypted message.
"""
def findPairs(encrypted_message: str):
    encrypted_message = encrypted_message.upper()
    pairs_array = []
    i = 0
    while (i < len(encrypted_message)):
        pairs_array.append((encrypted_message[i], encrypted_message[i + 1]))
        i += 2
    return pairs_array

"""
Decrypts a list of character pairs using a key grid and alphabet coordinates
Args:
    key_grid: A 2D list representing the key grid used for decryption
    pairs_array: A list of alphabet pairs(tuples) to decrypt
    alphabet_coordinates: A dictionary mapping each alphabet to its coordinates in the key grid
Returns:
    str: The decrypted plain text
"""
def decrypt(key_grid: list, pairs_array: list, alphabet_coordinates: dict):
    plain_text = []
    for pair in pairs_array:
        first_alphabet_in_pair, second_alphabet_in_pair = pair
        first_alphabet_row_in_grid, first_alphabet_col_in_grid = alphabet_coordinates[first_alphabet_in_pair]
        second_alphabet_row_in_grid, second_alphabet_col_in_grid = alphabet_coordinates[second_alphabet_in_pair]

        if (first_alphabet_row_in_grid == second_alphabet_row_in_grid):
            first_alphabet_decrypted = key_grid[first_alphabet_row_in_grid][(first_alphabet_col_in_grid - 1) % 5]
            second_alphabet_decrypted = key_grid[second_alphabet_row_in_grid][(second_alphabet_col_in_grid - 1) % 5]
            plain_text.append(first_alphabet_decrypted)
            plain_text.append(second_alphabet_decrypted)
        elif (first_alphabet_col_in_grid == second_alphabet_col_in_grid):
            first_alphabet_decrypted = key_grid[(first_alphabet_row_in_grid - 1) % 5][first_alphabet_col_in_grid]
            second_alphabet_decrypted = key_grid[(second_alphabet_row_in_grid - 1) % 5][second_alphabet_col_in_grid]
            plain_text.append(first_alphabet_decrypted)
            plain_text.append(second_alphabet_decrypted)
        else:
            first_alphabet_decrypted = key_grid[first_alphabet_row_in_grid][second_alphabet_col_in_grid]
            second_alphabet_decrypted = key_grid[second_alphabet_row_in_grid][first_alphabet_col_in_grid]
            plain_text.append(first_alphabet_decrypted)
            plain_text.append(second_alphabet_decrypted)

    return ''.join([char for char in plain_text if char != FILLER_CHARACTER])

def main():
    key = "SUPERSPY"
    encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key_grid, alphabet_coordinates_in_grid = makeGrid(key)
    pairs_array = findPairs(encrypted_message)
    decrypted_message = decrypt(key_grid, pairs_array, alphabet_coordinates_in_grid)
    print(decrypted_message)

if __name__ == "__main__":
    main()