def generate_table(keyword):
    key_table = [[None] * 5 for _ in range(5)]
    # not using numpy as idk if shopify pipinstalled it...
    alphabet = 'abcdefghiklmnopqrstuvwxyz'.upper()
    # clean alphabet by removing chars present in keyword
    alphabet_clean = [char for char in alphabet if char not in keyword]
    # turn back into string and add to keyword
    keyword += "".join(alphabet_clean)
    # super duper way to remove all duplicates from keyword
    keyword = list(dict.fromkeys(keyword))
    counter = 0
    # loop over 5 by 5 and generate key_table
    for i in range(len(key_table)):
        for j in range(len(key_table)):
            key_table[i][j] = keyword[counter]
            counter += 1
    
    return key_table

def decrypt(letter1, letter2, key_table):
    first_row, first_col = letter1[0], letter1[1]
    second_row, second_col =  letter2[0], letter2[1] 
    if first_row == second_row:
        first_letter = key_table[first_row][first_col-1]
        second_letter = key_table[second_row][second_col-1]
    # if in same column
    elif first_col == second_col:
        first_letter = key_table[first_row][first_col]
        second_Letter = key_table[second_row][second_col]
    # not in same col or row
    else:
        first_letter = key_table[first_row][second_col]
        second_letter = key_table[second_row][first_col]
    
    # replace with no char if either of them are x
    first_letter = "" if first_letter == 'X' else first_letter
    second_letter = "" if second_letter == 'X' else second_letter
    return first_letter, second_letter

def main(key, message):
    # generate key table
    key_table = generate_table(key)

    positions_dict = {}
    # uses dictionary for easier lookup
    for i in range(len(key_table)):
        for j in range(len(key_table)):
            positions_dict[key_table[i][j]] = (i,j)

    # process message
    message_processed = ""

    message = list(message)

    for i in range(0, len(message), 2):
        # grab a pair of characters
        char_pair =  message[i:i+2]
        # get positions from dictionary
        letter1 = positions_dict[char_pair[0]]
        letter2 = positions_dict[char_pair[1]]
        message_processed += "".join(decrypt(letter1, letter2, key_table))

    # print final message
    print(message_processed)

if __name__ == '__main__':
    main("SUPERSPY", "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV")
