def generate_matrix_map(key):
    key_map = {}
    temp = key.replace('J', 'I').upper()+'ABCDEFGHIKLMNOPQRSTUVWXYZ' 
    count = 0
    key_string = ""
    for alph in temp:
        if alph.isalpha() and alph not in key_map:
            key_map[alph] = (count//5, count%5)
            key_string += alph
            count+=1

    return (key_map,key_string)

def generate_pairs(encrypted):
    encrypted = ''.join([char for char in encrypted.replace('J','I').upper() if char.isalpha()])
    pad_encrypted = ''
    i = 0
    while i < len(encrypted):
        a = encrypted[i]
        b = 'X' if i+1 >= len(encrypted) or encrypted[i+1]==a else encrypted[i+1]
        pad_encrypted += a+b
        i = i + 1 if b=='X' else i+2

    return [pad_encrypted[i:i + 2] for i in range(0, len(pad_encrypted), 2)]


def decrypt(encrypted, key):
    ans =""
    key_map,key_string = generate_matrix_map(key)
    encrypted_pair = generate_pairs(encrypted)
    for (a ,b) in encrypted_pair:
        a_row, a_col = key_map[a]
        b_row, b_col = key_map[b]

        if a_row == b_row:
            ans += key_string[a_row*5 + (a_col-1)%5] + key_string[b_row*5 + (b_col-1)%5] 
        elif a_col == b_col:
            ans += key_string[(a_row - 1) % 5*5+a_col] + key_string[(b_row - 1) % 5*5+b_col]
        else:
            ans += key_string[a_row*5 + b_col] + key_string[b_row*5 + a_col]
    return ans.replace('X','')


if __name__ == '__main__':
    key = "SUPERSPY"
    encrypted = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    print(decrypt(encrypted, key))
