class KeyTable:
    def __init__(self, key:str) -> None:
        #No J in this matrix
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        self.matrix = []
        for char in key.upper():
            if char not in self.matrix and char in alphabet:
                self.matrix.append(char)
        for char in alphabet:
            if char not in self.matrix:
                self.matrix.append(char)
    
    def getRowCol(self, char):
        idx = self.matrix.index(char)
        return divmod(idx, 5)
    
    def decrypt_pair(self, pair) -> str:
        row1, col1 = self.getRowCol(pair[0])
        row2, col2 = self.getRowCol(pair[1])
        
        if row1 == row2:
            return self.matrix[row1 * 5 + (col1 - 1) % 5] + self.matrix[row2 * 5 + (col2 - 1) % 5]
        if col1 == col2:
            return self.matrix[((row1 - 1) % 5) * 5 + col1] + self.matrix[((row2 - 1) % 5) * 5 + col2]
        else:
            return self.matrix[row1 * 5 + col2] + self.matrix[row2 * 5 + col1]
        
    
def decrypt(s:str, key:str) -> str:
    key_table = KeyTable(key)
    s = ''.join([c.upper() for c in s if c.isalpha()])
    if len(s) % 2 != 0:
        s += "X"
    decrypted_text = ""
    for i in range(0, len(s), 2):
        decrypted_text += key_table.decrypt_pair(s[i:i+2])
    if decrypted_text.endswith("X"):
        decrypted_text = decrypted_text[:-1]
    #Check for Filler and Remove
    if len(decrypted_text) > 1:
        new_text = []
        i = 0
        while i < len(decrypted_text) - 1:
            if decrypted_text[i] == "X" and decrypted_text[i - 1] == decrypted_text[i + 1]:
                new_text.append(decrypted_text[i + 1]) 
                i += 1 
            else:
                new_text.append(decrypted_text[i])
            i += 1
        if i == len(decrypted_text) - 1:
            new_text.append(decrypted_text[i])
        decrypted_text = "".join(new_text)
    return decrypted_text
    
    
        
encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
key = "SUPERSPY"
print(decrypt(encrypted_message, key))