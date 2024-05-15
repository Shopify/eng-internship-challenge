# Generate a 5x5 matrix for the Playfair cipher based on the given key
#
# @param key [String] The key to generate the matrix
# @return [Array<Array<String>>] A 5x5 matrix
def matrix_generator(key)
    key = key.upcase
    unique = ""
    seen = []

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

# Decrypt a Playfair cipher
#
# @param text [String] The encrypted text
# @param matrix [Array<Array<String>>] The matrix used to encrypt the text
# @return [String] The decrypted text
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
    pairs = text.chars.each_slice(2).map(&:join)    # Split the text into pairs of characters   

    # Decrypt pairs of characters based on their positions in the matrix
    pairs.each do |pair|
        a, b = pair.chars
        row_a, col_a = position[a]
        row_b, col_b = position[b]

        if row_a == row_b
            # If the characters are in the same row, shift each character one position to the left within the same row.
            new_a = matrix[row_a][(col_a - 1) % 5]
            new_b = matrix[row_b][(col_b - 1) % 5]
        elsif col_a == col_b
            # If the characters are in the same column, shift each character one position up within the same column.
            new_a = matrix[(row_a - 1) % 5][col_a]
            new_b = matrix[(row_b - 1) % 5][col_b]
        else
            # If the characters form a rectangle, swap their columns while keeping their rows unchanged.
            new_a = matrix[row_a][col_b]
            new_b = matrix[row_b][col_a]
        end

        res << new_a << new_b
    end

    # Remove 'X' characters and join the decrypted characters
    decrypted_text = res.reject { |char| char == 'X' }.join
end

key = "SUPERSPY"
encrypted_text = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
matrix = matrix_generator(key)
answer = decrypt_playfair(encrypted_text, matrix)
puts answer
