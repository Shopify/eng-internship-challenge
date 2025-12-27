#Removes duplicates from the key and generates the values for the grid
def arrangeKey(pfkey):
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    playfairKeyDeDuped = ''
    
    for letter in pfkey:
        if letter not in playfairKeyDeDuped:
            playfairKeyDeDuped += letter

    for letter in alphabet:
        if letter.upper() not in playfairKeyDeDuped:
            playfairKeyDeDuped += letter.upper()
        
    return playfairKeyDeDuped

#Retrieves the formatted string for the grid and creates a 5x5 grid
def createGrid(playfairkey):
    pfkey = arrangeKey(playfairkey)
    
    substrings = [pfkey[i:i+5] for i in range(0, len(pfkey), 5)]
    grid = [list(substring) for substring in substrings]
    
    return grid

#Finds the row and column of grid that letter is in
def findLetters(grid, letter):
    for i in range(5):
        for j in range(5):
            if grid[i][j] == letter:
                return i, j

#Utilizes the grid and key to compare the rows and columns of each pair of letters and decipher the code
def pfDecipher(cipher, playfairkey):
    plaintext = ''
    cipher = ''.join(char.upper() for char in cipher if char.isalpha()).replace(' ','').replace('J', 'I')
    grid = createGrid(playfairkey)
    
    i = 0
    
    while i < len(cipher):
        #Selects a pair of letters
        letter1 = cipher[i]
        letter2 = cipher[i+1]
        
        #Finds the row and column in grid for each of the letters
        row1, col1 = findLetters(grid, letter1)
        row2, col2 = findLetters(grid, letter2)
        
        #If the letters are in the same row, adds value in grid to the right of it (looping around if it's at the end of the list)
        if row1 == row2:
            plaintext += grid[row1][(col1 - 1) % 5]
            plaintext += grid[row2][(col2 - 1) % 5]
            
        #If the letters are in the same column, adds value in grid below 
        elif col1 == col2:
            plaintext += grid[(row1 - 1) % 5][col1]
            plaintext += grid[(row2 - 1) % 5][col2]
        
        #Otherwise, adds value diagonal to the letter
        else:
            plaintext += grid[row1][col2]
            plaintext += grid[row2][col1]
        
        i += 2
    
    plaintext = ''.join(char for char in plaintext if char != 'X')
        
    return plaintext

cipherCode = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
playfairKey = "SUPERSPY"
plaintext = pfDecipher(cipherCode, playfairKey)
print(plaintext)