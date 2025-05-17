# Python Instructions

- Ensure your code can run in the command-line with the command `python3 solution.py`

## Explanation of the Python Solution

The Python solution in [`solution.py`](python/solution.py) is designed to decrypt a given Playfair Cipher string and output the decrypted text in accordance with the challenge requirements. Here's why it works effectively:

1. **Command-Line Execution**: The script is executable from the command line using `python3 solution.py`, as specified in the instructions. This ensures that the solution can be easily run and tested in a consistent environment.

2. **Decryption Logic**: At the core of `solution.py` is the decryption logic that accurately deciphers the encrypted Playfair Cipher text. This logic takes into account the unique aspects of the Playfair Cipher, such as the handling of digraphs (pairs of letters) and the special rules for decryption.

3. **Output Formatting**: The decrypted string is processed to meet the specific output requirements:
    - The output is entirely in **UPPER CASE**.
    - Spaces, the letter `"X"`, and special characters are removed from the output.
    - The application outputs only the decrypted string, without any additional text or formatting.

4. **Automated Testing**: The accompanying [`solution.test.py`](python/solution.test.py) file contains a test case that verifies the output of the decryption script. This test ensures that the script produces the expected output `HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA` when run. It serves as a validation of the solution's correctness.

By adhering to the challenge instructions and focusing on accurate decryption and proper output formatting, the Python solution effectively solves the given problem. The automated test provides an additional layer of confidence in the solution's reliability.