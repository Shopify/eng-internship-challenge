var key = "SUPERSPY";
var ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
deciphertext = decipher(key, ciphertext.toUpperCase());
console.log(deciphertext);

/**
 * Function to generate the 5x5 key square
 * @param {character[]} key the key to create the playfair square
 * @return {character[][]} the playfair square
 */
function creatSquare(key) {
  const rows = 5;
  const cols = 5;
  const playfairSquare = new Array(rows);
  for (let i = 0; i < rows; i++) {
    playfairSquare[i] = new Array(cols);
  }
  let charSet = new Set();
  for (let i = 0; i < key.length; i++) {
    charSet.add(key[i]);
  }
  let cnt = 0;
  for (let value of charSet) {
    let rowIdx = Math.floor(cnt / 5);
    let colIdx = cnt % 5;
    playfairSquare[rowIdx][colIdx] = value;
    cnt++;
  }
  for (let i = 0; i < 26 && cnt < 25; i++) {
    let char = String.fromCharCode(65 + i);
    if (char === "J") {
      continue;
    }
    if (!charSet.has(char)) {
      let rowIdx = Math.floor(cnt / 5);
      let colIdx = cnt % 5;
      playfairSquare[rowIdx][colIdx] = char;
      cnt++;
    }
  }
  return playfairSquare;
}

/**
 * Function to store the rowIdx and colIdx in the square in a Map
 * to fastly find the position of a character in the square in O(1) time consuming
 * key-value pair example: "S": [0, 0], "U": [0, 1], "P": [0, 2], "E": [0, 3], "R": [0, 4]
 * @param {character[][]} playfairSquare the playfair square created by the key
 * @return {Map()} the playfair square map
 */
function createSquareMap(playfairSquare) {
  let playfairSquareMap = new Map();
  for (let i = 0; i < 5; i++) {
    for (let j = 0; j < 5; j++) {
      playfairSquareMap.set(playfairSquare[i][j], [i, j]);
    }
  }
  return playfairSquareMap;
}

/**
 * decipher
 * @param {character[]} key the key to create the playfair square
 * @param {character[]} ciphertext the text to be deciphered
 * @return {character[]} the deciphered text with non-processed 'X'
 */
function decipher(key, ciphertext) {
  let playfairSquare = creatSquare(key);
  let playfairSquareMap = createSquareMap(playfairSquare);
  let result = "";
  for (let i = 0; i < ciphertext.length; i += 2) {
    let char1 = ciphertext[i];
    let char2 = ciphertext[i + 1];
    let row1 = 0;
    let col1 = 0;
    let row2 = 0;
    let col2 = 0;
    [row1, col1] = playfairSquareMap.get(char1);
    [row2, col2] = playfairSquareMap.get(char2);
    let p1 = '', p2 = '';
    if (row1 === row2) {
      p1 = playfairSquare[row1][(col1 + 4) % 5];
      p2 = playfairSquare[row2][(col2 + 4) % 5];
    } else if (col1 === col2) {
      p1 = playfairSquare[(row1 + 4) % 5][col1];
      p2 = playfairSquare[(row2 + 4) % 5][col2];
    } else {
      p1 = playfairSquare[row1][col2];
      p2 = playfairSquare[row2][col1];
    }
    result += p1;
    result += p2;
  }
  result = processResult(result);
  return result;
}

/**
 * Function to remove the 'X' between the same characters and the last 'X' in the text
 * @param {character[]} str the text to be processed
 * @return {character[]} the text processed
 */
function processResult(str) {
  result = "";
  for (let i = 0; i < str.length; i++) {

    if (i > 0 && i + 1 < str.length &&
      str[i] === 'X' && str[i - 1] === str[i + 1]) {
      continue;
    }
    if (i == str.length - 1 && str[i] === 'X') {
      continue;
    }
    result += str[i];
  }
  return result;
}


