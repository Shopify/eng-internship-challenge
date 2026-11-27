def generateKeySquare(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J usually omitted
    keySquare = []
    keySet = set() # no duplicates

    # add key letters to key square
    for char in key:
        if char not in keySet and char in alphabet:
            keySquare.append(char)
            keySet.add(char)

    # add remaining letters of alphabet
    for char in alphabet:
        if char not in keySet:
            keySquare.append(char)
            keySet.add(char)

    # transform the keySquare list into a 5x5 matrix
    return [keySquare[i:i + 5] for i in range(0, 25, 5)]

def preprocessMessage(message):
    message = message.replace("J", "I")
    preparedMessage = "" # placeholder for now
    i = 0

    while i < len(message):
        preparedMessage += message[i]
        if i + 1 < len(message) and message[i] == message[i + 1]:
            preparedMessage += "X"
            i += 1
        elif i + 1 < len(message):
            preparedMessage += message[i + 1]
            i += 2
        else:
            preparedMessage += "X"
            i += 1
    return preparedMessage

def findPosition(keySquare, char):
    for row in range(5):
        for col in range(5):
            if keySquare[row][col] == char:
                return row, col
    return None

def decryptDigraph(digraph, keySquare):
    row1, col1 = findPosition(keySquare, digraph[0])
    row2, col2 = findPosition(keySquare, digraph[1])
    
    # handles different cases based on positions of characters in the key square
    if row1 == row2:
        return keySquare[row1][(col1 - 1) % 5] + keySquare[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return keySquare[(row1 - 1) % 5][col1] + keySquare[(row2 - 1) % 5][col2]
    else:
        return keySquare[row1][col2] + keySquare[row2][col1]

def decryptMessage(encryptedMessage, keySquare):
    decryptedMessage = ""
    for i in range(0, len(encryptedMessage), 2):
        # extract pair of characters (a digraph) 
        digraph = encryptedMessage[i:i + 2]
        decryptedMessage += decryptDigraph(digraph, keySquare)
    return decryptedMessage

def main():
    # given in question
    encryptedMessage = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"
    
    keySquare = generateKeySquare(key)
    preparedMessage = preprocessMessage(encryptedMessage)
    decryptedMessage = decryptMessage(preparedMessage, keySquare)
    
    decryptedMessage = decryptedMessage.replace("X", "")
    print(decryptedMessage)

if __name__ == "__main__":
    main()