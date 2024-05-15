class Playfair:
    def __init__(self, key):
        #initialize the cipher key
        self.key = key.upper()
        #create the Playfair table as a char list of 5x5
        self.table = self.create_table(self.key)

    def create_table(self, key):
        """
        Creates a 5x5 table for the Playfair cipher using the given key 
        and removes duplicates and characters that aren't alphabetic from the key.
        The table is first filled with the key's characters and then the remaining 
        alphabetical characters are added with 'J' and 'I' combined into one.
        """
        seen = set()
        table = []
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        key = key.upper().replace('J', 'I') #exclude 'J' since it is combined with 'I'

        #key characters added to the table
        for c in key:
            if c in alphabet and c not in seen:
                seen.add(c)
                table.append(c)
        
        #the remaining alphabet characters added to the table
        for c in alphabet:
            if c not in seen:
                seen.add(c)
                table.append(c)
        
        return [table[i * 5:(i + 1) * 5] for i in range(5)] #return a 5x5 table
    
    def find(self, c):
        for i in range(len(self.table)):
            if c in self.table[i]:
                return i, self.table[i].index(c) #return the row and column of the character
        return None, None

    def decrypt_pair(self, a, b):
        """
        Decrypts a pair of letters using the Playfair cipher rules:
        same row, replace each with the letter to its left
        same column, replace each with the letter above it
        forms a rectangle, replace them with letters on the same row, but in the columns of the other letter of the pair.
        """
        row1, col1 = self.find(a)
        row2, col2 = self.find(b)
        
        if row1 == row2:
            #shift each left
            return self.table[row1][(col1-1) % 5] + self.table[row2][(col2-1) % 5]
        elif col1 == col2:
            #shift each up
            return self.table[((row1-1) % 5)][col1] + self.table[((row2-1) % 5)][col2]
        else:
            #swap columns
            return self.table[row1][col2] + self.table[row2][col1]

    def decrypt(self, ciphertext):
        """
        Decrypts the ciphertext following the Playfair cipher rules.
        Processes digraphs (pairs of letters) according to the rules. 
        """
        ciphertext = ciphertext.upper().replace('J', 'I')
        plaintext = ""

        if len(ciphertext) % 2 != 0:
            ciphertext += 'X' #'X' added to pad the ciphertext if it has an odd length
        
        #find and process digraphs
        for i in range(0, len(ciphertext), 2):
            pair = ciphertext[i], ciphertext[i + 1]
            plaintext += self.decrypt_pair(pair[0], pair[1])
        
        #remove any 'X' characters that were added to pad the plaintext
        plaintext = plaintext.replace('X', '')
        return plaintext

#solution!
key = "SUPERSPY"
ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
solution = Playfair(key)
plaintext = solution.decrypt(ciphertext)
print(plaintext)
