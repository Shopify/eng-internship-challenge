import unittest
from solution import PlayfairCipherSolver

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.playfairSolver = PlayfairCipherSolver()

    def test_find_char_in_first_row(self):
        keyTable = [['K', 'E', 'Y', 'W', 'O'], ['R', 'D', 'A', 'B', 'C'], ['F', 'G', 'H', 'I', 'L'], ['M', 'N', 'P', 'Q', 'S'], ['T', 'U', 'V', 'X', 'Z']]
        char = 'K'
        position = self.playfairSolver.find_char_position(char, keyTable)
        self.assertEqual(position, (0, 0))
    
    def test_find_char_in_last_row(self):
        keyTable = [['K', 'E', 'Y', 'W', 'O'], ['R', 'D', 'A', 'B', 'C'], ['F', 'G', 'H', 'I', 'L'], ['M', 'N', 'P', 'Q', 'S'], ['T', 'U', 'V', 'X', 'Z']]
        char = 'Z'
        position = self.playfairSolver.find_char_position(char, keyTable)
        self.assertEqual(position, (4, 4))

    def test_find_char_in_middle_row(self):
        keyTable = [['K', 'E', 'Y', 'W', 'O'], ['R', 'D', 'A', 'B', 'C'], ['F', 'G', 'H', 'I', 'L'], ['M', 'N', 'P', 'Q', 'S'], ['T', 'U', 'V', 'X', 'Z']]
        char = 'G'
        position = self.playfairSolver.find_char_position(char, keyTable)
        self.assertEqual(position, (2, 1))

    def test_find_char_not_in_table(self):
        keyTable = [['K', 'E', 'Y', 'W', 'O'], ['R', 'D', 'A', 'B', 'C'], ['F', 'G', 'H', 'I', 'L'], ['M', 'N', 'P', 'Q', 'S'], ['T', 'U', 'V', 'X', 'Z']]
        char = 'J'
        position = self.playfairSolver.find_char_position(char, keyTable)
        self.assertEqual(position, None)
    
    


if __name__ == '__main__':
    unittest.main()
