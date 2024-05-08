let key = "SUPERSPY"
let secret = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

const rowMax = 5
const columnMax = 5

const alphabet = [..."ABCDEFGHIKLMNOPQRSTUVWXYZ"];
secret = secret.match(/.{1,2}/g)
key = [...key];

// Empty solution
const solution = []

// Creates an array that represents the grid
let grid = [];
let inner = [];

// Creates a dictionary that tracks if an alphabet has been added to the Grid. E.g. dict = {'A': false, 'B': true, ...}
let alphDict = new Map();

for (i = 0; i < alphabet.length; i++) {
  alphDict.set(alphabet[i], false);
}

// Updates the dictionary and the grid with the 'KEY' values
for (i = 0; i < key.length; i++) {

  // Creates a new inner list if one is full (max 5 integers per row)
  if (i % rowMax == 0 && inner.length != 0) {
    grid.push(inner)
    inner = [];
  }
  // Adds the alphabet of the 'KEY' that has not been added to the grid yet
  if (alphDict.get(key[i]) == false) {
    alphDict.set(key[i], true);
    inner.push(key[i])
  }
}

// Add the rest of the alphabet to the grid
for (i = 0; i < alphabet.length; i++) {

  if (inner.length == rowMax) {
    grid.push(inner)
    inner = [];
  }

  if (alphDict.get(alphabet[i]) == false) {
    alphDict.set(alphabet[i], true);
    inner.push(alphabet[i])
  }
}

// Push the last inner list to the grid; it could be an empty list or a partially filled list with characters from KEY
grid.push(inner)

// Map the letter to their coordinates in the grid
const letterPos = new Map();

for (i = 0; i < rowMax; i++) {
  for (j = 0; j < columnMax; j++) {
    letterPos.set(grid[i][j], [i, j])
  }
}

// Start deciphering the cipher
for (i = 0; i < secret.length; i++) {

  // Get the coordinates of the letter in the grid
  let letterXCoord = letterPos.get(secret[i][0])
  let letterYCoord = letterPos.get(secret[i][1])

  // Check if the letters are in the same row
  if (letterXCoord[0] == letterYCoord[0]) {

    let getLetterX = grid[letterXCoord[0]][((letterXCoord[1] - 1) + rowMax) % rowMax]
    let getLetterY = grid[letterYCoord[0]][((letterYCoord[1] - 1) + rowMax) % rowMax]
    solution.push(getLetterX)
    solution.push(getLetterY)
  }

  // Check if the letters are in the same column
  else if (letterXCoord[1] == letterYCoord[1]) {
    let getLetterX = grid[((letterXCoord[0] - 1) + rowMax) % rowMax][letterXCoord[1]]
    let getLetterY = grid[((letterYCoord[0] - 1) + rowMax) % rowMax][letterYCoord[1]]
    solution.push(getLetterX)
    solution.push(getLetterY)
  }

  // Letter are diagonal to each other
  else {

    let getLetterX = grid[letterXCoord[0]][letterYCoord[1]]
    let getLetterY = grid[letterYCoord[0]][letterXCoord[1]]
    solution.push(getLetterX)
    solution.push(getLetterY)
  }
}

const revealed = solution.filter(bogusChar => bogusChar !== 'X').join("").toUpperCase();
console.log(revealed)