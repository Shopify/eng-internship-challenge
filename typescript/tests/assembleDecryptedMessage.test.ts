import { assembleDecryptedMessage } from '../solution'; 

describe('assembleDecryptedMessage', () => {
    it('should assemble decrypted digrams into one string without spaces, "X", or special characters', () => {
        const decryptedDigrams = ['FY', 'YP', 'VB']; 
        const expectedDecryptedMessage = 'FYYPVB'; 

        const decryptedMessage = assembleDecryptedMessage(decryptedDigrams);

        
        expect(decryptedMessage).toEqual(expectedDecryptedMessage);
    });

    it('should remove "X" from the final message', () => {
      const decryptedDigrams = ['FY', 'XP', 'VB'];
      const expectedDecryptedMessage = 'FYPVB';

      const decryptedMessage = assembleDecryptedMessage(decryptedDigrams);

      expect(decryptedMessage).toEqual(expectedDecryptedMessage);
  });

});
