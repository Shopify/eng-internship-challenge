import unittest
from solution import PlayfairCipherSolver

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.playfairSolver = PlayfairCipherSolver()

    def test_odd_number_of_chars_in_message(self):
        message = "HELLO"
        digrams = self.playfairSolver.split_to_digram(message)
        self.assertEqual(digrams, [['H', 'E'], ['L', 'L'], ['O', 'X']])

    def test_even_number_of_chars_in_message(self):
        message = "HelloWorld"
        digrams = self.playfairSolver.split_to_digram(message)
        self.assertEqual(digrams, [['H', 'E'], ['L', 'L'], ['O', 'W'], ['O', 'R'], ['L', 'D']])
    
    def test_non_alph_chars_in_message(self):
        message = "Hello, World!"
        digrams = self.playfairSolver.split_to_digram(message)
        self.assertEqual(digrams, [['H', 'E'], ['L', 'L'], ['O', 'W'], ['O', 'R'], ['L', 'D']])

    def test_j_in_message(self):
        message = "Just a test"
        digrams = self.playfairSolver.split_to_digram(message)
        self.assertEqual(digrams, [['I', 'U'], ['S', 'T'], ['A', 'T'], ['E', 'S'], ['T', 'X']])
    
    def test_i_and_j_in_message(self):
        message = "Ij test"
        digrams = self.playfairSolver.split_to_digram(message)
        self.assertEqual(digrams, [['I', 'I'], ['T', 'E'], ['S', 'T']])
    
    


if __name__ == '__main__':
    unittest.main()
