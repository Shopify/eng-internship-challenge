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