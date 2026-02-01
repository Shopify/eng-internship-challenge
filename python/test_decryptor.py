import unittest
from decrypt import Decryptor
from utils import Utils

class TestDecryptor(unittest.TestCase):

    def setUp(self):
        self.decrypt = Decryptor()
        self.matrix = [
            ['S', 'U', 'P', 'E', 'R'],
            ['Y', 'A', 'B', 'C', 'D'],
            ['F', 'G', 'H', 'I', 'K'],
            ['L', 'M', 'N', 'O', 'Q'],
            ['T', 'V', 'W', 'X', 'Z']
        ]

    def test_decrypt_pairs_same_row(self):
        pairs = ['UP', 'RS']
        expected = ['SU', 'ER']
        result = self.decrypt.decrypt_pairs(pairs, self.matrix)
        self.assertEqual(result, expected)

    def test_decrypt_pairs_same_column(self):
        pairs = ['YL', 'FT']
        expected = ['SF', 'YL']
        result = self.decrypt.decrypt_pairs(pairs, self.matrix)
        self.assertEqual(result, expected)

    def test_decrypt_pairs_different_row_column(self):
        pairs = ['UY', 'EB']
        expected = ['SA', 'PC']
        result = self.decrypt.decrypt_pairs(pairs, self.matrix)
        self.assertEqual(result, expected)

    def test_decrypt_message(self):
        encrypted_message = 'UPERSUSB'
        expected = 'SUPERSPY' 
        result = self.decrypt.decrypt_message(encrypted_message, self.matrix)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
