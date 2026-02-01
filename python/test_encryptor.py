import unittest
from encrypt import Encryptor
from utils import Utils

class TestEncryptor(unittest.TestCase):

    def setUp(self):
        self.encrypt = Encryptor()
        self.matrix = [
            ['S', 'U', 'P', 'E', 'R'],
            ['Y', 'A', 'B', 'C', 'D'],
            ['F', 'G', 'H', 'I', 'K'],
            ['L', 'M', 'N', 'O', 'Q'],
            ['T', 'V', 'W', 'X', 'Z']
        ]

    def test_encrypt_pairs_same_row(self):
        pairs = ['SU', 'ER']
        expected = ['UP', 'RS']
        result = self.encrypt.encrypt_pairs(pairs, self.matrix)
        self.assertEqual(result, expected)

    def test_encrypt_pairs_same_column(self):
        pairs = ['SF', 'YL']
        expected = ['YL', 'FT']
        result = self.encrypt.encrypt_pairs(pairs, self.matrix)
        self.assertEqual(result, expected)

    def test_encrypt_pairs_different_row_column(self):
        pairs = ['SA', 'PC']
        expected = ['UY', 'EB']
        result = self.encrypt.encrypt_pairs(pairs, self.matrix)
        self.assertEqual(result, expected)

    def test_encrypt_message(self):
        message = 'superspy'
        expected = 'UPERSUSB' 
        result = self.encrypt.encrypt_message(message, self.matrix)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
