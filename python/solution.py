grid_dict = {}
grid = []

def create_playfair_grid(keyword):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" # omit J
    keyword = "".join(sorted(set(keyword), key=keyword.index)) # remove duplicates
    sequence = keyword + "".join([c for c in alphabet if c not in keyword])

    for i in range(5):
        row = ""
        for j in range(5):
            row += sequence[i*5 + j]
            grid_dict[sequence[i*5 + j]] = (i, j)
        grid.append(row)
    
    return grid, grid_dict

def decipher_row(c1, c2):
    row = grid_dict[c1][0]
    col_1 = (grid_dict[c1][1] - 1) % 5
    col_2 = (grid_dict[c2][1] - 1) % 5
    return f"{grid[row][col_1]}{grid[row][col_2]}"

def decipher_col(c1, c2):
    col = grid_dict[c1][1]
    row_1 = (grid_dict[c1][0] - 1) % 5
    row_2 = (grid_dict[c2][0] - 1) % 5
    return f"{grid[row_1][col]}{grid[row_2][col]}"

def decipher_rect(c1, c2):
    row_1, col_2 = grid_dict[c1]
    row_2, col_1 = grid_dict[c2]
    return f"{grid[row_1][col_1]}{grid[row_2][col_2]}"


def decipher():
    KEYWORD = "SUPERSPY"
    MESSAGE = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

    grid, grid_dict = create_playfair_grid(KEYWORD)
    
    decrypted_message = ""
    i = 0
    while i < len(MESSAGE):
        c1 = MESSAGE[i]
        c2 = MESSAGE[i+1]

        # Check if pairs are in same row
        if grid_dict[c1][0] == grid_dict[c2][0]:
            decrypted_message += decipher_row(c1, c2)
        # Check if pairs are in same column
        elif grid_dict[c1][1] == grid_dict[c2][1]:
            decrypted_message += decipher_col(c1, c2)
        # Otherwise, pairs form a rectangle
        else:
            decrypted_message += decipher_rect(c1, c2)
        
        i += 2
    
    decrypted_message = decrypted_message.replace("X", "")
    print(decrypted_message)

if __name__ == "__main__":
    decipher()