const ENCRYPTED_TEXT = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const ENCRYPTION_KEY = "SUPERSPY";
const OMMITED_LETTER = "J";
const PADDING = "X";
const ROW_SIZE = 5;

interface Position {
    row: number;
    column: number;
}

class Decryptor {
    private readonly grid: string[][];
    private readonly padding: string;

    constructor(key: string, padding: string) {
        this.grid = this.generateKeyGrid(key);
        this.padding = padding;
    }

    public decode(encryptedText: string): string {
        let decryptedText = "";

        for (let i = 0; i < encryptedText.length; i += 2) {
            const pair = this.getPair(encryptedText, i);
            const decryptedPair = this.decryptPair(pair);
            decryptedText += decryptedPair;
        }

        return this.removePadding(decryptedText);
    }

    private getPair(string: string, index: number) {
        return (string[index] + string[index + 1]);
    }


    private decryptPair(pair: string): string {
        const [firstLetter, secondLetter] = pair;

        const firstPosition = this.findLetterPosition(firstLetter);
        const secondPosition = this.findLetterPosition(secondLetter);

        if (firstPosition.row === secondPosition.row) {
            return this.decryptRow(firstPosition, secondPosition);
        }

        if (firstPosition.column === secondPosition.column) {
            return this.decryptColumn(firstPosition, secondPosition);
        }

        return this.decryptRectangle(firstPosition, secondPosition);
    }

    private decryptRow(firstPosition: Position, secondPosition: Position): string {
        let result = "";

        result += this.grid[firstPosition.row][(firstPosition.column + ROW_SIZE - 1) % ROW_SIZE];
        result += this.grid[secondPosition.row][(secondPosition.column + ROW_SIZE - 1) % ROW_SIZE];

        return result;
    }


    private decryptColumn(firstPosition: Position, secondPosition: Position): string {
        let result = "";

        result += this.grid[(firstPosition.row + ROW_SIZE - 1) % ROW_SIZE][firstPosition.column];
        result += this.grid[(secondPosition.row + ROW_SIZE - 1) % ROW_SIZE][secondPosition.column];

        return result;
    }

    private decryptRectangle(firstPosition: Position, secondPosition: Position): string {
        let result = "";

        result += this.grid[firstPosition.row][secondPosition.column];
        result += this.grid[secondPosition.row][firstPosition.column];

        return result;
    }

    private findLetterPosition(letter: string): Position {
        for (let i = 0; i < this.grid.length; i++) {
            const row = this.grid[i];
            const columnIndex = row.indexOf(letter);
            if (columnIndex !== -1) {
                return { row: i, column: columnIndex };
            }
        }

        throw new Error(`Letter ${letter} not found in the grid!`);
    }

    private generateKeyGrid(key: string): string[][] {
        // Determine which letters are in the key
        const keySet = new Set<string>(key);
        const gridLetters = Array.from(keySet);
        let alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        alphabet = alphabet.replace(OMMITED_LETTER, "");

        for (const letter of alphabet) {
            if (!keySet.has(letter)) {
                gridLetters.push(letter);
            }

            if (gridLetters.length === (ROW_SIZE * ROW_SIZE)) {
                break;
            }
        }

        const grid: string[][] = [];

        for (let i = 0; i < gridLetters.length; i += ROW_SIZE) {
            const row = gridLetters.slice(i, i + ROW_SIZE);
            grid.push(row);
        }

        return grid;
    }

    private removePadding(text: string) {
        return text.replace(new RegExp(this.padding, "g"), "");
    }
}

function main() {
    const decryptor = new Decryptor(ENCRYPTION_KEY, PADDING);
    const decryptedText = decryptor.decode(ENCRYPTED_TEXT);
    console.log(decryptedText);
}

main();

