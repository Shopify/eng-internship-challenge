// Function to generate the key square
function generateKeySquare(key) {
  key = key.toUpperCase().replace("J", "I");
  let keySquare = "";
  for (let char of key) {
    if (!keySquare.includes(char)) {
      keySquare += char;
    }
  }
  const alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ";
  for (let char of alphabet) {
    if (!keySquare.includes(char)) {
      keySquare += char;
    }
  }
  return keySquare;
}

// Function to decrypt the message
function decryptPlayfair(message, key) {
  const keySquare = generateKeySquare(key);
  let decryptedMessage = "";
  // Prepare message
  message = message.toUpperCase().replace(/J/g, "I").replace(/ /g, "");
  // Adjust message length if odd
  if (message.length % 2 !== 0) {
    message += "X";
  }
  // Decrypt
  for (let i = 0; i < message.length; i += 2) {
    const pair = message.substring(i, i + 2);
    const row1 = Math.floor(keySquare.indexOf(pair[0]) / 5);
    const col1 = keySquare.indexOf(pair[0]) % 5;
    const row2 = Math.floor(keySquare.indexOf(pair[1]) / 5);
    const col2 = keySquare.indexOf(pair[1]) % 5;
    if (row1 === row2) {
      decryptedMessage +=
        keySquare[row1 * 5 + ((col1 + 4) % 5)] +
        keySquare[row2 * 5 + ((col2 + 4) % 5)];
    } else if (col1 === col2) {
      decryptedMessage +=
        keySquare[((row1 + 4) % 5) * 5 + col1] +
        keySquare[((row2 + 4) % 5) * 5 + col2];
    } else {
      decryptedMessage +=
        keySquare[row1 * 5 + col2] + keySquare[row2 * 5 + col1];
    }
  }
  return decryptedMessage;
}

// Encrypted message and key
const encryptedMessage = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const key = "SUPERSPY";

// Decrypt the message
const decryptedMessage = decryptPlayfair(encryptedMessage, key);

// the decryptedMessage above will return our answer to us
// but it will include the character 'X' (which we don't want)
// to eliminate this, i used the regex expression '/X/g' by replacing it with an empty string
// then i output the value

console.log(decryptedMessage.replace(/X/g, ""));
