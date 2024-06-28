from utils import Utils

class Encryptor:

    def encrypt_message(self, message, matrix):
        """
        Encrypt the message using the provided matrix.
        
        Args:
            message (str): The message to encrypt.
            matrix (list of list of str): The matrix to use for encryption.
        
        Returns:
            str: The encrypted message.
        """
        pairs = Utils.split_into_pairs(message)
        encrypted_pairs = self.encrypt_pairs(pairs, matrix)
        return ''.join(encrypted_pairs)
    
    def encrypt_pairs(self, pairs, matrix):
        """
        Transform pairs of characters for encryption using the matrix.
        
        Args:
            pairs (list of str): The pairs of characters to transform.
            matrix (list of list of str): The matrix to use for transformation.
        
        Returns:
            list of str: The transformed pairs of characters.
        """
        encrypted_pairs = []
        for pair in pairs:
            if len(pair) != 2:
                raise ValueError("Each string in the array must contain exactly two characters.")

            row1, col1 = Utils.find_position(matrix, pair[0])
            row2, col2 = Utils.find_position(matrix, pair[1])

            if row1 == row2:  # Check if both characters are in the same row
                new_col1 = (col1 + 1) % len(matrix[0])
                new_col2 = (col2 + 1) % len(matrix[0])
                encrypted_pair = matrix[row1][new_col1] + matrix[row1][new_col2]
            elif col1 == col2:  # Check if both characters are in the same column
                new_row1 = (row1 + 1) % len(matrix)
                new_row2 = (row2 + 1) % len(matrix)
                encrypted_pair = matrix[new_row1][col1] + matrix[new_row2][col2]
            else:  # Swap the columns of the characters if they are not in the same row or column
                new_letter1 = matrix[row1][col2]
                new_letter2 = matrix[row2][col1]
                encrypted_pair = new_letter1 + new_letter2  

            encrypted_pairs.append(encrypted_pair)

        return encrypted_pairs
