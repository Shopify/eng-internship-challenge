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

const decrypt = (encryptedText, keyTable) => {};

const runDecryption = (encryptedText, key) => {
  const keyTable = createKeyTable(key);
  console.log(keyTable);
};

const sampleText = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const sampleKey = "SUPERSPY";

const result = runDecryption(sampleText, sampleKey);
// console.log(result);
