import string

def decrypt_message(encrypted_message: str, key: str) -> None:
    decrypted_message_list = []
    key_table = get_key_table(key, encrypted_message)
    key_table_hashmap = get_key_table_hashmap(key_table)

    for i in range(0, len(encrypted_message), 2):
        char_pair = (encrypted_message[i], encrypted_message[i + 1])

        first_row, first_column = key_table_hashmap[char_pair[0]][0], key_table_hashmap[char_pair[0]][1]
        second_row, second_column = key_table_hashmap[char_pair[1]][0], key_table_hashmap[char_pair[1]][1]

        if first_row == second_row:
            first_column = (first_column - 1) % 5
            second_column = (second_column - 1) % 5
        elif first_column == second_column:
            first_row = (first_row - 1) % 5
            second_row = (second_row - 1) % 5
        else:
            first_column, second_column = second_column, first_column

        decrypted_message_list.append(key_table[first_row][first_column])
        decrypted_message_list.append(key_table[second_row][second_column])
    
    clean_decrypted_message_list(decrypted_message_list)
    decrypted_message = ''.join(decrypted_message_list)
    
    return decrypted_message
    
def clean_decrypted_message_list(decrypted_message_list: list) -> None:
    index = 0
    while index < len(decrypted_message_list):
        if decrypted_message_list[index] == 'X' and index > 0:
            decrypted_message_list.pop(index)
        else:
            index += 1

def get_key_table_hashmap(key_table: list) -> dict:
    key_table_hashmap = {}

    for row_index, row in enumerate(key_table):
        for column_index, char in enumerate(row):
            key_table_hashmap[char] = (row_index, column_index)
    
    return key_table_hashmap

def get_key_table(key: str, encrypted_message: str) -> list:
    key_table = []
    whole_key_list = []

    for char in key:
        if char not in whole_key_list:
            whole_key_list.append(char)
    for char in string.ascii_uppercase:
        if char not in whole_key_list:
            whole_key_list.append(char)

    remove_key_letter(key, 'J', whole_key_list, encrypted_message)
    remove_key_letter(key, 'Q', whole_key_list, encrypted_message)

    while len(key_table) < 5:
        key_table.append(whole_key_list[len(key_table) * 5 : len(key_table) * 5 + 5])
    
    return key_table

def remove_key_letter(key: str, letter: str, whole_key_list: list, encrypted_message: str) -> None:
    if len(whole_key_list) > 25 and letter in whole_key_list and letter not in key and letter not in encrypted_message:
        whole_key_list.remove(letter)

if __name__ == '__main__':
    decrypted_message = decrypt_message('IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV', 'SUPERSPY')
    print(decrypted_message)