"""
Shopify Engineering Internship Playfair Cipher Solver Submission
Elai Mizrahi
June 21, 2024
"""

class PlayfairCipherSolver:
    def __init__(self, key):
        # Initialize the PlayfairCipherSolver with the provided key and generate the key square
        self.key_square = self.generate_key_square(key)

    def generate_key_square(self, key):
        # Create a 5x5 key square based on the given key
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        key_square = []
        for char in key:
            if char not in key_square and char != 'J':
                key_square.append(char)
        for char in alphabet:
            if char not in key_square:
                key_square.append(char)
        return key_square

    def find_position(self, char):
        # Find the row and column position of a character in the key square
        index = self.key_square.index(char)
        row, col = divmod(index, 5)
        return row, col

    def decrypt_digraph(self, digraph):
        # Decrypt a digraph (pair of letters) using the Playfair cipher rules
        row1, col1 = self.find_position(digraph[0])
        row2, col2 = self.find_position(digraph[1])

        if row1 == row2:
            # If both letters are in the same row, shift left
            col1 = (col1 - 1) % 5
            col2 = (col2 - 1) % 5
        elif col1 == col2:
            # If both letters are in the same column, shift up
            row1 = (row1 - 1) % 5
            row2 = (row2 - 1) % 5
        else:
            # If the letters form a rectangle, swap the columns
            col1, col2 = col2, col1

        return self.key_square[row1 * 5 + col1] + self.key_square[row2 * 5 + col2]

    def decrypt(self, cipher_text):
        # Decrypt the entire ciphertext by processing each digraph
        decrypted_text = ""
        for i in range(0, len(cipher_text), 2):
            digraph = cipher_text[i:i+2]
            decrypted_text += self.decrypt_digraph(digraph).replace('X', '')
        return decrypted_text

if __name__ == "__main__":
    cipher_text = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"
    solver = PlayfairCipherSolver(key)
    decrypted_message = solver.decrypt(cipher_text)
    print(decrypted_message)
