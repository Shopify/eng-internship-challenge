#!/usr/bin/env python3

table = [['/' for _ in range(5)] for _ in range(5)]
key = "SUPERSPY"
encMsg = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

def fillTable():
    # Fill table with key, omitting duplicates
    for i in range(5):
        table[0][i] = key[i]
    for i in range(1):
        table[1][i] = key[i+7]

    # Fill rest of table with remaining alphabet
    curCol = 1
    curRow = 1
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if letter == 'J':
            continue
        elif letter in key:
            continue
        table[curRow][curCol] = letter
        curCol += 1
        if curCol > 4:
            curRow += 1
            curCol = 0

# Returns position of character in table
def search(elem):
    for i in range(5):
        for j in range(5):
            if (table[i][j] == elem):
                return i,j

def decrypt(msg):
    fillTable()
    # Split key into pairs
    pairs = [msg[i:i + 2] for i in range(0, len(msg), 2)]

    newPairs = []
    for pair in pairs:
        x1, y1 = search(pair[0])
        x2, y2 = search(pair[1])

        # 1) Both letters are in the same row of the key table
        if x1 == x2:
            if y1 - 1 < 0:
                x1New, y1New = x1, 4
            else:
                x1New, y1New = x1, y1 - 1
            if y2 - 1 < 0:
                x2New, y2New = x2, 4
            else:
                x2New, y2New = x2, y2 - 1
        
        # 2) Both letters are in the same column of the key table
        elif y1 == y2:
            if x1 - 1 < 0:
                x1New, y1New = 4, y1
            else:
                x1New, y1New = x1 - 1, y1
            if x2 - 1 < 0:
                x2New, y2New = 4, y2
            else:
                x2New, y2New = x2 - 1, y2
        
        # 3) In any other case, the letter is replaced by the letter in its own row and the column occupied by the other letter in its pair
        else:
            x1New, y1New = x1, y2
            x2New, y2New = x2, y1

        newPairs.append(table[x1New][y1New] + table[x2New][y2New])
    msg = ''.join(newPairs)

    # Remove additional Xs that are either in between a pair of letters or at the end of the message
    for i in range(len(msg)-1):
        if msg[i] == 'X' and i < len(msg) - 1 and msg[i-1] == msg[i+1]: 
            msg = msg[:i] + msg[i+1:]
    if msg[len(msg)-1] == 'X':
        msg = msg[:len(msg)-1]
    print(msg)

decrypt(encMsg)
