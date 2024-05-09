def get_cypher(key):
    used_letters = {}
    new_key = ''
    for i in range(0,len(key)):
        if key[i] not in used_letters:
            new_key += key[i]
            used_letters[key[i]] = 1
    complete_key = new_key + ''.join(chr(i) for i in range(65,91) if chr(i) not in used_letters and i != 74)
    key_matrix = [[] for _ in range(0,5)]
    for i in range(0, 25):
        key_matrix[i//5].append(complete_key[i])
    return key_matrix

def decrypt_message(encrypted_message, key):
    key_matrix = get_cypher(key)
    if len(encrypted_message) % 2 != 0:
        encrypted_message += 'X'
    
    return key_matrix


key = "SUPERSPY"
encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
decrypted_message = decrypt_message(encrypted_message, key)
print(decrypted_message)