class PlayfairCipher
  def initialize(keyword)
    @grid = generate_grid(keyword)
  end

  def decrypt(ciphertext)
    plaintext_pairs = prepare_text(ciphertext).each_slice(2).map { |a, b| decode_pair(a, b) }
    handle_padding(plaintext_pairs).join
  end

  private

  def generate_grid(keyword)
    unique_letters = keyword.upcase.chars.uniq.join.delete("J") + ('A'..'Z').to_a.join.delete("J")
    unique_letters.chars.uniq.join.chars.each_slice(5).to_a
  end

  def prepare_text(text)
    text.upcase.gsub(/J/, 'I').gsub(/[^A-Z]/, '').chars
  end

  def find_position(letter)
    @grid.each_with_index do |row, row_idx|
      col_idx = row.index(letter)
      return [row_idx, col_idx] if col_idx
    end
  end

  def decode_pair(a, b)
    a_pos = find_position(a)
    b_pos = find_position(b)
    transform_pair(a_pos, b_pos)
  end

  def transform_pair(a_pos, b_pos)
    if a_pos[0] == b_pos[0]  # same row
      row = @grid[a_pos[0]]
      [row[(a_pos[1] - 1) % 5], row[(b_pos[1] - 1) % 5]]
    elsif a_pos[1] == b_pos[1]  # same column
      [ @grid[(a_pos[0] - 1) % 5][a_pos[1]],
        @grid[(b_pos[0] - 1) % 5][b_pos[1]] ]
    else  # rectangle
      [ @grid[a_pos[0]][b_pos[1]],
        @grid[b_pos[0]][a_pos[1]] ]
    end.join
  end

  def handle_padding(pairs)
    adjusted_text = []
    pairs.each_with_index do |pair, index|
      if pair[-1] == 'X' && (index < pairs.size - 1 && pair[0] == pairs[index + 1][0])
        pair = pair[0]  # Remove the 'X' when it's used as padding within repeating characters
      elsif pair[-1] == 'X' && index == pairs.size - 1
        pair = pair[0]  # Remove trailing 'X' if it's at the end of the message
      end
      adjusted_text << pair
    end
    adjusted_text
  end
end

cipher = PlayfairCipher.new("SUPERSPY")
ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
decrypted_text = cipher.decrypt(ciphertext)

puts decrypted_text

