msg = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
key = "SUPERSPY"
# assume i and j are on same square, so remove j from alphabet if no J in key
alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
if 'J' in key:
    alphabet = "ABCDEFGHJKLMNOPQRSTUVWXYZ"

# remove all repeats in the key
repeats = {}
no_rep_key = ""
for i in key:
    if i not in repeats.keys():
        no_rep_key += i
        repeats[i] = 1

# remove all key letters from the alphabet        
no_key_alpha = ""
for i in alphabet:
    if i not in no_rep_key:
        no_key_alpha += i

square = (no_rep_key + no_key_alpha)

# create 5x5 matrix for the letters
alpha_matrix = [square[i:i+5] for i in range(0, len(square), 5)]

# create letter to matrix positioning mapping
letter_pos = {}
row = 0
col = 0
for i in square:
    letter_pos[i] = (row, col)
    col += 1
    if col == 5:
        row += 1
        col = 0

# turn encoded message into letter pairs
paired_msg = [msg[i:i+2] for i in range(0, len(msg), 2)]
decoded = ""

# helper function to get the correct decoded letters
def get_letters(a, b):
    rect_length = abs(a[1] - b[1])
    # same row case
    if a[0] == b[0]:
        return (a[0], a[1]- 1 if a[1] - 1 >= 0 else 4), (b[0], b[1]- 1 if b[1] - 1 >= 0 else 4)
    # same column case
    elif a[1] == b[1]:
        return (a[0]- 1 if a[0] - 1 >= 0 else 4, a[1]), (b[0]- 1 if b[0] - 1 >= 0 else 4, b[1])
    # rectangle cases
    elif a[1] > b[1]:
        return (a[0], a[1] - rect_length), (b[0], b[1] + rect_length)
    else:
        return (a[0], a[1] + rect_length), (b[0], b[1] - rect_length)

# decode message
for m in paired_msg:
    a, b = get_letters(letter_pos[m[0]], letter_pos[m[1]])
    decoded += alpha_matrix[a[0]][a[1]]
    decoded += alpha_matrix[b[0]][b[1]]

# remove X's (null letters) from initial decoding
decoded_no_X = decoded[0]
# number of removed X's 
removed = 0
# check for X's that replace duplicate lettering 
for i in range(1, len(decoded) - 1):
    if decoded[i] == 'X' and decoded[i-1] == decoded[i+1]:
        removed += 1
    else:
        decoded_no_X += decoded[i]
decoded_no_X += decoded[-1]

# if the initial decoding was even, with the final letter being X, then remove the X
if len(decoded) % 2 == 0 and decoded[-1] == 'X':
    decoded_no_X = decoded_no_X[0:-1]

# output original message
print(decoded_no_X)