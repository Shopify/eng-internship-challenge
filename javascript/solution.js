//////////////////////////////////////////VARIABLES//////////////////////////////////////////
const message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const key = "SUPERSPY";
const rows = 5;
const cols = 5;
//2D array
let matrix = Array.from({ length: rows }, () => new Array(cols).fill(0));

//////////////////////////////////////////MAIN//////////////////////////////////////////
createMatrix(key, matrix);
let newMessage = decrypt(message, matrix);
console.log(removeX(newMessage));

//////////////////////////////////////////FUNCTIONS//////////////////////////////////////////

//check if a character has been used
function hasCharBeenUsed(usedChars, char) {
  let size = usedChars.length;
  for (let i = 0; i < size; i++) {
    if (usedChars[i] == char) {
      return true;
    }
  }
  return false;
}

//create a 5x5 matrix from the key
function createMatrix(key, matrix) {
  let usedChar = "J";
  let size = key.length;
  let counter = 0;
  //the alphabet to fill the matrix once the key has been used
  let char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  let index = 0;
  for (let row = 0; row < 5; row++) {
    for (let col = 0; col < 5; col++) {
      //fill the matrix with the key
      if (counter < size) {
        let charFromKey = key[counter];
        if (!hasCharBeenUsed(usedChar, charFromKey)) {
          matrix[row][col] = charFromKey;
          usedChar += charFromKey;
        } else {
          col--;
        }
        counter++;
      }
      //fill the matrix with the alphabet
      else {
        if (!hasCharBeenUsed(usedChar, char[index])) {
          matrix[row][col] = char[index];
          usedChar += char[index];
        } else {
          col--;
        }
        index++;
      }
    }
  }
}

//find the index of a character in the matrix
function indexInMatrix(char, matrix) {
  for (let row = 0; row < 5; row++) {
    for (let col = 0; col < 5; col++) {
      if (matrix[row][col] == char) {
        return [row, col];
      }
    }
  }
}

//decrypt the message
function decrypt(message, matrix) {
  let size = message.length;
  let newMessage = "";

  for (let i = 0; i < size; i += 2) {
    //find the index of a pair of characters from the message in the matrix
    let index1 = indexInMatrix(message[i], matrix);
    let index2 = indexInMatrix(message[i + 1], matrix);
    //if the characters are in the same row
    if (index1[0] == index2[0]) {
      newMessage += matrix[index1[0]][(index1[1] + 5 - 1) % 5];
      newMessage += matrix[index2[0]][(index2[1] + 5 - 1) % 5];
    }
    //if the characters are in the same column
    else if (index1[1] == index2[1]) {
      newMessage += matrix[(index1[0] + 5 - 1) % 5][index1[1]];
      newMessage += matrix[(index2[0] + 5 - 1) % 5][index2[1]];
    }
    //if the characters are in different rows and columns
    else {
      newMessage += matrix[index1[0]][index2[1]];
      newMessage += matrix[index2[0]][index1[1]];
    }
  }
  return newMessage;
}

function removeX(message) {
  let size = message.length;
  let newMessage = "";
  for (let i = 0; i < size; i++) {
    if (message[i] != "X") {
      newMessage += message[i];
    }
  }
  return newMessage;
}
