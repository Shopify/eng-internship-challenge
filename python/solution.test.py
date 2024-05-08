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

    def test_decrypt_message(self):
        key = "SUPERSPY"
        matrix = create_playfair_matrix(key)
        encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
        decrypted_message = decrypt_message(matrix, encrypted_message)
        expected_output = "HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA"
        self.assertEqual(decrypted_message, expected_output)

    def test_short_message(self):
        key = "SUPERSPY"
        matrix = create_playfair_matrix(key)
        encrypted_message = "IPOTMQ"
        decrypted_message = decrypt_message(matrix, encrypted_message)
        expected_output = "HELLO"
        self.assertEqual(decrypted_message, expected_output)

    def test_long_message(self):
        key = "SUPERSPY"
        matrix = create_playfair_matrix(key)
        encrypted_message = (
            "FXIKQHBMSYDUSXIPCPYSWFHOFUXLUROTMQL"
            "PINEHLFCPDBPUSXIPBFGUUCMQXLISARDBXFQ"
            "OYMUGMSSXNEEQXGCRXLBDIKQYOFIRXSGVXNDQ"
            "QEIXPSGMCXSRXUMWQEBDOXPUOPETEYBMYMNYS"
            "XGAHIVSEFMHBMSYYUEQOSNQCRTY"
        )
        decrypted_message = decrypt_message(matrix, encrypted_message)
        expected_output = (
            "ITHINKANTSARETHEBESTTHINGSTOSELLONSHOPIFYBECAUSE"
            "THEYHAVEALOTOFEDUCATIONALVALUETOPROVIDETOACHILDLIKE"
            "TEAMWORKORCOURAGEOREVENVORACIOUSNESSCANALLBETAUGHT"
            "USINGANTSASROLEMODELS"
        )
        self.assertEqual(decrypted_message, expected_output)

    def test_non_alphebetical(self):
        key = "SUPERSPY"
        matrix = create_playfair_matrix(key)
        encrypted_message = "WFFE*FE6BCBY)7Y2:SE&KMH!"
        decrypted_message = decrypt_message(matrix, encrypted_message)
        expected_output = "THISISABADSTRING"
        self.assertEqual(decrypted_message, expected_output)

    def test_with_spaces(self):
        key = "SUPERSPY"
        matrix = create_playfair_matrix(key)
        encrypted_message = "WFFE FE Y UZSHOH VFXF PUBICET"
        decrypted_message = decrypt_message(matrix, encrypted_message)
        expected_output = "THISISASTRINGWITHSPACES"
        self.assertEqual(decrypted_message, expected_output)

    def test_different_key(self):
        key = "INTERN"
        matrix = create_playfair_matrix(key)
        encrypted_message = "GNQWQPQPIQGUEPEIPUDYSONOSNFBGEPQGPANCV"
        decrypted_message = decrypt_message(matrix, encrypted_message)
        expected_output = "HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA"
        self.assertEqual(decrypted_message, expected_output)

if __name__ == '__main__':
    unittest.main()