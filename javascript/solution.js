//encrypted message
const ENCRYPTED_MESSAGE = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";

//cipher key
const CIPHER_KEY = "SUPERSPY";

function decryptMessage(encrypted, key) {
  //establish a Set of letters starting with the cipher key,
  const letterSet = new Set(key.split(""));

  //add the remaining alphabet letters that have not been used yet, omitting J so that there are 25 letters in total
  const ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ";
  ALPHABET.split("").forEach((letter) => {
    letterSet.add(letter);
  });

  //turn set into an array to facilitate removing one letter at a time
  const letterArray = Array.from(letterSet);

  //take the cipher key and turn it into a 5x5 matrix
  const cipherMatrix = [];

  for (let row = 0; row < 5; row++) {
    cipherMatrix.push([]);

    for (let col = 0; col < 5; col++) {
      cipherMatrix[row].push(letterArray.shift());
    }
  }

  //the cipherMatrix rows are easily accessible, now build a collection of its columns for similar ease of iteration below
  const cipherColumns = [];

  for (let col = 0; col < 5; col++) {
    cipherColumns.push([]);
    for (let row = 0; row < 5; row++) {
      cipherColumns[col].push(cipherMatrix[row][col]);
    }
  }

  //break the encrypted message into letter pairs
  const encryptedLetterPairs = [];
  const encryptedArray = encrypted.split("");

  for (let i = 0; i < encryptedArray.length; i += 2) {
    encryptedLetterPairs.push([encryptedArray[i], encryptedArray[i + 1]]);
  }

  //iterate through letter pairings to check for decrypting conditions
  let decryptedMessage = "";

  encryptedLetterPairs.forEach((letterPair) => {
    //if both letters are in the same row, then move up left one column to get decrypted letters, wrapping around if needed

    let lettersAreInRow;
    let lettersAreInColumn;

    console.log("checking rows");
    //check letter pair to see if they are in the same row of the matrix
    for (let row = 0; row < cipherMatrix.length; row++) {
      const thisRow = cipherMatrix[row];
      lettersAreInRow =
        thisRow.includes(letterPair[0]) && thisRow.includes(letterPair[1]);

      console.log(thisRow, letterPair[0], letterPair[1], lettersAreInRow);
      if (lettersAreInRow) {
        //add decrypted letters to decryptedMessage by
        //getting index of letterPair[0] and letterPair[1] and taking one index to the left, wrapping around as needed
        const encryptedPair1RowIndex = thisRow.indexOf(letterPair[0]);
        const encryptedPair2RowIndex = thisRow.indexOf(letterPair[1]);

        const decryptedPair1RowIndex =
          encryptedPair1RowIndex - 1 >= 0
            ? encryptedPair1RowIndex - 1
            : encryptedPair1RowIndex + 4;

        const decryptedPair2RowIndex =
          encryptedPair2RowIndex - 1 >= 0
            ? encryptedPair2RowIndex - 1
            : encryptedPair2RowIndex + 4;

        console.log(
          thisRow[encryptedPair1RowIndex],
          thisRow[encryptedPair2RowIndex]
        );
        console.log(
          thisRow[decryptedPair1RowIndex],
          thisRow[decryptedPair2RowIndex],
          "\n"
        );

        decryptedMessage +=
          thisRow[decryptedPair1RowIndex] + thisRow[decryptedPair2RowIndex];

        //if the letters have been found in the same row, the rest of the search for columns can be skipped for this pair
        break;
      }
    }

    if (!lettersAreInRow){
        console.log("checking columns");

        //if not in the same row, then check letter pair to see if they are in the same column of the matrix
        for (let col = 0; col < cipherColumns.length; col++) {
          const thisColumn = cipherColumns[col];
          lettersAreInCol =
            thisColumn.includes(letterPair[0]) &&
            thisColumn.includes(letterPair[1]);
    
          console.log(thisColumn, letterPair[0], letterPair[1], lettersAreInCol);
          if (lettersAreInCol) {
            //add decrypted letters to decryptedMessage by
            //getting index of letterPair[0] and letterPair[1] and taking one index to the left, wrapping around as needed
            const encryptedPair1ColIndex = thisColumn.indexOf(letterPair[0]);
            const encryptedPair2ColIndex = thisColumn.indexOf(letterPair[1]);
    
            const decryptedPair1ColIndex =
              encryptedPair1ColIndex - 1 >= 0
                ? encryptedPair1ColIndex - 1
                : encryptedPair1ColIndex + 4;
    
            const decryptedPair2ColIndex =
              encryptedPair2ColIndex - 1 >= 0
                ? encryptedPair2ColIndex - 1
                : encryptedPair2ColIndex + 4;
    
            console.log(
              thisCol[encryptedPair1ColIndex],
              thisCol[encryptedPair2ColIndex]
            );
            console.log(
              thisCol[decryptedPair1ColIndex],
              thisCol[decryptedPair2ColIndex],
              "\n"
            );
    
            decryptedMessage +=
              thisCol[decryptedPair1ColIndex] + thisCol[decryptedPair2ColIndex];
    
            //if the letters have been found in the same columnn, the rest of the search for boxes can be skipped for this pair
            break;
          }
        }
    
    }

    //else establish the box between these letters as the corner points and get the other corners as the decrypted letters
    if (!lettersAreInRow && !lettersAreInColumn){

        console.log("checking boxes");

        //the decrypted letter will exist on the same row as the encrypted letter,
        //and while the letters may appear in different order in the box,
        //the letters when decrypted must still be added in the same order in which the encrypted letters were places

        //check through all the rows to see which row co-ordinate the first letter is at
        let firstLetterRow;
        for(firstLetterRow = 0; firstLetterRow < cipherMatrix.length; firstLetterRow++){
            if (cipherMatrix[firstLetterRow].includes(letterPair[0]))
                break;
        }
        
        //get column index of first letter
        let firstLetterCol = cipherMatrix[firstLetterRow].indexOf(letterPair[0]);
        
        
        //check through all the rows to see which row co-ordinate the second letter is at
        let secondLetterRow;
        for(secondLetterRow = 0; secondLetterRow < cipherMatrix.length; secondLetterRow++){
            if (cipherMatrix[secondLetterRow].includes(letterPair[1]))
                break;
        }
        //get column index of second letter
        let secondLetterCol = cipherMatrix[secondLetterRow].indexOf(letterPair[1]);
        
        console.log(letterPair[0], firstLetterRow, firstLetterCol);
        console.log(letterPair[1], secondLetterRow, secondLetterCol);

        //get the first letter's row, at the column index of the second letter, to decrypt first letter
        decryptedMessage += cipherMatrix[firstLetterRow][secondLetterCol];
        
        //get the second letter's row, at the column index of the first letter, to decrypt second letter
        decryptedMessage += cipherMatrix[secondLetterRow][firstLetterCol];


    }

  });

  decryptedMessage += "2!#!   @5/?"

  console.log(decryptedMessage);
  //output must be in upper case, not include spaces, the letter X, or special characters
  return decryptedMessage.toUpperCase().replaceAll("X","").replace(/[^A-Z ]/g, "");
}



//decrypted message
const DECRYPTED_MESSAGE = decryptMessage(ENCRYPTED_MESSAGE, CIPHER_KEY);

//output decrypted message
console.log(DECRYPTED_MESSAGE);
