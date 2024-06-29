class PlayfairCipher {
    constructor(key) {
      this.matrix = this.generateMatrix(key);
    }
  
    // Function to generate the 5x5 matrix
    generateMatrix(key) {
      key = key.toUpperCase().replace(/J/g, 'I');
      const alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ';
      const keyMatrix = [];
      const usedChars = new Set();
  
      // Add key characters to the matrix
      for (let char of key) {
        if (!usedChars.has(char)) {
          keyMatrix.push(char);
          usedChars.add(char);
        }
      }
  
      // Add remaining alphabet characters to the matrix
      for (let char of alphabet) {
        if (!usedChars.has(char)) {
          keyMatrix.push(char);
          usedChars.add(char);
        }
      }
  
      // Create 5x5 matrix
      const matrix = [];
      while (keyMatrix.length) {
        matrix.push(keyMatrix.splice(0, 5));
      }
  
      return matrix;
    }
  
    // Function to preprocess the input text
    preprocessInput(text) {
      text = text.toUpperCase().replace(/J/g, 'I').replace(/[^A-Z]/g, '');
      const digraphs = [];
      
      for (let i = 0; i < text.length; i += 2) {
        let pair = text[i];
        if (i + 1 < text.length) {
          if (text[i] === text[i + 1]) {
            pair += 'X';
          } else {
            pair += text[i + 1];
          }
        } else {
          pair += 'X';
        }
        digraphs.push(pair);
      }
  
      return digraphs;
    }
  
    // Function to find the position of a character in the matrix
    findPosition(char) {
      for (let row = 0; row < 5; row++) {
        for (let col = 0; col < 5; col++) {
          if (this.matrix[row][col] === char) {
            return { row, col };
          }
        }
      }
    }
  
    // Function to decrypt a single digraph
    decryptPair(pair) {
      const pos1 = this.findPosition(pair[0]);
      const pos2 = this.findPosition(pair[1]);
      let decryptedPair = '';
  
      if (pos1.row === pos2.row) {
        // Same row: shift left
        decryptedPair += this.matrix[pos1.row][(pos1.col + 4) % 5];
        decryptedPair += this.matrix[pos2.row][(pos2.col + 4) % 5];
      } else if (pos1.col === pos2.col) {
        // Same column: shift up
        decryptedPair += this.matrix[(pos1.row + 4) % 5][pos1.col];
        decryptedPair += this.matrix[(pos2.row + 4) % 5][pos2.col];
      } else {
        // Rectangle swap
        decryptedPair += this.matrix[pos1.row][pos2.col];
        decryptedPair += this.matrix[pos2.row][pos1.col];
      }
  
      return decryptedPair;
    }
  
    // Main decryption function
    decrypt(ciphertext) {
      const digraphs = this.preprocessInput(ciphertext);
      let plaintext = '';
  
      for (let digraph of digraphs) {
        plaintext += this.decryptPair(digraph);
      }
  
      return plaintext;
    }
  }
  
  const key = "SUPERSPY";
  const ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
  
  const playfair = new PlayfairCipher(key);
  const plaintext = playfair.decrypt(ciphertext);
  
  console.log("Decrypted message:", plaintext);
  