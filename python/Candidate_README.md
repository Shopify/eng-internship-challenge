## Playfair Cipher Solution

This repository contains my solution to the Playfair Cipher challenge. The project includes both encryption and decryption functionalities using the Playfair cipher algorithm. 

### Features
- **Custom Matrix Creation:** Allows the creation of a custom 5x5 matrix from any given key and omitted letter.
- **Encryption & Decryption:** Functionality to both encrypt and decrypt messages using the Playfair cipher.

### Assumptions
1. **Omission of Letter 'J':** The Playfair cipher implementation here omits 'J' to maintain a 5x5 matrix. If 'J' appears in the message, the decryption process is halted.
2. **Even-Length Messages:** All encrypted messages are assumed to be even. If an encrypted message is odd in length, the last letter is omitted during decryption.
3. **Uppercase Inputs:** The decryption function assumes that only uppercase alphabetic characters are input. Any non-conforming characters are cleaned from the message prior to decryption.

### Limitations and Edge Cases
1. **Non-Alphabetical Omission:** The application will not function correctly if the omitted letter is non-alphabetical or more than one character.
2. **Non-Standard Matrix Sizes:** The decryption function is designed to work with a 5x5 matrix only. Any deviation from this expected size will cause the function to break.

### Acknowledgments
Thank you for the opportunity to participate in this internship challenge! I appreciate the chance to develop and showcase my skills through this interesting and challenging task.

