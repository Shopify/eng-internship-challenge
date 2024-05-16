#!/usr/bin/env python3

table = [['/' for _ in range(5)] for _ in range(5)]
key = "SUPERSPY"
encMessage = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
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
        if curRow > 4:
            print("ERROR")
            break
        table[curRow][curCol] = letter
        curCol += 1
        if curCol > 4:
            curRow += 1
            curCol = 0
fillTable()
print(table)
