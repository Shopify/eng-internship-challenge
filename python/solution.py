import string

#This function will create the '5x5' table used in the cipher
def create_key_table(key):
    table = []
    for char in key:    #Put chars in the key first
        if char not in table:   #skip chars already in
            table.append(char)

    uppercase_alphabet = string.ascii_uppercase

    for char in uppercase_alphabet: #Put rest of alphabet in table
        if char not in table and char != 'J':   #skip chars already in plus 'J'
            table.append(char)
    
    key_table = []
    for i in range(0, 25, 5):   #Convert into 5x5 table
        key_table.append(table[i:i+5])

    return key_table

def getIndices(char, table):
    row = 0
    while(row < 5):
        col = 0
        while(col < 5):
            if table[row][col] == char:
                return [row, col]
            col += 1
        row += 1

def decrypt_message(table, message):
    key = ""
    i = 0
    while(i < len(message)):
        firstIndex = getIndices(message[i], table)
        secondIndex = getIndices(message[i+1], table)
        
        if(firstIndex[0] == secondIndex[0]):    #if pair is in same row replace with letter to the left
            char = table[firstIndex[0]][firstIndex[1]-1 % 5]
            if(char != 'X'):
                key += char
            char = table[secondIndex[0]][secondIndex[1]-1 % 5]
            if(char != 'X'):
                key += char
        elif(firstIndex[1] == secondIndex[1]):  #if pair is in same col replace with letter to the right
            char = table[firstIndex[0]-1 % 5][firstIndex[1]]
            if(char != 'X'):
                key += char
            char = table[secondIndex[0]-1 % 5][secondIndex[1]]
            if(char != 'X'):
                key += char
        else:                                   #Otherwise replace with the corners of the rect they make
            char = table[firstIndex[0]][secondIndex[1]]
            if(char != 'X'):
                key += char
            char = table[secondIndex[0]][firstIndex[1]]
            if(char != 'X'):
                key += char
        i += 2
    return key



key = "SUPERSPY"
message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
table = create_key_table(key)
code = decrypt_message(table, message)
print(code)
