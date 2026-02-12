def generateMatrix(secretKey):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" #Without J to fit the alphabet in a 5x5 matrix
    matrix = []
    
    for c in secretKey:
        if c not in matrix:
            matrix.append(c)
    for c in alphabet:
        if c not in matrix:
            matrix.append(c)
    # Matrix = 
    #[S, U, P, E, R,
    # Y, A, B, C, D,
    # F, G, H, I, K,
    # L, M, N, O, Q,
    # T, V, W, X, Z]
    return matrix

def decode(secretText, matrix):

    stringAnswer = ""

    for c in range(0,len(secretText), 2):
        #Swapping "J" characters
        firstChar = secretText[c] if secretText[c] != "J" else "I"
        if c + 1 < len(secretText):
            secondChar = secretText[c + 1] if secretText[c + 1] != "J" else "I"
        else:
            #if ending with odd length, add "X"
            secondChar = "X"

        firstChar = matrix.index(firstChar)
        secondChar = matrix.index(secondChar)

        if (secondChar // 5) == (firstChar // 5): #Same Row
            #handling the uses of a 1d list
            a = firstChar - 1 if firstChar // 5 == (firstChar - 1) // 5 else firstChar + 4
            b = secondChar - 1 if secondChar // 5 == (secondChar - 1) // 5 else secondChar + 4
        elif (secondChar % 5) ==  (firstChar % 5): #Same Column
            a = firstChar - 5
            b = secondChar - 5
        else:
            difference = abs((secondChar % 5) - (firstChar % 5))
            if firstChar % 5 > secondChar % 5:
                a = firstChar - difference
                b = secondChar + difference
            else:
                a = firstChar + difference
                b = secondChar - difference

        stringAnswer += matrix[a] + matrix[b]
    #Remove Xs
    stringAnswer = stringAnswer.replace("X", "").replace(" ", "")
    return stringAnswer

secretKey = "SUPERSPY"
encodedText = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
matrix = generateMatrix(secretKey)
answer = decode(encodedText, matrix)
print(answer)
