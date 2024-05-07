def find_row_col(grid, ch):
    for row in range(5):
        for col in range(5):
            if grid[row][col] == ch:
                return row, col


def build_grid(key):
    remaining_set = set("ABCDEFGHIKLMNOPQRSTUVWXYZ") - set(key)
    remaining_alphabet = sorted(list(remaining_set))

    # create 5x5 matrix grid
    grid = [["" for _ in range(5)] for _ in range(5)]
    for r in range(5):
        for c in range(5):
            if key:
                grid[r][c] = key[0]
                key = key[1:]
            else:
                grid[r][c] = remaining_alphabet[0]
                remaining_alphabet = remaining_alphabet[1:]
    return grid


if __name__ == '__main__':
    encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    # removed duplicate letters in the key
    key = "SUPERY"

    # create 5x5 matrix grid
    grid = build_grid(key)

    message = []
    for i in range(0, len(encrypted_message) - 2, 2):
        pair = encrypted_message[i:i + 2]
        row1, col1 = find_row_col(grid, pair[0])
        row2, col2 = find_row_col(grid, pair[1])

        if row1 == row2:
            message.append(grid[row1][(col1 + 1) % 5] + grid[row2][(col2 + 1) % 5])
        elif col1 == col2:
            message.append(grid[(row1 + 1) % 5][col1] + grid[(row2 + 1) % 5][col2])
        else:
            message.append(grid[row1][col2] + grid[row2][col1])
    print(''.join(message), end='')
