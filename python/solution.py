import math

def make_matrix (keys):
    found= []
    lists = []
    square= []
    alphabet= "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    #We iterate through the keys and put the unique one in the found list
    for i in keys:
        if i not in found:
            found.append(i)    
   
    #Then we iterate through all the alphabet and put it in found list
    for i in alphabet:
        if i not in found:
            found.append(i)
    
    for i in range(len(found)):
        # we use the found list and create a 5 x 5 matrix with all the alphabet in proper order
        lists.append(found[i])
        if (i + 1) % 5 == 0:
            square.append(lists)
            lists=[]
    return square

def make_pair(encryption):
    lists=[]
    pairs=[]
    # we iterate through the encrypted text and make pairs
    for i in range(len(encryption)):
        if i % 2 == 0:
            lists.append(encryption[i])
        else:
            # if two letter are similar we replace the later one with X
            if encryption[i-1] == encryption[i]:
                lists.append('X')
            else:
                lists.append(encryption[i])
            pairs.append(lists)
            lists = []
    #if we have odd letter we insert an X at the end
    if len(encryption) % 2 != 0:
        pairs.append([encryption[len(encryption) - 1], 'X'])
        
    return pairs

def search_square(square, value):
    # we iterate through the square matrix and return the coordinate of the targeted value
    for i in range(len(square)):
        for j in range(len(square[i])):
            if value == square[i][j]:
                return [i, j]
    
def decrypt(pairs, square):
    first = ''
    second = ''
    message = ""
    cfirst = []
    csecond = []
    # we iterate through each pair and get the decrypted message
    for pair in pairs:
        first = pair[0]
        second = pair[1]
        # we get the coordinate for both the letter in the pair
        cfirst = search_square(square, first)
        csecond = search_square(square, second)
       # if the rows of both the pairs are similar we iterate
        if cfirst[0] == csecond[0]:
            if cfirst[1] > 0 and csecond[1] > 0:
                # we shift one column to the left
                message += square[cfirst[0]] [cfirst[1] - 1] 
                message += square[csecond[0]] [csecond[1] - 1]
            else:
                if cfirst[1] > 0:
                    # if one column is the first column we shift to the left and hence wrap to the last column
                    message += square[cfirst[0]] [cfirst[1] - 1]
                    message += square[csecond[0]] [ 4]
                else:
                    message += square[cfirst[0]] [ 4]
                    message += square[csecond[0]] [ csecond[1] - 1]
        elif cfirst[1] == csecond[1]:
            # if both letter are in the same column we shift one row up 
            if cfirst[0] > 0 and csecond[0] > 0:
                message += square[cfirst[0] - 1] [ cfirst[1] ]
                message += square[csecond[0] - 1] [ csecond[1] ]
            else:
                # if one letter in first row we shift up adn hence wrap and return the last row value
                if cfirst[0] > 0:
                    message += square[cfirst[0] - 1] [ cfirst[1]]
                    message += square[4] [ csecond[1]]
                else:
                    message += square[4] [ cfirst[1]]
                    message += square[csecond[0] - 1] [ csecond[1]]
        else:
            # if the letters are not on the same row or column, we replace them with the letters on the same row but at the other pair of corners of the rectangle defined by the original pair
            message += square[cfirst[0]] [ csecond[1]]
            message += square[csecond[0]] [ cfirst[1]]
    # when returning we remove the extra X as they are redundant and was added either at the end or for similar pair
    return message.replace('X', '')

if __name__ == '__main__':
    key= "SUPERSPY"
    encrypted= "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    matrix= make_matrix(key)
    pairs = make_pair(encrypted)
    print(decrypt(pairs, matrix))
    