export function createGrid(keyword: string): string[][] {
  const grid: string[][] = [];
  const seen: Set<string> = new Set();
  const alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"; // J is omitted

  let row: string[] = [];
  for (const char of keyword.toUpperCase()) {
      if (!seen.has(char) && char !== 'J') {
          seen.add(char);
          row.push(char);
          if (row.length === 5) {
              grid.push(row);
              row = [];
          }
      }
  }

  for (const char of alphabet) {
      if (!seen.has(char)) {
          seen.add(char);
          row.push(char);
          if (row.length === 5) {
              grid.push(row);
              row = [];
          }
      }
  }

  if (row.length > 0) {
      grid.push(row);
  }

  return grid;
}

export function splitIntoDigrams(input: string): string[] {
  const digrams: string[] = [];
  let i = 0;

  while (i < input.length) {
      const currentChar = input[i].toUpperCase();
      const nextChar = i + 1 < input.length ? input[i + 1].toUpperCase() : 'X';

      if (currentChar === nextChar) {
          digrams.push(currentChar + 'X');
          i++;
      } else {
          digrams.push(currentChar + nextChar)
          i += 2;
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



