#Create a list of the alphabet without the letter 'J' to stay within table 5x5 capacity (25 letters)
ALPHABET= "ABCDEFGHIKLMNOPQRSTUVWXYZ"

#Special characters to filter out
SPECIAL = "!@#$%^&*()_+-=<>?,./;':\"[]{}\\|`~"



#This function generates a 5x5 grid with the key values and the remaining alphabet
def generate_playfair_grid(key):
    #Initialize the grid with 5x5 empty strings
    grid = [['' for _ in range(5)] for _ in range(5)]

    #Create a set to store the letters that have been added to the grid to prevent duplicates from being added to grid
    added_to_grid = set()

    #Accounts for in key cotains "J" and replaces it with "I" and converts the key to uppercase
    key = key.replace("J", "I").replace(" ", "").upper()

    row, col = 0, 0
    #Fill the grid with the key values first
    for letter in key:
        #If the letter is not in the grid or a special character, add it to grid
        if letter not in added_to_grid and letter not in SPECIAL:
            grid[row][col] = letter
            added_to_grid.add(letter)
            col += 1
            if col == 5:
                col = 0
                row += 1
    
    #Fill remaining slots in grid with the alphabet
    for letter in ALPHABET:
        #If the letter is not in the grid or a special character, add it to grid
        if letter not in added_to_grid and letter not in SPECIAL:
            grid[row][col] = letter
            added_to_grid.add(letter)
            col += 1
            if col == 5:
                col = 0
                row += 1
    return grid



#This function finds the position of a letter in the 5x5 grid and returns (row, col)
def find_grid_position(letter, grid):
    for row in range(5):
        for col in range(5):
            if grid[row][col] == letter:
                return (row, col)
    return None



#This function decrypts a message using the 5x5 grid generated by the generate_playfair_grid function
def decrypt_playfair(message, grid):
    #Initialize the result variable to store the decrypted message
    result = ""

    #Filter out special characters, non-alphabetical characters and spaces from the message. Upper case incoming message.
    message = "".join(char for char in message if char.isalpha() and char not in SPECIAL).upper()

    #If the message length is odd, add an "X" to the end of the message to allow for even pair creation
    if len(message) % 2 != 0:
        message += "X"
    
    #Creates a list of 2 letter pairs from the encrypted message
    pairs =  ([message[letter:letter+2] for letter in range(0, len(message), 2)])

    #Iterates through list of 2 letter pairs
    for pair in pairs:
        #Returns the position of the letters in the grid (row, col)
        letter_1_position = find_grid_position(pair[0], grid)
        letter_2_position = find_grid_position(pair[1], grid)


        #If the letters are in the same column (modulo 5 to account for wrap around to the bottom if position[row] < 0)
        if letter_1_position[1] == letter_2_position[1]:
            result += grid[(letter_1_position[0] - 1) % 5][letter_1_position[1]]
            result += grid[(letter_2_position[0] - 1) % 5][letter_2_position[1]]

        #If the letters are in the same row (modulo 5 to account for wrap around to the right if position[col] < 0)
        elif letter_1_position[0] == letter_2_position[0]:
            result += grid[letter_1_position[0]][(letter_1_position[1] - 1) % 5]
            result += grid[letter_2_position[0]][(letter_2_position[1] - 1) % 5]

        #If the letters are in different rows and columns create a rectangle, taking the values of horizontal opposite corners
        else:
            result += grid[letter_1_position[0]][letter_2_position[1]]
            result += grid[letter_2_position[0]][letter_1_position[1]]

    #Return the decrypted message without any X's or spaces
    return result.replace("X", "").replace(" ","")



#Testing the decryption function with the given key and message
key = "SUPERSPY"
message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
grid = generate_playfair_grid(key)
decrypted_message = decrypt_playfair(message, grid)
print(decrypted_message)