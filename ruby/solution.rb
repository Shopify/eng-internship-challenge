def generate_matrix(key)
    key = key.upcase.tr('J', 'I')  # Replace 'J' with 'I'
    key_and_letter = (key + "ABCDEFGHIKLMNOPQRSTUVWXYZ").chars.uniq.select { |char| char.match?(/[A-Z]/) }.join('')
  end
  
  def locate_character(char, matrix)
    index = matrix.index(char)
    [index / 5, index % 5]
  end
  
  def playfair_decrypt(ciphertext, key)
    matrix = generate_matrix(key)
    decrypted_text = ""
  
    (0...ciphertext.length).step(2) do |i|
      row1, col1 = locate_character(ciphertext[i], matrix)
      row2, col2 = locate_character(ciphertext[i + 1], matrix)
  
      if row1 == row2
        # If the characters are in the same row, shift left
        decrypted_text += matrix[row1 * 5 + (col1 - 1) % 5]
        decrypted_text += matrix[row2 * 5 + (col2 - 1) % 5]
      elsif col1 == col2
        # If the characters are in the same column, shift up
        decrypted_text += matrix[(row1 - 1) % 5 * 5 + col1]
        decrypted_text += matrix[(row2 - 1) % 5 * 5 + col2]
      else
        # If the characters form a rectangle, swap columns
        decrypted_text += matrix[row1 * 5 + col2]
        decrypted_text += matrix[row2 * 5 + col1]
      end
    end
  
    # Clean up the decrypted text by removing 'X' used as padding
    decrypted_text.tr("X", "")

  end
  
  if __FILE__ == $PROGRAM_NAME
    key = "SUPERSPY"
    encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    decrypted_message = playfair_decrypt(encrypted_message, key)
    puts decrypted_message
  end
  