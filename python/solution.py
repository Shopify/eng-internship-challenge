class PlayfairCipher:
    def __init__(self, key):
        self.key = key
        self.matrix = self.generate_matrix(key)

    def generate_matrix(self, key):
        key = key.upper().replace("J", "I")  # Replace J with I
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Remove J
        key_set = set()
        matrix = []
        for letter in key:
            if letter not in key_set:
                matrix.append(letter)
                key_set.add(letter)
        for letter in alphabet:
            if letter not in key_set:
                matrix.append(letter)
                key_set.add(letter)
        matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]
        return matrix


    def find_position(self, letter):
        for i, row in enumerate(self.matrix):
            if letter in row:
                return i, row.index(letter)
        return None

    def decrypt(self, text):
        text = text.upper().replace("J", "I")  # Replace J with I
        pairs = []
        i = 0
        while i < len(text):
            if i == len(text) - 1 or text[i] == text[i + 1]:  # If two consecutive letters are the same or only one letter left
                pairs.append((text[i], 'X'))
                i += 1
            else:
                pairs.append((text[i], text[i + 1]))
                i += 2

        decrypted_text = ""
        for pair in pairs:
            pos1 = self.find_position(pair[0])
            pos2 = self.find_position(pair[1])
            if pos1 is not None and pos2 is not None:
                if pos1[0] == pos2[0]:  # Same row
                    decrypted_text += self.matrix[pos1[0]][(pos1[1] - 1) % 5] + self.matrix[pos2[0]][(pos2[1] - 1) % 5]
                elif pos1[1] == pos2[1]:  # Same column
                    decrypted_text += self.matrix[(pos1[0] - 1) % 5][pos1[1]] + self.matrix[(pos2[0] - 1) % 5][pos2[1]]
                else:  # Different row and column
                    decrypted_text += self.matrix[pos1[0]][pos2[1]] + self.matrix[pos2[0]][pos1[1]]
            else:  # If one of the characters is not found in the matrix, append as is
                decrypted_text += pair[0] + pair[1]
        
        # Remove "X" and spaces
        decrypted_text = decrypted_text.replace('X', '').replace(' ', '')
        # Convert to uppercase
        decrypted_text = decrypted_text.upper()

        return decrypted_text


def main():
    cipher = PlayfairCipher("SUPERSPY")
    encrypted_text = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    decrypted_text = cipher.decrypt(encrypted_text)
    print(decrypted_text)


if __name__ == "__main__":
    main()