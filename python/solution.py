from textwrap import *

message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
key = "SUPERSPY"

##def print_grid(grid):
##    for i in range(25):
##        if i % 5 == 0:
##            print("")
##        print(grid[i], end="")
##    print("")

def create_grid(key, omit=""): 
    result = "".join(dict.fromkeys(omit + key)) # removes duplicates by generating a dictionary
    count = 0                                   # then join all of the keys together to form a new string
                                                # omit is added first to be removed later
    while len(result) < 25 + len(omit):
        result = "".join(dict.fromkeys(result + chr(ord("A") + count))) # increment alphabetically, and it skips existing letters for meeeee
        count += 1
        
    return result[len(omit):]       # let's get rid of the stuff we wanted to omit

new_grid = create_grid(key, "J")    # generate my grid!
split_message = wrap(message, 2)    # split my encrypted message into pairs
solution = ""                       # for the final solution

while(len(split_message) > 0):
    pair = split_message.pop(0)
    
    if new_grid.index(pair[0]) // 5 == new_grid.index(pair[1]) // 5: # case 1, they're in the same row
        offset = new_grid.index(pair[0]) // 5 * 5   # gives me my row offset value
        
        solution += ( # string append
            new_grid[offset + (new_grid.index(pair[0]) - 1) % 5] +  # move 1 to the left, modulus helps me wrap around
            new_grid[offset + (new_grid.index(pair[1]) - 1) % 5]    # second character
            )
        
    elif new_grid.index(pair[0]) % 5 == new_grid.index(pair[1]) % 5: # case two, they're in the same column
        offset = new_grid.index(pair[0]) % 5 # gives me my column offset value
        
        solution += (
            new_grid[offset + (new_grid.index(pair[0] // 5 - 1)) % 5 * 5] + # move 1 upwards, so 5 index positions, modulus wrap
            new_grid[offset + (new_grid.index(pair[1] // 5 - 1)) % 5 * 5]   # and then column offset gets added last, thanks BEDMAS
            )

    else: # case 3, box!
        x0 = new_grid.index(pair[0]) % 5 
        y0 = new_grid.index(pair[0]) // 5 * 5
        x1 = new_grid.index(pair[1]) % 5 
        y1 = new_grid.index(pair[1]) // 5 * 5

        solution += (new_grid[y0 + x1] + new_grid[y1 + x0]) # swapping columns of the characters, making the box!
        
[print(i, end="") for i in solution if i != "X" and i.isalpha()] # prints, omitting X and making sure it's in the alphabet 
