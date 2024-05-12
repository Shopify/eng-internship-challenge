/**
 * Author: Keaton Lees
 * Email: klees@uwaterloo.ca
 *
 */

const alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"; // standard alphabet without 'J'

/**
 * createKeyTable: Creates a 5x5 Key Table based on a secret Key
 *
 * Args:
 * - key (str): The secret Key to make the Key Table
 *
 * Returns:
 * - Array: 5x5 array of characters in format of a Key Table
 *
 */
const createKeyTable = (key) => {
  // define variables
  let keyTable = [];
  let keySet = new Set();

  // convert key to uppercase and replace 'J' with 'I', combine with alphabet
  key.toUpperCase().replace(/J/g, "I");
  const characters = key + alphabet;

  // split each character and add to set/table if not seen before
  characters.split("").forEach((char) => {
    if (!keySet.has(char)) {
      keySet.add(char);
      keyTable.push(char);
    }
  });

  // need to convert 1x25 keyTable into a 5x5 matrix
  let keyTableFormatted = [];
  const chunkSize = 5;
  // slice every 5 elements
  for (let i = 0; i < keyTable.length; i += chunkSize) {
    const chunk = keyTable.slice(i, i + chunkSize);
    keyTableFormatted.push(chunk);
  }

  // return formatted Key Table
  return keyTableFormatted;
};

/**
 * getKeyTableIndex: Gets the index of row and col given Key Table and target char
 *
 * Args:
 * - keyTable (Array): The Key Table to be searched
 * - char (str): The target char
 *
 * Returns:
 * - Array: The index of char in Key Table returned as [row, col]
 *
 */
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

/**
 * decrypt: Decrypts an Encrypted Text given a Key Table using a PlayFair Cipher
 *
 * Args:
 * - encryptedText (str): The Encrypted Text to be decrypted
 * - keyTable (Array): The Key Table to be used in decrypting
 *
 * Returns:
 * - decryptedText (str): The result of decrypting the Encrypted Text using the given Key Table
 *
 */
const decrypt = (encryptedText, keyTable) => {
  let decryptedText = "";

  // loop through encryptedText 2 chars at a time
  for (let i = 0; i < encryptedText.length; i += 2) {
    // get chars from text
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

  // return result of decryption
  return decryptedText;
};

/**
 * runDecryption: Processes the PlayFair Cipher given a sample text and sample key
 *
 * Args:
 * - encryptedText (str): The Encrypted Text to be decrypted
 * - key (str): The secret Key used to decrypt the text
 *
 * Returns:
 * - formattedText (str): The result of the decryption, formatted to remove 'X' and spaces
 *
 */
const runDecryption = (encryptedText, key) => {
  // create Key Table
  const keyTable = createKeyTable(key);

  // decrypt text based on generated Key Table
  const decryptedText = decrypt(encryptedText, keyTable);

  // remove 'X' and spaces from decryptedText
  const formattedText = decryptedText.replace(/X/g, "").replace(/\s/g, "");

  // return final formatted result
  return formattedText;
};

// provided encrypted text and related key
const sampleText = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const sampleKey = "SUPERSPY";

const result = runDecryption(sampleText, sampleKey);
console.log(result);
// Output: HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA (the fear of long words)
