# Bi Yi Huang


#Create 5x5 Playfair grid - fill with unique characters from the key followed by the alphabet (omitting J)
def create_grid(key)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = key.upcase.gsub("J", "I").chars.uniq.join
    key += (alphabet.chars-key.chars).join
   
    grid = key.chars.each_slice(5).to_a
    return grid
end
   
#Process each charater in encrypted message to form pairs
def pre_process(message)
    message = message.upcase.gsub("J", "I").chars
    pairs = []
    i = 0
   
    while i < message.length
        
        #If Last character, pair it with X
        if i == message.length-1
            pairs << [message[i], "X"]
            break
        end
        
        #If the two characters are the same, insert X between 
        if message[i] == message[i+1]
            pairs << [message[i], "X"]
            
        #If the two characters are different, both characters become pairs
        else
            pairs << [message[i], message[i+1]]
            i+=1 
        end
        i+=1
    end
    pairs
end
   
#Find the position of the letter in the grid (Check from rows then column)
def position(grid, letter)

    row = grid.index {|r| r.include?(letter)}
    return nil unless row
    col = grid[row].index(letter)
    return row, col
end

#Ensures row index wraps within grid's boundary
def wrap_around_row(grid,row,col)
    return row % 5
end
   
#Ensures column index wraps within grid's boundary
def wrap_around_col(grid, row, col)
    return col % 5
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

    if row1 == row2  #if both letters are in the same row, shift left
        return [grid[row1][wrap_around_col(grid, row1, col1-1)], 
        grid[row2][wrap_around_col(grid,row2,col2-1)]]
    

    elsif col1 == col2 #if both letters are in the same column, shift up
        return [grid[wrap_around_row(grid,row1-1, col1)][col1],
        grid[wrap_around_row(grid,row2-1, col2)][col2]]
    else
        #If both characters different rows and columns, swap them
        return [grid[row1][col2], grid[row2][col1]]
    end
end

#Decrypt entire messsage
def decryption(message,key)
    grid = create_grid(key)
    pairs = pre_process(message)
    decrypted_pairs = pairs.map{|pair| decrypt_pair(grid, pair)}

    #Combine into string and remove the filler character 'X'
    decrypted_message = decrypted_pairs.flatten.join.gsub(/X(?=[A-Z]{2}|$)/, '')

    return decrypted_message
end

#test case
def test_case
    encrypted_messages = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"
    decrypted_message = decryption(encrypted_messages, key)
    puts decrypted_message
end


#Output message on the command line
if __FILE__ == $0
    test_case
end
