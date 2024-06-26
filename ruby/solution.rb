# Bi Yi Huang


#Create and the fill the 5x5 Playfair grid (Treating all occurences of J as I)
def create_grid(key)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = key.upcase.gsub("J", "I").chars.uniq.join
    key += (alphabet.chars-key.chars).join
   
    grid = key.chars.each_slice(5).to_a
    return grid
end
   
   #Pre-process the encrypted message
   def pre_process(message)
    message = message.upcase.gsub("J", "I").chars.each_slice(2).to_a
   
    pairs = []
    i = 0
   
    while i < message.length
        
        #Last character - Insert X
        if i == message.length-1
            pairs << [message[i], "X"]
            break
        end
        
        #If the two characters are the same, insert X 
        if message[i] == message[i+1]
            pairs << [message[i], "X"]
            
        #If the two characters are different, insert both characters as pairs
        else
            pairs << [message[i], message[i+1]]
            i+=1
        end
        i+=1
    end
    pairs
end
   
#Find position of letter in the key square - if grid contains the letters searching from row then column
def position(grid, letter)

    #Printing grid for troubleshooting
    puts "Grid:"
    grid.each { |row| puts row.join(' ')}

    row = grid.index {|r| r.include?(letter)}
    return nil unless row
    col = grid[row].index(letter)
    return row, col
end
   
#Wrap index from beginning to end of the row when it gets shifted
def wrap_around_col(grid, row, col)
    return col % 5
end

def wrap_around_row(grid,row,col)
    return row % 5
end


#Decrypt each pairs of letters
def decrypt_pair(grid,pair)
    letter1, letter2 = pair
    row1, col1 = position(grid, letter1)
    row2, col2 = position(grid, letter2)

    #Check if either letter was found in the grid
    if row1.nil? || row2.nil?
        puts "Error: One or more of the letters in the pair #{pair} not found."
        return [nil, nil]
    end

    #if both letters are in the same row/col, shift each letter to either to the left or up
    if row1 == row2
        return [grid[row1][wrap_around_col(grid, row1, col1-1)], 
        grid[row2][wrap_around_col(grid,row2,col2-1)]]
    
    elsif col1 == col2
        return [grid[wrap_around_row(grid,row1-1, col1)][col1],
        grid[wrap_around_row(grid,row2-1, col2)][col2]]
    else
        #swap the letters
        return [grid[row1][col2], grid[row2][col1]]
    end
end

def decryption(message,key)
    grid = create_grid(key)
    pairs = pre_process(message)
    decrypted_pairs = pairs.map{|pair| decrypt_pair(grid, pairs)}

    #Combine into string
    decrypted_message = decrypted_pairs.flatten.join

    return decrypted_message
end

#test cases
def test_cases
    encrypted_messages = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"
    decrypted_message = decryption(encrypted_messages, key)
    puts decrypted_message
end

#Output message on the command line
if __FILE__ == $0
    test_cases
end
