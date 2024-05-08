# Giovanni Belval solution

import itertools

ENCODED_STRING = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
KEYCODE  = "SUPERSPY"
ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"


# we reorder the alphabet based of the keycode
rearranged_letters = []
for letter in itertools.chain(KEYCODE, ALPHABET):
    rearranged_letters.append(letter) if letter not in rearranged_letters else ""


mapping = {} # mapping between a letter and its position in the grid
grid    = [] # decoding grid

# filling the grid with the reordered letters
# and the mapping

for i in range(5):
    grid.append([])
    
    for j in range(5):
        letter = rearranged_letters.pop(0)
        mapping[letter] = (i, j)
        grid[-1].append(letter)
        

decrypted_text = []

# we loop trough each following pairs of letters
for i in range(0, len(ENCODED_STRING), 2):
    
    first_letter  = ENCODED_STRING[i]
    second_letter = ENCODED_STRING[i+1]
    
    # we store the indexes in the grid
    i1, j1 = mapping[first_letter]
    i2, j2 = mapping[second_letter]
    
    if j1 == j2:
        # the two letters are on the same column in the grid
        
        # we add the letter at the left circularely
        # for the two letters in our pair
        decrypted_text.append(
            grid[i1 - 1][j1] if i1 > 0 else grid[4][j1]
        )
        
        decrypted_text.append(
            grid[i2 - 1][j2] if i2 > 0 else grid[4][j2]
        )
        

    elif i1 == i2:
        # the two letters are on the same line in the grid
        
        # we add the letter at the top circularely
        # for the two letters in our pair
        decrypted_text.append(
            grid[i1][j1 - 1] if j1 > 0 else grid[i1][4]
        )
        
        decrypted_text.append(
            grid[i2][j2 - 1] if j2 > 0 else grid[i2][4]
        )
    
    else:
        # we switch the column index of the two letters
        # in the grid
        decrypted_text.append(
            grid[i1][j2]
        )
        
        decrypted_text.append(
            grid[i2][j1]
        )
   
# we remove the X and print the final text    
final_text = "".join(decrypted_text).replace('X', '') 
print(final_text)