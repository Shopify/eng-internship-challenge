# NG 10/5/24
#Assumptions made: Letter J ommited from the decipher table
#                   Letter X used as a filler character
# decipher table goes left to right, top to bottom
# decipher table does not be generated everytime, only asked to provide a solver for the cipher


# S U P E R
# Y A B C D
# F G H I K
# L M N O Q
# T V W X Z

encrypted_phrase = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

decipher_table = [['S', 'U', 'P', 'E', 'R'], 
                  ['Y', 'A', 'B', 'C', 'D'], 
                  ['F', 'G', 'H', 'I', 'K'], 
                  ['L', 'M', 'N', 'O', 'Q'],
                  ['T', 'V', 'W', 'X', 'Z']]

def find_letter_in_table(letter):
    for row in range(5):
        for column in range(5):
            if decipher_table[row][column] == letter.upper():
                return (row, column)
    return None

def solver(phrase):
    ans = ""
    for i in range(0, len(phrase), 2): #iterate over phrase, forming pairs by stepping over
        letter1_row, letter1_column = find_letter_in_table(phrase[i])
        letter2_row, letter2_column = find_letter_in_table(phrase[i+1])
        #negative index in python prints correct
        if letter1_row == letter2_row: #shift to left
            ans += decipher_table[letter1_row][letter1_column-1] + decipher_table[letter2_row][letter2_column-1]
        elif letter1_column == letter2_column: #shift up
            ans += decipher_table[letter1_row-1][letter1_column] + decipher_table[letter2_row-1][letter2_column]
        else:
            ans += decipher_table[letter1_row][letter2_column] + decipher_table[letter2_row][letter1_column] #this allows to swap the letters in the rectangle formed
    return ans

def filter_ans(phrase):
    new_ans = ""
    for letter in phrase:
        if letter != "X" and letter != " " and find_letter_in_table(letter) != None:
            new_ans += letter   #remove filler char(x) , space, special char
    return new_ans


unfilter_ans = solver(encrypted_phrase)
ans = filter_ans(unfilter_ans)

print(ans)

