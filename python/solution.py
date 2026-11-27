# Python code to solve Playfair cipher problem


from typing import List, Tuple


# Function to generate the key square
def generate_key_square(key: str) -> List[List[str]]:
    """
    Generate a 5x5 matrix (key square) from the given key.
    Replaces all occurrences of 'J' with 'I'.
    """
    key = key.replace("J", "I")  # Replace 'J' with 'I'
    key_square = []
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # 'J' is omitted

    # Add the key to the key square
    for letter in key:
        if letter not in key_square:
            key_square.append(letter)

    # Add the remaining letters of the alphabet to the key square
    for letter in alphabet:
        if letter not in key_square:
            key_square.append(letter)

    # Reshape the key square to a 5x5 matrix
    return [key_square[i:i + 5] for i in range(0, 25, 5)]


# Function to split the encoded text into pairs of two letters
def split_encoded_text(encoded_text: str) -> List[str]:
    """
    Split the encoded text into pairs of two letters.
    """
    return [encoded_text[i:i + 2] for i in range(0, len(encoded_text), 2)]


# Function to find the position of a letter in the key square
def find_position(letter: str, key_square: List[List[str]]) -> Tuple[int, int]:
    """
    Find the position of a letter in the key square.
    Replaces 'J' with 'I'.
    """
    letter = 'I' if letter == 'J' else letter  # Replace 'J' with 'I'
    for i in range(5):
        if letter in key_square[i]:
            return i, key_square[i].index(letter)
    raise ValueError(f"Letter '{letter}' not found in the key square.")


# Function to decrypt the encoded pair
def decrypt_pair(pair: str, key_square: List[List[str]]) -> Tuple[str, str]:
    """
    Decrypt a pair of letters according to Playfair cipher rules.
    """
    # Find position of the pair
    letter1_pos = find_position(pair[0], key_square)
    letter2_pos = find_position(pair[1], key_square)

    # If the letters are in the same row
    if letter1_pos[0] == letter2_pos[0]:
        return (
            key_square[letter1_pos[0]][(letter1_pos[1] - 1) % 5],
            key_square[letter2_pos[0]][(letter2_pos[1] - 1) % 5],
        )
    # If the letters are in the same column
    elif letter1_pos[1] == letter2_pos[1]:
        return (
            key_square[(letter1_pos[0] - 1) % 5][letter1_pos[1]],
            key_square[(letter2_pos[0] - 1) % 5][letter2_pos[1]],
        )
    # If the letters form a rectangle
    else:
        return (
            key_square[letter1_pos[0]][letter2_pos[1]],
            key_square[letter2_pos[0]][letter1_pos[1]],
        )


# Function to decrypt the encoded text
def decrypt_text(key: str, encoded_text: str) -> str:
    """
    Decrypt the encoded text using the provided key.
    """
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


# Function to validate and clean up the input text
def text_verification(text: str, is_encoded: bool = False) -> Tuple[str, bool]:
    """
    Validate and clean the input text. If 'is_encoded' is True, ensure it's of even length.
    """
    # Remove spaces and ensure only alphabets remain
    text = text.replace(" ", "")
    if not text.isalpha():
        return text, False

    # Convert to uppercase
    text = text.upper()

    # If encoded, ensure even length
    if is_encoded and len(text) % 2 != 0:
        return text, False

    return text, True


# Main function
def main():
    key = "SUPERSPY"
    encoded_text = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

    # Text validation
    key, key_valid = text_verification(key)
    encoded_text, encoded_text_valid = text_verification(encoded_text, True)

    if not key_valid:
        print("Invalid key.")
        return
    elif not encoded_text_valid:
        print("Invalid encoded text.")
        return

    # Decrypt the encoded text
    decrypted_text = decrypt_text(key, encoded_text)

    # Remove 'X' used as padding characters in the decrypted message
    print(decrypted_text.replace("X", ""))


if __name__ == "__main__":
    main()
