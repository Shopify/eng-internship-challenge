def generateTable(key):
    # Create a dictionary to map each letter (except 'J') to a tuple (-1,-1) initially
    dict = {chr(i): (-1,-1) for i in range(65,91)}
    dict.pop('J')

    # Initialize a 5x5 table with empty strings
    table = [["" for i in range(5)] for j in range(5)]

    # Set initial position for filling the table
    row, col = 0, 0
    # Fill the table with the letters in the key first, checking for duplicates
    for i in (key):
        if dict[i] == (-1,-1):
            table[row][col] = i
            dict[i] = (row, col)
            col += 1
            # Move to the next row after filling one row
            if col == 5:
                col = 0
                row += 1
    
    # Fill the table with the remaining letters in alphabetical order
    for i in dict:
        if dict[i] == (-1,-1):
            table[row][col] = i
            dict[i] = (row, col)
            col += 1
            # Move to the next row after filling one row
            if col == 5:
                col = 0
                row += 1
    # Return the dictionary of letter coordinates and the completed table
    return dict, table

def decrypt(key, text):
    # Generate the dictionary and table from the key
    dict, table = generateTable(key)
    decText = ""
    
    # Process the ciphertext two characters at a time
    for i in range(0, len(text), 2):
        # Get the positions of each pair of characters
        a, b = dict[text[i]], dict[text[i+1]]
        # If characters are in the same row, shift them left
        if a[0] == b[0]:
            decText += table[a[0]][(a[1]-1)%5] + table[b[0]][(b[1]-1)%5]
        # If characters are in the same column, shift them up
        elif a[1] == b[1]:
            decText += table[(a[0]-1)%5][b[1]] + table[(b[0]-1)%5][b[1]]
        # If characters form a rectangle, swap the columns
        else:
            decText += table[a[0]][b[1]] + table[b[0]][a[1]]

    # Return the plaintext, replacing any 'X' used for padding in the encryption
    return decText.replace('X','')


if __name__ == '__main__':
    key = "SUPERSPY"
    text = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    decText = decrypt(key, text)
    print(decText, end='')
