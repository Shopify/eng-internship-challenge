/* 
  Author: Keaton Lees
  Email: klees@uwaterloo.ca
*/

const alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"; // standard alphabet without 'J'

const createKeyTable = (key) => {
  let keyTable = [];
  let keySet = new Set();

  key.toUpperCase().replace(/J/g, "I"); // convert to uppercase and replace 'J' with 'I'
  const characters = key + alphabet; // combine key with alphabet

  characters.split("").forEach((char) => {
    if (!keySet.has(char)) {
      keySet.add(char);
      keyTable.push(char);
    }
  });

  // need to convert 1x25 keyTable into a 5x5 matrix
  let keyTableFormatted = [];
  const chunkSize = 5;
  for (let i = 0; i < keyTable.length; i += chunkSize) {
    const chunk = keyTable.slice(i, i + chunkSize);
    keyTableFormatted.push(chunk);
  }

  return keyTableFormatted;
};

const getKeyTableIndex = (keyTable, char) => {
  // loop through rows of keyTable
  for (let i = 0; i < keyTable.length; i++) {
    // if char found in row, return [i, j] index
    if (keyTable[i].includes(char)) {
      return [i, keyTable[i].indexOf(char)];
    }
  }

  // if char not found in keyTable, return [-1, -1]
  return [-1, -1];
};

const decrypt = (encryptedText, keyTable) => {
  let decryptedText = "";

  // loop through encryptedText 2 chars at a time
  for (let i = 0; i < encryptedText.length; i += 2) {
    // get chars
    let charA = encryptedText[i];
    let charB = encryptedText[i + 1];

    // get [row, col] index of each char
    let [rowA, colA] = getKeyTableIndex(keyTable, charA);
    let [rowB, colB] = getKeyTableIndex(keyTable, charB);

    if (rowA === rowB) {
      // same row -> shift left one index
      decryptedText += keyTable[rowA][(colA + 4) % 5];
      decryptedText += keyTable[rowA][(colB + 4) % 5];
    } else if (colA === colB) {
      // same col -> shift up one index
      decryptedText += keyTable[(rowA + 4) % 5][colA];
      decryptedText += keyTable[(rowB + 4) % 5][colA];
    } else {
      // rectangular swap
      decryptedText += keyTable[rowA][colB];
      decryptedText += keyTable[rowB][colA];
    }
  }

  return decryptedText;
};

const runDecryption = (encryptedText, key) => {
  const keyTable = createKeyTable(key);
  const decryptedText = decrypt(encryptedText, keyTable);

  // remove 'X' and spaces from decryptedText
  const formattedText = decryptedText.replace(/X/g, "").replace(/\s/g, "");
  return formattedText;
};

const sampleText = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const sampleKey = "SUPERSPY";

const result = runDecryption(sampleText, sampleKey);
console.log(result);
