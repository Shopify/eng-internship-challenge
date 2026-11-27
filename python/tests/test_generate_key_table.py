import unittest
from solution import PlayfairCipherSolver

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.playfairSolver = PlayfairCipherSolver()

    def test_no_i_or_j_in_keyword(self):
        keyword = "KEYWORD"
        keyTable = self.playfairSolver.generate_key_table(keyword)
        self.assertEqual(keyTable, [['K', 'E', 'Y', 'W', 'O'], ['R', 'D', 'A', 'B', 'C'], ['F', 'G', 'H', 'I', 'L'], ['M', 'N', 'P', 'Q', 'S'], ['T', 'U', 'V', 'X', 'Z']])

    def test_j_in_keyword(self):
        keyword = "KEYJWORD"
        keyTable = self.playfairSolver.generate_key_table(keyword)
        self.assertEqual(keyTable, [['K', 'E', 'Y', 'I', 'W'], ['O', 'R', 'D', 'A', 'B'], ['C', 'F', 'G', 'H', 'L'], ['M', 'N', 'P', 'Q', 'S'], ['T', 'U', 'V', 'X', 'Z']])
    
    def test_i_and_j_in_keyword(self):
        keyword = "KEYIJWORD"
        keyTable = self.playfairSolver.generate_key_table(keyword)
        self.assertEqual(keyTable, [['K', 'E', 'Y', 'I', 'W'], ['O', 'R', 'D', 'A', 'B'], ['C', 'F', 'G', 'H', 'L'], ['M', 'N', 'P', 'Q', 'S'], ['T', 'U', 'V', 'X', 'Z']])

    def test_keyword_with_repeated_chars(self):
        keyword = "KKEEYWORDD"
        keyTable = self.playfairSolver.generate_key_table(keyword)
        self.assertEqual(keyTable, [['K', 'E', 'Y', 'W', 'O'], ['R', 'D', 'A', 'B', 'C'], ['F', 'G', 'H', 'I', 'L'], ['M', 'N', 'P', 'Q', 'S'], ['T', 'U', 'V', 'X', 'Z']])

    def test_non_alph_chars_in_keyword(self):
        keyword = "KE@Y WORD123"
        keyTable = self.playfairSolver.generate_key_table(keyword)
        self.assertEqual(keyTable, [['K', 'E', 'Y', 'W', 'O'], ['R', 'D', 'A', 'B', 'C'], ['F', 'G', 'H', 'I', 'L'], ['M', 'N', 'P', 'Q', 'S'], ['T', 'U', 'V', 'X', 'Z']])

if __name__ == '__main__':
    unittest.main()
