class PlayfairCipher
    def initialize(key)
      # Process the key to remove duplicates and replace 'J' with 'I'
      @key = process_key(key)
      # Generate the 5x5 matrix using the processed key
      @matrix = generate_matrix(@key)
    end
  
    def process_key(key)
      # Convert key to uppercase, replace 'J' with 'I', remove duplicates
      key.upcase.gsub('J', 'I').chars.uniq.join
    end
  
    def generate_matrix(key)
      # Generate the alphabet excluding 'J'
      alphabet = ("A".."Z").to_a - ["J"]
      # Create the key character array
      key_chars = key.chars
      # Get the remaining characters from the alphabet
      remaining_chars = alphabet - key_chars
      # Combine key characters and remaining characters, then split into 5x5 matrix
      (key_chars + remaining_chars).each_slice(5).to_a
    end
  
    def preprocess_text(text)
      # Convert text to uppercase and replace 'J' with 'I'
      text = text.upcase.gsub('J', 'I')
      processed_text = ""
      i = 0
      while i < text.length
        if i == text.length - 1
          # If only one character is left, append 'X' to it
          processed_text += text[i] + 'X'
          i += 1
        elsif text[i] == text[i + 1]
          # If two consecutive characters are the same, append 'X' between them
          processed_text += text[i] + 'X'
          i += 1
        else
          # Otherwise, take the pair of characters
          processed_text += text[i] + text[i + 1]
          i += 2
        end
      end
      # Split the processed text into pairs of characters
      processed_text.scan(/../)
    end
  
    def find_position(char)
      # Find the position of the character in the matrix
      @matrix.each_with_index do |row, i|
        j = row.index(char)
        return [i, j] if j
      end
      nil
    end
  
    def decrypt_pair(pair)
      # Get positions of the two characters in the pair
      r1, c1 = find_position(pair[0])
      r2, c2 = find_position(pair[1])
      
      if r1 == r2
        # If characters are in the same row, shift left
        @matrix[r1][(c1 - 1) % 5] + @matrix[r2][(c2 - 1) % 5]
      elsif c1 == c2
        # If characters are in the same column, shift up
        @matrix[(r1 - 1) % 5][c1] + @matrix[(r2 - 1) % 5][c2]
      else
        # If characters form a rectangle, swap columns
        @matrix[r1][c2] + @matrix[r2][c1]
      end
    end
  
    def decrypt(ciphertext)
      # Preprocess the ciphertext into pairs
      pairs = preprocess_text(ciphertext)
      # Decrypt each pair and join the results
      decrypted_text = pairs.map { |pair| decrypt_pair(pair) }.join
      # Remove 'X' used for padding
      decrypted_text.gsub('X', '')
    end
  end
  
  if __FILE__ == $0
    # Create a new PlayfairCipher instance with the key "SUPERSPY"
    cipher = PlayfairCipher.new("SUPERSPY")
    # Define the encrypted message
    encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    # Decrypt the encrypted message
    decrypted_message = cipher.decrypt(encrypted_message)
    # Output the decrypted message
    puts decrypted_message
  end
  