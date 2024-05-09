def generate_playfair_grid(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = key.upper().replace("J", "I")
    key_set = set(key)
    grid = []
    for char in key + alphabet:
        if char not in key_set:
            key_set.add(char)
            grid.append(char)
    return [grid[i:i+5] for i in range(0, 25, 5)]