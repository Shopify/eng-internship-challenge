import string
import random

from ..solution import PlayFair

def test_encrypt():
    """
    Test cipher encryption
    """

    # use default cipher key
    cipher = PlayFair(key='playfair example')

    # Define the test cases
    test_cases = [
        ("HIDETHEGOLDINTHETREESTUMP", "BMODZBXDNABEKUDMUIXMMOUVIF"),
        ("PETERSHOULDWORKATSHOPIFY", "AIVIMNDSLRGVNEOPZKDSIBPF")
    ]

    # check if the plaintext is correct
    for plaintext, expected in test_cases:
        assert cipher.encrypt(plaintext) == expected, f"Failed encryption for: {plaintext}"

def test_collision():
    """
    Test to make sure two different encryption key produces two different results on the same string
    """

    # initialize two unique ciphers
    cipher1 = PlayFair(key='playfair example')
    cipher2 = PlayFair(key='playfair examples')

    # all uppercase letters
    letters = string.ascii_uppercase

    # test 100 times
    for i in range(100):
        # generate random string length from 1 - 10^5
        length = random.randrange(1, 10**5)

        # generate a random string
        text = ''.join(random.choice(letters) for i in range(length))

        # check to make sure there is no collision
        assert cipher1.encrypt(text) != cipher2.encrypt(text), f"Failed encryption for: {text}"

def test_decrypt():
    """
    Test cipher decryption
    """

    # use default cipher key
    cipher = PlayFair(key='playfair example')

    # Define the test cases
    test_cases = [
        ("HIDETHEGOLDINTHETREESTUMP", "BMODZBXDNABEKUDMUIXMMOUVIF"),
        ("PETERSHOULDWORKATSHOPIFY", "AIVIMNDSLRGVNEOPZKDSIBPF")
    ]

    # check if the plaintext is correct
    for plaintext, expected in test_cases:
        assert cipher.decrypt(expected) == plaintext, f"Failed decryption for: {plaintext}"

def test_consistency():
    """
    Test to make sure the encryption and decryption are inverse function
    """

    # initialize cipher
    cipher = PlayFair(key='playfair example')

    # all uppercase letters
    letters = string.ascii_uppercase

    # remove X for edge case
    letters = letters.replace('X', '')

    # test 100 times
    for i in range(100):
        # generate random string length from 1 - 10^5
        length = random.randrange(3, 5)

        # generate a random string
        text = ''.join(random.choice(letters) for i in range(length))
        text = text.replace('J', 'I')

        inverse_text = cipher.decrypt(cipher.encrypt(text=text))

        # handle information loss from character replacement
        inverse_text = inverse_text.replace('J', 'I')

        # assert to make sure the decrypted of the encrypted text is the same
        assert inverse_text == text, f"Failed encryption for: {text}"
