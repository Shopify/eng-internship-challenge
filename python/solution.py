import numpy as np

encryptedMessage="IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
polybiasSquare=np.array([
                ["S", "U", "P", "E", "R"],
                ["Y", "A", "B", "C", "D"],
                ["F", "G", "H", "I", "K"],
                ["L", "M", "N", "O", "Q"],
                ["T", "V", "W", "X", "Z"]])

decryptedMessage=""
messageLength=len(encryptedMessage)

#decrypt groups of 2 letters
for i in range(0,messageLength,2):
    firstLetter=""
    secondLetter=""

    firstLetterRow=np.where(polybiasSquare==encryptedMessage[i])[0][0]
    firstLetterColumn=np.where(polybiasSquare==encryptedMessage[i])[1][0]
    secondLetterRow=np.where(polybiasSquare==encryptedMessage[i+1])[0][0]
    secondLetterColumn=np.where(polybiasSquare==encryptedMessage[i+1])[1][0]

    #same column
    if(firstLetterColumn==secondLetterColumn): 
        if(firstLetterRow==0): 
           firstLetter=polybiasSquare[4][firstLetterColumn] #wrap around
        else:
           firstLetter=polybiasSquare[firstLetterRow-1][firstLetterColumn] 

        if(secondLetterColumn==0): 
           secondLetter=polybiasSquare[4][firstLetterColumn] #wrap around
        else:
           secondLetter=polybiasSquare[secondLetterRow-1][firstLetterColumn]
    #same row
    elif(firstLetterRow==secondLetterRow): 
        if(firstLetterColumn==0):
           firstLetter=polybiasSquare[firstLetterRow][4] #wrap around
        else:
           firstLetter=polybiasSquare[firstLetterRow][firstLetterColumn-1]

        if(secondLetterColumn==0):
           secondLetter=polybiasSquare[secondLetterRow][4] #wrap around
        else:
           secondLetter=polybiasSquare[secondLetterRow][secondLetterColumn-1]
    #rectangle
    else: 
       firstLetter=polybiasSquare[firstLetterRow][secondLetterColumn]
       secondLetter=polybiasSquare[secondLetterRow][firstLetterColumn]

    decryptedMessage=decryptedMessage+firstLetter+secondLetter
       
for i in range(0,messageLength,2): #adjust for double letters
   if(i+2<len(decryptedMessage)):
      if (decryptedMessage[i+1]=="X" and decryptedMessage[i]==decryptedMessage[i+2] ):
         decryptedMessage=decryptedMessage[:i]+decryptedMessage[i+2:]

if(decryptedMessage[len(decryptedMessage)-1]=="X"): #remove ending X
   decryptedMessage=decryptedMessage[:len(decryptedMessage)-1]

print(decryptedMessage)