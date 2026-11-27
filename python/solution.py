def generate_table(key):
    letters = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' 
    table = []
    key = key.upper().replace('J', 'I')  

    #two for loops generate to table
    for char in key:
        if char not in table:
            table.append(char)
    for char in letters:
        if char not in table:
            table.append(char)

    #generates a 5x5 matrix from table
    table = [table[i:i+5] for i in range(0, len(table), 5)]
    return table

def decrypt(text, table):
    decrypted_text = ''

    #iterate through the text two characters at a time
    for i in range(0, len(text), 2):
        char1 = text[i]
        char2 = text[i+1]
        row1, col1 = [(index, row.index(char1)) for index, row in enumerate(table) if char1 in row][0]
        row2, col2 = [(index, row.index(char2)) for index, row in enumerate(table) if char2 in row][0]

        #handle the three cases here: same col, row, and rectangle
        if row1 == row2:
            decrypted_text += table[row1][(col1-1)%5] + table[row2][(col2-1)%5]
        elif col1 == col2:
            decrypted_text += table[(row1-1)%5][col1] + table[(row2-1)%5][col2]
        else:
            decrypted_text += table[row1][col2] + table[row2][col1]
    return decrypted_text.replace('X', '')

def main():
    key = 'SUPERSPY'
    encrypt = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'
    table = generate_table(key)
    decrypt_txt = decrypt(encrypt, table)
    print(decrypt_txt)

if __name__ == '__main__':
    main()
