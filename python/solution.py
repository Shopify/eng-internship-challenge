LETTERS = "ABCDEFGHIKLMNOPQRSTUVWXYZ" # J is removed in order to have 25 letters and fit in a 5x5 grid

# Returns the position of a letter in the grid in the form of a tuple (row, column)
def searchGrid (grid, letter):
    for i in range(5):
        for j in range(5):
            if grid[i][j] == letter:
                return (i, j)
    return None

def decipher (key, message):
    # Remove J and spaces, and convert to uppercase
    key = key.replace("J", "I").replace(" ", "").upper()

    message = message.replace("J", "I").replace(" ", "").upper()
    if len(message) % 2 != 0:     # Add an X at the end if the length is odd
        message += "X"


    # Create the grid
    gridLetters = ""
    for c in key:
        if c not in gridLetters:
            gridLetters += c
    for c in LETTERS:
        if c not in gridLetters:
            gridLetters += c
    grid = []
    for i in range(5):
        grid.append(gridLetters[i*5:i*5+5])

    
    # Decipher the message
    output = ""
    for i in range(0, len(message), 2):

        # If two consecutive letters are the same, we replace the second one with an X
        if message[i] == message[i+1]:
            message = message[:i+1] + "X" + message[i+1:]
            
        # Get the positions of the two letters as tuples (row, column)
        a = searchGrid(grid, message[i]) 
        b = searchGrid(grid, message[i+1])
        
        # If they are on the same row, we take the letter to the left of each one (with modulo 5 to wrap around the grid if needed)
        if a[0] == b[0]:
            output += grid[a[0]][(a[1]-1)%5] + grid[b[0]][(b[1]-1)%5]

        # If they are on the same column, we take the letter above each one (with modulo 5 to wrap around the grid if needed)
        elif a[1] == b[1]:
            output += grid[(a[0]-1)%5][a[1]] + grid[(b[0]-1)%5][b[1]]

        # If not on same row or column, they must form a rectangle. We take the other two corners of the rectangle (with horizontal respect).
        else:
            output += grid[a[0]][b[1]] + grid[b[0]][a[1]]

    return output.replace("X", "")


# Test the decipher algorithm
key = "SUPERSPY"
message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
output = decipher(key, message)
print(output)