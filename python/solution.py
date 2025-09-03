
alphabets = [0] * 26

key = "SUPERSPY"

grid = [['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]

# fill matrix

# fill matrix using key first
i = 0
k = 0
saveI = 0
saveJ = 0
while i < 5:
    j = 0
    if 5 * i + j + k < len(key):
        while j < 5:
            if 5 * i + j + k < len(key):
                # print(5*i + j)
                # print(j)
                if alphabets[ord(key[5 * i + j + k]) - ord('A')] == 0:
                    grid[i][j] = key[5 * i + j + k]
                    # print(grid)
                    alphabets[ord(key[5 * i + j + k]) - ord('A')] += 1
                else:
                    j -= 1
                    k += 1
            else:
                saveJ = j
                break
            saveJ = j
            j += 1
    else:
        saveI
        break
    saveI = i
    i += 1

# fill in rest of the grid
i = saveI
j = saveJ
first = True
k = 0
while i < 5:
    if first:
        first = False
    else:
        j = 0
    while j < 5:
        if alphabets[k] == 0:
            grid[i][j] = chr(k + ord('A'))
            alphabets[k] += 1
            # I and J are same
            if k == 8 or k == 9:
                alphabets[8] += 1
                alphabets[9] += 1
        else:
            j -= 1
        k += 1
        j += 1
    i += 1

# split cipher text into digraphs
ciphertext = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'
x = ciphertext
chunks, chunk_size = len(x), 2
res = [ x[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
# print(res)

# LOOP THROUGH DIGRAPHS AND DECIPHER EACH ONE
k = 0
while k < len(res):
    i = 0
    found = False

    # ALGORITHM CHECK 1: COLUMN CHECK
    while i < 5:
        j = 0
        find0 = True
        find1 = False
        save = ""
        while j < 5:
            if find0 and grid[j][i] == res[k][0]:
                if j == 0:
                    save += grid[4][i]
                else:
                    save += grid[j - 1][i]
                find1 = True
                find0 = False
                j = -1
            elif find1 and grid[j][i] == res[k][1]:
                if j == 0:
                    save += grid[4][i]
                else:
                    save += grid[j - 1][i]
                find1 = False
                find0 = False

            j += 1

        if len(save) == 2:
            found = True
            # print("foundCol")
            res[k] = save

        i += 1

    # ALGORITHM CHECK 2: ROW CHECK
    if not found:
        j = 0
        while j < 5:
            i = 0
            find0 = True
            find1 = False
            save = ""
            while i < 5:
                if find0 and grid[j][i] == res[k][0]:
                    if i == 0:
                        save += grid[j][4]
                    else:
                        save += grid[j][i - 1]
                    find1 = True
                    find0 = False
                    i = -1
                elif find1 and grid[j][i] == res[k][1]:
                    if i == 0:
                        save += grid[j][4]
                    else:
                        save += grid[j][i - 1]
                    find1 = False
                    find0 = False

                i += 1

            if len(save) == 2:
                found = True
                # print("foundRow")
                res[k] = save

            j += 1
    
    # ALGORITHM CHECK 3: FINAL RECTANGLE DECIPHER
    if not found:
        a,b,x,y = 0,0,0,0
        i = 0
        while i < 5:
            j = 0
            while j < 5:
                if grid[i][j] == res[k][0]:
                    a,b = i,j
                if grid[i][j] == res[k][1]:
                    x,y = i,j
                j += 1
            i += 1

        res[k] = grid[a][y] + grid[x][b]

    k += 1

# PRINT DECIPHERED STRING
for digraph in res:
    for char in digraph:
        if char != 'X' and char != ' ' and char.isalpha():
            print(char.upper(),end='')