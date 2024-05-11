import string

def gen_key_table(key):
    '''
    :param key: key taken as string
    :return:
    '''
    # generate placeholder for 5x5 2d array
    key_table = [['' for i in range(5)] for j in range(5)]

    #generate list of uppercase alphabet letters
    alphabet_letters = list(string.ascii_uppercase)

    #fill in key into 2d key table
    i, j = 0,0
    for char in key:
        # if the character is in alphabet letters, it is occuring for the first time
        if char in alphabet_letters:
            key_table[i][j] = char

            #remove it from eligible alphabet letters
            alphabet_letters.remove(char)
            if j == 4:
                i += 1
                j = 0
            else:
                j += 1


    # all letters remaining in alphabet letters must be added to the key table
    for rem_char in alphabet_letters:

        #omitting j
        if rem_char != 'J':
            key_table[i][j] = rem_char

            if j == 4:
                i += 1
                j = 0
            else:
                j += 1
    return key_table

def get_row_num(letter,key_table):
    '''

    :param letter: a letter as a string
    :param key_table: a 2d array of size 5x5
    :return: an integer representing the row in which the letter is
    '''

    for i in range(len(key_table)):
        if letter in key_table[i]:
            return i

def get_column_num(letter,key_table):
    '''

    :param letter: a letter as a string
    :param key_table: a 2d array of size 5x5
    :return: an integer representing the column in which the letter is
    '''

    for i in range(len(key_table)):
        for j in range(len(key_table[i])):
            if key_table[i][j] == letter:
                return j

def get_column_or_row_index(column_or_row_number):
    '''

    :param column_or_row_number: a column or row number
    :return: integer representing column immediately to left or above
    '''
    if column_or_row_number == 0:
        return 4
    return column_or_row_number-1


def decrypt(text, key):
    #ensuring ciphertext is even in length
    #if not we add an x to the end
    if len(text) % 2:
        text += 'X'
    #converting to uppercase
    text = text.upper()
    key_table = gen_key_table(key)

    plaintext = ""

    for i in range(0,len(text),2):

        first_letter = text[i]
        second_letter = text[i+1]

        first_letter_row = get_row_num(first_letter,key_table)
        second_letter_row = get_row_num(second_letter,key_table)

        first_letter_column = get_column_num(first_letter,key_table)
        second_letter_column = get_column_num(second_letter, key_table)

        #if their row numbers match, replace them with the letters to their immediate left
        if first_letter_row == second_letter_row:
            plaintext += key_table[first_letter_row][get_column_or_row_index(first_letter_column)]
            plaintext += key_table[second_letter_row][get_column_or_row_index(second_letter_column)]

        # if their column numbers match, replace them with the letters immediately above them
        elif first_letter_column == second_letter_column:
            plaintext+=key_table[get_column_or_row_index(first_letter_row)][first_letter_column]
            plaintext+=key_table[get_column_or_row_index(second_letter_row)][second_letter_column]

        #otherwise, create rectangle and get corner values
        else:
            plaintext+=key_table[first_letter_row][second_letter_column]
            plaintext+=key_table[second_letter_row][first_letter_column]

    #removing X
    plaintext = plaintext.replace('X','')
    #removing spaces
    plaintext = plaintext.replace(' ', '')
    return plaintext

print(decrypt("IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV","SUPERSPY"))
