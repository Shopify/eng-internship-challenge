from collections import deque

def fill_polybius(queue, used, polybius):
    for i in range(5):
        for j in range(5):
            next_letter = queue.popleft()
            while next_letter in used:
                next_letter = queue.popleft()
            polybius[next_letter] = (i,j)
            polybius[f"{i}{j}"] = next_letter
            if (next_letter == 'I'): used.add("J")
            if (next_letter == 'J'): used.add("I")
            used.add(next_letter)

def clean_key(key):
    return key.replace(" ", "").upper()

def split_into_pairs(word):
    pairs = []
    for i in range (0, len(word) - 1, 2):
        pairs.append([word[i], word[i+1]])

    return pairs

def rejoin_pairs(pairs):
    return "".join([pair[0] + pair[1] for pair in pairs])

def remove_uncommon(word):
    return word.replace("X", "")

def process_pairs(pairs, polybius):
    for pair in pairs:
        if polybius[pair[0]][0] == polybius[pair[1]][0]: # Same row
            pair[0] = polybius[f"{polybius[pair[0]][0]}{(polybius[pair[0]][1] - 1) % 5}"]
            pair[1] = polybius[f"{polybius[pair[1]][0]}{(polybius[pair[1]][1] - 1) % 5}"]
        elif polybius[pair[0]][1] == polybius[pair[1]][1]: # Same col
            pair[0] = polybius[f"{(polybius[pair[0]][0] - 1) % 5 }{polybius[pair[0]][1]}"]
            pair[1] = polybius[f"{(polybius[pair[1]][0] - 1) % 5 }{polybius[pair[1]][1]}"]
        else: # Diagonal
            pair_0_corner = f"{polybius[pair[0]][0]}{polybius[pair[1]][1]}"
            pair_1_corner = f"{polybius[pair[1]][0]}{polybius[pair[0]][1]}"
            pair[0] = polybius[pair_0_corner]
            pair[1] = polybius[pair_1_corner]

def main():
    key = "playfair example"
    key =  clean_key(key)

    cipher_text = "BMODZBXDNABEKUDMUIXMMOUVIF"

    queue = deque([char for char in key + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]) # REMOVED I,J
    used = set()

    polybius = {}
    fill_polybius(queue, used, polybius)
    split_text = split_into_pairs(cipher_text)
    process_pairs(split_text, polybius)
    joined_word = rejoin_pairs(split_text)
    final = remove_uncommon(joined_word)

    print(final)


if __name__ == '__main__':
    main()
