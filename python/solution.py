def processText(text):
    """
    Removes everything from the text that isnt part of the alphabet and returns it.
    """
    processed = ""
    for char in text.upper():
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            processed += char
    return processed

def getKeyTable(keyword):
    """
    Generates the key table using the keyword and returns it.\n
    The letter 'J' is merged with letter 'I' to fit the 5x5 matrix.\n
    The table is represented by a 1D list of length 25.
    """
    table = []
    for char in keyword:
        if not char in table:
            table.append(char)
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if not char in table:
            table.append(char)
    return table

def positionOf(char, table):
    """
    Finds the x and y position of the character within the table and returns it.\n
    The returned position is a 2-tuple with x and y representing the row and column, respectively.
    """
    for i in range(25):
        if table[i] == char:
            return (i%5, i//5)
        
def charAt(pos, table):
    """
    Finds the character at the position within the table and returns it.\n
    The input position should be a 2-tuple with x and y representing the row and column, respectively.
    """
    return table[pos[0] + pos[1]*5]

def rowReplace(pos1, pos2, table):
    """
    Performs a row replace on the letter pair using the table and returns the new letter pair.\n
    The 2-tuple positions for the input letter pair should be given.
    """
    # Row positions are decremented (modulus to loop back), columns remain the same
    # Simulates a replacement with letters immediately left
    pos1, pos2 = ((pos1[0]-1) % 5, pos1[1]), ((pos2[0]-1) % 5, pos2[1])
    return charAt(pos1, table) + charAt(pos2, table)

def columnReplace(pos1, pos2, table):
    """
    Performs a column replace on the letter pair using the table and returns the new letter pair.\n
    The 2-tuple positions for the input letter pair should be given.
    """
    # Column positions are decremented (modulus to loop back), rows remain the same
    # Simulates a replacement with letters immediately above
    pos1, pos2 = (pos1[0], (pos1[1]-1) % 5), (pos2[0], (pos2[1]-1) % 5)
    return charAt(pos1, table) + charAt(pos2, table)

def rectangleReplace(pos1, pos2, table):
    """
    Performs a rectangle replace on the letter pair using the table and returns the new letter pair.\n
    The 2-tuple positions for the input letter pair should be given.
    """
    # Row positions are swapped, columns remain the same
    # Simulates a replacement with letters in a rectangle formation (corner row swap)
    pos1, pos2 = (pos2[0], pos1[1]), (pos1[0], pos2[1])
    return charAt(pos1, table) + charAt(pos2, table)


def decrypt(keyword, ciphertext):
    """
    Decrypts the ciphertext using the keyword and returns it.
    """
    # Input strings are processed (alpha only) before being used
    table = getKeyTable(processText(keyword))
    ciphertext = processText(ciphertext)
    message = ""

    # Iterates over the ciphertext in pairs of letters (at i and i+1)
    for i in range(0, len(ciphertext), 2):
        pos1 = positionOf(ciphertext[i], table)
        pos2 = positionOf(ciphertext[i+1], table)

        # Check letter positions and perform either a row, column, or rectangle replacement
        if pos1[0] == pos2[0]:
            message += columnReplace(pos1, pos2, table)
        elif pos1[1] == pos2[1]:
            message += rowReplace(pos1, pos2, table)
        else:
            message += rectangleReplace(pos1, pos2, table)

    # Ensure the final message does not contain an "X"
    return message.replace("X", "")


if __name__ == "__main__":
    print(decrypt("SUPERSPY", "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"))