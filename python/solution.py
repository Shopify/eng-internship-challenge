#!/usr/bin/env python3

"""
Playfair Cipher Decryption
Author: Christopher Rossi
Date: 2024-06-28

This script decrypts a message encoded with the Playfair cipher using a given key.
The Playfair cipher is a digraph substitution cipher that encrypts pairs of letters.

Usage:
    python playfair_decrypt.py

Requirements:
    Python 3.x
"""

def create_grid(key):
    """
    Create a 5x5 grid for the Playfair cipher using the provided key.
    The grid will contain each letter of the alphabet once, with 'I' and 'J' treated as the same letter.
    
    :param key: The keyword to create the grid.
    :return: A 5x5 list of lists representing the grid.
    """
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Note: 'J' is omitted as 'I' and 'J' are treated the same
    key = "".join(dict.fromkeys(key))  # Remove duplicates while preserving order
    key = key.replace("J", "")  # Remove 'J' as it's considered the same as 'I'
    used_chars = set(key)  # Track characters already used in the key

    # Append remaining letters of the alphabet to the key
    for char in alphabet:
        if char not in used_chars:
            key += char
    
    # Create a 5x5 grid from the key
    return [list(key[i:i + 5]) for i in range(0, len(key), 5)]


def find_position(grid, char):
    """
    Find the row and column of a character in the grid.
    
    :param grid: The 5x5 grid.
    :param char: The character to find.
    :return: A tuple (row, col) indicating the position of the character.
    """
    for row in range(5):
        for col in range(5):
            if grid[row][col] == char:
                return row, col
    return None, None  # Character not found


def decrypt_pair(grid, char1, char2):
    """
    Decrypt a pair of characters using the Playfair cipher rules.
    
    :param grid: The 5x5 grid.
    :param char1: The first character of the pair.
    :param char2: The second character of the pair.
    :return: The decrypted pair of characters.
    """
    row1, col1 = find_position(grid, char1)
    row2, col2 = find_position(grid, char2)
    
    if row1 == row2:
        # Same row: replace with characters immediately to the left
        return grid[row1][(col1 - 1) % 5] + grid[row2][(col2 - 1) % 5]
    elif col1 == col2:
        # Same column: replace with characters immediately above
        return grid[(row1 - 1) % 5][col1] + grid[(row2 - 1) % 5][col2]
    else:
        # Rectangle: replace with characters on the same row but in opposite corners of the rectangle
        return grid[row1][col2] + grid[row2][col1]


def decrypt_playfair_cipher(ciphertext, key):
    """
    Decrypt a ciphertext encrypted with the Playfair cipher using the provided key.
    
    :param ciphertext: The encrypted message.
    :param key: The key to create the Playfair cipher grid.
    :return: The decrypted plaintext message.
    """
    grid = create_grid(key)  # Create the grid from the key
    plaintext = ""
    i = 0
    
    # Process the ciphertext in pairs of characters
    while i < len(ciphertext):
        char1 = ciphertext[i]
        char2 = ciphertext[i + 1]
        
        decrypted_pair = decrypt_pair(grid, char1, char2)
        plaintext += decrypted_pair
        i += 2

    return plaintext.replace("X", "")  # Remove filler 'X' characters


# Given ciphertext and key
ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
key = "SUPERSPY"

# Decrypting the ciphertext
decrypted_message = decrypt_playfair_cipher(ciphertext, key)
print(decrypted_message)
