def create_cipher_table(keyword):
    """
    Generates a 5x5 cipher table for the Playfair cipher based on a provided keyword.
    
    The function first normalizes the keyword by converting it to uppercase and removing duplicate letters.
    It then creates a list of characters from the normalized keyword, followed by the remaining letters of the
    alphabet, excluding 'J' (which is traditionally omitted in the Playfair cipher to fit the 25-cell table).
    
    Parameters:
    keyword (str): The keyword used to generate the initial part of the cipher table.
    
    Returns:
    list of list of str: A 5x5 matrix representing the cipher table.
    """
    
    # Normalize the keyword: uppercase and remove duplicates
    formatted_keyword = ''.join(sorted(set(keyword.upper()), key=keyword.index))
    
    # Remove 'J' from the alphabet and prepare the rest of the letters
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    
    # Create the cipher table starting with the keyword
    used_letters = set(formatted_keyword)
    table = [char for char in formatted_keyword]
    
    # Fill the table with the remaining letters
    for char in alphabet:
        if char not in used_letters:
            table.append(char)
    
    # Group the letters into a 5x5 matrix
    cipher_table = [table[i:i+5] for i in range(0, 25, 5)]
    return cipher_table

