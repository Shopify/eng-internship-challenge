# Function to generate the key table for Playfair Cipher
def generateTable(key):
    # Create an empty 5x5 table
    table = [['' for i in range(5)] for j in range(5)]
    dict = {chr(i + 97): 0 for i in range(26)}

    for i in range(len(key)):
        if key[i] != 'j':
            dict[key[i]] = 2
    dict['j'] = 1

    i, j, k = 0, 0, 0
    # Populate the table with the key and the remaining letters of the alphabet
    while k < len(key):
        if dict[key[k]] == 2:
            dict[key[k]] -= 1
            table[i][j] = key[k]
            j += 1
            if j == 5:
                i += 1
                j = 0
        k += 1

    # Fill the remaining cells of the table with the remaining letters of the alphabet
    for k in dict.keys():
        if dict[k] == 0:
            table[i][j] = k
            j += 1
            if j == 5:
                i += 1
                j = 0
 
    return table

# Function to search for the positions of characters in the key table
def search(table, a, b):
    arr = [0, 0, 0, 0]

    if a == 'j':
        a = 'i'
    elif b == 'j':
        b = 'i'
 
    for i in range(5):
        for j in range(5):
            if table[i][j] == a:
                arr[0], arr[1] = i, j
            elif table[i][j] == b:
                arr[2], arr[3] = i, j
 
    return arr

# Function to decrypt a message using Playfair Cipher
def decrypt(message, table):
    i = 0

    # Iterate through the message in pairs
    while i < len(message):
        # Search for the positions of the characters in the key table
        a = search(table, message[i], message[i + 1])
        # Decrypt based on the positions
        if a[0] == a[2]:
            message = message[:i] + table[a[0]][(a[1]-1) % 5] + table[a[0]][(a[3]-1) % 5] + message[i + 2:]
        elif a[1] == a[3]:
            message = message[:i] + table[(a[0]-1) % 5][a[1]] + table[(a[2]-1) % 5][a[1]] + message[i + 2:]
        else:
            message = message[:i] + table[a[0]][a[3]] + table[a[2]][a[1]] + message[i + 2:]
        i += 2

    # Remove all 'x' characters, remove special characters, and convert to uppercase
    message = message.replace('x', '').upper()
    message = ''.join(char.upper() for char in message if char.isalpha())
    return message

# Function to decrypt a cipher using Playfair Cipher
def decryptCipher(message, key):
    table = generateTable(key.lower())
    return decrypt(message.lower(), table)

def main():
    key = "SUPERSPY"
    encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

    decrypted_message = decryptCipher(encrypted_message, key)

    print(decrypted_message)

if __name__ == "__main__":
    main()