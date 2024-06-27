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
