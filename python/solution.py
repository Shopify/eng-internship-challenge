# This solves a Playfair Cipher in two different ways: one with a matrix-based solution and one that solves it using 
# a linear array.

# MATRIX-BASED SOLUTION
import numpy as np

message = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'
key = 'SUPERYABCDFGHIKLMNOQTVWXZ'

# Creating a 5x5 matrix using the key
def create_board(board_chars):
    board = np.array(list(key)).reshape(5, 5)
    print(board)

# Method to split the message into two-letter pairs
def digraph():
    return [message[i:i+2] for i in range(0, len(message), 2)]



