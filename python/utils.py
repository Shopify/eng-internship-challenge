class Utils:
    @staticmethod
    def find_position(matrix, char):
        """
        Find the position of a character in a matrix.
        
        Args:
            matrix (list of list of str): The matrix to search.
            char (str): The character to find.
        
        Returns:
            tuple: The row and column index of the character, or (None, None) if not found.
        """
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == char:
                    return row, col
        return None, None

    @staticmethod
    def split_into_pairs(message):
        """
        Split a message into pairs of characters for encryption/decryption.
        
        Args:
            message (str): The message to split.
        
        Returns:
            list of str: The message split into pairs of characters.
        """
        filtered_string = ''.join([char.upper() for char in message if char.isalpha()])

        pairs = []
        i = 0

        while i < len(filtered_string):
            char1 = filtered_string[i]
            if i + 1 < len(filtered_string):
                char2 = filtered_string[i + 1]
                if char1 == char2:
                    pairs.append(char1 + 'X')
                    i += 1
                else:
                    pairs.append(char1 + char2)
                    i += 2
            else:
                pairs.append(char1 + 'X')
                i += 1

        return pairs
