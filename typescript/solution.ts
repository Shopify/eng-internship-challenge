/**
 * Represents a position in the grid
 */
interface Position {
    row: number;
    column: number;
}

/**
 * Decryptor class that decrypts a message using the Playfair cipher
 * @param key Encryption key
 * @param padding Padding character
 * @returns Decrypted message
 * @example
 *
 * const decryptor = new Decryptor("KEY", "X");
 * const decryptedText = decryptor.decrypt("ENCRYPTED_TEXT");
 *
 */
class Decryptor {
    private readonly grid: string[][];
    private readonly padding: string;
    private readonly rowSize = 5;
    private readonly gridIndex: Map<string, Position>;
    private readonly ommitedLetter = "J";

    /**
     * Creates a new instance of the Decryptor class
     *
     * @param key The encryption key
     * @param padding The padding character used in the encryption
     */
    constructor(key: string, padding: string) {
        this.grid = this.generateKeyGrid(key);
        this.gridIndex = this.createGridIndex();
        this.padding = padding;
    }

    /**
     * Decrypts an encrypted message using the Playfair cipher
     *
     * @param encryptedText Encrypted message to decrypt
     * @returns Decrypted message
     */
    public decrypt(encryptedText: string): string {
        let decryptedText = "";

        for (let i = 0; i < encryptedText.length; i += 2) {
            const pair = this.getPair(encryptedText, i);
            const decryptedPair = this.decryptPair(pair);
            decryptedText += decryptedPair;
        }

        decryptedText = this.removePadding(decryptedText);
        return decryptedText;
    }

    /**
     * Decrypts an encrypted message using the Playfair cipher
     *
     * @param encryptedText Encrypted message to decrypt
     * @param key Encryption key
     * @param padding Padding character
     * @returns Decrypted message
     *
     * @example
     *
     * const decryptedText = Decryptor.decrypt("ENCRYPTED_TEXT", "KEY", "X");
     */
    public static decrypt(encryptedText: string, key: string, padding: string) {
        const decryptor = new Decryptor(key, padding);
        return decryptor.decrypt(encryptedText);
    }

    /**
     *
     * @param string String to get the pair from
     * @param index Index of the first letter of the pair
     * @returns A pair of letters from the string
     */
    private getPair(string: string, index: number) {
        return string[index] + string[index + 1];
    }

    /**
     *
     * @param pair Pair of letters to decrypt
     * @returns Decrypted pair of letters
     */
    private decryptPair(pair: string): string {
        const [firstLetter, secondLetter] = pair;

        const first = this.findLetterPosition(firstLetter);
        const second = this.findLetterPosition(secondLetter);

        if (first.row === second.row) {
            return this.decryptRow(first, second);
        }

        if (first.column === second.column) {
            return this.decryptColumn(first, second);
        }

        return this.decryptRectangle(first, second);
    }

    /**
     * Helper function to decrypt a pair of letters in the same row
     * @param first First letter position
     * @param second Second letter postion
     * @returns Decrypted pair of letters
     */
    private decryptRow(first: Position, second: Position): string {
        let result = "";

        result += this.grid[first.row][(first.column + this.rowSize - 1) % this.rowSize];
        result += this.grid[second.row][(second.column + this.rowSize - 1) % this.rowSize];

        return result;
    }

    /**
     * Helper function to decrypt a pair of letters in the same column
     * @param first First letter position
     * @param second Second letter postion
     * @returns Decrypted pair of letters
     */
    private decryptColumn(first: Position, second: Position): string {
        let result = "";

        result += this.grid[(first.row + this.rowSize - 1) % this.rowSize][first.column];
        result += this.grid[(second.row + this.rowSize - 1) % this.rowSize][second.column];

        return result;
    }

    /**
     * Helper function to decrypt a pair of letters neither in the same row nor column
     * @param first First letter position
     * @param second Second letter postion
     * @returns Decrypted pair of letters
     */
    private decryptRectangle(first: Position, second: Position): string {
        let result = "";

        result += this.grid[first.row][second.column];
        result += this.grid[second.row][first.column];

        return result;
    }

    /**
     *
     * @param letter Letter to find in the grid
     * @returns `Position` of the letter in the grid if found, else throws an error
     */
    private findLetterPosition(letter: string): Position {
        const position = this.gridIndex.get(letter);
        if (!position) {
            throw new Error(`Letter ${letter} not found in the grid!`);
        }

        return position;
    }

    /**
     *
     * @param key Encryption key
     * @returns A 5x5 grid generated from the encryption key for the Playfair cipher
     */
    private generateKeyGrid(key: string): string[][] {
        // Determine which letters are in the key
        const keySet = new Set<string>(key);
        const gridLetters = Array.from(keySet);
        let alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        alphabet = alphabet.replace(this.ommitedLetter, "");
        const maxLetters = this.rowSize * this.rowSize;

        // Add the remaining letters of the alphabet to the grid
        for (const letter of alphabet) {
            if (keySet.has(letter)) {
                continue;
            }

            gridLetters.push(letter);

            if (gridLetters.length === maxLetters) {
                break;
            }
        }

        const grid: string[][] = [];

        // Create the grid from the letters
        for (let i = 0; i < gridLetters.length; i += this.rowSize) {
            const row = gridLetters.slice(i, i + this.rowSize);
            grid.push(row);
        }

        return grid;
    }

    /**
     *
     * @returns A map of the letters in the grid to their positions
     */
    private createGridIndex(): Map<string, Position> {
        const gridIndex = new Map<string, Position>();

        for (let row = 0; row < this.grid.length; row++) {
            for (let column = 0; column < this.grid[row].length; column++) {
                const letter = this.grid[row][column];
                gridIndex.set(letter, { row, column });
            }
        }

        return gridIndex;
    }

    /**
     *
     * @param text Text to remove padding from
     * @returns Text with all instances of the padding character removed
     */
    private removePadding(text: string) {
        return text.replace(new RegExp(this.padding, "g"), "");
    }
}

const ENCRYPTED_TEXT = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const ENCRYPTION_KEY = "SUPERSPY";
const PADDING = "X";

function main() {
    const decryptor = new Decryptor(ENCRYPTION_KEY, PADDING);
    const decryptedText = decryptor.decrypt(ENCRYPTED_TEXT);
    console.log(decryptedText);
}

main();
