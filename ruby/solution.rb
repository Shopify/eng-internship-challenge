require 'set'

# Method to create the Playfair cipher grid based on a keyword
def create_playfair_grid(keyword)
  keyword = keyword.upcase.gsub(/[^A-Z]/, '')  # Convert keyword to uppercase and remove non-alphabetic characters

  # Determine alphabet based on keyword containing 'J' or not
  if keyword.include?('J')
    alphabet = ("A".."Z").to_a - ["I"]  # Exclude 'I' if keyword contains 'J'
  else
    alphabet = ("A".."Z").to_a - ["J"]  # Exclude 'J' if keyword does not contain 'J'
  end

  used_letters = Set.new(keyword.chars + alphabet)  # Combine keyword and alphabet into a set
  grid = used_letters.to_a.each_slice(5).to_a  # Convert set to array and then slice into 5x5 grid

  grid  # Return the constructed Playfair grid
end

# Define find_position method to find the position of a character in the grid
def find_position(grid, char)
  grid.each_with_index do |row, i|
    j = row.index(char)
    return [i, j] if j  # Return the position [row, column] if character is found in the grid
  end
  nil  # Return nil if character is not found in the grid
end

# Method to decrypt a digraph using the Playfair cipher grid
def decrypt_digraph(grid, digraph)
  a, b = digraph.map { |char| find_position(grid, char) }  # Find positions of characters in the grid
  ai, aj = a
  bi, bj = b

  if ai == bi
    [grid[ai][(aj - 1) % 5], grid[bi][(bj - 1) % 5]]  # Characters in the same row
  elsif aj == bj
    [grid[(ai - 1) % 5][aj], grid[(bi - 1) % 5][bj]]  # Characters in the same column
  else
    [grid[ai][bj], grid[bi][aj]]  # Characters in different rows and columns
  end
end

# Method to reassemble text after decryption
def reassemble_text(digraphs, original_grid)
  text = digraphs.join  # Combine digraphs into a single string

  # Remove padding 'X' that were added during preparation
  cleaned_text = ""
  i = 0
  while i < text.length
    if i < text.length - 1 && text[i] == text[i + 1] && text[i + 1] == 'X'
      cleaned_text << text[i]
      i += 1
    elsif i < text.length - 1 && text[i + 1] == 'X'
      cleaned_text << text[i]
      i += 2
    else
      cleaned_text << text[i]
      i += 1
    end
  end

  # If the original grid doesn't contain 'J', convert 'I' back to 'J' if the original message had 'J'
  if original_grid.flatten.include?('J')
    cleaned_text = cleaned_text.gsub('I', 'J')
  end

  cleaned_text  # Return the cleaned-up text
end

# Method to decrypt text using the Playfair cipher
def decrypt_text(grid, text)
  digraphs = text.scan(/../)  # Split text into digraphs of two characters each
  decrypted_digraphs = digraphs.map { |digraph| decrypt_digraph(grid, digraph.chars) }  # Decrypt each digraph
  reassemble_text(decrypted_digraphs, grid)  # Reassemble decrypted digraphs into the original text
end

# Usage of the Playfair cipher implementation
keyword = "SUPERSPY"
grid = create_playfair_grid(keyword) 
encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
decrypted_message = decrypt_text(grid, encrypted_message)
puts "#{decrypted_message}"
