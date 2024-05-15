import { decryptDigram } from '../solution';


describe('decryptDigram', () => {
  const grid: string[][] = [
      ['S', 'U', 'P', 'E', 'R'],
      ['Y', 'A', 'B', 'C', 'D'],
      ['F', 'G', 'H', 'I', 'K'],
      ['L', 'M', 'N', 'O', 'Q'],
      ['T', 'V', 'W', 'X', 'Z']
  ];

  it('should decrypt digram "MO" to "LN"', () => {
      const encryptedDigram = 'MO';
      const expectedDecryptedDigram = 'LN';

      const decryptedDigram = decryptDigram(encryptedDigram, grid);

      expect(decryptedDigram).toEqual(expectedDecryptedDigram);
  });

  it('should decrypt digram "RC" to "ED"', () => {
      const encryptedDigram = 'RC';
      const expectedDecryptedDigram = 'ED';

      const decryptedDigram = decryptDigram(encryptedDigram, grid);

      expect(decryptedDigram).toEqual(expectedDecryptedDigram);
  });

  it('should decrypt digram "EN" to "PO"', () => {
      const encryptedDigram = 'EN';
      const expectedDecryptedDigram = 'PO';

      const decryptedDigram = decryptDigram(encryptedDigram, grid);

      expect(decryptedDigram).toEqual(expectedDecryptedDigram);
  });
});
