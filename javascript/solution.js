const encryptedMessage = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const key = "SUPERSPY";

const cipherArray = [];
for (i = 0; i < key.length; i++) {
  if (!cipherArray.includes(key[i])) {
    cipherArray.push(key[i]);
  }
}
const filler = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
for (i = 0; i < filler.length; i++) {
  if (!cipherArray.includes(filler[i]) && filler[i] !== 'J' && cipherArray.length < 25) {
    cipherArray.push(filler[i]);
  }
}

const cipherGrid = [];
for (i = 0; i < cipherArray.length; i += 5) {
  const gridRow = cipherArray.slice(i, i + 5);
  cipherGrid.push(gridRow);
}

function decrypt(message) {
  let decryptedMessage = '';
  const digram = message.match(/.{1,2}/g);
  digram.forEach(pair => {
    const rowA = cipherGrid.findIndex((array) => array.includes(pair[0]));
    const rowB = cipherGrid.findIndex((array) => array.includes(pair[1]));
    const columnA = cipherGrid[rowA].findIndex((letter) => letter === pair[0]);
    const columnB = cipherGrid[rowB].findIndex((letter) => letter === pair[1]);
    if (rowA === rowB) {
       decryptedLetterA = cipherGrid[rowA][columnA - 1] || cipherGrid[rowA][4];
       decryptedLetterB = cipherGrid[rowB][columnB - 1] || cipherGrid[rowB][4];
       decryptedMessage += decryptedLetterA + decryptedLetterB;
    } else if (columnA === columnB) {
       decryptedLetterA = cipherGrid[rowA - 1][columnA] || cipherGrid[4][columnA];
       decryptedLetterB = cipherGrid[rowB - 1][columnB] || cipherGrid[4][columnB];
       decryptedMessage += decryptedLetterA + decryptedLetterB;
    } else {
       decryptedLetterA = cipherGrid[rowA][columnB];
       decryptedLetterB = cipherGrid[rowB][columnA];
       decryptedMessage += decryptedLetterA + decryptedLetterB;
    }
  });
  for (i = 0; i < decryptedMessage.length; i++) {
      if (decryptedMessage[i] === 'X') {
          if (decryptedMessage[i-1] === decryptedMessage[i+1] || i === decryptedMessage.length - 1) {
              decryptedMessage = decryptedMessage.replace('X', '')
          }
      }
  }
  return decryptedMessage;
}

const decryptedMessage = decrypt(encryptedMessage);
console.log(decryptedMessage);