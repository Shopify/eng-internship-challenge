import string

# Generate the playfair cipher matrix:


def keyGeneration(key):
    # We don't want the letter j in the matrix so we will replace it with '.'
    ascii = string.ascii_uppercase.replace('J', '.')

    key_matrix = ['' for i in range(5)]
    i = 0
    j = 0

    # Insert the key to ascii and create the matrix
    for c in key:
        if c in ascii:
            key_matrix[i] += c
            ascii = ascii.replace(c, '.')

            j += 1

            # When j = 5, we will need to start a new line in the matrix
            # Then we know that we need to increase i in 1 and define j = 0
            if j > 4:
                i += 1
                j = 0
    for c in ascii:
        if c != ".":
            key_matrix[i] += c

            j += 1
            if j > 4:
                i += 1
                j = 0

    return key_matrix

# calculate the position of the new letter:


def newLetterPosition(i):
    return (i + 4) % 5

# remove the letter X from the decrypted_message list


def removeX(char):
    if char != 'X':
        decrypted_message.append(char)


key = keyGeneration("SUPERSPY")
encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
decrypted_message = []
encrypted_pairs = []

# Check if there are special characters/spaces in the encrypted message
# If contains special characters, print "invalid string"
# According to the encrepted message that you provided, it's not a must but I decided to cover this case also
is_alpha = encrypted_message.isalpha()
if is_alpha == False:
    print("invalid string")
    exit()

i = 0
while i < len(encrypted_message):
    a = encrypted_message[i]
    b = encrypted_message[i + 1]

    # Split the encrypted message into pairs of two letters (digraphs)
    encrypted_pairs.append(a + b)
    i += 2

for pair in encrypted_pairs:
    appliedRule = False

    # Rule 1: check if the letters are in the same row
    # If in the same row -  replace each letter with the letter to its immediate left
    # Insert the new letters to the list: decrypted_message
    for row in key:
        if pair[0] in row and pair[1] in row:
            j0 = row.find(pair[0])
            j1 = row.find(pair[1])

            char1 = row[newLetterPosition(j0)]
            char2 = row[newLetterPosition(j1)]

            removeX(char1)
            removeX(char2)

            appliedRule = True

    if appliedRule:
        continue

    # Rule 2: check if the letters are in the same col
    # If in the same col - replace each letter with the letter above it
    # Insert the new letters to the list: decrypted_message
    for j in range(5):
        col = "".join([key[i][j] for i in range(5)])
        if pair[0] in col and pair[1] in col:
            i0 = col.find(pair[0])
            i1 = col.find(pair[1])

            char1 = col[newLetterPosition(i0)]
            char2 = col[newLetterPosition(i1)]

            removeX(char1)
            removeX(char2)

            appliedRule = True

    if appliedRule:
        continue

    # Rule 3: check if the letters form a rectangle
    # If rectangle, replace each letter with the letter on the same row but in the opposite corner of the rectangle
    # Insert the new letters to the list: decrypted_message
    i0 = 0
    i1 = 0
    j0 = 0
    j1 = 0
    for i in range(5):
        row = key[i]
        if pair[0] in row:
            i0 = i
            j0 = row.find(pair[0])

        if pair[1] in row:
            i1 = i
            j1 = row.find(pair[1])

    char1 = key[i0][j1]
    char2 = key[i1][j0]

    removeX(char1)
    removeX(char2)

# print the decryption:
print("".join(decrypted_message))
