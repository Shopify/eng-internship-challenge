//encrypted message
const ENCRYPTED_MESSAGE = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";

//cipher key
const CIPHER_KEY = "SUPERSPY";

function decryptMessage(encrypted, key) {
  //establish a Set of letters starting with the cipher key,
  const letterSet = new Set(key.split(""));

  //add the remaining alphabet letters that have not been used yet, omitting J so that there are 25 letters in total
  const alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ";
  alphabet.split("").forEach((letter) => {
    letterSet.add(letter);
  });

  //turn set into an array to facilitate removing one letter at a time
  const letterArray = Array.from(letterSet);

  //take the cipher key and turn it into a 5x5 matrix
  const CIPHER_MATRIX = [];

  for (let row = 0; row < 5; row++) {
    CIPHER_MATRIX.push([]);

    for (let col = 0; col < 5; col++) {
      CIPHER_MATRIX[row].push(letterArray.shift());
    }
  }

  //break the encrypted message into letter pairs
  const encryptedLetterPairs = [];
  const encryptedArray = encrypted.split("");

  console.log(CIPHER_MATRIX);

  for (let i = 0; i < encryptedArray.length; i += 2) {
    encryptedLetterPairs.push([encryptedArray[i], encryptedArray[i + 1]]);
  }

  let decryptedMessage = [];

  //iterate through letter pairings to check for decrypting conditions
  encryptedLetterPairs.forEach((letterPair) => {
    console.log(letterPair[0], letterPair[1]);

    //check letter pair to see if they are in the same column of the matrix
    for (let row = 0; row < CIPHER_MATRIX.length; row++) {
      const thisRow = CIPHER_MATRIX[row];
      const lettersAreInRow = thisRow.includes(letterPair[0]) && thisRow.includes(letterPair[1]);
      
      console.log(thisRow, letterPair[0], letterPair[1], lettersAreInRow);
      if (lettersAreInRow) {
        //add decrypted letters to decryptedMessage by
        //getting index of letterPair[0] and letterPair[1] and taking one index to the left, wrapping around as needed
        const encryptedPair1RowIndex = thisRow.indexOf(letterPair[0]);
        const encryptedPair2RowIndex = thisRow.indexOf(letterPair[1]);

        const decryptedPair1RowIndex = encryptedPair1RowIndex - 1 >= 0? encryptedPair1RowIndex - 1: encryptedPair1RowIndex + 4;
        const decryptedPair2RowIndex = encryptedPair2RowIndex - 1 >= 0? encryptedPair2RowIndex - 1: encryptedPair2RowIndex + 4;
        
        console.log(thisRow[encryptedPair1RowIndex], thisRow[encryptedPair2RowIndex]);
        console.log(thisRow[decryptedPair1RowIndex], thisRow[decryptedPair2RowIndex], "\n");

        decryptedMessage += thisRow[decryptedPair1RowIndex];
        decryptedMessage += thisRow[decryptedPair2RowIndex];
        
        // console.log(decryptedPairIndex[0], decryptedPairIndex[1]);

        break;
      }
    }

    /*
    [ 'S', 'U', 'P', 'E', 'R' ],
    [ 'Y', 'A', 'B', 'C', 'D' ],
    [ 'F', 'G', 'H', 'I', 'K' ],
    [ 'L', 'M', 'N', 'O', 'Q' ],
    [ 'T', 'V', 'W', 'X', 'Z' ]
    */

    //if yes, then move up one row to get decrypted letters, wrapping around if needed

    //else check letter pair to see if they are in same row of the matrix

    //if yes, then move left  one row to get decrypted letters, wrapping around if needed

    //else establish the box size between these letters as the corner points and get the other corners as the decrypted letters
  });

  //output must be in upper case, not include spaces, the letter X, or special characters

  return decryptedMessage;
}

//decrypted message
const DECRYPTED_MESSAGE = decryptMessage(ENCRYPTED_MESSAGE, CIPHER_KEY);

//output decrypted message
console.log(DECRYPTED_MESSAGE);
