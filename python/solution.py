def main():
    encryptedMessage = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV" # encrypted message provided
    decodedMessage = "" # string to represent the decoded message which we can append to after iterating through each pair of letters in the encrypted message
 
    # key table created using documentation and the key string provided
    keyTable = [['S', 'U', 'P', 'E', 'R'],
                ['Y', 'A', 'B', 'C', 'D'],
                ['F', 'G', 'H', 'I', 'K'],
                ['L', 'M', 'N', 'O', 'Q'],
                ['T', 'V', 'W', 'X', 'Z']]


    # initialize a hash map for efficient constant time look up of indices  of each letter since each letter appears once --> takes O(5^2) space complexity -> constant space
    dictIndex = {}
    for i in range(len(keyTable)):
        for j in range(len(keyTable[0])):
            dictIndex[keyTable[i][j]] = (i, j) # create a dictionary of each letter mapped to its respective index within the grid fo O(1) lok up time later on when iterating through the encrypted message

    # iterate through the encrypted message
    for i in range(0, len(encryptedMessage), 2):
        # get the pair of letters through each iteration
        letter1 = encryptedMessage[i]
        letter2 = encryptedMessage[i+1]

        # get the corresponding index of each letter
        letter1Index = dictIndex[letter1]
        letter2Index = dictIndex[letter2]

        # extract the x and y coordinates each letter on the key table board
        x1 = letter1Index[1]
        y1 = letter1Index[0]

        x2 = letter2Index[1]
        y2 = letter2Index[0]

        # initialize a string for appending the decoded pair of letters from the encoded message
        curPair = ""

        # condition for row
        if (y1 == y2):
            # move left along a row for decoding
            curPair += keyTable[y1][x1-1]
            curPair += keyTable[y2][x2-1]

        # condition for column
        elif (x1 == x2):
            # move up in table along a column for decoding
            curPair += keyTable[y1 - 1][x1]
            curPair += keyTable[y2 - 1][x2]

        # condition for rectangle
        else:
            # get the complementary corners of the rectangle wiht the first letter being the first letter from encoded message
            curPair += keyTable[y1][x2]
            curPair += keyTable[y2][x1]
        
        # condition to check if X is present in the current pair,
        if 'X' in curPair:
            curPair = curPair.replace('X','') # remove the X if it is present

        # append the current decoded letter pair to the overall decoded message
        decodedMessage += curPair
    
    print(decodedMessage)
    return decodedMessage
    # overall time complexity = O(n) , where n is the length of the encoded message and space complexity is O(n) for auxiliary space from deocded message


if __name__ == '__main__':
    main()