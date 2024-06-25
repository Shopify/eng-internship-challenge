# This code was written by Tarang Patel
# Time Complexity: O(n), where n is the length of the input string

def solution():
    cipher = [['S','U','P','E','R'],
              ['Y','A','B','C','D'],
              ['F','G','H','I','K'],
              ['L','M','N','O','Q'],
              ['T','V','W','X','Z']]
    cipherCoords = {}
    inputString = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    decodedWord = ""

    # Record the coordinates of each letter in the cipher table using a dictionary
    for x in range(len(cipher)):
        for y in range(5):
            cipherCoords[cipher[x][y]] = (x, y)

    # Loop through each pair of characters in the input string
    for i in range(0, len(inputString), 2):
        decodedFirst, decodedSecond = "", ""
        encodedPair = inputString[i:i+2]
        firstLetter = cipherCoords[encodedPair[0]]
        secondLetter = cipherCoords[encodedPair[1]]

        # If the letters are in the same row
        if firstLetter[0] == secondLetter[0]:
            decodedFirst = cipher[firstLetter[0]][(firstLetter[1] - 1) % 5]
            decodedSecond = cipher[secondLetter[0]][(secondLetter[1] - 1) % 5]

        # If the letters are in the same column
        elif firstLetter[1] == secondLetter[1]:
            decodedFirst = cipher[(firstLetter[0] - 1) % 5][firstLetter[1]]
            decodedSecond = cipher[(secondLetter[0] - 1) % 5][secondLetter[1]]

        # If the letters are in different rows and columns
        else:
            decodedFirst = cipher[firstLetter[0]][secondLetter[1]]
            decodedSecond = cipher[secondLetter[0]][firstLetter[1]]

        # Add the decoded letters to the decoded word, ignoring 'X'
        if decodedFirst != "X":
            decodedWord += decodedFirst
        if decodedSecond != "X":
            decodedWord += decodedSecond

    return decodedWord

if __name__ == '__main__':
    print(solution())
