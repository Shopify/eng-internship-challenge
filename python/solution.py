def encryptDigraph(digraph, keySquare):
    """Encrypts a single digraph (pair of letters) using the Playfair cipher rules."""

    letter1_position = findPosition(digraph[0], keySquare)
    letter2_position = findPosition(digraph[1], keySquare)

    # Rule 1: Same Row (Both letters are in the same row of the key square)
    if letter1_position[0] == letter2_position[0]:
        # Calculate the new column index for the first and second letters.
        # It adds 1 to shift the letter one position to the right, implementing wrapping behavior,
        # meaning that the index loops back to the beggining of the row if the index goes beyond the grid size.
        new_col1 = (letter1_position[1] + 1) % 5
        new_col2 = (letter2_position[1] + 1) % 5
        # Get the new letters from the keySquare
        new_letter1 = keySquare[letter1_position[0]][new_col1]
        new_letter2 = keySquare[letter2_position[0]][new_col2]
        # Return the encrypted digraph
        return new_letter1 + new_letter2

    # Rule 2: Same Column (Both letters are in the same column of the key square)
    elif letter1_position[1] == letter2_position[1]: 
        # Add 1 to move one position down, implementing wrapping behavior, meaning that the
        # index loops back to the beggining of the column if the index goes beyond the grid size.
        new_row1 = (letter1_position[0] + 1) % 5  
        new_row2 = (letter2_position[0] + 1) % 5
        # Get the new letters from the keySquare
        new_letter1 = keySquare[new_row1][letter1_position[1]]
        new_letter2 = keySquare[new_row2][letter2_position[1]]
        # Return the encrypted digraph
        return new_letter1 + new_letter2

    # Rule 3: Rectangle
    else: 
        # Get the letter at the same row as letter1, column of letter2
        new_letter1 = keySquare[letter1_position[0]][letter2_position[1]]
        # Get the letter at the same row as letter2, column of letter1
        new_letter2 = keySquare[letter2_position[0]][letter1_position[1]]
        return new_letter1 + new_letter2


def decryptDigraph(digraph, keySquare):
    """Decrypts a single digraph (pair of letters) using the Playfair cipher rules."""

    letter1_pos = findPosition(digraph[0], keySquare)
    letter2_pos = findPosition(digraph[1], keySquare)

    # Rule 1: Same Row 
    if letter1_pos[0] == letter2_pos[0]:
        new_col1 = (letter1_pos[1] - 1) % 5
        new_col2 = (letter2_pos[1] - 1) % 5
        new_letter1 = keySquare[letter1_pos[0]][new_col1]
        new_letter2 = keySquare[letter2_pos[0]][new_col2]
        return new_letter1 + new_letter2

    # Rule 2: Same Column 
    elif letter1_pos[1] == letter2_pos[1]: 
        new_row1 = (letter1_pos[0] - 1) % 5
        new_row2 = (letter2_pos[0] - 1) % 5
        new_letter1 = keySquare[new_row1][letter1_pos[1]]
        new_letter2 = keySquare[new_row2][letter2_pos[1]]
        return new_letter1 + new_letter2

    # Rule 3: Rectangle 
    else: 
        new_letter1 = keySquare[letter1_pos[0]][letter2_pos[1]]
        new_letter2 = keySquare[letter2_pos[0]][letter1_pos[1]]
        return new_letter1 + new_letter2


def findPosition(letter, keySquare):
  """ Finds the position of a letter (row, column) of a letter in the key square.
      This assumes that a 5x5 key square is stored as a list of lists.
  """
  for row_index, row in enumerate(keySquare):
    # Check if the letter exists in the current row that we are checking
    if letter in row:
      # Get the index of the column where the letter is
      column_index = row.index(letter)
      return (row_index, column_index)
  
  # If the letter is not found
  return None


def prepareCiphertext(ciphertext):
    """Prepares the ciphertext for Playfair cipher decryption."""
    ciphertext = ciphertext.upper().replace("J", "I")
    
    digraphs = []
    for i in range(0, len(ciphertext), 2):
        digraph = ciphertext[i:i+2]
        if len(digraph) == 1:
            digraph += "X"
        if digraph[0] == digraph[1]:
            digraph = digraph[0] + "X" + digraph[1]
        digraphs.append(digraph)

    return digraphs

  
def buildKeySquare(keyword):
    """Builds the 5x5 Playfair key square from the given keyword."""
    
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_square = []
    seen_letters = set()  

    for char in keyword.upper():
        if char == "J":
            char = "I"
        if char not in seen_letters:
            key_square.append(char)
            seen_letters.add(char)
    
    for char in alphabet:
        if char not in seen_letters:
            key_square.append(char)
            seen_letters.add(char)

    key_square_grid = [key_square[i:i+5] for i in range(0, 25, 5)]
    return key_square_grid


def solvePlayfair(ciphertext, keyword):
    """Decrypts the given ciphertext using the Playfair cipher with the provided keyword."""
    key_square = buildKeySquare(keyword)
    digraphs = prepareCiphertext(ciphertext)
    decrypted_text = "".join(decryptDigraph(dg, key_square) for dg in digraphs)
    decrypted_text = decrypted_text.replace('X', '')
    return decrypted_text  


if __name__ == "__main__":
    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    keyword = "SUPERSPY"  
    result = solvePlayfair(ciphertext, keyword) 
    print(result) 
