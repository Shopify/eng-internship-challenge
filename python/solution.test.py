import unittest
import subprocess
import os

class TestSolution(unittest.TestCase):
    def test_decryption_output(self):
        # Run the solution.py script
        result = subprocess.run(['python3', 'solution.py'], text=True, capture_output=True)
        
        # Check the output
        expected_output = 'HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA'
        self.assertEqual(result.stdout.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()