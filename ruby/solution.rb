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
    # plan:
    # check length and add letter if necessary
    # create hashtable to store position of each letter in matrix. this will make it faster than iterating through the matrix each time
    # split ciphertext into pairs of 2
    # iterate over each pair, and apply the rules of playfair cipher using the matrix. store the plaintext it in a result variable
    # remove "X" if seen in the result and return the decrypted text.
    
end




outp = matrix_generator("SUPERSPY")
puts outp