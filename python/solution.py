## The key "SUPERSPY", where I=J
key = [["S","U","P","E","R"],
       ["Y","A","B","C","D"],
       ["F","G","H","I","K"],
       ["L","M","N","O","Q"],
       ["T","V","W","X","Z"]]

##The encrypted message
encrypted = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

## maps letter, [row,col] pairs
map = {}

##Effects: Initializes the map, mapping letters to a row column array
def initMap():
    for i, row in enumerate(key):
        for j, letter in enumerate(row):
            map[letter] = [i,j]
            

##Effects: Decrypts the Rectangle Rule, Returns a two letter string
##first, second = the first and second letters to decrypt
def rect(first,second):
    firstcol = map[first][1]
    secondcol = map[second][1]
    firstrow = map[first][0]
    secondrow = map[second][0]

    return key[firstrow][secondcol] + key[secondrow][firstcol]

##Effects: Decrypts the Row Rule, Returns a two letter string
##first, second = the first and second letters to decrypt
def row(first,second):
    firstcol = map[first][1]
    secondcol = map[second][1]
    row = map[first][0]
    if(firstcol == 0):
        firstcol = 4
    else:
        firstcol = firstcol-1
    
    if(secondcol == 0):
        secondcol = 4
    else:
        secondcol = secondcol-1

    return key[row][firstcol] + key[row][secondcol]

##Effects: Decrypts the Col Rule, Returns a two letter string
##first, second = the first and second letters to decrypt
def col(first,second):
    firstrow = map[first][0]
    secondrow = map[second][0]
    col = map[first][1]
    if(firstrow == 0):
        firstrow = 4
    else:
        firstrow = firstrow-1
    
    if(secondrow == 0):
        secondrow = 4
    else:
        secondrow = secondrow-1

    return key[firstrow][col] + key[secondrow][col]

##Effects: Removes regular expression "X" from the string and returns it
##s = the string to remove X from
def removeX(s):
    return s.replace("X","")

##Effects: Returns true if first and second are in the same row in key
def sameRow(first,second):
    return map[first][0] == map[second][0]

##Effects: Returns true if first and second are in the same col in key
def sameCol(first,second):
    return map[first][1] == map[second][1]


##Effects: Decrypts the encrypted global with the global key
##         Prints the decrptyed string
def decrypt():
    ##Stub
    rsf =""
    i = 0
    ##Gets two letter pairs as first and second (encryped is even length)
    while (i < len(encrypted)):
        first = encrypted[i:i+1]
        second = encrypted[i+1:i+2]

        if (sameRow(first,second)):
            rsf = rsf + row(first,second)
        elif (sameCol(first,second)):
            rsf = rsf + col(first,second)
        else:
            rsf = rsf + rect(first,second)
        
        i = i + 2

    rsf = removeX(rsf)
    print(rsf)



## First Call initMap to create the map and then decrypt to print the solution.
initMap()
decrypt()