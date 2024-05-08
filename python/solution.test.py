import unittest
import subprocess
import os
from solution import decrypt_message, create_playfair_matrix

class TestDecryption(unittest.TestCase):
    def test_decryption_output(self):
        # Run the solution.py script
        result = subprocess.run(['python3', 'solution.py'], text=True, capture_output=True)
        
        # Check the output
        expected_output = os.getenv('TEST_ANSWER')
        self.assertEqual(result.stdout.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()