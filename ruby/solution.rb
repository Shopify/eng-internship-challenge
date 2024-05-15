class PlayfairCypherDecoder
  # initialize playfair cypher decoder with cypher_text and key
  def initialize(cypher_text, key)
    @cypher_text = cypher_text
    @key = key
  end
  
  def decode
    # return an array of decoded bigrams
    decoded_array = decoded_bigrams.map do |decoded_bigram|
      matrix[decoded_bigram[0]] + matrix[decoded_bigram[1]]
    end
    
    # join the array, transforming it into an uppercase string, removing non-alphabetic characters and letter "X"
    decoded_array.join("").upcase.gsub(/[^A-Z]/, "").gsub(/X/, "")
  end 	

  private

  def decoded_bigrams
    # for each 2 letters in the cypher text, find the corresponding transform indexes
    @cypher_text.chars.each_slice(2).map do |letters|
      first_letter_index = matrix.index(letters[0])
      second_letter_index = matrix.index(letters[1])
      
      first_letter_row = (first_letter_index/5).to_i
      second_letter_row = (second_letter_index/5).to_i
      
      first_letter_column = first_letter_index % 5
      second_letter_column = second_letter_index % 5

      new_index = []
      
      # if the letters are in the same row find the corresponding transformed indexes in that row
      # normalize it to be the first row, find it's corresponding index and then move it back to it's original position
      
      if first_letter_row == second_letter_row
        new_index << ((first_letter_index - first_letter_row * 5) - 1) % 5 + first_letter_row * 5
        new_index << ((second_letter_index - second_letter_row * 5) - 1) % 5 + second_letter_row * 5
        
      # if the letters are in the same column find the corresponding transformed indexes in that column
      # go 5 positions back in the array, then grabs the mod of the length of the matrix.
        
      elsif first_letter_column == second_letter_column
        new_index << (first_letter_column - 5) % 25
        new_index << (second_letter_column - 5) % 25
        
      # if the letters are in a rectangle or square find the corresponding transformed indexes inside it
      # for both, first and second letter indexes, it sums up the difference of the columns
        
      else
        new_index << first_letter_index + second_letter_column - first_letter_column
        new_index << second_letter_index + first_letter_column - second_letter_column
      end

      new_index

    end
  end

  def matrix
    # create a variable that stores the alphabet without the letter "J"
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    concat_matrix = @key + alphabet
    # after concating the key and alphabet, remove duplicates
    concat_matrix.split("").uniq.join("")
  end
end

# calls the class and method to decode the cypher text
puts PlayfairCypherDecoder.new("IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV", "SUPERSPY").decode
