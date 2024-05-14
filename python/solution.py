from typing import Dict, List, Tuple

# takes the cipher key
# returns the 5x5 table which is used for encrypting/decrypting
def make_key_table(key: str) -> List[str]:
    key = key.upper() #make sure it is uppercase
    
    if not key.isalpha(): raise Exception("Cipher key has unknown characters.") #throw exception if the value is invalid

    letters: str = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    notTaken: set[str] = set(letters) # the set of characters that have not been put in the table yet

    key_table: list[str] = [["" for i in range(5)] for j in range(5)] # the table to fill and return

    row, col = 0,0 

    for let in (key+letters): # go through every letter, first from the key then from the rest of the alphabet in order
        if let not in notTaken: # if the letter is already in the table, it cannot be added again
            continue
    
        key_table[row][col] = let 

        notTaken.remove(let) # letter cannot be used ever again as it is taken

        if col == 4 and row == 4: return key_table # reached the end
        elif col == 4: # end of a row
            row += 1
            col = 0
        else:
            col += 1

    return key_table

# takes the key table with the cipher
# returns (row,col) tuple for every unique letter
# relies on the fact that every letter is unique otherwise map is useless
def get_positions(table: List[str]) -> Dict[str, Tuple[int]]:
    positions: dict[str, tuple[int]] = {}

    for i in range(5):
        for j in range(5):
            let: str = table[i][j]
            positions[let] = (i, j) # set the let position to be the index tuple (i,j)
    
    return positions
    
# takes the encrypted message and the key cipher table (5x5 only)
# returns the decrypted message
def decrypt_message(message: str, key_table: List[str]) -> str:
    if not message.isalpha(): raise Exception("Encrypted message has unknown characters. ") # stop program if message cannot be understood

    message = message.upper()

    # if message is odd, add an X between 2 same letters or at the end
    if len(message) % 2 == 1:
        for i in range(len(message)-1):
            if message[i] == message[i+1]:
                message = message[:i+1] + "X" + message[i+1:]
                break
        if len(message) % 2 == 1: message+='X'


    pairs: list[str] = [] # holds the pairs of the split string, will be used to decrypt
    for i in range(0, len(message)-1, 2):
        pairs.append(message[i] + message[i+1])
    
    positions = get_positions(key_table) # get the positions map for each letter for fast lookup

    result: str = ""
    for pair in pairs: 
        let1, let2 = pair[0], pair[1]

        if let1 == let2: raise Exception("Letters in pair are the same: " + let1) # stop program if letters are the same. Some pre-program steps were wrong

        #get the row and col positions for each letter. they are guaranteed to be different here
        r1, c1 = positions[let1]
        r2, c2 = positions[let2]

        if r1 == r2: # if the row is the same, we take the letters to the left of them in the same row
            newCol1 = c1-1 if c1 > 0 else 4
            newCol2 = c2-1 if c2 > 0 else 4

            result += key_table[r1][newCol1] + key_table[r1][newCol2]
        elif c1 == c2: # if the col is the same, we take the letters above them in the same column
            newRow1 = r1-1 if r1 > 0 else 4
            newRow2 = r2-1 if r2 > 0 else 4

            result += key_table[newRow1][c1] + key_table[newRow2][c1]
        else: #if the letters form a rectangle, we want to take the opposite corners as our decrypted pair
            result += key_table[r1][c2] + key_table[r2][c1]

    #remove invalid characters
    result = result.replace("X", "") 
    result = result.replace(" ", "")

    if not result.isalpha(): raise Exception("Decrypted message should not have special characters. ") # if there were unknown characters, stop program
    result = result.upper() 
    return result


if __name__ == "__main__":
    encrypted = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"

    table = make_key_table(key)

    decrypted = decrypt_message(encrypted, table)

    print(decrypted)
    