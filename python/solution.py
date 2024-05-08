from collections import OrderedDict

secret_string = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
key = "SUPERSPY"
plain_text = ""
alphabet = OrderedDict()

# alphabet without j
for i, letter in enumerate('abcdefghiklmnopqrstuvwxyz', start=1):
    alphabet[letter] = i

# create diagraph that will contain the letters
diagraph = [["" for _ in range(5)] for _ in range(5)]
key_index = 0

for row in diagraph:
    row_index = 0
    while row_index < len(row):
        if key_index < len(key):
            if key[key_index].lower() in alphabet:
                row[row_index] = key[key_index]
                alphabet.pop(key[key_index].lower())
                row_index += 1
            key_index += 1
        else:
            first_value = next(iter(alphabet))
            row[row_index] = first_value.upper()
            alphabet.pop(first_value)
            row_index += 1
            
#visualize diagraph
for row in diagraph:
    print(row)