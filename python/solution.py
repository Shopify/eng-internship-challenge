import string

# Key for the Playfair cipher
key = 'SUPERSPY'
# Remove duplicates from the given key
key = "".join(dict.fromkeys(key))

# Encoded text to be decrypted
encoded_text = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'
# Calculate the number of pairs in the encoded text
num_pairs = int(len(encoded_text) / 2)

# Split the encoded text into pairs of characters
pairs = [encoded_text[i:i + 2] for i in range(0, len(encoded_text), 2)]

# Initialize a 5x5 matrix for the Playfair cipher
N = 5
cols, rows = 5, 5
arr = [['A' for i in range(cols)] for j in range(rows)]

# Initialize counters and a set to keep track of used characters
counter = 0
alpha_counter = 0
S = set()

# Populate the matrix with the key and remaining alphabet excluding 'J'
for i in range(len(arr)):
    for j in range(len(arr)):
        if counter < len(key):
            arr[i][j] = key[counter]
            S.add(key[counter])
            counter += 1
        else:
            while string.ascii_uppercase[alpha_counter] in S:
                alpha_counter += 1
            if string.ascii_uppercase[alpha_counter] == 'J':
                alpha_counter += 1
            arr[i][j] = string.ascii_uppercase[alpha_counter]
            alpha_counter += 1

# Initialize a list to store decrypted pairs
decrypt_pair = []

# Decrypt each pair of characters
for pair in pairs:
    # Iterates through the rows of arr
    for i in range(len(arr)):
        # A try-except to find the index of pair[0] in the list arr[i]
        try:
            index_0=arr[i].index(pair[0])
            # If both characters in pairs,pair[0] and pair[1] are in the same row then we find the character to its left
            # if nothing is to its left then get the character at the front
            try:
                index_1 = arr[i].index(pair[1])
                # Add the decrypted char to the decrypt_pair list
                p0 = index_0 - 1 if index_0 > 0 else 4
                p1 = index_1 - 1 if index_1 > 0 else 4
                decrypt_pair.append(arr[i][p0] + arr[i][p1])
                # Checks If the character, pair[1]  is in different rows

                # Normally, you would check to see if pair[1] is in the same column
                # but that is not true in this case for any of the pairs.
                # That step is skipped, and we check for the character
                # on the opposite of the square formed by the pair
            except ValueError:

                # Loop through arr's rows again to look for pair[1]
                for k in range(len(arr)):
                    # Add the decrypted char to the decrypt_pair list
                    try:
                        index_1 = arr[k].index(pair[1])
                        pi = index_0
                        pk = index_1
                        d_pi = arr[i][pk]
                        d_pk = arr[k][pi]
                        decrypt_pair.append(d_pi + d_pk)
                    except ValueError:
                        pass
        except ValueError:
            pass

# Construct the decrypted text from the pairs, excluding 'X'
decrypt_txt = ""
for pair in decrypt_pair:
    if pair[0] != 'X':
        decrypt_txt = decrypt_txt + pair[0]
    if pair[1] != 'X':
        decrypt_txt = decrypt_txt + pair[1]

# Print the decrypted text
print(decrypt_txt)
