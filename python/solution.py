encrypted_msg = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

output = ""

# the table that is made from the given key
table = [
    ['S', 'U', 'P', 'E', 'R'],
    ['Y', 'A', 'B',  'C', 'D'],
    ['F', 'G', 'H', 'I', 'K'],
    ['L', 'M', 'N', 'O', 'Q'],
    ['T', 'V', 'W', 'X', 'Z']
]

coords = {}

# get the coordinates of each letter in the table
# this will simplify the process of finding the letters and comparing positions relative to eachother
for i in range(len(table)):
    for j in range(len(table[1])):
        coords[table[i][j]] = (i, j)

for i in range(1, len(encrypted_msg), 2):
    char1 = encrypted_msg[i - 1]
    char2 = encrypted_msg[i]

    #get coordinates of each character
    i1, j1 = coords[char1]
    i2, j2 = coords[char2]

    if i1 != i2 and j1 != j2:
        # if the characters are not in the same row or column, we get our rectangular case
        output += table[i1][j2] + table[i2][j1]
    elif i1 == i2:
        if abs(j1 - j2) == 1:
            # next to eachother
            if j1 > j2:
                output += table[i1][j2 - 1] + char2
            else:
                output += table[i1][j1 - 1] + char1

        else:
            # same row, but not next to eachother
            output += table[i1][j1 - 1] + table[i2][j2 - 1]

    else:
        if abs(i1 - i2) == 1:
            # next to eachother
            if i1 > i2:
                output += table[i2 - 1][j1] + char2
            else:
                output += table[i1 - 1][j1] + char1
        else:
            # same column, but not next to eachother
            output += table[i1 - 1][j1] + table[i2 - 1][j1]

# since our 'uncommon letter' is X, we can remove it from our final output
output = output.replace('X', '')

print(output.strip())



