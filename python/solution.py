def create_matrix(key):
    #remove duplicate letters and convert to uppercase
    filtered_key = ''.join(sorted(set(key.upper()), key = key.index))
    #add the remianing letters of the alphabet
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    for char in alphabet:
        if char not in filtered_key:
            filtered_key += char
    # create the 5x5 matrix
    matrix = [filtered_key[i:i+5] for i in range(0,25,5)]
    return matrix

key = "SUPERSPY"
matrix = create_index_matrix(key)
print("Matrix:\n", "\n".join([" ".join(row) for row in matrix]))