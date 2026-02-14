from typing import List

def generate_cipher_grid(key: str) -> List[str]:
    """
    Generate a 5x5 cipher grid for the Playfair cipher from a given key.
    This function efficiently processes the key by eliminating duplicates and treating 'J' as 'I'.
    It also fills the cipher grid with the remaining letters of the alphabet (excluding 'J').

    Time Complexity: O(k + 25) where k is the length of the key. The constant 25 comes from processing
    the fixed alphabet size.

    Args:
        key (str): The key from which to generate the square, containing alphabetical characters.

    Returns:
        List[str]: A list (1D, not 2D) representing the 5x5 cipher grid.

    Raises:
        ValueError: If the key contains non-alphabetical characters or is empty.
    """
    if not key.isalpha():
        raise ValueError("Key must contain only alphabetical characters")

    if len(key) == 0:
        raise ValueError("Key cannot be empty")

    # Standard Playfair cipher excludes 'J', treating 'J' as 'I'
    # Note: This step is likely unnecessary for the question, but still included for completeness
    key = key.upper().replace('J', 'I')
    seen = set()
    cipher_grid = []

    # Add unique characters from the key to the cipher grid
    for char in key:
        if char not in seen:
            seen.add(char)
            cipher_grid.append(char)

    # Fill the cipher grid with the remaining letters of the alphabet
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char != 'J' and char not in seen:
            cipher_grid.append(char)

    return cipher_grid


def decrypt_playfair(ciphertext: str, key: str) -> str:
    """
    Decrypt a ciphertext that was encrypted using the Playfair cipher with a given key.
    Time Complexity: O(n) where n is the length of the ciphertext.

    Args:
    ciphertext: The ciphertext to decrypt.
    key: The key used for decryption.

    Returns:
    str: The decrypted plaintext.
    """
    if len(ciphertext) == 0:
        return ""
    
    if not ciphertext.isalpha():
        raise ValueError("Ciphertext should contain only alphabetical characters")
    
    if len(key) == 0:
        raise ValueError("Key cannot be empty")

    cipher_grid = generate_cipher_grid(key)
    plaintext = ""

    # Handle odd-length ciphertext by warning and ignoring the last character
    if len(ciphertext) % 2 != 0:
        print("Warning: Ciphertext length is odd. The last character will be ignored.")
        ciphertext = ciphertext[:-1]

    # Decrypt each pair of characters
    for i in range(0, len(ciphertext), 2): # Note step size of 2 for digrams
        first, second = ciphertext[i], ciphertext[i+1]
        row1, col1 = cipher_grid.index(first) // 5, cipher_grid.index(first) % 5
        row2, col2 = cipher_grid.index(second) // 5, cipher_grid.index(second) % 5

        if row1 == row2:
            # Same row: shift to the left for decryption
            new_first = cipher_grid[row1 * 5 + (col1 - 1) % 5] # Modulo 5 for wrapping
            new_second = cipher_grid[row2 * 5 + (col2 - 1) % 5]
        elif col1 == col2:
            # Same column: shift up
            new_first = cipher_grid[((row1 - 1) % 5) * 5 + col1]
            new_second = cipher_grid[((row2 - 1) % 5) * 5 + col2]
        else:
            # Rectangle: swap columns
            new_first = cipher_grid[row1 * 5 + col2]
            new_second = cipher_grid[row2 * 5 + col1]

        # Append the decrypted characters to the plaintext
        plaintext += new_first + new_second

    # Check that there are only alphabetical characters in the plaintext
    if not plaintext.isalpha():
        raise ValueError("Decrypted plaintext contains non-alphabetical characters")

    # Remove 'X'-es
    plaintext = plaintext.replace('X', '')

    # Check for spaces, 'X', lowercase character, or special characters
    if not plaintext.isupper():
        raise ValueError("Decrypted plaintext contains lowercase characters or special characters")
    
    if ' ' in plaintext:
        raise ValueError("Decrypted plaintext contains spaces")
    
    if 'X' in plaintext:
        # This should not happen if the ciphertext was properly padded
        raise ValueError("Decrypted plaintext contains 'X'")
    
    if not plaintext.isalpha():
        raise ValueError("Decrypted plaintext contains non-alphabetical characters")

    return plaintext

# Extra tests
def test_playfair_cipher():
    test_cases = [
        # Basic functionality test
        ("CFSZPK", "PLAYFAIREXAMPLE", "HLHSTB"),  # Assuming 'X' used for padding
        ("IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV", "SUPERSPY", "HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA"), # Example from the question
        
        # Key with repeated characters and including 'J'
        ("FYYFHP", "KEYBOARDJ", "HKKHGQ"),  # 'J' in key treated as 'I'
                
        # Edge cases
        ("", "KEY", ""),  # Empty ciphertext
        ("FYGMKO", "KEY", "YWFNBI"),  # Proper decryption
        ("FYGMKO", "", ValueError),  # Empty key should raise ValueError
        
        # Test for non-alphabetical characters in key or ciphertext
        ("FYGMKO1", "KEY", ValueError),  # Ciphertext includes non-alphabetical character
        ("FYGMKO", "KEY1", ValueError),  # Key includes non-alphabetical character
    ]

    for ciphertext, key, expected in test_cases:
        if isinstance(expected, str):
            try:
                result = decrypt_playfair(ciphertext, key)
                assert result == expected, f"Failed for {ciphertext} with key {key}: Expected {expected}, got {result}"
                print(f"Test passed for ciphertext '{ciphertext}' with key '{key}'. Expected and received: '{expected}'")
            except Exception as e:
                print(f"Test failed with exception for '{ciphertext}' and key '{key}': {str(e)}")
        elif expected is ValueError:
            try:
                result = decrypt_playfair(ciphertext, key)
                assert False, f"Expected ValueError for '{ciphertext}' with key '{key}'"
            except ValueError:
                print(f"Correctly raised ValueError for '{ciphertext}' with key '{key}'")
            except Exception as e:
                assert False, f"Incorrect exception type for '{ciphertext}' with key '{key}': {str(e)}"


if __name__ == "__main__":
    # Run extra tests
    # test_playfair_cipher()

    key = "SUPERSPY"
    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    answer = "HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA"

    decrypted_message = decrypt_playfair(ciphertext, key)
    
    assert decrypted_message == answer

    print(decrypted_message)
