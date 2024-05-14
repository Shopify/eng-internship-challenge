def createKeyTable(keyword: str) -> list[list[str]]:
    if len(keyword) > 25:
        raise Exception("Length of keyword exceeds decryption table size")
    keyword = keyword.upper().replace(" ", "").replace("J", "I")
    dim = 5 # dimension of table 5x5
    resultTable = [['*' for _ in range(dim)] for _ in range(dim)]
    chars = set() # non-duplicate letters in keyword
    currRow, currCol = 0, 0
    for char in keyword:
        if char not in chars:
            chars.add(char)
            resultTable[currRow][currCol] = char # populate the table with keyword letters
            currCol += 1
        if currCol == dim:
            currCol = 0
            currRow += 1
    alphaIdx = 65 # index of letter A in Unicode
    # populate table with alphabet
    while True:
        while chr(alphaIdx) in chars:
            alphaIdx += 1
        # 'I' and 'J' are interchangeable so 'J' will never be in the table
        if chr(alphaIdx) == 'J':
            alphaIdx += 1
        resultTable[currRow][currCol] = chr(alphaIdx)
        alphaIdx += 1 # go to next letter in alphabet
        currCol += 1
        if currCol == dim:
            currRow += 1
            currCol = 0
        if currRow == dim:
            break
    return resultTable

def decrypt(string: str, keyword: str) -> str:
    dim = 5
    table = createKeyTable(keyword) # decryption table
    locationMap = {table[i][j]: (i, j) for i in range(dim) for j in range(dim)} # map each letter to its location in the table
    # remove spaces in string
    string = string.upper().replace(" ", "")
    result = []
    for i in range(0, len(string), 2):
        x1, y1 = locationMap[string[i]] # location of first letter in table
        x2, y2 = locationMap[string[i+1]] # location of second letter in table
        # case 1: same row 
        if x1 == x2:
            result.append(table[x1][y1-1] if y1-1>=0 else table[x1][dim - 1])
            result.append(table[x2][y2-1] if y2-1>=0 else table[x2][dim - 1])
        # case 2: same col
        elif y1 == y2:
            result.append(table[x1-1][y1] if x1-1>=0 else table[dim-1][y1])
            result.append(table[x2-1][y2] if x2-1>=0 else table[dim-1][y2])
        # case 3: rectangle
        else:
            result.append(table[x1][y2])
            result.append(table[x2][y1])
    return "".join(filter(lambda x: x != "X", result)) # return final string without letter "X"

if __name__ == "__main__":
    keyword = "superspy"
    phrase = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    print(decrypt(phrase, keyword))


