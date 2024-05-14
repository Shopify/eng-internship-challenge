import { assembleDecryptedMessage } from '../solution'; // Import the function to test

describe('assembleDecryptedMessage', () => {
    it('should assemble decrypted digrams into one string without spaces, "X", or special characters', () => {
        const decryptedDigrams = ['FY', 'YP', 'VB']; // Example decrypted digrams
        const expectedDecryptedMessage = 'FYYPVB'; // Expected decrypted message

        // Call the function
        const decryptedMessage = assembleDecryptedMessage(decryptedDigrams);

        // Expect the decrypted message to match the expected message
        expect(decryptedMessage).toEqual(expectedDecryptedMessage);
    });

    // Add more test cases as needed
});
