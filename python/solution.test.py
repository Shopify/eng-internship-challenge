import unittest
import subprocess
import os
from solution import decryptPlayfairCipher

# Tests for Playfair Cipher solution
class TestSolution(unittest.TestCase):
    def testBasicDecryption(self):
        key = "SUPERSPY"
        ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
        expected = "HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA"
        result = decryptPlayfairCipher(ciphertext, key)
        self.assertEqual(result, expected)

    def testSpecialCharacters(self):
        key = "SUPERSPY"
        ciphertext = "IKEWENENXLNQLPZSLERUMRH@@@ERYBOFNEINCHCV"
        expected = "HIPPOPOTOMONSTROSESQUIPSDCNHLCOBIBTW"
        result = decryptPlayfairCipher(ciphertext, key)
        self.assertEqual(result, expected)

    def testShortMessage(self):
        key = "SUPERSPY"
        ciphertext = "AB"
        expected = "YA"
        result = decryptPlayfairCipher(ciphertext, key)
        self.assertEqual(result, expected)

    def testWithKeyIncludingAllLetters(self):
        key = "ABCDEFGHIJKLMNOPQRSTUVWXY"  # All letters but 'J'
        ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
        expected = "HIBZCPCPVNLSPOUPAQTGMKCBUWDLIPCHOCA"
        result = decryptPlayfairCipher(ciphertext, key)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()