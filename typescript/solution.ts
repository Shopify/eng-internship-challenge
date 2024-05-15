const GRID_ROW_LENGTH = 5

export function createGrid(keyword: string): string[][] {
  if (typeof keyword !== 'string') {
    throw new Error('Keyword must be a string.');
  }
  
  if (!keyword) {
      throw new Error("Keyword cannot be empty.");
  }

  if (!/^[A-Z]+$/i.test(keyword)) {
    throw new Error('Keyword must only contain alphabetic characters.');
  }

  const grid: string[][] = [];
  const lettersAdded: Set<string> = new Set();
  const ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"; // J is omitted to fit the grid

  keyword = keyword.toUpperCase();

  function addCharactersToGrid(
    source: string,
    lettersAdded: Set<string>,
    grid: string[][],
    currentRow: string[]
  ): string[] {
    for (const char of source) {
        if (!lettersAdded.has(char) && char !== 'J') {
            lettersAdded.add(char);
            currentRow.push(char);
            if (currentRow.length === GRID_ROW_LENGTH) {
                grid.push(currentRow);
                currentRow = [];
            }
        }
    }
    return currentRow;
  }

  let currentRow: string[] = [];
  currentRow = addCharactersToGrid(keyword, lettersAdded, grid, currentRow);
  currentRow = addCharactersToGrid(ALPHABET, lettersAdded, grid, currentRow);

  if (currentRow.length > 0) {
      grid.push(currentRow);
  }

  return grid;
}

export function splitIntoDigrams(message: string): string[] {
  const digrams: string[] = [];
  let index = 0;

  while (index < message.length) {
      const currentChar = message[index].toUpperCase();
      const nextChar = index + 1 < message.length ? message[index + 1].toUpperCase() : 'X';

      if (currentChar === nextChar) {
          digrams.push(currentChar + 'X');
          index++;
      } else {
          digrams.push(currentChar + nextChar)
          index += 2;
      }
  }

  return digrams
}

export function decryptDigram(digram: string, grid: string[][]): string {
  const [char1, char2] = digram.toUpperCase().split('');
  let decryptedDigram = '';

  let pos1: [number, number] | undefined;
  let pos2: [number, number] | undefined;
  for (let i = 0; i < grid.length; i++) {
      const row = grid[i];
      const col1 = row.indexOf(char1);
      const col2 = row.indexOf(char2);
      if (col1 !== -1) pos1 = [i, col1];
      if (col2 !== -1) pos2 = [i, col2];
  }

  if (pos1 && pos2) {
      if (pos1[0] === pos2[0]) { // Same row
          decryptedDigram += grid[pos1[0]][(pos1[1] - 1 + 5) % 5]; 
          decryptedDigram += grid[pos2[0]][(pos2[1] - 1 + 5) % 5]; 
      } else if (pos1[1] === pos2[1]) { // Same column
          decryptedDigram += grid[(pos1[0] - 1 + 5) % 5][pos1[1]]; 
          decryptedDigram += grid[(pos2[0] - 1 + 5) % 5][pos2[1]]; 
      } else { // Not same row or column
          decryptedDigram += grid[pos1[0]][pos2[1]];
          decryptedDigram += grid[pos2[0]][pos1[1]];
      }
  }

  return decryptedDigram;
}

export function assembleDecryptedMessage(decryptedDigrams: string[]): string {
  let decryptedMessage = "";

  for (const digram of decryptedDigrams) {
      decryptedMessage += digram.toUpperCase();
      
  }

  decryptedMessage = decryptedMessage.replace(/X/g, '');

  return decryptedMessage;
}

function decryptedMessage(keyword: string, encryptedMessage: string): string {

  const grid = createGrid(keyword);

  const encryptedDigrams = splitIntoDigrams(encryptedMessage);

  const decryptedDigrams = encryptedDigrams.map(digram => decryptDigram(digram, grid));

  const finalMessage = assembleDecryptedMessage(decryptedDigrams);

  return finalMessage
}

console.log(decryptedMessage("SUPERSPY", "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"));