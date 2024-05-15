class PlayfairCypherDecoder
  def initialize(cypher_text, key)
    @cypher_text = cypher_text
    @key = key
  end
  
  def decode
    decoded_array = decoded_bigrams.map do |decoded_bigram|
      matrix[decoded_bigram[0]] + matrix[decoded_bigram[1]]
    end

    decoded_array.join("").upcase.gsub(/[^A-Z]/, "").gsub(/X/, "")
  end 	

  private

  def decoded_bigrams
    @cypher_text.chars.each_slice(2).map do |letters|
      first_letter_index = matrix.index(letters[0])
      second_letter_index = matrix.index(letters[1])

      first_letter_row = (first_letter_index/5).to_i
      second_letter_row = (second_letter_index/5).to_i

      first_letter_column = first_letter_index % 5
      second_letter_column = second_letter_index % 5

      new_index = []

      if  first_letter_row == second_letter_row
        new_index << ((first_letter_index - first_letter_row * 5) - 1) % 5 + first_letter_row * 5
        new_index << ((second_letter_index - second_letter_row * 5) - 1) % 5 + second_letter_row * 5
      elsif first_letter_column == second_letter_column
        new_index << (first_letter_column - 5) % 25
        new_index << (second_letter_column - 5) % 25
      else
        new_index << first_letter_index + second_letter_column - first_letter_column
        new_index << second_letter_index + first_letter_column - second_letter_column
      end

      new_index

    end
  end

  def matrix
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    concat_matrix = @key + alphabet
    concat_matrix.split("").uniq.join("")
  end
end

puts PlayfairCypherDecoder.new("IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV", "SUPERSPY").decode
