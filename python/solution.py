# solution.py

def toLowerCase(plain):
    # Convert all the characters of a string to lowercase
    return plain.lower()

def toUpperCase(plain):
    return plain.upper()

def removeSpaces(plain):
    # Remove all spaces in a string
    # can be extended to remove punctuation
    return ''.join(plain.split())


def generateKeyTable(key):
    # generates the 5x5 key square
    keyT = [['' for i in range(5)] for j in range(5)]
    dicty = {chr(i + 97): 0 for i in range(26)}

    for i in range(len(key)):
        if key[i] != 'j':
            dicty[key[i]] = 2
    dicty['j'] = 1

    i, j, k = 0, 0, 0
    while k < len(key):
        if dicty[key[k]] == 2:
            dicty[key[k]] -= 1
            keyT[i][j] = key[k]
            j += 1
            if j == 5:
                i += 1
                j = 0
        k += 1

    for k in dicty.keys():
        if dicty[k] == 0:
            keyT[i][j] = k
            j += 1
            if j == 5:
                i += 1
                j = 0

    return keyT


def search(keyT, a, b):
    # Search for the characters of a digraph in the key square and return their position
    arr = [0, 0, 0, 0]

    if a == 'j':
        a = 'i'
    elif b == 'j':
        b = 'i'

    for i in range(5):
        for j in range(5):
            if keyT[i][j] == a:
                arr[0], arr[1] = i, j
            elif keyT[i][j] == b:
                arr[2], arr[3] = i, j

    return arr


def mod5(a):
    # Function to find the modulus with 5
    if a < 0:
        a += 5
    return a % 5


def decrypt(str, keyT):
    # Function to decrypt
    ps = len(str)
    i = 0
    while i < ps:
        a = search(keyT, str[i], str[ i +1])
        if a[0] == a[2]:
            str = str[:i] + keyT[a[0]
            ][mod5(a[1 ] -1)] + keyT[a[0]][mod5(a[3 ] -1)] + str[ i +2:]
        elif a[1] == a[3]:
            str = str[:i] + keyT[mod5(a[0 ] -1)][a[1]] + \
                  keyT[mod5(a[2 ] -1)][a[1]] + str[ i +2:]
        else:
            str = str[:i] + keyT[a[0]][a[3]] + keyT[a[2]][a[1]] + str[ i +2:]
        i += 2

    return str


def decryptByPlayfairCipher(str, key):
    # Function to call decrypt
    ks = len(key)
    key = removeSpaces(toLowerCase(key))
    str = removeSpaces(toLowerCase(str))
    keyT = generateKeyTable(key)
    return decrypt(str, keyT)


if __name__ == '__main__':
    str = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"

    # encrypt using Playfair Cipher
    decrypts = decryptByPlayfairCipher(str, key)

    # Decrypted text
    print(toUpperCase(decrypts))

# Pyhton Code Written By Kushal Prajapati