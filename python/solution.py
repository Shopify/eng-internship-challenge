def generate_playfair_grid(key):
    """
    This function generates a 5x5 Playfair grid using a given key
    """
    matrix = []
    alphabet = list('ABCDEFGHIKLMNOPQRSTUVWXYZ') 

    # Convert key to uppercase, replace 'J' with 'I', and remove duplicates, while keeping order
    seen = set()
    key = ''.join(ch for ch in key.upper().replace('J', 'I') if not (ch in seen or seen.add(ch)))

    # create 5x5 matrix
    for k in key:
        if k in alphabet:
            matrix.append(k)
            alphabet.remove(k)
    matrix += sorted(alphabet)

    matrix = [matrix[n:n+5] for n in range(0, len(matrix), 5)]  # split into 5x5

    return matrix

def find_grid_position(letter, grid):
    """
    This function finds and returns the position (i, j) of a given letter in the grid.
    If the letter is not found, it returns None
    """
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == letter:
                return i, j

def playfair_decrypt(key, text):
    """
    This function decrypts a given text using a Playfair cipher with a given key.
    """
    matrix = generate_playfair_grid(key)

    # process text
    if len(text) % 2 != 0:
        text += 'Z'  # append filler character if text length is odd
    pairs = [text[n:n+2] for n in range(0, len(text), 2)]

    decrypted_text = ''
    for pair in pairs:
        pos1 = find_grid_position(pair[0], matrix)
        pos2 = find_grid_position(pair[1], matrix)

        if pos1[0] == pos2[0]:  # same row
            decrypted_text += matrix[pos1[0]][(pos1[1]-1)%5] + matrix[pos2[0]][(pos2[1]-1)%5]
        elif pos1[1] == pos2[1]:  # same column
            decrypted_text += matrix[(pos1[0]-1)%5][pos1[1]] + matrix[(pos2[0]-1)%5][pos2[1]]
        else:  # rectangle
            decrypted_text += matrix[pos1[0]][pos2[1]] + matrix[pos2[0]][pos1[1]]

    # Post-processing: remove 'X', spaces, and special characters, and ensure upper case
    decrypted_text = decrypted_text.replace('X', '').replace(' ', '').upper()
    special_chars = list('`~!@#$%^&*()-_=+[{]}\|;:\'",<.>/?')
    for char in special_chars:
        decrypted_text = decrypted_text.replace(char, '')

    return decrypted_text

print(playfair_decrypt('SUPERSPY', 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'))