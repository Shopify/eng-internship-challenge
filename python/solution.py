
def solution():
    cipher = [['S','U','P','E','R'],
              ['Y','A','B','C','D'],
              ['F','G','H','I','K'],
              ['L','M','N','O','Q'],
              ['T','V','W','X','Z']]
    cipherCoords = {}
    inputString = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    decodedWord = ""

    #Mark down the coords using a dictionary
    for x in range(len(cipher)):
        for y in range(5):
            cipherCoords[cipher[x][y]] = (x,y)

    #Loop through each pair
    for i in range(0,len(inputString),2):
        encodedPair = inputString[i:i+2]
        firstLetter = cipherCoords[encodedPair[0]]
        secondLetter = cipherCoords[encodedPair[1]]

        #When the letters are on the same row
        if firstLetter[0] == secondLetter[0]:

            if firstLetter[1] == 0:
                decodedFirst = cipher[firstLetter[0]][4]
            else:
                decodedFirst = cipher[firstLetter[0]][firstLetter[1]-1]
            
            if decodedFirst != "X":
                decodedWord += decodedFirst

            if secondLetter[1] == 0:
                decodedSecond = cipher[secondLetter[0]][4]
            else:
                decodedSecond = cipher[secondLetter[0]][secondLetter[1]-1]

            if decodedSecond != "X":
                decodedWord += decodedSecond

        #When the letters are on the same column
        elif firstLetter[1] == secondLetter[1]:

            if firstLetter[0] == 0:
                decodedFirst = cipher[4][firstLetter[1]]
            else:
                decodedFirst = cipher[firstLetter[0]-1][firstLetter[1]]
            
            if decodedFirst != "X":
                decodedWord += decodedFirst

            if secondLetter[0] == 0:
                decodedFirst = cipher[4][secondLetter[1]]
            else:
                decodedFirst = cipher[secondLetter[0]-1][secondLetter[1]]
        
            if decodedSecond != "X":
                decodedWord += decodedSecond

        else:
            decodedFirst = cipher[firstLetter[0]][secondLetter[1]]
            decodedSecond = cipher[secondLetter[0]][firstLetter[1]]
    
            if decodedFirst != "X":
                decodedWord += decodedFirst
                
            if decodedSecond != "X":
                decodedWord += decodedSecond

    return decodedWord

if __name__ == '__main__':
    print(solution())