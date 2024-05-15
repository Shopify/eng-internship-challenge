import { createGrid } from '../solution';

describe('createPlayfairGrid', () => {
    it('should create a 5x5 grid with the keyword "SUPERSPY"', () => {
        const keyword = "SUPERSPY";
        const expectedGrid = [
            ['S', 'U', 'P', 'E', 'R'],
            ['Y', 'A', 'B', 'C', 'D'],
            ['F', 'G', 'H', 'I', 'K'],
            ['L', 'M', 'N', 'O', 'Q'],
            ['T', 'V', 'W', 'X', 'Z']
        ];

        const grid = createGrid(keyword);

        expect(grid).toEqual(expectedGrid);
    });

    it('should handle keywords with duplicate letters correctly', () => {
        const keyword = "BALLOON";
        const expectedGrid = [
            ['B', 'A', 'L', 'O', 'N'],
            ['C', 'D', 'E', 'F', 'G'],
            ['H', 'I', 'K', 'M', 'P'],
            ['Q', 'R', 'S', 'T', 'U'],
            ['V', 'W', 'X', 'Y', 'Z']
        ];

        const grid = createGrid(keyword);

        expect(grid).toEqual(expectedGrid);
    });

    it('should throw an error if the keyword is an empty string', () => {
        expect(() => createGrid("")).toThrow("Keyword cannot be empty.");
    });

    it('should throw an error if the keyword is not a string', () => {
        expect(() => createGrid(123 as any)).toThrow("Keyword must be a string.");
    });

    it('should throw an error if the keyword contains non-alphabetic characters', () => {
        expect(() => createGrid("SUP3R!@#")).toThrow("Keyword must only contain alphabetic characters.");
    });
});
