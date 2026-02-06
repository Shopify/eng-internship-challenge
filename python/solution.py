#solving grid, uses the key as the top row of grid then fills w/ alphabet
def create_grid(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    grid = ""
    for char in key + alphabet:
        if char not in grid:
            grid += char
    return [grid[i:i+5] for i in range(0, len(grid), 5)]

#uppercase text
def prepare_text(text):
    text = text.replace(" ", "").upper()
    return "".join(text[i] + ("X" if i + 1 < len(text) and text[i] == text[i + 1] else text[i + 1]) for i in range(0, len(text), 2))

# find char in grid
def find_position(grid, char):
    for i, row in enumerate(grid):
        if char in row:
            return i, row.index(char)

# creating letter pairs
def decrypt_pair(grid, a, b):
    row_a, col_a = find_position(grid, a)
    row_b, col_b = find_position(grid, b)
    if row_a == row_b:
        return grid[row_a][(col_a - 1) % 5] + grid[row_b][(col_b - 1) % 5]
    elif col_a == col_b:
        return grid[(row_a - 1) % 5][col_a] + grid[(row_b - 1) % 5][col_b]
    else:
        return grid[row_a][col_b] + grid[row_b][col_a]

# creating final print, gets rid of x too
def decrypt_message(grid, message):
    message = prepare_text(message)
    decrypted_message = "".join(decrypt_pair(grid, message[i], message[i + 1]) for i in range(0, len(message), 2))
    return decrypted_message.replace('X', '')

# key, but really only need first 5 letters
key = "SUPERSPY"
# cypher
message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

grid = create_grid(key)
decrypted_message = decrypt_message(grid, message)
print(decrypted_message)