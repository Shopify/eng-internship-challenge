"""
Assuming 'J' is omitted and the key is 'SUPERSPY'

   0  1  2  3  4
0 [S][U][P][E][R]
1 [Y][A][B][C][D]
2 [F][G][H][I][K]
3 [L][M][N][O][Q]
4 [T][V][W][X][Z]

'IK EW EN EN XL NQ LP ZS LE RU MR HE ER YB OF NE IN CH CV'
'HI PX PO PO '

Decryption Rules: 

RECTANGLE: Select the letter horizontally opposite to each item within the rectangle.
SAME-ROW: Select the letter to the left of each item. 
SAME-COLUMN: Select the letter above each item.  

* item = current letter in pair

"""
from collections import deque


class Matrix:

    @staticmethod 
    def generate(key):

        if key is None:
            print('Key is None')
            return None

        matrix = [[] for i in range(5)]
        visited = set()
        letters = deque(key.upper().replace('J','I') + 'ABCDEFGHIKLMNOPQRSTUVWXYZ')

        for y in range(5):
            while len(matrix[y]) < 5:
                    letter = letters.popleft()
                    if letter not in visited:
                        matrix[y].append(letter)
                        visited.add(letter)
        return matrix
    
    # @staticmethod
    # def find(item, matrix):
    #     for y in range(5):
    #         for x in range(5):
    #             if matrix[y][x] == item:
    #                 return (x, y)
    #     return None
    
    @staticmethod
    def map(matrix, letter_to_coord=True):
        res = {}
        for y in range(5):
            for x in range(5):
                if letter_to_coord:
                    res[matrix[y][x]] = [x, y]
                else:
                    res[(x, y)] = matrix[y][x]
        return res


                    
class Decrypt:
    def __init__(self, key, encrypted):
        self.matrix = Matrix.generate(key)
        self.letters = Matrix.map(self.matrix)
        self.coord = Matrix.map(self.matrix, letter_to_coord=False)
        self.encrypted = encrypted
    
    def decrypt(self):
        
        if len(self.encrypted) % 2 != 0:
            print('Invalid odd length encrypted string')
            return None

        decrypted_string = ''
        for i in range(0,len(self.encrypted),2):
            a = self.letters[self.encrypted[i]] # [x, y]
            b = self.letters[self.encrypted[i+1]] # [x, y]
            
            if  a[0] != b[0] and a[1] == b[1]: # same row
                decrypted_string += ''.join(self.solve_same_row(self, self.matrix, a, b))
            elif a[0] == b[0] and a[1] != b[1]: # same column
                decrypted_string += ''.join(self.solve_same_column(self, self.matrix, a, b))
            elif a[0] != b[0] and a[1] != b[1]: # rectangle
                decrypted_string += ''.join(self.solve_rectangle(self, self.matrix, a, b))
            else:
                print('Invalid pair')
                return None
            

        return decrypted_string

    @staticmethod
    def solve_same_row(self, matrix, a, b):
        x1, y1 = a
        x2, y2 = b

        if x1 - 1 < 0:
            x1 = 4
        else: 
            x1 -= 1

        if x2 - 1 < 0:
            x2 = 4
        else:
            x2 -= 1

        return self.process_duplicate(self, [matrix[y1][x1], matrix[y2][x2]])

    @staticmethod
    def solve_same_column(self, matrix, a, b):
        x1, y1 = a
        x2, y2 = b

        if y1 - 1 < 0:
            y1 = 4
        else: 
            y1 -= 1

        if y2 - 1 < 0:
            y2 = 4
        else:
            y2 -= 1

        return self.process_duplicate(self, [matrix[y1][x1], matrix[y2][x2]])
    
    @staticmethod
    def solve_rectangle(self, matrix, a, b):
        x1, y1 = a # y1,x2
        x2, y2 = b # y2,x1
        return self.process_duplicate(self, [matrix[y1][x2], matrix[y2][x1]])

    @staticmethod
    def process_duplicate(self, pair):
        if pair[1] == 'X':
            return [pair[0] , '']
        return pair



#main
key = 'SUPERSPY'
encrypted = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'

decryption = Decrypt(key, encrypted)
print(decryption.decrypt())

