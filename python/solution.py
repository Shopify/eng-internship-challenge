encoded_pairs = ['IK', 'EW', 'EN', 'EN', 'XL', 'NQ', 'LP', 'ZS', 'LE', 'RU',
                 'MR', 'HE', 'ER', 'YB', 'OF', 'NE', 'IN', 'CH', 'CV']

playfair_grid = [['S', 'U', 'P', 'E', 'R'],
                 ['Y', 'A', 'B', 'C', 'D'],
                 ['F', 'G', 'H', 'I', 'K'],
                 ['L', 'M', 'N', 'O', 'Q'],
                 ['T', 'V', 'W', 'X', 'Z']]


def main() -> None:
    decoded_text = ''

    for i in range(len(encoded_pairs)):
        f_row, f_col = find_row_col(encoded_pairs[i][0])
        s_row, s_col = find_row_col(encoded_pairs[i][1])

        new_f_row, new_f_col = f_row, f_col
        new_s_row, new_s_col = s_row, s_col

        if f_row == s_row:
            new_f_col = adjust_index(f_col - 1)
            new_s_col = adjust_index(s_col - 1)
        elif f_col == s_col:
            new_f_row = adjust_index(f_row - 1)
            new_s_row = adjust_index(s_row - 1)
        else:
            new_f_col, new_s_col = s_col, f_col

        decoded_text += playfair_grid[new_f_row][new_f_col]
        decoded_text += playfair_grid[new_s_row][new_s_col]

    decoded_text = decoded_text.replace('X', '')
    return(decoded_text)


def find_row_col(letter: str) -> tuple[int, int]:
    for i in range(5):
        for j in range(5):
            if playfair_grid[i][j] == letter:
                return i, j

    return -1, -1


def adjust_index(index: int) -> int:
    if index < 0:
        return 5 + index
    if index > 4:
        return index - 5
    return index


if __name__ == '__main__':
    print(main())
