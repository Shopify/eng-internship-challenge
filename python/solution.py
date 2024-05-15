import sys
from collections import OrderedDict

# Removes all X's from the result
def process_result(result):
    return result.replace("X", "")

# Removes all spaces and special characters and numbers
def process_input(input):
    return ''.join(e for e in input if e.isalpha()).upper()

# Creates the playfair ta
def create_table(key, alphabet):
    key = process_key(key)

# The key should not contain any duplicates, and should be all uppercase
def process_key(key):
    return OrderedDict.fromkeys(key.upper())

# returns the new index of a character that has been shifted to the left using playfair cypher rules
def shift_left(index):
    prev_row = index // 5
    new_index = (prev_row + 1) * 5 - 1 if (index - 1) // 5 < prev_row else index - 1
    return new_index

# returns the new index of a character that has been shifted up using playfair cypher rules
def shift_up(index):
    prev_col = index % 5
    new_index = index - 5 if ((index - 5) >= 0) else 20 + prev_col
    return new_index

# Outputs a decrypted playfair cypher given the encrypted message and the used playfair table
def decrypt(message, key):
    process_input(message)
    table = create_playfair_table(key)


    playfair_list = []
    for key, value in table.items():
        playfair_list.append(key)

    output = ""

    # Select a pair of letters
    for i in range(0, len(message), 2):

        index1 = table[message[i]]
        index2 = table[message[i + 1]] 
        row1 = index1 // 5
        row2 = index2 // 5
        column1 = index1 % 5
        column2 = index2 % 5

        # Characters are on the same row
        if (row1 == row2):
            new_index1 = shift_left(index1)
            new_index2 = shift_left(index2)

            output += (playfair_list[new_index1])
            output += (playfair_list[new_index2])

        # Characters are on the same column
        elif (column1 == column2):
            new_index1 = shift_up(index1)
            new_index2 = shift_up(index2)

            output += playfair_list[new_index1]
            output += playfair_list[new_index2]

        # Characters should form a rectangle
        else:
            if (column1 > column2):
                rectangle_width = column1 - column2 + 1

                new_index1 = index1 - (rectangle_width - 1)
                new_index2 = index2 + (rectangle_width - 1)

                output += playfair_list[new_index1]
                output += playfair_list[new_index2]

            else:
                rectangle_width = column2 - column1 + 1

                new_index1 = index1 + (rectangle_width - 1)
                new_index2 = index2 - (rectangle_width - 1)

                output += playfair_list[new_index1]
                output += playfair_list[new_index2]

    return output

# Create the playfair table given a key
def create_playfair_table(key):
    alphabet = OrderedDict.fromkeys("ABCDEFGHIKLMNOPQRSTUVWXYZ") # J = I
    processed_key = process_key(key)
    playfair_table = processed_key | alphabet
    
    i = 0
    for key, value in playfair_table.items():
        playfair_table[key] = i
        i += 1

    return playfair_table


# The key to the cypher
key = "SUPERSPY"
# Take in the input from commandline
input = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
result = decrypt(input, key)
# No spaces, X's or special characters should be present in the output
result = result.replace("X", "")

print(result)
