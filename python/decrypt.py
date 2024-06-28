from utils import Utils

class Decryptor:

    def decrypt_message(self, encrypted_message, matrix):
        """
        Decrypt the message using the provided matrix.
        
        Args:
            encrypted_message (str): The message to decrypt.
            matrix (list of list of str): The matrix to use for decryption.
        
        Returns:
            str: The decrypted message with 'X' removed.
        """
        pairs = Utils.split_into_pairs(encrypted_message)
        transformed_pairs = self.decrypt_pairs(pairs, matrix)
        decrypted_message_str = ''.join(transformed_pairs)
        cleaned_message = decrypted_message_str.replace('X', '')
        return cleaned_message

    def decrypt_pairs(self, pairs, matrix):
        """
        Transform pairs of characters for decryption using the matrix.
        
        Args:
            pairs (list of str): The pairs of characters to transform.
            matrix (numpy.ndarray): The matrix to use for transformation.
        
        Returns:
            list of str: The transformed pairs of characters.
        """
        decrypted_pairs = []

        for pair in pairs:
            if len(pair) != 2:
                raise ValueError("Each string in the array must contain exactly two characters.")

            row1, col1 = Utils.find_position(matrix, pair[0])
            row2, col2 = Utils.find_position(matrix, pair[1])

            if row1 == row2:  # Check if both characters are in the same row
                new_col1 = (col1 - 1) % len(matrix[0])
                new_col2 = (col2 - 1) % len(matrix[0])
                decrypted_pair = matrix[row1][new_col1] + matrix[row1][new_col2]
            elif col1 == col2:  # Check if both characters are in the same column
                new_row1 = (row1 - 1) % len(matrix)
                new_row2 = (row2 - 1) % len(matrix)
                decrypted_pair = matrix[new_row1][col1] + matrix[new_row2][col2]
            else: # Swap the columns of the characters if they are not in the same row or column
                new_letter1 = matrix[row1][col2]
                new_letter2 = matrix[row2][col1]
                decrypted_pair = new_letter1 + new_letter2  

            decrypted_pairs.append(decrypted_pair)

        return decrypted_pairs
