const cipher = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const key = "SUPERSPY";

// function to generate decryption key/table
function generateKeyTable(key) {
  key = key
    .replace(/[^A-Z]/g, "")
    .toUpperCase()
    .replace(/J/g, "I");
  let keyTable = "";
  let alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ";

  // fill table with key and remianing alphabet
  for (let char of key) {
    if (!keyTable.includes(char)) {
      keyTable += char;
    }
  }

  for (let char of alphabet) {
    if (!keyTable.includes(char)) {
      keyTable += char;
    }
  }
  return keyTable;
}

// function to decrypt digram
function decryptDigram(keyTable, digram) {
  let decryptedDigraph = "";

  // find position of digram characters in key table
  let pos1 = keyTable.indexOf(digram[0]);
  let pos2 = keyTable.indexOf(digram[1]);

  //handle same characters
  if (pos1 === pos2) {
    decryptedDigraph += keyTable[(pos1 + 1) % 25];
    decryptedDigraph += keyTable[pos2];
    return decryptedDigraph;
  }

  // decrypt based on positions
  if (pos1 % 5 === pos2 % 5) {
    // same column
    decryptedDigraph += keyTable[(pos1 - 5 + 25) % 25];
    decryptedDigraph += keyTable[(pos2 - 5) % 25];
  } else if (Math.floor(pos1 / 5) === Math.floor(pos2 / 5)) {
    // same row
    decryptedDigraph += keyTable[((pos1 - 1) % 5) + Math.floor(pos1 / 5) * 5];
    decryptedDigraph += keyTable[((pos2 - 1) % 5) + Math.floor(pos2 / 5) * 5];
  } else {
    // rectangle case
    decryptedDigraph += keyTable[(pos2 % 5) + Math.floor(pos1 / 5) * 5];
    decryptedDigraph += keyTable[(pos1 % 5) + Math.floor(pos2 / 5) * 5];
  }

  decryptedDigraph = decryptedDigraph.replace(/X/g, "");
  return decryptedDigraph;
}

// function to decrypt Playfair Cipher

function decryptCipher(cipher, key) {
  let plaintext = "";
  let keyTable = generateKeyTable(key);

  //decrypt digrams
  for (let i = 0; i < cipher.length; i += 2) {
    let digram = cipher.substr(i, 2);
    let decryptedDigram = decryptDigram(keyTable, digram);
    plaintext += decryptedDigram;
  }

  return plaintext;
}

console.log(decryptCipher(cipher, key));

//input: "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
//key is a string: "SUPERSPY"
//output: "HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA"
