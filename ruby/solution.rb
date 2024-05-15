# Generate a 5x5 matrix for the Playfair cipher based on the given key
#
# @param key [String] The key to generate the matrix
# @return [Array<Array<String>>] A 5x5 matrix
def matrix_generator(key)
    key = key.upcase
    unique = ""
    seen = []       # since there are only 25 alphabets, looping through "seen" is always O(1) 

    # Remove duplicate characters from the key and handle 'J' (Traditionally combined with 'I')
    key.each_char do |char|
        next if seen.include?(char)
        char = 'I' if char == 'J'
        seen << char
        unique += char
    end

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    # Fill the remaining characters of the matrix with the alphabet not seen in key
    alphabet.each_char do |char|
        next if seen.include?(char)
        unique += char
    end

    matrix = []

    # Split the unique characters into rows of the matrix
    (0...25).step(5) do |i|
        matrix << unique[i, 5]
    end

    matrix
end

def decrypt_playfair(text, matrix)
    # TODO:
    # -- check length and add letter if necessary
    # -- create hashtable to store position of each letter in matrix. this will make it faster than iterating through the matrix each time
    # -- split ciphertext into pairs of 2
    # -- iterate over each pair, and apply the rules of playfair cipher using the matrix. store the plaintext it in a result variable
    # -- remove "X" if seen in the result and return the decrypted text.

    # Check if the length of the text is odd and append 'X' if necessary
    text += 'X' if text.length.odd?

    position = {}

    # Create a hash table to store the positions of characters in the matrix
    matrix.each_with_index do |row, i|
        row.each_char.with_index do |ch, j|
            position[ch] = [i, j]
        end
    end

    res = []
    pairs = text.chars.each_slice(2).map(&:join)
    

    pairs.each do |pair|
        a, b = pair.chars
        row_a, col_a = position[a]
        row_b, col_b = position[b]
        # puts "#{a}: #{row_a}, #{col_a}; #{b}: #{row_b}, #{col_b}"    

        if row_a == row_b
            new_a = matrix[row_a][(col_a - 1) % 5]
            new_b = matrix[row_b][(col_b - 1) % 5]
        elsif col_a == col_b
            new_a = matrix[(row_a - 1) % 5][col_a]
            new_b = matrix[(row_b - 1) % 5][col_b]
        else
            new_a = matrix[row_a][col_b]
            new_b = matrix[row_b][col_a]
        end

        res << new_a << new_b
    end

    decrypted_text = res.reject { |char| char == 'X' }.join
end

matrix = matrix_generator("SUPERSPY")
encrypted_text = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
answer = decrypt_playfair(encrypted_text, matrix)
puts answer

