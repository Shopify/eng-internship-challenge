# Engineering Internship
## Technical Assessment Challenge

### Playfair Cipher Solver

#### Challenge
Your goal is to build an application that can solve a Playfair Cipher. To learn more about Playfair Ciphers and how they are constructed, consult the following Wikipedia page on the subject: [https://en.wikipedia.org/wiki/Playfair_cipher](https://en.wikipedia.org/wiki/Playfair_cipher).

Ideally this challenge should be able to be completed in 3 hours or less. You may choose one of the 5 following programming languages to complete this challenge:
- Ruby
- JavaScript
- TypeScript
- Python
- Go

Ensure your code is properly commented and formatted for readability and ease-of-understanding.

#### Thematics
*"Attention spy network! You've been assigned a task of the utmost importance! We've received an encrypted message from an agent in the field containing the password to a top secret club for super spies. The encrypted message reads as follows: **"IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"**. We've been told if we can crack this code and give the password to the door-person at the corner of 32nd Street, we will gain access to the illustrious spy club **Spy City**! We must get inside! However the password has been encrypted with an older system known as a **Playfair Cipher**. Our agent in the field says the key to the cipher is the string **"SUPERSPY"**. However, for the life of us we cannot crack this code! Devise an application that can solve this encryption, get the password, and join us inside Spy City for what we are sure will be a night to remember!"*

#### Instructions
1. Fork this repo to your personal Github account.
2. Clone your forked repo to begin working on the challenge locally.
3. Create a new Branch in your repo where you will be pushing your code to.
4. Choose which programming language you wish to complete the challenge with.
    - Navigate to the folder of that programming language and complete your work in the `solution` file found inside. ie: `ruby/solution.rb`
    - **Do not** edit the test file in the folder. Tests will only work as intended after you have submitted a PR.
    - You'll find a separate `README.md` in that folder with language specific instructions.
5. Ensure your application is executable from the command-line by running your `solution` file.
6. Your decrypted string must by entirely **UPPER CASE**, and not include `spaces`, the letter `"X"`, or `special characters`. Ensure you meet all these conditions before outputting the result.
7. Your application must output ***only*** the decrypted Playfair Cipher string.
    - ie: `BANANAS` ***not*** `The decrypted text is: BANANAS`

#### Submission
Upon completion of the challenge, create a PR of your work and compare it against the original Assessment Repo's `main` branch. Submit a link to your PR with your internship application in the appropriate field. 

This repo is designed to run a test against your work to ensure the correct decrypted string is outputted to the console when executing your code. Admins on this repo will deploy the test manually only after you have submitted your PR.
