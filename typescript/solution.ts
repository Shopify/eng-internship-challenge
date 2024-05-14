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
