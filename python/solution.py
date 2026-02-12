def create_square(key):
    letters = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    square = []
    # the square can only have 25 letters replace J with I 
    key =  key.upper().replace('J', 'I')

    # writing the keyword to the square without repeating letters
    for char in key:
        if char not in square:
            square.append(char)
    # adding the rest of the letters to the square
    for char in letters:
        if char not in square:
            square.append(char)

    # turn it into a 5x5 matrix
    square = [square[i:i+5] for i in range(0, 25, 5)]
    return square

def decrypt(txt, square):
    result = ''

    # looking at 2 chars at a time 
    for i in range(0, len(txt), 2):
        char1 = txt[i]
        char2 = txt[i+1] if i+1 < len(txt) else 'X'

        row1, col1 = [(index, row.index(char1)) for index, row in enumerate(square) if char1 in row][0] 
        row2, col2 = [(index, row.index(char2)) for index, row in enumerate(square) if char2 in row][0]

        # if the chars are in the same row
        if row1 == row2:
            result += square[row1][(col1-1)%5] + square[row2][(col2-1)%5]

        # if the chars are in the same column
        elif col1 == col2:
            result += square[(row1-1)%5][col1] + square[(row2-1)%5][col2]
        
        # if the chars are in different rows and columns
        else:
            result += square[row1][col2] + square[row2][col1]

    result = result.replace('X', '')
    return result

def main(): 
    key = 'SUPERSPY'
    cipher_txt = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'
    square = create_square(key)
    message = decrypt(cipher_txt, square)
    print(message)

if __name__ == '__main__':
    main()
