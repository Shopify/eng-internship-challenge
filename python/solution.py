# This solves a Playfair Cipher in two different ways: one with a matrix-based solution and one that solves it using 
# a linear array.

# MATRIX-BASED SOLUTION
import numpy as np

message = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'
key = 'SUPERYABCDFGHIKLMNOQTVWXZ'

# Creating a hashmap that represents the board where each letter is mapped to its coordinate [i, j]
def create_board(letters):
    board_map = {}
    for i, char in enumerate(letters):
        row = i // 5
        col = i % 5
        board_map[char] = (row, col)
    return (board_map)

# Method to split the message into two-letter pairs
def digraph(encrypted_msg):
    return [encrypted_msg[i:i+2] for i in range(0, len(encrypted_msg), 2)]

# split_message = digraph(message)




