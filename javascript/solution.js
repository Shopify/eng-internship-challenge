// function to create 5x5 matrix
function createMatrix(key) {
    let matrix = [];
    const alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ";
  
    // use the key word to fill in the matrix first
    for (let i = 0; i < key.length; i++) {
      if (!matrix.includes(key[i])) {
        matrix.push(key[i]);
      }
    }
  
    // fill the rest of the matrix with alphabet letters
    for (let i = 0; i < alphabet.length; i++) {
      if (!matrix.includes(alphabet[i])) {
        matrix.push(alphabet[i]);
      }
    }
    return matrix;
  }
  
  function decryptDigraph(digraph, matrix) {
    // find the index of both characters in the digraph
    let index1 = matrix.indexOf(digraph[0]);
    let index2 = matrix.indexOf(digraph[1]);
  
    // find the row and column index of the characters in the digraph
  
    let row1 = Math.floor(index1 / 5);
    let col1 = index1 % 5;
    let row2 = Math.floor(index2 / 5);
    let col2 = index2 % 5;
  
    // if the letters are in the same row they are replaced by the letter to the left
  
    if (row1 === row2) {
      col1 = (col1 + 4) % 5;
      col2 = (col2 + 4) % 5;
    }
    // if the letters are in the same column they are replaced by the letters above
    else if (col1 === col2) {
      row1 = (row1 + 4) % 5;
      row2 = (row2 + 4) % 5;
    }
    // if else, each letter is replaced by the letter in its own row and the column of the other letter
    else {
      let other = col1;
      col1 = col2;
      col2 = other;
    }
  
    return matrix[row1 * 5 + col1] + matrix[row2 * 5 + col2];
  }
  
  // function to decrypt message
  function decryptMessage(message, key) {
    let matrix = createMatrix(key);
    let password = "";
  
    for (let i = 0; i < message.length; i += 2) {
      let digraph = message.substr(i, 2);
      let decodedPassword = decryptDigraph(digraph, matrix);
      password += decodedPassword;
    }
  
    // remove the letter X and special characters from printed message
    password = password.replace(/[X\s]|[^A-Z]/g, "");
    console.log(password);
  }
  
  const message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
  const key = "SUPERSPY";
  
  decryptMessage(message, key);  