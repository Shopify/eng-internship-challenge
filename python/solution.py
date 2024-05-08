def main():
    
    # Define constants
    key = 'SUPERSPY'
    message = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'
    
    # Decrypt message
    decrypted = decrypt(message, key)
    
    # Print decrypted message
    print(decrypted)

def decrypt(n, m):
    

    # Your decrypted string must by entirely UPPER CASE, and not include spaces, the letter "X", or special characters. Ensure you meet all these conditions before outputting the result.
    # Your application must output only the decrypted Playfair Cipher string.
    # ie: BANANAS not The decrypted text is: BANANAS
    

if __name__ == '__main__':
    main()