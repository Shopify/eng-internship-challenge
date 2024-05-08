from collections import OrderedDict

secret_string = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
# HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA
key = "SUPERSPY"
plain_text = ""
alphabet = OrderedDict()
position_map = {}

# alphabet without j
for i, letter in enumerate('abcdefghiklmnopqrstuvwxyz', start=1):
    alphabet[letter] = i

# create diagraph that will contain the letters
diagraph = [["" for _ in range(5)] for _ in range(5)]
key_index = 0
row_num = 0

for row in diagraph:
    row_index = 0
    while row_index < len(row):
        if key_index < len(key):
            if key[key_index].lower() in alphabet:
                row[row_index] = key[key_index]
                alphabet.pop(key[key_index].lower())
                position_map[row[row_index]] = (row_num, row_index)
                row_index += 1
            key_index += 1
        else:
            first_value = next(iter(alphabet))
            row[row_index] = first_value.upper()
            alphabet.pop(first_value)
            position_map[row[row_index]] = (row_num, row_index)
            row_index += 1
    row_num += 1

# decipher secret message
secret_index = 0
first = True
filler = ""

while secret_index < len(secret_string) - 1:
    position_first = position_map[secret_string[secret_index]]
    position_second = position_map[secret_string[secret_index + 1]]
    char1 = ''
    char2 = ''

    #check if same row
    if position_first[0] == position_second[0]:
        char1 = diagraph[position_first[0]][position_first[1] - 1]
        char2 = diagraph[position_second[0]][position_second[1] - 1]

    #check if same column
    elif position_first[1] == position_second[1]:
        char1 = diagraph[position_first[0] - 1][position_first[1]]
        char2 = diagraph[position_second[0] - 1][position_second[1]]
    
    #check if diagonal
    else:
        char2 = diagraph[position_second[0]][position_first[1]]
        char1 = diagraph[position_first[0]][position_second[1]]
    
    double = False
    #check if double chars
    if secret_index < len(secret_string) - 3:
        if secret_string[secret_index] == secret_string[secret_index+2]:
            if first:
                filler = char2
                first = False
                double = True
            else:
                if secret_string[secret_index + 1] == filler:
                    double = True
    
    if not double:   
        plain_text += char1
        plain_text += char2
    else:
        plain_text += char1
    

    secret_index += 2

if plain_text[-1] == filler:
    print(plain_text[:-1])
else:
    print(plain_text)

#visualize diagraph
for row in diagraph:
    print(row)
