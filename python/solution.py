def make_matrix(key: str) -> list[list[str]]:
    """Makes the cypher matrix from a given key"""
    key = ''.join(dict.fromkeys(key.upper().replace('J', 'I') + "ABCDEFGHIKLMNOPQRSTUVWXYZ")) # Proccess key (Unique, no J)
    key = ''.join([c for c in key if c.isalpha()])  # Ensure only alphabetic characters
    return [list(key[i:i + 5]) for i in range(0, 25, 5)] # Make matrix (Python, so list of lists)

def decrypt_pair(a: str, b: str, matrix: list[list[str]]) -> str:
    "Decrypts a pair a,b -> decyphered(a) + decyphered(b)"
    pos_dict = {char: (r, c) for r, row in enumerate(matrix) for c, char in enumerate(row)}

    ra, ca = pos_dict[a]
    rb, cb = pos_dict[b]
    if ra == rb: # Same row: shift right
        return matrix[ra][(ca - 1) % 5] + matrix[rb][(cb - 1) % 5]
    if ca == cb: # Same column: shift down
        return matrix[(ra - 1) % 5][ca] + matrix[(rb - 1) % 5][cb]
    return matrix[ra][cb] + matrix[rb][ca] # Always this is a box, so apply box rule (same row, opposite corner)

def decrypt(code: str, key: str) -> str:
    matrix = make_matrix(key)
    return ''.join(decrypt_pair(code[i], code[i + 1], matrix) for i in range(0, len(code), 2)).replace("X", "")

code = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
key = "SUPERSPY"
print(decrypt(code, key))
