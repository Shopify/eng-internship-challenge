import unittest
import subprocess
import os

class TestSolution(unittest.TestCase):
    def test_decryption_output_default(self):
        # Run the solution.py script
        text = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
        keyword = "SUPERSPY"
        result = subprocess.run(['python3', 'solution.py', text, keyword], text=True, capture_output=True)
        
        # Check the output
        expected_output = 'HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA'
        self.assertEqual(result.stdout.strip(), expected_output)

    # A nice test case that tests removing X's. An odd length original text.
    def test_decryption_output_remove_x(self):
        text = "FYPRGQCFPMLGEATWTYAQHKQAYTEKVN"
        keyword = "WATERLOO"
        result = subprocess.run(['python3', 'solution.py', text, keyword], text=True, capture_output=True)
        
        # Check the output
        expected_output = 'IUSTINLINSOFTWAREENGINEERING'
        self.assertEqual(result.stdout.strip(), expected_output)

    # A longer test case with wrapping around the matrix.
    def test_decryption_output_shopify(self):
        text = "XQCZHTLQDHZLFODHASTMOSHPGAQMOSFDHTDNHQGFABCMKNQHWPRV"
        keyword = "SHOPIFY"
        result = subprocess.run(['python3', 'solution.py', text, keyword], text=True, capture_output=True)
        
        # Check the output
        expected_output = 'WRITINGTESTCASESFORTHISOAONTHISFINEMONDAYAFTERNOON'
        self.assertEqual(result.stdout.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()