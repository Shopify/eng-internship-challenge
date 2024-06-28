# Playfair Cipher Thought Process

## Ruby Instructions

- Ensure your code can run in the command-line with the command `ruby solution.rb`

## Introduction

This repository contains implementations of the Playfair cipher in Ruby. The Playfair cipher is a polygraphic substitution cipher that encrypts pairs of letters instead of single letters at a time.


---

## Grid Creation Possible Version and Why We Chose a Set-based Implementation

### Version 1: Array-based Implementation

#### Version 1: Array-based Playfair Cipher Implementation

```ruby
def create_playfair_grid_v1(keyword)
  keyword = keyword.upcase.gsub(/[^A-Z]/, '')  # Convert keyword to uppercase and remove non-alphabetic characters

  # Determine alphabet based on keyword containing 'J' or not
  if keyword.include?('J')
    alphabet = ("A".."Z").to_a - ["I"]  # Exclude 'I' if keyword contains 'J'
  else
    alphabet = ("A".."Z").to_a - ["J"]  # Exclude 'J' if keyword does not contain 'J'
  end

  grid = []
  used_letters = []

  # Add keyword letters to the grid
  keyword.each_char do |char|
    next if used_letters.include?(char)  # Skip if letter is already used
    grid << char
    used_letters << char
  end

  # Add remaining alphabet letters to the grid
  alphabet.each do |char|
    next if used_letters.include?(char)  # Skip if letter is already used
    grid << char
    used_letters << char
  end

  # Convert the flat array into a 5x5 grid
  playfair_grid = []
  5.times { playfair_grid << grid.shift(5) }
  playfair_grid
end
```

### Version 2: Set-based Implementation

#### Version 2: Set-based Playfair Cipher Implementation

```ruby
require 'set'

# Method to create the Playfair cipher grid based on a keyword
def create_playfair_grid(keyword)
  keyword = keyword.upcase.gsub(/[^A-Z]/, '')  # Convert keyword to uppercase and remove non-alphabetic characters

  # Determine alphabet based on keyword containing 'J' or not
  if keyword.include?('J')
    alphabet = ("A".."Z").to_a - ["I"]  # Exclude 'I' if keyword contains 'J'
  else
    alphabet = ("A".."Z").to_a - ["J"]  # Exclude 'J' if keyword does not contain 'J'
  end

  used_letters = Set.new(keyword.chars + alphabet)  # Combine keyword and alphabet into a set
  grid = used_letters.to_a.each_slice(5).to_a  # Convert set to array and then slice into 5x5 grid

  grid  # Return the constructed Playfair grid
end
```

### Why Set-based Implementation Was Chosen

The set-based implementation was chosen for the following reasons:

- **Efficiency in Element Access:** Sets offer average O(1) time complexity for lookups, inserts, and deletions. This efficiency is crucial for operations involving checking and adding letters to the Playfair grid.
  
- **Simplicity and Readability:** Using a set simplifies the code and improves readability. It clearly expresses the intent of tracking used letters and ensures that each letter is added only once.
  
- **Alignment with Shopify Coding Values:** Shopify emphasizes code clarity, efficiency, and maintainability. The set-based approach aligns with these values by reducing unnecessary complexity and ensuring optimal performance for letter operations in the Playfair cipher.

### Why Array-based Implementation Was Not Chosen

The array-based implementation, though feasible, was not chosen primarily due to the following reasons:

- **Higher Time Complexity:** Arrays require linear time complexity O(n) for certain operations like searching or checking if an element exists. This could potentially lead to slower performance when handling large datasets or frequent letter operations.
  
- **Potential for Duplicate Entries:** Arrays may require additional logic to ensure that each letter is added only once, increasing complexity and potentially introducing bugs related to duplicate entries.
  
- **Less Readable Code:** Managing arrays for unique letter tracking and grid construction can make the code less readable compared to using a set, where the intent of letter uniqueness and grid formation is clearer.

---

## Playfair Cipher Decryption and Text Reassembly Methods

In our implementation of the Playfair cipher, several key methods are utilized to decrypt ciphertext and reassemble plaintext. Here’s an explanation of each method and why we implemented them this way, along with considerations for their performance and functionality.

### Method to Find Position of a Character in the Grid (`find_position`)

```ruby
def find_position(grid, char)
  grid.each_with_index do |row, i|
    j = row.index(char)
    return [i, j] if j  # Return the position [row, column] if character is found in the grid
  end
  nil  # Return nil if character is not found in the grid
end
```

**Explanation:**
- **Grid Search:** This method iterates over each row in the Playfair cipher grid to find the position (row, column) of a specified character.
- **Return Value:** It returns the position as an array `[row, column]` if the character is found in the grid, or `nil` if the character is not present.
- **Performance Considerations:** The method performs a linear search within each row of the grid, making it efficient for a small-sized grid like the Playfair cipher (typically 5x5).
- **Why This Approach:** This approach is straightforward and directly implements the search logic needed to locate characters within the Playfair cipher grid.

### Method to Decrypt a Digraph (`decrypt_digraph`)

```ruby
def decrypt_digraph(grid, digraph)
  a, b = digraph.map { |char| find_position(grid, char) }  # Find positions of characters in the grid
  ai, aj = a
  bi, bj = b

  if ai == bi
    [grid[ai][(aj - 1) % 5], grid[bi][(bj - 1) % 5]]  # Characters in the same row
  elsif aj == bj
    [grid[(ai - 1) % 5][aj], grid[(bi - 1) % 5][bj]]  # Characters in the same column
  else
    [grid[ai][bj], grid[bi][aj]]  # Characters in different rows and columns
  end
end
```

**Explanation:**
- **Grid Lookup:** The method starts by mapping each character in the digraph to its position (row, column) in the Playfair cipher grid using the `find_position` method.
- **Decryption Logic:** Based on the positions (`a` and `b`), it determines the decryption logic:
  - If both characters are in the same row, it shifts each character leftward (cyclically within the row).
  - If both characters are in the same column, it shifts each character upward (cyclically within the column).
  - If the characters are in different rows and columns, it swaps them diagonally.
- **Performance Considerations:** The `find_position` method runs in O(1) time for each character, making the decryption operation efficient.
- **Why This Approach:** This approach is chosen for its clarity in handling the three possible cases of character positions efficiently.

### Method to Reassemble Text After Decryption (`reassemble_text`)

```ruby
def reassemble_text(digraphs, original_grid)
  text = digraphs.join  # Combine digraphs into a single string

  # Remove padding 'X' that were added during preparation
  cleaned_text = ""
  i = 0
  while i < text.length
    if i < text.length - 1 && text[i] == text[i + 1] && text[i + 1] == 'X'
      cleaned_text << text[i]
      i += 1
    elsif i < text.length - 1 && text[i + 1] == 'X'
      cleaned_text << text[i]
      i += 2
    else
      cleaned_text << text[i]
      i += 1
    end
  end

  # If the original grid doesn't contain 'J', convert 'I' back to 'J' if the original message had 'J'
  if original_grid.flatten.include?('J')
    cleaned_text = cleaned_text.gsub('I', 'J')
  end

  cleaned_text  # Return the cleaned-up text
end
```

**Explanation:**
- **Text Cleanup:** This method takes an array of digraphs (pairs of characters) and reassembles them into a single string of plaintext.
- **Handling 'X' Padding:** During encryption, 'X' is added as padding to handle certain cases (like consecutive identical characters). This method removes unnecessary 'X' characters.
- **Restoring 'I' and 'J':** In the Playfair cipher, 'I' and 'J' are treated interchangeably. If the original grid used for encryption contained 'J', this method replaces 'I' back with 'J' to restore the original plaintext.
- **Performance Considerations:** The method efficiently removes padding 'X' characters and performs a single pass through the text, ensuring optimal performance.
- **Why This Approach:** This method ensures that the decrypted plaintext is clean and readable by removing unnecessary 'X' characters added during encryption.

---

## Encryption Functions for Fun 

### Playfair Cipher Encryption Methods

In our Playfair cipher implementation, we utilize several key methods for encrypting plaintext into ciphertext. Here’s an explanation of each method and why we chose to implement them this way.

#### Method to Prepare Text for Encryption (`prepare_text`)

```ruby
#

 Method to prepare text for encryption
def prepare_text(text, grid)
  text = text.upcase.gsub(/[^A-Z]/, '')  # Convert text to uppercase and remove non-alphabetic characters
  text = text.gsub('J', 'I') unless grid.flatten.include?('J')  # Replace 'J' with 'I' if grid does not contain 'J'

  digraphs = []  # Array to store digraphs
  i = 0  # Initialize index for iterating over the text
  
  # Add padding 'X' if needed and store digraph pairs in digraphs
  while i < text.length
    a = text[i]
    b = text[i + 1]

    if b.nil?
      digraphs << [a, 'X']  # If only one character left, pad with 'X'
      break
    elsif a == b
      digraphs << [a, 'X']  # If consecutive characters are the same, pad with 'X'
      i += 1
    else
      digraphs << [a, b]  # Create digraph pairs
      i += 2
    end
  end

  digraphs  # Return the array of digraphs
end
```

#### Method to Encrypt a Digraph (`encrypt_digraph`)

```ruby
# Method to encrypt a digraph using the Playfair cipher grid
def encrypt_digraph(grid, digraph)
  a, b = digraph.map { |char| find_position(grid, char) }  # Find positions of characters in the grid
  ai, aj = a
  bi, bj = b

  if ai == bi
    [grid[ai][(aj + 1) % 5], grid[bi][(bj + 1) % 5]]  # Characters in the same row
  elsif aj == bj
    [grid[(ai + 1) % 5][aj], grid[(bi + 1) % 5][bj]]  # Characters in the same column
  else
    [grid[ai][bj], grid[bi][aj]]  # Characters in different rows and columns
  end
end
```

## Conclusion

These methods (`create_playfair_grid`,`prepare_text`, `encrypt_digraph`, `decrypt_digraph`, `reassemble_text`, and `find_position`) collectively form the backbone of our Playfair cipher implementation. They are designed to handle encryption and decryption tasks efficiently, ensuring secure communications by adhering to Playfair cipher rules and maintaining clarity in code structure.
