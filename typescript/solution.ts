const cipherKey = "SUPERSPY";
const encryptedText = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";

const generateGrid = (key: string) => {
  // J is omitted by default
  // If J is in the key, then the last letter that doesn't show up in the key is omitted
  const alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ".split('');
  const keyArr = key.split('');
  
  const allChars = keyArr.concat(alphabet);
  let seenChars : string[] = []
  let cipherChars : string[] = []
  for (const c of allChars) {
    if(seenChars.indexOf(c) === -1) {
      cipherChars.push(c);
      seenChars.push(c);
    }
  }

  const grid : string[][] = [];
  cipherChars.splice(25);
  while(cipherChars.length) {
    grid.push(cipherChars.splice(0, 5));
  }

  return grid;
}

const decryptText = (key: string, encrypted: string) => {
  const grid = generateGrid(key);
  const gridHeight = grid.length;
  const gridWidth = grid[0].length;
  
  const digraph = encrypted.match(/../g) || [];
  
  const getCharPosition = (c: string) => {
    for(let i = 0; i<grid.length; ++i) {
      for(let j = 0; j<grid[0].length; ++j) {
        if(grid[i][j] === c) return {y: i, x: j};
      }
    }
    throw Error("Character not found");
  }

  const decryptedText = digraph.map((charPair: string) => {
    const getShiftUpIndex = (y: number) => {
      return (y - 1 + gridHeight) % gridHeight;
    }

    const getShiftLeftIndex = (x: number) => {
      return (x - 1 + gridWidth) % gridWidth;
    }

    const {x: x1, y: y1} = getCharPosition(charPair[0]);
    const {x: x2, y: y2} = getCharPosition(charPair[1]);
    
    if(x1 == x2) {
      // Same column, shift up
      return grid[getShiftUpIndex(y1)][x1] + grid[getShiftUpIndex(y2)][x2];
    } else if(y1 == y2) {
      //Same row, shift left
      return grid[y1][getShiftLeftIndex(x1)] + grid[y2][getShiftLeftIndex(x2)];
    } else {
      return grid[y1][x2] + grid[y2][x1];
    }
  }).join('');
  
  const decryptedFiltered = decryptedText.replace(/X/g, '');

  return decryptedFiltered;
}

const decrypted = decryptText(cipherKey, encryptedText);
console.log(decrypted);