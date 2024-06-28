const ENCRYPTED_TEXT = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const ENCRYPTION_KEY = "SUPERSPY";
const OMMITED_LETTER = "J";
const PADDING = "X";
const ROW_SIZE = 5;

interface Position {
    row: number;
    column: number;
}

console.log(decode(ENCRYPTED_TEXT, ENCRYPTION_KEY, PADDING));

function decode(encryptedText: string, encryptionKey: string, padding: string): string {
    const grid = generateKeyGrid(encryptionKey);
    let decryptedText = "";

    for (let i = 0; i < encryptedText.length; i += 2) {
        const pair = getPair(encryptedText, i);
        const decryptedPair = decryptPair(pair, grid);
        decryptedText += decryptedPair;
    }

    return removePadding(decryptedText, padding);
}

function getPair(string: string, index: number) {
    return (string[index] + string[index + 1]);
}

function decryptPair(pair: string, grid: string[][]): string {
    const [firstLetter, secondLetter] = pair;

    const firstLetterPosition = findLetterPosition(grid, firstLetter);
    const secondLetterPosition = findLetterPosition(grid, secondLetter);

    if (firstLetterPosition.row === secondLetterPosition.row) {
        return decryptRow(grid, firstLetterPosition, secondLetterPosition);
    }

    if (firstLetterPosition.column === secondLetterPosition.column) {
        return decryptColumn(grid, firstLetterPosition, secondLetterPosition);
    }

    return decryptRectangle(grid, firstLetterPosition, secondLetterPosition);
}


function decryptRow(grid: string[][], firstPosition: Position, secondPosition: Position): string {
    let result = "";

    result += grid[firstPosition.row][(firstPosition.column + ROW_SIZE - 1) % ROW_SIZE];
    result += grid[secondPosition.row][(secondPosition.column + ROW_SIZE - 1) % ROW_SIZE];

    return result;
}


function decryptColumn(grid: string[][], firstPosition: Position, secondPosition: Position): string {
    let result = "";

    result += grid[(firstPosition.row + ROW_SIZE - 1) % ROW_SIZE][firstPosition.column];
    result += grid[(secondPosition.row + ROW_SIZE - 1) % ROW_SIZE][secondPosition.column];

    return result;
}

function decryptRectangle(grid: string[][], firstPosition: Position, secondPosition: Position): string {
    let result = "";

    result += grid[firstPosition.row][secondPosition.column];
    result += grid[secondPosition.row][firstPosition.column];

    return result;
}

function findLetterPosition(grid: string[][], letter: string): Position {
    for (let i = 0; i < grid.length; i++) {
        const row = grid[i];
        const columnIndex = row.indexOf(letter);
        if (columnIndex !== -1) {
            return { row: i, column: columnIndex };
        }
    }

    throw new Error(`Letter ${letter} not found in the grid!`);
}

/**
 * 
 * @param key 
 * @returns 
 */
function generateKeyGrid(key: string): string[][] {
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

function removePadding(text: string, padding: string) {
    return text.replace(new RegExp(padding, "g"), "");
}

