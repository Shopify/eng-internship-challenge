# O(26)
def create_matrix_lookup(keyword):
    def matrix_append(char):
        nonlocal cur_row
        if len(matrix[cur_row]) == 5:
            matrix.append([])
            cur_row += 1

        matrix[cur_row].append(char)
        lookup[char] = (cur_row, len(matrix[cur_row])-1)


    keyword = keyword.upper()
    matrix = [[]]
    lookup = {}
    cur_row = 0

    for char in keyword:
        if char not in lookup and char != 'J':
            matrix_append(char)

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in lookup:
            matrix_append(char)
            
    return matrix, lookup

# O(n)
def playfair_cipher(text, keyword) -> str:
    result = ""

    text = text.upper()
    matrix, lookup = create_matrix_lookup(keyword)

    for i in range(0, len(text), 2):
        char_1 = text[i]
        char_2 = text[i+1] if i+1 < len(text) else 'X'

        row_1, col_1 = lookup[char_1]
        row_2, col_2 = lookup[char_2]

        new_char_1 = ''
        new_char_2 = ''

        # Decode
        if row_1 == row_2:
            new_char_1 = matrix[row_1][(col_1-1)]
            new_char_2 = matrix[row_2][(col_2-1)]
        elif col_1 == col_2:
            new_char_1 = matrix[(row_1-1)][col_1]
            new_char_2 = matrix[(row_2-1)][col_2]
        else:
            new_char_1 = matrix[row_1][col_2]
            new_char_2 = matrix[row_2][col_1]

        if new_char_1 != 'X':
            result += new_char_1
        if new_char_2 != 'X':
            result += new_char_2

    return result
    
def __main__():
    print(playfair_cipher("IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV", "SUPERSPY"))

if __name__ == "__main__":
    __main__()