import unittest
from solution import PlayfairCipherSolver

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.playfairSolver = PlayfairCipherSolver()

    def test_decrypt_IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV_SUPERSPY(self):
        keyword = "SUPERSPY"
        message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
        decryptedMessage = self.playfairSolver.decrypt(message,keyword)
        self.assertEqual(decryptedMessage, "HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA")
    
    def test_decrypt_with_special_characters_message(self):
        keyword = "SUPERSPY"
        message = "IKEWE&NENXL@NQLPZSLERUMR!HEERYBOFNEINCHCV"
        decryptedMessage = self.playfairSolver.decrypt(message,keyword)
        self.assertEqual(decryptedMessage, "HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA")

    def test_decrypt_with_space_message(self):
        keyword = "SUPERSPY"
        message = "IKE WENENXL NQLPZSLERUMRHE ERYBOFN EINCHCV"
        decryptedMessage = self.playfairSolver.decrypt(message,keyword)
        self.assertEqual(decryptedMessage, "HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA")

    def test_decrypt_with_special_characters_keyword(self):
        keyword = "S!UPE#RSPY"
        message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
        decryptedMessage = self.playfairSolver.decrypt(message,keyword)
        self.assertEqual(decryptedMessage, "HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA")

    def test_decrypt_with_space_keyword(self):
        keyword = "S UPE RSPY"
        message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
        decryptedMessage = self.playfairSolver.decrypt(message,keyword)
        self.assertEqual(decryptedMessage, "HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA")

if __name__ == '__main__':
    unittest.main()
