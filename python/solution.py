

## The key "SUPERSPY", WHER I=J
key = [["S","U","P","E","R"],
       ["Y","A","B","C","D"],
       ["F","G","H","I","K"],
       ["L","M","N","O","Q"],
       ["T","V","W","X","Z"]]

##The encrypted Message
encrypted = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

##Effects: Decrypts the Rectangle Rule, Returns a two letter string
##first, second = the first and second letters to decrypt
def rect(first,second):
    ##STUB
    return ""

##Effects: Decrypts the Row Rule, Returns a two letter string
##first, second = the first and second letters to decrypt
def row(first,second):
    ##STUB
    return ""

##Effects: Decrypts the Col Rule, Returns a two letter string
##first, second = the first and second letters to decrypt
def col(first,second):
    ##STUB
    return ""

##Effects: Removes all instances of "X" from the string and returns it
##s = the string to remove X from
def removeX(s):
    ##STUB
    return ""

##Effects: Returns true if first and second are in the same row in key
def sameRow(first,second):
    return True

##Effects: Returns true if first and second are in the same col in key
def sameCol(first,second):
    return True


##Effects: Decrypts the encrypted global with the global key
##         Prints the decrptyed string
def decrypt():
    ##Stub
    rsf =""
    i = 0

    ##Gets two letter pairs as first and second
    while (i < len(encrypted)):
        first = encrypted[i:i+1]
        second = encrypted[i+1:i+2]

        if (sameRow(first,second)):
            ##STUB
            print("hi")
        elif (sameCol(first,second)):
            ##STUB
            print("hi")
        else:
            print("hi")
        
        
        i = i + 2

decrypt()