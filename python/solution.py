def preprocess_string(text):
    #will do this myself
    ans = ""
    for c in text:
        if c.isalpha():
            ans +=c
    return ans.upper()

def create_pf_grid(keyword):
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    grid = []
    newkeyword = "" 
    hset = set()
    #removing duplicates from keyword
    for c in keyword:
        if c not in hset:
            newkeyword+=c
            hset.add(c)
    #adding remaining alphabet characters to keywordstring
    for c in alphabet:
        if c not in newkeyword:
            newkeyword+=c
    #building 5x5 grid with newkeyword string
    for i in range(0, 25, 5):
        grid.append(newkeyword[i:i+5])
    return grid

#method to find the position in grid (row,col) and return it for the character
def find_position(grid, char):
    for i in range(5):
        for j in range(5):
            if grid[i][j] == char:
                return i, j

def decrypt_key(playfair_grid, ciphertext):
    plaintext = ""
    #firstly finding the row,col for each character in grid
    for i in range(0, len(ciphertext), 2):
        c1, c2 = ciphertext[i], ciphertext[i+1]
        row1, col1 = find_position(playfair_grid, c1)
        row2, col2 = find_position(playfair_grid, c2)
        
        #decrypting based on if rows match or colums match or its in the corners
        if row1 == row2:
            decrypted_c1 = playfair_grid[row1][(col1 - 1) % 5]
            decrypted_c2 = playfair_grid[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted_c1 = playfair_grid[(row1 - 1) % 5][col1]
            decrypted_c2 = playfair_grid[(row2 - 1) % 5][col2]
        else:
            decrypted_c1 = playfair_grid[row1][col2]
            decrypted_c2 = playfair_grid[row2][col1]
        
        plaintext += decrypted_c1
        #if second value is X we want to remove it as its a placeholder
        if decrypted_c2 != 'X':  
            plaintext += decrypted_c2
    return plaintext

def main():
    cipherText = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    cipherKey = "SUPERSPY"
    fciphertext = preprocess_string(cipherText)
    keyword = preprocess_string(cipherKey)
    playfair_grid = create_pf_grid(keyword)
    plaintext = decrypt_key(playfair_grid, fciphertext)
    return plaintext

if __name__ == "__main__":
    print(main())
