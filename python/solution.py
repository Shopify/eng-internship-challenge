# function to create the 5 x 5 matrix with the key in the first n cells
# followed by the rest of the alphabet
def create_matrix(key):
    matrix = [] 
    key = key.replace('J', 'I') # Replace 'J' with 'I'
    used_chars = set() # Track used chars to avoid duplicate letters
    # Fill the matrix with characters from the key
    for char in key:
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)
    
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" # omit J from the alphabet
    for char in alphabet:
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)
    
    return [matrix[i:i+5] for i in range(0, 25, 5)]


def decrypt(cipher, key):
    matrix = create_matrix(key)
    return ""

def main():
    cipher = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"
    print(decrypt(cipher, key))

if __name__ == '__main__':
    main()