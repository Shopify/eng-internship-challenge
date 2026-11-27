KEY = "SUPERSPY"
MESSAGE = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ" # omitting J

# Search the alphabet for the next unused letter
# Returns the index of the first letter in ALPHABET that does not belong to free, starting from i
def search_alphabet(free: set, i: int) -> str:
    # increment index until we find a letter that hasn't been used
    # the alphabet is 26 letters so index error isn't possible
    while ALPHABET[i] not in free:
        i += 1
    return i


# Generate the key table for decryption
# Returns the 5x5 key table using key as the key
def make_key_table(key: str) -> list:
    # length of the key
    n = len(key)
    # keep track of what letters we haven't used yet
    free = set(ALPHABET)
    # keep track of the index of the letter we are adding next
    next_letter = 0
    # flag to indicate whether we are done with the key
    key_used = False

    # we are creating a 5x5 table
    table = []
    # make 5 rows
    for _ in range(5):
        # each row will have 5 elements
        row = []
        for _ in range(5):
            # check if we have already added the whole key to the table
            # if not, then we try to add another letter
            if not key_used:
                # increment index of next letter until we are on a new letter or reach the end of the key
                while next_letter < n and key[next_letter] not in free:
                    next_letter += 1
                # if we have not reached the end of the key then we must be on a new letter
                if next_letter < n:
                    row.append(key[next_letter])
                    free.remove(key[next_letter])
                # otherwise, we take from the alphabet
                else:
                    # set our flag to true so we don't enter this branch again
                    key_used = True

                    # take the next letter from the alphabet:
                    # find the index of the first unique alphabet letter
                    next_letter = search_alphabet(free, 0)
                    # add it to the table and remove it from our set of unused letters
                    row.append(ALPHABET[next_letter])
                    free.remove(ALPHABET[next_letter])
            # otherwise, if the key has already been completely used, we add letters from the alphabet
            else:
                # find the index of the first unique alphabet letter
                next_letter = search_alphabet(free, next_letter)
                # add it to the table and remove it from our set of unused letters
                row.append(ALPHABET[next_letter])
                free.remove(ALPHABET[next_letter])
        # add our completed row to the table
        table.append(row)

    # return the resulting 5x5 table
    return table


# Split the encrypted message into pairs of letters for decryption and return them in a list
# Precondition: len(msg) % 2 == 0
def split_message(msg: str) -> list:
    # length of the encrypted message
    n = len(msg)
    assert n % 2 == 0

    return [msg[i : i + 2] for i in range(0, n, 2)]


# Get the location of a letter in the key table
# Returns the (row, col) location as a tuple of ints
# Precondition: table is a properly made 5x5 key table
def get_location(table: list, x: str) -> tuple:
    # in our key table, we treated I and J interchangeably
    if x == "J":
        x = "I"
    # search for the letter
    for row in range(5):
        for col in range(5):
            # if the current letter in the table matches our target, return the location
            if table[row][col] == x:
                return (row, col)


# Retrieve the letter immediately to the left of the one at (row, col) and return it
def get_left(table: list, row: int, col: int) -> str:
    # wrap around if letter is at the far left
    if col == 0:
        return table[row][4]
    else:
        return table[row][col - 1]


# Retrieve the letter immediately above the one at (row, col) and return it
def get_above(table: list, row: int, col: int) -> str:
    # wrap around if letter is at the top
    if row == 0:
        return table[4][col]
    else:
        return table[row - 1][col]


# Decrypt the message!
# Returns the decrypted message
def decrypt(msg: str, key: str) -> str:
    # result of decryption
    result = ""

    # split the message into pairs to decrypt
    pairs = split_message(msg)
    # generate the key table
    table = make_key_table(key)
    
    # decrypt pairs one at a time
    for p in pairs:
        # get (row, col) locations of both letters
        p0_row, p0_col = get_location(table, p[0])
        p1_row, p1_col = get_location(table, p[1])

        # determine which case we have for this pair (using encryption instructions):
        # 1.    "If the letters appear on the same row of your table,
        #       replace them with the letters to their immediate right respectively
        #       (wrapping around to the left side of the row if a letter in the original
        #       pair was on the right side of the row)".
        if p0_row == p1_row:
            # to decrypt: replace with letters to their immediate left
            first = get_left(table, p0_row, p0_col)  # first letter
            second = get_left(table, p1_row, p1_col) # second letter
            
            # add letters to result, omitting X's
            result += first
            if second != "X":
                result += second
        # 2.    "If the letters appear on the same column of your table,
        #       replace them with the letters immediately below respectively
        #       (wrapping around to the top side of the column if a letter in the original
        #       pair was on the bottom side of the column)."
        elif p0_col == p1_col:
            # to decrypt: replace with letters immediately above
            first = get_above(table, p0_row, p0_col)  # first letter
            second = get_above(table, p1_row, p1_col) # second letter

            # add letters to result, omitting X's
            result += first
            if second != "X":
                result += second
        # 3.    If the letters are not on the same row or column,
        #       replace them with the letters on the same row respectively
        #       but at the other pair of corners of the rectangle defined by the original
        #       pair. The order is important – the first letter of the encrypted pair is
        #       the one that lies on the same row as the first letter of the plaintext pair.
        else:
            # to decrypt: same as encryption
            first = table[p0_row][p1_col] # first letter
            second = table[p1_row][p0_col] # second letter

            # add letters to result, omitting X's
            result += first
            if second != "X":
                result += second
    # return decryted string
    return result


if __name__ == "__main__":
    print(decrypt(MESSAGE, KEY))
