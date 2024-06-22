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
for (i = 0; i < cipherArray.length; i+=5) {
  const gridRow = cipherArray.slice(i, i+5);
  cipherGrid.push(gridRow);
}

function decrypt(message) {
  const digram = message.match(/.{1,2}/g);
}



