# Python code to solve playfair cipher problem

# Function to generate the key square 
def generate_key_square(key):
    key = key.replace("J", "I")  # Replace J with I
    key_square = [] 
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J is omitted

    # Add the key to the key square
    for letter in key:
        if letter not in key_square:
            key_square.append(letter)

    # Add the remaining letters of the alphabet to the key square
    for letter in alphabet:
        if letter not in key_square:
            key_square.append(letter)

    # Reshape the key square to a 5x5 matrix
    key_square = [key_square[i:i+5] for i in range(0, 25, 5)]  

    return key_square

# Function to split the encoded text into pairs of two letters
def split_encoded_text(encoded_text):
    # Split the encoded text into pairs of two letters
    encoded_text_pairs = [encoded_text[i:i+2] for i in range(0, len(encoded_text), 2)]

    return encoded_text_pairs

# Function to find the position of a letter in the key square
def find_position(letter, key_square):
    letter = 'I' if letter == 'J' else letter  # Replace J with I
    for i in range(5):
        if letter in key_square[i]:
            return (i, key_square[i].index(letter))
        
# Function to decrypt the encoded pair
def decrypt_pair(pair, key_square):
    # Find position of pair 
    letter1_pos = find_position(pair[0], key_square)
    letter2_pos = find_position(pair[1], key_square)

    # If the letters are in the same row
    if letter1_pos[0] == letter2_pos[0]:
        decrypted_pair = (key_square[letter1_pos[0]][(letter1_pos[1]-1)%5], key_square[letter2_pos[0]][(letter2_pos[1]-1)%5])
    # If the letters are in the same column
    elif letter1_pos[1] == letter2_pos[1]:
        decrypted_pair = (key_square[(letter1_pos[0]-1)%5][letter1_pos[1]], key_square[(letter2_pos[0]-1)%5][letter2_pos[1]])
    # If the letters form a rectangle
    else:
        decrypted_pair = (key_square[letter1_pos[0]][letter2_pos[1]], key_square[letter2_pos[0]][letter1_pos[1]])
        
    return decrypted_pair

# Function to decrypt the encoded text
def decrypt_text(key, encoded_text):
    # Convert key and encoded text to uppercase
    key = key.upper()
    encoded_text = encoded_text.upper()

    # Generate the key square
    key_square = generate_key_square(key)

    # Split the encoded text into pairs of two letters
    encoded_text_pairs = split_encoded_text(encoded_text)

    # Decrypt the encoded text
    decrypted_text = ""
    for pair in encoded_text_pairs:
        decrypted_pair = decrypt_pair(pair, key_square)
        decrypted_text += "".join(decrypted_pair)

    return decrypted_text

# Clean up decrypted text
def clean_text(text):
    # If the last letter is X, remove it
    if text[-1] == "X":
        text = text[:-1]

    # If there is X in between two same letters, remove it
    text = "".join([text[i] for i in range(len(text)-1) if text[i] != "X" or text[i-1] != text[i+1]]) + text[-1]

    return text

# Input and Encoded text validation
def text_verification(text, is_encoded = False):
    # Check if space is present in the text
    if " " in text:
        text = text.replace(" ", "")

    # Check if all characters are alphabets
    if not text.isalpha():
        return text, False
    
    # Check if all characters are uppercase
    if not text.isupper():
        text = text.upper()
    
    # Check if encoded text is of even length
    if is_encoded and len(text) % 2 != 0:
        return text, False
    
    return text, True
    
    
def main():
    key = "TestJ"
    encoded_text = "IAmAmazingJK"

    # Text validation
    key, key_valid = text_verification(key)
    encoded_text, encoded_text_valid = text_verification(encoded_text, True)

    if not key_valid:
        print("Invalid key")
        return
    elif not encoded_text_valid:
        print("Invalid encoded text")
        return

    # Decrypt the encoded text
    decrypted_text = decrypt_text(key, encoded_text)

    print(clean_text(decrypted_text))

if __name__ == "__main__":
    main()
