/*
This function will build the 5x5 keyword square that will be used for the decryption.
It will return the square
*/
function createKeywordSquare(keyword) {
    // Convert keyword to uppercase
    keyword = keyword.toUpperCase();
  
    // Get unique keyword characters
    let uniqueKeywordSet = new Set();
  
    // Loop over all characters in the keyword and try to insert unique values to set
    for (let char of keyword) {
      // Only try to insert if character is in alphabet
      if (char >= "A" && char <= "Z") {
        // Sets only allow unique values
        uniqueKeywordSet.add(char);
      }
    }
  
    // The key square needs 25 characters to build the square
    // Therefor we add the remaining characters of the alphabet to the key set, excluding 'J'
    // By removing duplicated characters, we will always have 25 values in the set.
    for (let char of "ABCDEFGHIKLMNOPQRSTUVWXYZ") {
      uniqueKeywordSet.add(char);
    }
  
    // Build the 5x5 square by slicing the 25 character set into equal sizes of 5
    // This will give us 5 rows of 5 values
    let keySquare = [];
    // Convert set to array for slicing
    let uniqueKeywordArray = Array.from(uniqueKeywordSet)
    for (let i = 0; i < 5; i++) {
      keySquare.push(uniqueKeywordArray.slice(i * 5, i * 5 + 5));
    }
  
    return keySquare;
  }
  
  /*
  Loop through the key square to find the position of the given character
  */
  function findPosition(char, keySquare) {
    for (let row = 0; row < 5; row++) {
      for (let col = 0; col < 5; col++) {
        if (keySquare[row][col] === char) {
          return [row, col];
        }
      }
    }
    return null;
  }
  
  /*
  This function will decrypt a pair using the keyword square.
  */
  function decryptPair(pair, keySquare) {
    // Split the pair into individual characters
    let [char1, char2] = pair;
  
    // Find the positions of the characters in the key square
    let [row1, col1] = findPosition(char1, keySquare);
    let [row2, col2] = findPosition(char2, keySquare);
  
    // If the characters are in the same row, shift left
    if (row1 === row2) {
      // The modulo operator will handle wrapping if shifting left is not possible
      return keySquare[row1][(col1 + 4) % 5] + keySquare[row2][(col2 + 4) % 5];
    }
    // If the characters are in the same column, shift up
    else if (col1 === col2) {
      // The modulo operator will handle wrapping if shifting up is not possible
      return keySquare[(row1 + 4) % 5][col1] + keySquare[(row2 + 4) % 5][col2];
    }
    // If the characters form a rectangle, swap columns
    else {
      return keySquare[row1][col2] + keySquare[row2][col1];
    }
  }
  
  /*
  This function will split an array into pairs of 2
  */
  function createPairs(array) {
    const pairs = [];
    for (let i = 0; i < array.length; i += 2) {
      pairs.push(array.slice(i, i + 2));
    }
    return pairs;
  }
  
  /*
  This is the function that takes the encrypted message value and the keyword.
  It will use the keyword to decrypt the message.
  */
  function decryptMessageWithKeyword(encryptedTextValue, keyword) {
    // Create the keyword 5x5 square using the keyword
    let keywordSquare = createKeywordSquare(keyword);
  
    // Split the message text into pairs of two characters
    let pairs = createPairs(encryptedTextValue);
    
    let decryptedMessage = "";
  
    // Decrypt each pair and append to the decrypted text
    for (let pair of pairs) {
      // Decrypt the pair
      let decryptedPair = decryptPair(pair, keywordSquare);
      // Add decryptedPair to decrypted message
      decryptedMessage += decryptedPair;
    }
  
    // Remove any 'X' used as padding and return the result
    return decryptedMessage.replace(/X/g, "");
  }
  
  function startDecryption() {
    // The message to be decrypted
    const encryptedTextValue = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
    
    // The keywork to use for building the 5x5 square
    const keyword = "SUPERSPY";
  
    // Decrypt the message using the keyword
    let decryptedTextValue = decryptMessageWithKeyword(encryptedTextValue, keyword);
  
    // Output the decrypted text to the console, which will be read by the unit test for validation
    console.log(decryptedTextValue);
  }
  
  // Start the decryption
  startDecryption();
  