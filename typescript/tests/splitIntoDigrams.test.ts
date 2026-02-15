import { splitIntoDigrams } from '../solution';


describe('splitIntoDigrams', () => {
  it('should split the string "Monarchy" into digrams', () => {
      const input = "Monarchy";
      const expectedDigrams = ["MO", "NA", "RC", "HY"];

      const digrams = splitIntoDigrams(input);

      expect(digrams).toEqual(expectedDigrams);
  });

  it('should handle repeated letters by adding an "X" between them', () => {
      const input = "Hello";
      const expectedDigrams = ["HE", "LX", "LO"];

      const digrams = splitIntoDigrams(input);

      expect(digrams).toEqual(expectedDigrams);
  });

  it('should handle an odd-length string by adding an "X" at the end', () => {
      const input = "OpenAI";
      const expectedDigrams = ["OP", "EN", "AI"];

      const digrams = splitIntoDigrams(input);

      expect(digrams).toEqual(expectedDigrams);
  });
});
