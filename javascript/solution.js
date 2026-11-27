/*
"Attention spy network! You've been assigned a task of the utmost importance! 
We've received an encrypted message from an agent in the field containing the password to a top secret club for super spies. 
The encrypted message reads as follows: "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV". 
We've been told if we can crack this code and give the password to the door-person at the corner of 32nd Street, 
we will gain access to the illustrious spy club Spy City!
We must get inside! 
However the password has been encrypted with an older system known as a Playfair Cipher. 
Our agent in the field says the key to the cipher is the string "SUPERSPY". 
However, for the life of us we cannot crack this code! 
Devise an application that can solve this encryption, get the password, 
and join us inside Spy City for what we are sure will be a night to remember!"
*/

/* ENCRYPTION
SAME ROW: MOVE RIGHT 1 LETTER
SAME COLUMN: MOVE DOWN 1 LETTER
RECTAGLE: USE OPPOSITE
*/

/* DECRYPTION
SAME ROW: MOVE LEFT 1 LETTER (1)
SAME COLUMN: MOVE UP 1 LETTER (2)
RECTAGLE: USE OPPOSITE (3)
*/

const ENCRYPTED_MESS = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const KEY = "SUPERSPY";

/*
let tableCipher = [
  ["S", "U", "P", "E", "R"],
  ["Y", "A", "B", "C", "D"],
  ["F", "G", "H", "I", "K"],
  ["L", "M", "N", "O", "Q"],
  ["T", "V", "W", "X", "Z"],
];
*/

const decryptMessage = decrypt(KEY, ENCRYPTED_MESS);
console.log(decryptMessage);

function decrypt(key, encryptedMessage) {
  let decryptMessage = "";
  const tableCipher = createTableCipher(key);

  for (let count = 0; count < encryptedMessage.length; count += 2) {
    const coupleString = encryptedMessage[count] + encryptedMessage[count + 1];

    const [row1, column1] = getColumnRow(tableCipher, coupleString[0]);
    const [row2, column2] = getColumnRow(tableCipher, coupleString[1]);

    let type = checkType(row1, column1, row2, column2);

    switch (type) {
      case 1:
        {
          let row = row1;
          const columns = [column1, column2];
          for (let i = 0; i < columns.length; i++) {
            let column = columns[i] - 1;

            if (column < 0) {
              column += 5;
            }

            decryptedChar = tableCipher[row][column];
            decryptMessage += decryptedChar;
          }
        }
        break;
      case 2: // SAME COLUMN
        {
          console.log(coupleString);
          let column = column1;
          const rows = [row1, row2];
          for (let i = 0; i < rows.length; i++) {
            let row = rows[i] - 1;

            if (row < 0) {
              column += 5;
            }

            decryptedChar = tableCipher[row][column];
            decryptMessage += decryptedChar;
          }
        }
        break;
      default:
        {
          //RECTANGLE
          let firstCharDecrypted = tableCipher[row1][column2];
          let secondCharDecrypted = tableCipher[row2][column1];
          decryptMessage += firstCharDecrypted + secondCharDecrypted;
        }
        break;
    }
  }
  return decryptMessage.replaceAll("X", "");
}

function createTableCipher(key) {
  let ALPHA_BET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  ALPHA_BET = ALPHA_BET.replace("J", "");
  ALPHA_BET = key + ALPHA_BET;
  ALPHA_BET = removeRepetive(ALPHA_BET);

  let cipherTable = [[], [], [], [], []];
  let count = 0;

  for (let i = 0; i < cipherTable.length; i++) {
    for (let j = 0; j < 5; j++) {
      cipherTable[i].push(ALPHA_BET[count]);
      count++;
    }
  }

  return cipherTable;
}

function removeRepetive(text) {
  let cleanedText = "";
  for (let i = 0; i < text.length; i++) {
    const currentChar = text[i];
    if (text.indexOf(currentChar) == -1) {
      cleanedText += currentChar;
    } else {
      cleanedText += currentChar;
      text = cleanedText + text.substring(i + 1).replaceAll(currentChar, "");
    }
  }
  return cleanedText;
}

function checkType(row1, column1, row2, column2) {
  if (row1 === row2) {
    return 1;
  }
  if (column1 === column2) {
    return 2;
  }
  return 3;
}

function getColumnRow(tableCipher, char) {
  for (let i = 0; i < tableCipher.length; i++) {
    for (let j = 0; j < tableCipher[0].length; j++) {
      if (tableCipher[i][j] === char) {
        return [i, j];
      }
    }
  }
}
