import string

class PlayfairCipher:
    def __init__(self, key):
        self.key = self.process_key(key)
        self.matrix = self.generate_matrix(self.key)
        
    def process_key(self, key):
        key = ''.join(sorted(set(key), key=key.index))
        key = key.replace('J', 'I')
        return key.upper()
    
    def generate_matrix(self, key):
        alphabet = string.ascii_uppercase.replace('J', '')
        matrix = []
        used_chars = set()
        
        for char in key:
            if char not in used_chars:
                matrix.append(char)
                used_chars.add(char)
                
        for char in alphabet:
            if char not in used_chars:
                matrix.append(char)
                used_chars.add(char)
                
        return [matrix[i:i+5] for i in range(0, 25, 5)]
    
    def preprocess_text(self, text):
        text = text.replace('J', 'I').upper()
        processed_text = []
        i = 0
        while i < len(text):
            if i == len(text) - 1:
                processed_text.append(text[i] + 'X')
                i += 1
            elif text[i] == text[i + 1]:
                processed_text.append(text[i] + 'X')
                i += 1
            else:
                processed_text.append(text[i] + text[i + 1])
                i += 2
        return processed_text
    
    def find_position(self, char):
        for i, row in enumerate(self.matrix):
            if char in row:
                return i, row.index(char)
        return None
    
    def decrypt_pair(self, pair):
        r1, c1 = self.find_position(pair[0])
        r2, c2 = self.find_position(pair[1])
        
        if r1 == r2:
            return self.matrix[r1][(c1 - 1) % 5] + self.matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:
            return self.matrix[(r1 - 1) % 5][c1] + self.matrix[(r2 - 1) % 5][c2]
        else:
            return self.matrix[r1][c2] + self.matrix[r2][c1]
    
    def decrypt(self, ciphertext):
        pairs = self.preprocess_text(ciphertext)
        decrypted_text = ''.join([self.decrypt_pair(pair) for pair in pairs])
        return decrypted_text.replace('X', '')

if __name__ == "__main__":
    cipher = PlayfairCipher("SUPERSPY")
    encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    decrypted_message = cipher.decrypt(encrypted_message)
    print(decrypted_message)
