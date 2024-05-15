# frozen_string_literal: true
#Algorithm to decode a message using the Playfair cipher.
SPECIAL_CHARACTERS = ",./;'[]\-=`~!@#$%^&*()_+{}|:<>?" # These characters should not appear in our message.
ALPHABET = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' # J is omitted so 25 letters can be represented in a 5x5 grid.
MESSAGE = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV' # The message that needs to be decrypted.
KEY = 'SUPERSPY' # The key used to help decrypt the message.

def main
  # Tests the program.
  decrypted_message = decode_message(MESSAGE, KEY)
  print decrypted_message
end

def decode_message(message, key)
  # Check if the message and key contain special characters.
  result = special_character_check(message, key)

  return unless result

  # If the length is odd, add an X to the end of the message.
  message += 'X' if message.length.odd?

  # Remove spaces, replaces J with I and converts to uppercase.
  message = message.gsub('J', 'I').gsub(' ', '').upcase
  key = key.gsub('J', 'I').gsub(' ', '').upcase

  # Generates the grid.
  grid = generate_grid(key)

  # Decode the message.
  decoded_message = ''
  (0..message.length - 1).step(2).each do |i|
    first_letter = message[i]
    second_letter = message[i + 1]

    # Sets the second letter to X if both letters are the same.
    second_letter = 'X' if first_letter == second_letter

    # Gets the location of the letters in the grid.
    first_letter_location = get_letter_location(grid, first_letter)
    second_letter_location = get_letter_location(grid, second_letter)

    # When letters are in the same row, swap with the letter to the left. Modulo 5 is used when there is no left letter.
    if first_letter_location[0] == second_letter_location[0]

      decoded_message += grid[first_letter_location[0]][(first_letter_location[1] - 1) % 5]
      decoded_message += grid[second_letter_location[0]][(second_letter_location[1] - 1) % 5]

    # When letters are in the same column, swap with the letter above. Modulo 5 is used when there is no letter above.
    elsif first_letter_location[1] == second_letter_location[1]

      decoded_message += grid[(first_letter_location[0] - 1) % 5][first_letter_location[1]]
      decoded_message += grid[(second_letter_location[0] - 1) % 5][second_letter_location[1]]

    # When letters are in different rows and columns, form a rectangle and swap with the opposite corners.
    else

      decoded_message += grid[first_letter_location[0]][second_letter_location[1]]
      decoded_message += grid[second_letter_location[0]][first_letter_location[1]]

    end
  end
  # Removes X's and spaces, then switches to uppercase.
  decoded_message = decoded_message.gsub('X', '').gsub(' ', '').upcase
end

def special_character_check(message, key)
  # Checks if the message and key contain special characters.
  message.each_char do |char|
    return false if SPECIAL_CHARACTERS.include?(char)
  end

  key.each_char do |char|
    return false if SPECIAL_CHARACTERS.include?(char)
  end
  true
end

def generate_grid(key)
  # Generates the grid.
  grid_letters = ''

  # If the letter in the key or alphabet isnt in the grid_letters, add it.
  key.each_char do |char|
    grid_letters += char unless grid_letters.include?(char)
  end

  ALPHABET.each_char do |char|
    grid_letters += char unless grid_letters.include?(char)
  end

  grid = Array.new(5) { Array.new(5) }

  # Adds the letters to the grid.
  counter = 0
  (0..4).each do |i|
    (0..4).each do |j|
      grid[i][j] = grid_letters[counter]
      counter += 1
    end
  end

  grid
end

def get_letter_location(grid, letter)
  # Gets the location of a letter in the grid and returns an 2 element array containing the row and column.
  (0..4).each do |i|
    (0..4).each do |j|
      return [i, j] if grid[i][j] == letter
    end
  end
  nil
end

main
