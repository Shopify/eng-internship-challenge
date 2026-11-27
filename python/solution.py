import string

# Given Information
enc_msg = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
given_key = "SUPERSPY"

# Initialize 2D Playfair Grid
cols = 5
rows = 5
grid = [["" for _ in range(cols)] for _ in range(rows)]
# Final Solution
sol = ""

# Finds the [x,y] coordinates of a given char in the playfair grid
def find(char):
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == char:
                return [i, j]


# Step 1: Generate the 2D Playfair Grid using given_key

# Generate the entire 1D Key
oned_key = ""
char_set = set()
# Iterate over given_key to add unique letters
# We use char_set since checking if a character is in the set takes O(1) time
for char in given_key:
    if (char not in char_set):
        char_set.add(char)  
        oned_key += char
# Add the rest of the letters with the same approach
# string.ascii_uppercase is an array of uppercase letters
# Ignore "J" character as specified in the wikipedia page
for char in string.ascii_uppercase:
    if (char not in char_set) and (char != "J"):
        char_set.add(char)
        oned_key += char

# Convert 1D Keyword into 2D Playfair Grid
key_i = 0
for i in range(rows):
    for j in range(cols):
        grid[i][j] = oned_key[key_i]
        key_i += 1


# Step 2: Main decryption algorithm using the Playfair Grid and enc_msg

# Iterate over digrams
for i in range(0, len(enc_msg), 2):
    # Find x,y of both letters in the playfair grid
    [char1_row, char1_col] = find(enc_msg[i])
    [char2_row, char2_col] = find(enc_msg[i + 1])

    # Rule 2: if letters appear in the same row, shift each letter right 
    # That means to decrpyt, we shift left 
    if (char1_row == char2_row):
        sol += grid[char1_row][(char1_col - 1) % 5]
        sol += grid[char2_row][(char2_col - 1) % 5]

    # Rule 3: if letters appear in the same col, shift each letter down
    # That means to decrpyt, we shift up
    elif (char1_col == char2_col):
        sol += grid[(char1_row - 1) % 5][char1_col]
        sol += grid[(char2_row - 1) % 5][char2_col]

    # Rule 4: Each letter takes its own row and its partner's column
    # To decrypt, we can apply the same rule
    else:
        sol += grid[char1_row][char2_col]
        sol += grid[char2_row][char1_col]

# Rule 1: If both letters are the same, add "X" after the first letter
# To decrpyt, we remove all instances of "X"
sol = sol.replace('X', '')

# Output final solution to console!
print(sol)
