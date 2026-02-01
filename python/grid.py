import numpy as np

class Grid:
    def __init__(self, key_string, rows, cols):
        """
        Initialize the Grid object with a key string, number of rows, and number of columns.
        
        Args:
            key_string (str): The key string used to fill the grid.
            rows (int): The number of rows in the grid.
            cols (int): The number of columns in the grid.
        """
        self.key_string = key_string
        self.rows = rows
        self.cols = cols

    def create_unique_matrix(self):
        """
        Create a matrix filled with unique characters from the key string.
        
        Returns:
            list of list of str: The matrix filled with unique characters.
        """
        unique_chars = []
        for char in self.key_string:
            if char.upper() not in unique_chars and char.isalpha():
                unique_chars.append(char.upper())

        # Create an empty matrix
        matrix = np.full((self.rows, self.cols), '', dtype=str)

        # Insert unique characters into the matrix
        index = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if index < len(unique_chars):
                    matrix[i, j] = unique_chars[index]
                    index += 1

        return matrix

    def fill_remaining_matrix(self, matrix, alpha_string):
        """
        Fill the remaining empty spots in the matrix with unused letters from the alphabet string.
        
        Args:
            matrix (list of list of str): The matrix to fill.
            alpha_string (str): The alphabet string to use for filling.
        
        Returns:
            list of list of str: The matrix filled with all characters.
        """
        used_chars = set(char for row in matrix for char in row if char != '')
        fill_index = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == '':
                    while fill_index < len(alpha_string) and alpha_string[fill_index] in used_chars:
                        fill_index += 1
                    if fill_index < len(alpha_string):
                        matrix[i][j] = alpha_string[fill_index]
                        used_chars.add(alpha_string[fill_index])
                        fill_index += 1
                    else:
                        print("Not enough unique characters to fill the matrix.")
                        return matrix
                
        return matrix
