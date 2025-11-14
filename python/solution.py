def createTable(key):
    """
    createTable takes in the key and returns a 5 X 5 table

    First adds the keys to a list such that they are only added once using python sets.
    Next adds the remaining letters in the alphabet that are not part of the set (haven't been already added to the list)
    Finally takes the list and converts it into a 2D Grid

    O(n) time complexity 

    """
    table = []
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    # Have the key as Capital letters only and replace J with I
    key = key.upper().replace("J", "I")

    seen = set()

    # adds the keys to a list such that they are only added once using python sets
    for letter in key:
        if letter not in seen and letter.isalpha():
            seen.add(letter)
            table.append(letter)

    # adds the remaining letters in the alphabet that are not part of the set
    for letter in alphabet:
        if letter not in seen:
            seen.add(letter)
            table.append(letter)

    # takes the list and converts it into a 2D Grid
    return [table[i:i+5] for i in range(0, (25), 5)]


def decryptMessage(table, text):
    """
    decryptMessage takes the table created in the createTable function above and the encrypted text. It returns the decrypted text after replacing any special characters and 'X'

    For all the letters in the list increment by 2 each time since need to have them in pairs, and find the location of the letters
    Use the row, column, box rules to store the decrypted letters into a list (to reduce time complexity)
    Convert list into string and replace any special characters and 'X'
    """
    msg = []
    for i in range(0, len(text), 2):
        char1 = text[i]
        char2 = text[i+1]

        # find the location of the letters
        colChar1, rowChar1, colChar2, rowChar2 = 0, 0, 0, 0
        for i in range(5):
            for j in range(5):
                if table[i][j] == char1:
                    colChar1, rowChar1 = i, j
                if table[i][j] == char2:
                    colChar2, rowChar2 = i, j

        # Rules

        # Column rule: Since they are in the same column, take the letters 1 to the left
        if colChar1 == colChar2:
            msg.append(table[colChar1][(rowChar1-1) % 5] +
                       table[colChar2][(rowChar2-1) % 5])
        # Row rule: Since they are in the same row, take the letters 1 upward
        elif rowChar1 == rowChar2:
            msg.append(table[(colChar1-1) % 5][rowChar1] +
                       table[(colChar2-1) % 5][rowChar2-1])
        # Box rule: Since they aren't in the same box, take the letters in the opposite corners of the box
        else:
            msg.append(table[colChar1][rowChar2] + table[colChar2][rowChar1])

    # convert the list into a string
    decrypted = ''.join(msg)

    # replace 'X' from the final string
    return decrypted.replace("X", "")


if __name__ == '__main__':
    key = "SUPERSPY"
    encryptedMsg = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

    table = createTable(key)
    result = decryptMessage(table, encryptedMsg)
    print(result)
