import string

# Assuming the implementation that omits "J"

def generate_playfair_grid(key):
    # The alphabet in uppercase
    alphabet = string.ascii_uppercase.replace("J", "")

    added = set()
    grid = []

    # Make the grid (in a 1D list)
    for c in key + alphabet:
        if c not in added:
            added.add(c)
            grid.append(c)
    
    # Return the generated grid broken into a 5x5 grid
    return [grid[i:i+5] for i in range(0, 25, 5)]


def find_char_in_grid(char, grid):
    # Iterate through the grid to find the location of the character
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == char:
                # Return the row and column indices
                return r, c
    
    # Return None if it wasn't found
    return -1, -1


def solve_cipher(text, key):
    # Convert both the encripted text and key to UPPERCASE
    text = text.upper()
    key = key.upper()

    # Make the 5x5 grid
    grid = generate_playfair_grid(key)

    solved_text = ""

    # Iterate through the encrypted text
    # Assuming length of the text is ALWAYS EVEN
    i = 0
    while i < len(text):
        # Store the first and second characters temporarily
        first = text[i]
        second = text[i + 1]

        # Find the row and column of the two characters in the grid
        r_first, c_first = find_char_in_grid(first, grid)
        r_second, c_second = find_char_in_grid(second, grid)

        # Check for issues with the character being missing from grid
        if r_first == -1 or r_second == -1:
            print("An error has occured: a character wasn't found in the grid")
            print("Potentially an issue with 'J' not being in the grid")
            print("Exiting...")
            return None

        # Check for the 3 cases, row, column, rectangle
        if r_first == r_second:
            # They are in the same row
            solved_text += grid[r_first][(c_first - 1) % 5]
            solved_text += grid[r_second][(c_second - 1) % 5]
        elif c_first == c_second:
            # They are in the same column
            solved_text += grid[(r_first - 1) % 5][c_first]
            solved_text += grid[(r_second - 1) % 5][c_second]
        else:
            # They are in a rectangle shape
            solved_text += grid[r_first][c_second]
            solved_text += grid[r_second][c_first]

        # Go to the pair of characters
        i += 2
    
    # Find the Xs added during encryption
    to_be_removed = []
    for i, c in enumerate(solved_text):
        if c == "X" and i > 0:
            if i == len(solved_text) - 1:
                to_be_removed.append(i)
            elif solved_text[i - 1] == solved_text[i + 1]:
                to_be_removed.append(i)
    
    # Remove the Xs that was added during encryption
    offset = 0
    for i in to_be_removed:        
        solved_text = solved_text[:i - offset] + solved_text[i - offset + 1:]
        offset += 1

    # Return the solved text
    return solved_text

# Task
key = "SUPERSPY"
encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

# Result
result = solve_cipher(encrypted_message, key)

# Print
print(result)

