# Program to decrypt Playfair cipher message
# Mihir Kachroo

encryptedMessage = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'
key = 'SUPERSPY'

def generateKeyTable(key)
  # Flatten key table
  flatKeyTable = []
  key = key.upcase

  # Add each unique key to key table
  key.each_char do |char|
    flatKeyTable << char unless flatKeyTable.include?(char)
  end

  # Go over remaining letters
  (65..90).each do |i|
    # Insert I since both in key tbale
    if i.chr == 'I' || i.chr == 'J'
      flatKeyTable << 'I' if !flatKeyTable.include?('I') && !flatKeyTable.include?('J')
      next
    end
    # Insert character
    flatKeyTable << i.chr unless flatKeyTable.include?(i.chr)
  end

  # Create 5x5 key table form flattened
  keyTable = []
  (0..20).step(5) do |i|
    keyTable << flatKeyTable[i, 5]
  end
  keyTable
end

# Find if char in keyTable
def findInKeyTable(keyTable, char)
  keyTable.each_with_index do |row, i|
    row.each_with_index do |val, j|
      return [i, j] if val == char
    end
  end
  [-1, -1]
end

# Decrypts ciphertext using the keyword and returns it
def decryptMessage(encryptedMessage, key)
  decryptedMessage = ''
  # Input strings are processed to ensure consistency
  keyTable = generateKeyTable(key)
  encryptedMessage = encryptedMessage.upcase

  # Iterates over ciphertext in pairs of letters
  (0...encryptedMessage.length).step(2) do |i|
    char1 = encryptedMessage[i]
    char2 = encryptedMessage[i + 1]
    row1, col1 = findInKeyTable(keyTable, char1)
    row2, col2 = findInKeyTable(keyTable, char2)

    # Two characters in same row
    if row1 == row2
      decryptedMessage += keyTable[row1][(col1 - 1) % 5]
      decryptedMessage += keyTable[row2][(col2 - 1) % 5]
    # Two characters in same column
    elsif col1 == col2
      decryptedMessage += keyTable[(row1 - 1) % 5][col1]
      decryptedMessage += keyTable[(row2 - 1) % 5][col2]
    # Two characters in different row and column
    else
      decryptedMessage += keyTable[row1][col2]
      decryptedMessage += keyTable[row2][col1]
    end
  end

  # Remove filler
  decryptedMessage.delete('X')
end

puts decryptMessage(encryptedMessage, key)
