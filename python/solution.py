import re


def diagraph(text):
    Diagraph = []
    group = 0
    for i in range(2, len(text), 2):
        Diagraph.append(text[group:i])
        group = i

    Diagraph.append(text[group:])
    return Diagraph


def gen_key_table(cipher_key):
    key_table_cipher_key = []
    for letter in cipher_key:
        if letter not in key_table_cipher_key:
            key_table_cipher_key.append(letter)

    # Omitted J
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    key_table_list_format = [*key_table_cipher_key]
    for letter in alphabet:
        if letter not in key_table_list_format:
            key_table_list_format.append(letter)

    polybius_square = [key_table_list_format[i:i+5]
                       for i in range(0, len(key_table_list_format), 5)]

    return polybius_square


def search(letter, key_table):
    for i in range(5):
        for j in range(5):
            if (key_table[i][j] == letter):
                return i, j


def row(key_table, common_row, fl_col, sl_col):
    return key_table[common_row][fl_col-1 % 5] + key_table[common_row][sl_col-1 % 5]


def column(key_table, common_col, fl_row, sl_row):
    return key_table[fl_row-1 % 5][common_col] + key_table[sl_row-1 % 5][common_col]


def rectangle(key_table, fl_row, fl_col, sl_row, sl_col):
    return key_table[fl_row][sl_col] + key_table[sl_row][fl_col]


def decrypt(encrypted_message, cipher_key):
    # message needs to be in upper case
    encrypted_message = encrypted_message.upper()

    # group letters in pairs
    message_diagraph = diagraph(encrypted_message)
    # create polybius square
    key_table = gen_key_table(cipher_key)

    # start solving
    solution = ""
    for letter_pair in message_diagraph:
        # fl = first letter
        fl_row, fl_column = search(letter_pair[0], key_table)
        # sl = second letter
        sl_row, sl_column = search(letter_pair[1], key_table)
        mapping = ""
        if fl_row == sl_row:
            mapping = row(key_table, fl_row, fl_column, sl_column)
        elif fl_column == sl_column:
            mapping = column(key_table, fl_column, fl_row, sl_row)
        else:
            mapping = rectangle(key_table, fl_row, fl_column, sl_row,
                                sl_column)

        solution += mapping

    # subsitute special X placeholders (2 cases)
    indices = re.search(r"([A-Z]{1})X{1}\1", solution)
    solution = re.sub(r"([A-Z]{1})X{1}\1", indices.group()
                      [0] + indices.group()[2], solution)

    if len(solution) % 2 == 1 and solution[len(solution) - 1] == "X":
        solution = solution[0:len(solution)-1]

    print(solution)


decrypt("IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV", "SUPERSPY")
