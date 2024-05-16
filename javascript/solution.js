
const ALPHABET = "abcdefghiklmnopqrstuvwxyz";


  function removeDuplicates(str) {
// Function to eliminate duplicate characters in a string while retaining the first occurrence

    var result = "";
    var visited = {}; //keeps track of visited characters 
    
    for (let i = 0; i < str.length; i++) {
        var char = str[i];
        if (!visited[char]) 
        {
            result += char;
            visited[char] = true;
        }
    }

    return result;
}

function createMatrixString(key) {
  //Function to generate a string of letters, including the provided key and the alphabet to construct the matrix.
    key += ALPHABET;
    key = key.toLowerCase();
    key = key.split(' ').join('');

    return key;
  }
 

  function createMatrixFromLetters(letters) {
    //Function to generate a 5x5 matrix using the provided string

    if (letters.length !== 25) 
    {
        throw new Error("verify string must contain exactly 25 letters");
        //can only contain max 25 letters
    }

    let matrix = [];
    let index = 0;

    for (let i = 0; i < 5; i++) {
        matrix[i] = [];
        for (let j = 0; j < 5; j++) 
        {
            matrix[i][j] = letters[index];
            index++;
        }
    }

    return matrix;
}
function locatePositions(charOne, charTwo,matrix) {

    //Function to locate the pairs of two letters provided in the 5x5 matrix to then return their position
    //Can only contain 25 characters, all J's are replaced by I

    if (charOne == 'j') 
    {
      charOne = 'i';
    } 
    else if (charTwo == 'j') 
    {
      charTwo = 'i';
    }

    let positions = Array(4).fill(0);
    //array to hold the positions in matrix for both characters [i,j,i,j]
   
    for (let i = 0; i < 5; i++) {
      for (let j = 0; j < 5; j++) {
        if (matrix[i][j] == charOne) //found position of first character
        {
          positions[0] = i;
          positions[1] = j;
        } else if (matrix[i][j] == charTwo)  ////found position of second character
        {
          positions[2] = i;
          positions[3] = j;
        }
      }
    }

    return positions;
  }

  
  function decrypt(message, matrix) {
  //Function to decrypt message following Playfair Cipher digraph rules: 

   /* 
   - both letters same row -> take letters to left % 5
   - both letters same column -> take letters above % 5 
   - else if none apply create inner-table within the letters and retrieve the 
     letters positioned at the opposite corners of row containing letters in the inner-table
   */ 


  message =  message.toLowerCase();
  message= message.split(' ').join('');
  let max = message.length;

  
  let charCount = 0;
  
  while (charCount < max) {
  
   let current = locatePositions(message[charCount], message[charCount + 1],matrix);

   if (current[0] == current[2]) 
   { //if both letters in same column

    x = current[1] - 1;
    if (x < 0) { x += 5; }

    y = current[3] - 1;
    if (y < 0) { y += 5; }

    
   message = message.slice(0, charCount) + matrix[current[0]][x % 5] + 
   matrix[current[0]][y % 5] + message.slice(charCount + 2);
  
   } 
   else if (current[1] == current[3]) { // if both letters in the same row

   message = message.slice(0, charCount) + matrix[x % 5][current[1]] + 
   matrix[y % 5][current[1]] + message.slice(charCount + 2);
     x = current[0] - 1;
    if (x < 0) { x += 5; }

    y = current[2] - 1;
    if (y < 0) { y += 5; }
   } 

   else { //if not of previous rules apply

  message = message.slice(0, charCount) + matrix[current[0]][current[3]] + 
  matrix[current[2]][current[1]] + message.slice(charCount + 2);

  }

   charCount += 2;
  }
  
  return message;
}

  function playfairCipherSolver(message,key){
    //function to run decryption with given message and associated key
    let letters = removeDuplicates(createMatrixString(key));
    let matrix = createMatrixFromLetters(letters);
    message = message.replace(/[^\w]/g, "");
    let decryptedMessage = decrypt(message,matrix);
    decryptedMessage = decryptedMessage.replace(/x/g, '');
    decryptedMessage = decryptedMessage.toUpperCase().trim();

    console.log(decryptedMessage);

  }
  
  let key = "SUPERSPY";
  let message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";

  playfairCipherSolver(message, key);
