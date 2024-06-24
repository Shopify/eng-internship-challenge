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


        

def solve(encrypted, key):
    # Playfair cypher uses a 5x5 grid of letters of the alphabet
    matrix = createMatrix(key)
    # Breaks text into pairs of letters and swaps them in a rectangle within that grid
    digrams = createDigrams(encrypted)



    print(digrams)
    print(matrix)
    return encrypted


def main():
    encrypted = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"
    result = solve(encrypted, key)
    print(result)
    return result


if __name__ == "__main__":
    main()
