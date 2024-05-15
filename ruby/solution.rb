# creates the playfair matrix/table
def create_matrix(key)
  key.upcase.gsub(/[^A-Z]/, '').chars.uniq.join
  alphabet = ('A'..'Z').to_a - ['J']
  (key.chars + alphabet).uniq.each_slice(5).to_a
end

# gets the row & column indexes of chars in digraph
def get_rowcol(letter, matrix)
  matrix.each_with_index do |row, i|
    j = row.index(letter)
    return [i, j] if j
  end
end

def decrypt(cipher, key)
  matrix = create_matrix(key)
  decrypted_text = ''
  digraphs = cipher.each_char.each_slice(2).to_a

  digraphs.each do |digraph|
    row1, col1 = get_rowcol(digraph[0], matrix)
    row2, col2 = get_rowcol(digraph[1], matrix)

    if row1 == row2
      decrypted_text << matrix[row1][(col1 - 1) % 5]
      decrypted_text << matrix[row2][(col2 - 1) % 5]
    elsif col1 == col2
      decrypted_text << matrix[(row1 - 1) % 5][col1]
      decrypted_text << matrix[(row2 - 1) % 5][col2]
    else
      decrypted_text << matrix[row1][col2]
      decrypted_text << matrix[row2][col1]
    end
  end
  decrypted_text = decrypted_text.gsub('X', '')
end

cipher = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'
key = 'SUPERSPY'
decryption = decrypt(cipher, key)
puts decryption
