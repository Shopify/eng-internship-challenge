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

def decrypt_two_characters(two_characters, key_matrix):
    first_character = find_index(key_matrix,two_characters[0])
    second_character = find_index(key_matrix,two_characters[1])

    if first_character[0] == second_character[0]:
        return key_matrix[first_character[0]][first_character[1]-1 if first_character[1]!=0 else 4] + key_matrix[second_character[0]][second_character[1]-1 if second_character[1]!=0 else 4]
    elif first_character[1] == second_character[1]:
        return key_matrix[first_character[0]-1 if first_character[0]!=0 else 4][first_character[1]] + key_matrix[second_character[0]-1 if second_character[0]!=0 else 4][second_character[1]]
    else:
        return key_matrix[first_character[0]][second_character[1]] + key_matrix[second_character[0]][first_character[1]]

def find_index(key_matrix, character):
    for row in range(0,5):
        for col in range(0,5):
            if character == key_matrix[row][col]:
                return (row, col)

def decrypt_message(encrypted_message, key):
    key_matrix = get_cypher(key)
    if len(encrypted_message) % 2 != 0:
        encrypted_message += 'X'
    decrypted_message = ''
    for i in range(0, len(encrypted_message), 2):
        decrypted_message += decrypt_two_characters(encrypted_message[i:i+2], key_matrix)
    return decrypted_message.replace('X','')


key = "SUPERSPY"
encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
decrypted_message = decrypt_message(encrypted_message, key)
print(decrypted_message)