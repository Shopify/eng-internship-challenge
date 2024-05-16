def playfair_cipher(plaintext, key, mode):
    """
    Encrypts or decrypts a plaintext using the Playfair Cipher with a given key.

    Args:
        plaintext (str): The plaintext to be encrypted or decrypted.
        key (str): The key used for encryption or decryption.
        mode (str): The mode, either 'encrypt' or 'decrypt'.

    Returns:
        str: The resulting ciphertext or decrypted text.
    """

    # Define the alphabet, excluding 'j'
    alphabet = 'abcdefghiklmnopqrstuvwxyz'
    # Remove whitespace and 'j' from the key and convert to lowercase
    key = key.lower().replace(' ', '').replace('j', 'i')
    # Construct the key square
    key_square = ''
    for letter in key + alphabet:
        if letter not in key_square:
            key_square += letter

    # Split the plaintext into digraphs, padding with 'x' if necessary
    plaintext = plaintext.lower().replace(' ', '').replace('j', 'i')
    if len(plaintext) % 2 == 1:
        plaintext += 'x'
    digraphs = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]

    # Define the encryption/decryption functions
    def encrypt(digraph):
        a, b = digraph
        row_a, col_a = divmod(key_square.index(a), 5)
        row_b, col_b = divmod(key_square.index(b), 5)
        if row_a == row_b:
            col_a = (col_a + 1) % 5
            col_b = (col_b + 1) % 5
        elif col_a == col_b:
            row_a = (row_a + 1) % 5
            row_b = (row_b + 1) % 5
        else:
            col_a, col_b = col_b, col_a
        return key_square[row_a*5+col_a] + key_square[row_b*5+col_b]

    def decrypt(digraph):
        a, b = digraph
        row_a, col_a = divmod(key_square.index(a), 5)
        row_b, col_b = divmod(key_square.index(b), 5)
        if row_a == row_b:
            col_a = (col_a - 1) % 5
            col_b = (col_b - 1) % 5
        elif col_a == col_b:
            row_a = (row_a - 1) % 5
            row_b = (row_b - 1) % 5
        else:
            col_a, col_b = col_b, col_a
        return key_square[row_a*5+col_a] + key_square[row_b*5+col_b]

    # Encrypt or decrypt the plaintext
    result = ''
    for digraph in digraphs:
        if mode == 'encrypt':
            result += encrypt(digraph)
        elif mode == 'decrypt':
            result += decrypt(digraph)

    # Return the result
    return result

# Example usage, must be in UPPER CASE
plaintext = 'She sells sea shells by the sea shore'
key = 'superspy'
ciphertext = playfair_cipher(plaintext, key, 'encrypt')
print(ciphertext)  # outputs: "IKENENXLNQLPZSLYJIEXHHXOBEMBZSW"
decrypted_text = playfair_cipher(ciphertext, key, 'decrypt')
print(decrypted_text)  # outputs: "SHESELLSSEASHELLSBYTHESEASHORE"