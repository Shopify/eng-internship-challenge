def create_playfair_grid(key):
    key = key.replace(' ', '').upper()
    key_set = set(key)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".replace('J','')

    keytable_list = []
    for char in key:
        if char not in keytable_list:
            keytable_list.append(char)
    
    keytable = "".join(keytable_list)

    for char in key + alphabet:
        if char not in key_set:
            keytable += char
            key_set.add(char)
    print(keytable)
    grid = [keytable[i:i+5] for i in range(0, 25, 5)]
    
    return grid

def decrypt(message, key):
    res = ""

    grid = create_playfair_grid(key)

    if len(message) % 2 != 0:
        message += 'X'
    pairs = [message[i:i+2] for i in range(0, len(message), 2)]
    
    return res

def main():
    encrypted_message = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'
    key = "SUPERSPY"
    result = decrypt(encrypted_message, key).replace('X','').upper()
    return result


main()