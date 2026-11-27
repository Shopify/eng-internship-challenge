# import unittest
# import subprocess
# import os

# class TestSolution(unittest.TestCase):
#     def test_decryption_output(self):
#         # Run the solution.py script
#         path = r'C:/Users/ngong/Desktop/shopify-internship/eng-internship-challenge/python/solution.py'
#         result = subprocess.run(['python3', path], text=True, capture_output=True)
        
#         # Check the output
#         # expected_output = 'HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA'
#         self.assertEqual(result.stdout.strip(), 'HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA')

# if __name__ == '__main__':
#     unittest.main()



import unittest
import subprocess
import os

class TestSolution(unittest.TestCase):
    def test_decryption_output(self):
        # Path to solution.py (adjust as necessary for your environment)
        path = r'C:/Users/ngong/Desktop/shopify-internship/eng-internship-challenge/python/solution.py'
        
        # Run the solution.py script
        result = subprocess.run(['python', path], capture_output=True, text=True)
        
        # Check the output and any potential errors
        if result.returncode != 0:
            print("Error occurred while running the script:")
            print(result.stderr)
        
        # Check the output
        self.assertEqual(result.stdout.strip(), 'HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA')

if __name__ == '__main__':
    unittest.main()
