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

    unique
end





outp = matrix_generator("SUPERSPY")
puts outp