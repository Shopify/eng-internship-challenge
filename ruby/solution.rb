# Create grid using key
def create_grid(key)
    grid = [[]]

    # Saves the coordinates of each letter
    coords_x = Array.new(26, 0)
    coords_y = Array.new(26, 0)

    # Add all letters excluding j into grid
    all_letters = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    # Add both strings together to create the order of letters to check
    letters_to_add = (key << all_letters).split("").uniq.select{ |letter| "A".ord <= letter.ord && letter.ord <= "Z".ord}

    # Fill in grid and coordinates
    letters_to_add.each do |letter|
        # Check if new row needed
        if grid.last.length == 5
            grid.push([])
        end
        # Push letter and save coordinate
        grid.last.push(letter)
        coords_x[letter.ord - "A".ord] = grid.last.length - 1
        coords_y[letter.ord - "A".ord] = grid.length - 1
    end

    [grid, coords_x, coords_y]
end


# Decrypt message using grid and coordinates of letters
def decrypt_message(encrypted_message, grid, coords_x, coords_y)
    # Remove any non uppercase characters and turn into a list
    message = encrypted_message.split("").select{ |letter| "A".ord <= letter.ord && letter.ord <= "Z".ord}
    
    # Perform the decryption on the string
    decryption = []
    i = 0
    loop do
        if i >= message.length
            break
        end

        # Same row
        if coords_y[message[i].ord - "A".ord] == coords_y[message[i + 1].ord - "A".ord]
            decryption.push(grid[coords_y[message[i].ord - "A".ord]][(coords_x[message[i].ord - "A".ord] + 4) % 5])
            decryption.push(grid[coords_y[message[i + 1].ord - "A".ord]][(coords_x[message[i + 1].ord - "A".ord] + 4) % 5])
        # Same column
        elsif coords_x[message[i].ord - "A".ord] == coords_x[message[i + 1].ord - "A".ord]
            decryption.push(grid[(coords_y[message[i].ord - "A".ord] + 4) % 5][coords_x[message[i].ord - "A".ord]])
            decryption.push(grid[(coords_y[message[i + 1].ord - "A".ord] + 4) % 5][coords_x[message[i + 1].ord - "A".ord]])
        # Rectangle case
        else
            decryption.push(grid[coords_y[message[i].ord - "A".ord]][coords_x[message[i + 1].ord - "A".ord]])
            decryption.push(grid[coords_y[message[i + 1].ord - "A".ord]][coords_x[message[i].ord - "A".ord]])
        end

        # Do not have to worry about odd lengths since encrypted strings have even length
        i = i + 2
    end

    # Remove X's and join together
    decryption.select{ |letter| letter != "X" }.join("")
end


key = "SUPERSPY"
encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

grid, coords_x, coords_y = create_grid(key)
decrypted_message = decrypt_message(encrypted_message, grid, coords_x, coords_y)

print decrypted_message
