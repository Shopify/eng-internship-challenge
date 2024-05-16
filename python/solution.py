def remove_duplicates(text):
    """
    Returns the input text with duplicate characters removed, keeping only
    the first occurrence of every character (not case-sensitive).
    """
    seen = ""
    no_duplicates = ""
    for c in text:
        if c not in seen:
            no_duplicates += c
            seen += c
    return no_duplicates

def decrypt_playfair_cipher(ciphertext, key):
    """
    Decrypts the ciphertext encrypted with the Playfair cipher using the
    given key. Returns the decrypted plaintext.
    """
    # 'J' is omitted from the alphabet
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    # Creates the playfair cipher table corresponding to the given key.
    # [0:5] is the first row, [5:10] is the second row, and so on.
    table = remove_duplicates(key.upper() + alphabet)
    table = "".join(table.split())
    
    # Decrypt the ciphertext
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        x = ciphertext[i]
        y = ciphertext[i+1]

        # Compute the row and column of x and y
        x_idx = table.find(x)
        x_row = x_idx // 5
        x_col = x_idx % 5
        y_idx = table.find(y)
        y_row = y_idx // 5
        y_col = y_idx % 5

        # Decrypt x and y
        if x_row == y_row:
            row = table[x_row * 5: x_row * 5 + 5]
            x_decrypted = row[4] if x_col == 0 else row[x_col - 1]
            y_decrypted = row[4] if y_col == 0 else row[y_col - 1]
        elif x_col == y_col:
            col = table[x_col: len(table): 5]
            x_decrypted = col[4] if x_row == 0 else col[x_row - 1]
            y_decrypted = col[4] if y_row == 0 else col[y_row - 1]
        else:
            x_decrypted = table[x_row * 5 + y_col]
            y_decrypted = table[y_row * 5 + x_col]
        plaintext += x_decrypted + y_decrypted

    # Remove X's and special characters from the decrypted message
    modified_plaintext = ""
    for c in plaintext:
        if c != "X" and c in alphabet:
            modified_plaintext += c
    return modified_plaintext

def main():
    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"
    plaintext = decrypt_playfair_cipher(ciphertext, key)
    print(plaintext)

if __name__ == "__main__":
    main()
