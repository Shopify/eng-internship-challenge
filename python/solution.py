def createKeyMatrix(key : str):
    
    key = 'SUPERSPY'
    alpha = 65
    matrix = []
    
    for i in key:
        if i not in matrix:
            matrix.append(i)
    
    for i in range(0,26):
        if chr(alpha+i) != 'J' and chr(alpha+i) not in matrix:
            matrix.append(chr(alpha+i))
    
    return matrix

def createBigram(cipher : str):

    matrix = []
    i = 0
    while(i <= (len(cipher) - 2)):
        matrix.append(cipher[i]+cipher[i+1])
        i = i + 2

    return matrix

def checkRow(Bigram : str, key: list):
    
    l1 = key.index(Bigram[0])
    l2 = key.index(Bigram[1])
    
    if(int(l1/5) == int(l2/5)):
        subkey = key[int(l1/5)*5:int(l1/5)*5+5]
        return(subkey[l1%5 - 1] + subkey[l2%5 - 1], True)
    else:
        return(False,False)


def checkColumn(Bigram : str, key: list):

    l1 = key.index(Bigram[0])
    l2 = key.index(Bigram[1])

    if(int(l1%5) == int(l2%5)):
        return(key[(int(l1/5) - 1)*5 + l1%5] + key[(int(l2/5) - 1)*5 + l2%5], True)
    else:
        return(False,False)
    
def solveRectangle(Bigram : str, key: list):
    a = Bigram[0]

    l1 = key.index(Bigram[0])
    l2 = key.index(Bigram[1])

    l1_r, l1_c = int(l1/5), l1%5
    l2_r, l2_c = int(l2/5), l2%5

    return(key[l1_r*5 + l2_c] + key[l2_r*5 + l1_c])

def main():

    cipherKey = createKeyMatrix('SUPERSPY') 
    cipher = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'

    cipherBigram = createBigram(cipher)
    
    decrypt = ''

    for bigram in cipherBigram:
        
        if checkRow(bigram, cipherKey)[1] == True:
            decrypt += checkRow(bigram, cipherKey)[0]
        elif checkColumn(bigram, cipherKey)[1]  == True:
            decrypt += checkColumn(bigram, cipherKey)[0]
        else:
            decrypt += solveRectangle(bigram, cipherKey)

    no_x = list(decrypt)
    ind_x = []
    for i in range(len(no_x)):
        if no_x[i] == 'X':
            ind_x.append(i)
    for i in ind_x:
        no_x[i] = ''
    decrypt = "".join(no_x)

    print(decrypt)


if __name__ == '__main__':
    main()