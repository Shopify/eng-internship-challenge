class PlayfairCipher:
    def __init__(self, key):
        self.key_table = self.generate_table(key)

    def generate_table(self, key):
        key = key.upper()
        key_table = []
        used_chars = set()

        # Add key characters to the key table
        for char in key:
            if char not in used_chars and char.isalpha():
                key_table.append(char)
                used_chars.add(char)

        # Add remaining letters of the alphabet
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for char in alphabet:
            if char not in used_chars:
                key_table.append(char)
                used_chars.add(char)

        # Convert to 5x5 matrix
        key_table_matrix = [key_table[i:i+5] for i in range(0, 25, 5)]
        return key_table_matrix

    def find_position(self, letter):
        for row in range(5):
            for col in range(5):
                if self.key_table[row][col] == letter:
                    return row, col
        return None

    def decrypt(self, ciphertext):
        plaintext = []

        i = 0
        while i < len(ciphertext):
            a = ciphertext[i]
            b = ciphertext[i + 1] if i + 1 < len(ciphertext) else 'X'

            row1, col1 = self.find_position(a)
            row2, col2 = self.find_position(b)

            if row1 is None or row2 is None or col1 is None or col2 is None:
                i += 1
                continue

            move_operations = {
            (True, False): lambda r1, c1, r2, c2: (self.key_table[r1][(c1 - 1) % 5], self.key_table[r2][(c2 - 1) % 5]),  # Same row
            (False, True): lambda r1, c1, r2, c2: (self.key_table[(r1 - 1) % 5][c1], self.key_table[(r2 - 1) % 5][c2]),  # Same column
            (False, False): lambda r1, c1, r2, c2: (self.key_table[r1][c2], self.key_table[r2][c1])  # Rectangle swap
            }

            operation = move_operations[(row1 == row2, col1 == col2)]
            plaintext.extend(operation(row1, col1, row2, col2)) 

            i += 2

        plaintext_str = ''.join(plaintext)
        return plaintext_str.replace('X', '')


def main():
    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"

    cipher = PlayfairCipher(key)
    decrypted_message = cipher.decrypt(ciphertext)
    print(decrypted_message)

if __name__ == "__main__":
    main()
