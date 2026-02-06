def create_table(key):
    """
    Creates the 5x5 cipher table according to the Playfair cipher rules
    """
    
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

    # Check for invalid characters in key
    key = key.upper().replace('J', 'I')

    for c in key:
        if not c.isalpha():
            key.replace(c, '')

    table = []
    table_string = ''
    
    # Uniquely add the letters using the key, then the rest of the alphabet
    for c in key:
        if c not in table_string:
            table_string += c
    for c in alphabet:
        if c not in table_string:
            table_string += c

    # Create a list of lists (5x5) from the string created above
    table = [table_string[i:i+5] for i in range(0, 25, 5)]
    return table

def create_coordinates(table):
    """
    Returns the coordinates of each alphabet in the Playfair table as a map
    """

    coords = {}
    for i in range(5):
        for j in range(5):
            coords[table[i][j]] = (i, j)
    return coords

def group(text):
    """
    Groups the encoded text into list of 2 characters while following Playfair cipher rules
    """

    grouped = []
    newstring = ''

    # Add the character X when required (1. Two repeating chars, 2. Odd length)
    for i in range(0, len(text) - 1, 2):
        newstring += text[i] + ('X' if text[i] == text[i + 1] else text[i+1])

    if len(text) % 2 == 1: 
        text += 'X'

    # Group every two characters into list
    grouped = [text[i:i+2] for i in range(0, len(text), 2)]

    return grouped

def decode(grouped, table, coords):
    """
    Decodes the grouped text using the cipher table and coordinates of each letter
    """

    decoded = ''

    # Loop through each pair of letters
    for i in grouped:
        # Retrieve the coordinates of the letters
        rowA = coords[i[0]][0]
        colA = coords[i[0]][1]
        rowB = coords[i[1]][0]
        colB = coords[i[1]][1]

        # 3 Cases of rules in order: same row, same column, rectangle
        if rowA == rowB:
            decoded += table[rowA][(colA - 1) % 5]
            decoded += table[rowB][(colB - 1) % 5]
        elif colA == colB:
            decoded += table[(rowA - 1) % 5][colA]
            decoded += table[(rowB - 1) % 5][colB]
        else:
            decoded += table[rowA][colB]
            decoded += table[rowB][colA]

    return decoded.replace('X', '').replace(' ', '')

def main():
    key = 'SUPERSPY'
    text = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'

    # Creates the 5x5 table
    table = create_table(key)

    # Pre-computes the coordinates of each letter
    coords = create_coordinates(table)

    # Groups the encoded text
    grouped = group(text)

    # Deciphers using all the pre-computed items above
    print(decode(grouped, table, coords))
    
if __name__ == '__main__':
    main()