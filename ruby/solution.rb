def create_playfair_key_matrix(key)
    filtered_key = key.upcase.gsub(/[^A-Z]/, '')
    unique_characters = {}
    key_without_duplicates = ''
    
    filtered_key.each_char do |char|
      unless unique_characters.include?(char)
        unique_characters[char] = true
        key_without_duplicates += char
      end
    end
    
    remaining_letters = ('A'..'Z').to_a.reject { |char| char == 'J' || unique_characters.include?(char) }
    complete_key = key_without_duplicates + remaining_letters.join
    key_matrix = []
    
    complete_key.chars.each_slice(5) { |slice| key_matrix << slice }
    key_matrix
  end
  
  def decrypt_message_with_playfair(cipher_text, secret_key)
    key_matrix = create_playfair_key_matrix(secret_key)
    plain_text = ""
    digraphs = cipher_text.scan(/../)
  
    digraphs.each do |letter_pair|
      first_letter = letter_pair[0]
      second_letter = letter_pair[1]
      flat_key_matrix = key_matrix.flatten
      position1 = flat_key_matrix.index(first_letter)
      position2 = flat_key_matrix.index(second_letter)
      row1, column1 = position1 / 5, position1 % 5
      row2, column2 = position2 / 5, position2 % 5
  
      if row1 == row2
        shifted_column1 = (column1 - 1) % 5
        shifted_column2 = (column2 - 1) % 5
        plain_text += key_matrix[row1][shifted_column1] + key_matrix[row2][shifted_column2]
      elsif column1 == column2
        shifted_row1 = (row1 - 1) % 5
        shifted_row2 = (row2 - 1) % 5
        plain_text += key_matrix[shifted_row1][column1] + key_matrix[shifted_row2][column2]
      else
        plain_text += key_matrix[row1][column2] + key_matrix[row2][column1]
      end
    end
  
    plain_text.gsub('X', '')
  end
  
  cipher_text = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
  secret_key = "SUPERSPY"
  decrypted_text = decrypt_message_with_playfair(cipher_text, secret_key)
  puts decrypted_text
  