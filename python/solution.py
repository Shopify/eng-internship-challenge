# Create a matrix with the key first followed by the letters of the alphabet that aren't part of the key
def createMatrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    letters = []

    # Add in key minus duplicates
    for ch in key:
        if ch not in letters:
            letters.append(ch)
    # Add rest of alphabet
    for ch in alphabet:
        if ch not in key:
            letters.append(ch)

    # Make into a matrix
    matrix = []
    i = 0
    while i<25:
        matrix.append(letters[i:i+5])
        i += 5

    return matrix

def createDigrams(encrypted):
    digrams = []
    cur = ""
    for ch in encrypted:
        if len(cur) == 2:
            digrams.append(cur)
            cur = ""
        else:
            cur += ch
    return digrams

def getIndex(letter, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == letter:
                return [i, j]


def solve_digram(digram, matrix):
    indexL1X, indexL1Y = getIndex(digram[0], matrix)
    indexL2X, indexL2Y = getIndex(digram[1], matrix)
    
    result = ""

    # Same row, here we get the letter 1 to the left for each
    if indexL1X == indexL2X:
        indexL1Y = (indexL1Y - 1) % 5 # In case it was 0
        indexL2Y = (indexL2Y - 1) % 5 # In case it was 0
        result = matrix[indexL1X][indexL1Y] + matrix[indexL2X][indexL2Y]

    # Same column, here we get the letter 1 to the left for each
    elif indexL1Y == indexL2Y:
        indexL1X = (indexL1X - 1) % 5 # In case it was 0
        indexL2X = (indexL2X - 1) % 5 # In case it was 0
        result = matrix[indexL1X][indexL1Y] + matrix[indexL2X][indexL2Y]
    
    # Box method: swap the columns, with the first letter still coming first
    else:
        result = matrix[indexL1X][indexL2Y] + matrix[indexL2X][indexL1Y]
    
    return result


        

def solve(encrypted, key):
    # Playfair cypher uses a 5x5 grid of letters of the alphabet
    matrix = createMatrix(key)
    # Breaks text into pairs of letters and swaps them in a rectangle within that grid
    digrams = createDigrams(encrypted)
    # Solve each of the digrams
    result = ""
    for digram in digrams:
        result += solve_digram(digram, matrix)
    
    print(result)
    return result


def main():
    encrypted = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"
    result = solve(encrypted, key)
    print(result)
    return result


if __name__ == "__main__":
    main()
