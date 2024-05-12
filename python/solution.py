
def create_key_table(key):
    """
    create_key_table generates the key table
    :param key: The key word
    :return: the key table
    """
    key_table = [['' for i in range(5)] for j in range(5)]
    used_letters = {chr(i + 65): False for i in range(26)}
    used_letters['J'] = True

    i, j = 0, 0
    for k in range(len(key)):
        if not used_letters[key[k]]:
            used_letters[key[k]] = True
            key_table[i][j] = key[k]
            j += 1
            if j == 5:
                j = 0
                i += 1

    for letter in used_letters.keys():
        if not used_letters[letter]:
            key_table[i][j] = letter
            j += 1
            if j == 5:
                j = 0
                i += 1
    return key_table


def code_letter_positions(key_table, code):
    """
    Finds the position of the code word letters in the key table
    :param key_table: The key table
    :param code: The code word
    :return: a dictionary where the code is a letter from the key word,
    and the value is its location in the key table
    """
    locations = {code[i]: [-1, -1] for i in range(len(code))}
    for i in range(len(key_table)):
        for j in range(len(key_table[0])):
            if key_table[i][j] in code:
                locations[key_table[i][j]] = [i, j]
    return locations


def decrypt(code, key_table):
    """
    Decrypts the code given the key table
    :param code: The code word
    :param key_table: The key table
    :return: The resulting decrypted word
    """
    result = ""
    positions = code_letter_positions(key_table, code)
    i = 0
    while i < len(code):
        a, b = positions[code[i]], positions[code[i+1]]
        decrypted_a, decrypted_b = '', ''
        if a[0] == b[0]:
            decrypted_a = key_table[a[0]][a[1] - 1]
            decrypted_b = key_table[b[0]][b[1] - 1]
        elif a[1] == b[1]:
            decrypted_a = key_table[a[0] - 1][a[1]]
            decrypted_b = key_table[b[0] - 1][b[1]]
        else:
            decrypted_a = key_table[a[0]][b[1]]
            decrypted_b = key_table[b[0]][a[1]]
        if decrypted_a == 'X':
            result += decrypted_b
        elif decrypted_b == 'X':
            result += decrypted_a
        else:
            result += decrypted_a + decrypted_b
        i += 2

    return result

def playfair_cipher(code, key):
    """
    Performs the playfair cipher
    :param code: The code word
    :param key: The key word
    :return: The decrypted code word
    """
    table = create_key_table(key)
    return decrypt(code, table)


if __name__ == '__main__':
    print(playfair_cipher("IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV", "SUPERSPY"))

