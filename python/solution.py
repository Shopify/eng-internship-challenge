# given variables
ALPHABET = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' # J is omitted
KEY = 'SUPERSPY'
ENCRYPTED = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'
UNCOMMON_CHARACTER = 'X' # according to step 6 of instructions

# static variables
CIPHER_TABLE = []

# step 1: generate full cipher table key
def full_key(key):
    full_key = key + ALPHABET
    seen = set()
    unique = []

    for char in full_key:
        if char not in seen:
            seen.add(char)
            unique.append(char)

    return ''.join(unique)

# step 2: generate cipher table
CIPHER_TABLE = [list(full_key(KEY))[i:i + 5] for i in range(0, 25, 5)]

# step 3: generate pairs
def make_pairs(message):
    pairs = []
    string_length = len(message)

    for i in range(0, string_length, 2):
        if i + 1 < string_length:
            pairs.append(message[i:i + 2])
        # append an X to the final pair if the message is odd
        else:
            pairs.append(message[i] + UNCOMMON_CHARACTER)

    return pairs

# step 4: perform bigram swaps
def bigram_swaps_horizontal(pair, row):
    index1, index2 = CIPHER_TABLE[row].index(pair[0]) - 1, CIPHER_TABLE[row].index(pair[1]) - 1

    index1 = 4 if index1 == -1 else index1
    index2 = 4 if index2 == -1 else index2

    return ''.join([CIPHER_TABLE[row][index1], CIPHER_TABLE[row][index2]])

def bigram_swaps_vertical(pair, column):
    transposed_table = list(map(list, zip(*CIPHER_TABLE)))

    index1, index2 = transposed_table[column].index(pair[0]) - 1, transposed_table[column].index(pair[1]) - 1

    index1 = 4 if index1 == -1 else index1
    index2 = 4 if index2 == -1 else index2

    return ''.join([transposed_table[column][index1], transposed_table[column][index2]])

def bigram_swaps(pairs):
    swapped_pairs = []

    for pair in pairs:
        position1, position2 = None, None

        for row, row_data in enumerate(CIPHER_TABLE):
            if pair[0] in row_data:
                position1 = (row, row_data.index(pair[0]))
            if pair[1] in row_data:
                position2 = (row, row_data.index(pair[1]))
            
            if position1 and position2:
                break

        # horizontal case
        if position1[0] == position2[0]:
            swapped_pairs.append(bigram_swaps_horizontal(pair, position1[0]))
        # vertical case
        elif position1[1] == position2[1]:
            swapped_pairs.append(bigram_swaps_vertical(pair, position1[1]))
        # rectangular case
        else:
            swapped_pairs.append(''.join([CIPHER_TABLE[position1[0]][position2[1]], CIPHER_TABLE[position2[0]][position1[1]]]))
    
    return swapped_pairs

# step 5: reconstruct message and eliminate repeat separators (X)
def reconstruct(pairs):
    message = ''.join(pairs).replace(UNCOMMON_CHARACTER, '')

    return message

# step 6: output the result (not a great idea for a "secret password")
pairs = make_pairs(ENCRYPTED)
message = bigram_swaps(pairs)
decrypted = reconstruct(message)
print(decrypted)