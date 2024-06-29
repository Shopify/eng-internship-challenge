class PlayFair {
  constructor(key) {
    this.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    this.rows = 5;
    this.cols = 5;
    this.matrix = Array.from({ length: this.rows }, () =>
      Array(this.cols).fill("")
    );
    this.indices = new Map();
    this.buildMatrix(key);
  }

  // Print the matrix for debugging purposes
  printMatrix() {
    this.matrix.forEach((row) => {
      console.log(row.join(" "));
    });
  }

  // Increment the pointer in the matrix
  incrementPointer(i, j) {
    if (i === this.rows - 1 && j === this.cols - 1) {
      return [-1, -1];
    }
    if (j === this.cols - 1) {
      return [i + 1, 0];
    }
    return [i, j + 1];
  }

  // Convert a text into a list of digrams (pairs of letters)
  diagraminate(text) {
    text = text.toUpperCase();
    let digrams = [];
    let length = text.length;
    let index = 0;

    while (index <= length - 2) {
      let digram = text.substr(index, 2);
      if (
        digram[0] === digram[1] ||
        (digram[0] === "I" && digram[1] === "J") ||
        (digram[0] === "J" && digram[1] === "I")
      ) {
        digrams.push(digram[0] + "X");
        index -= 1;
      } else {
        digrams.push(digram);
      }
      index += 2;
    }
    if (index < length) {
      digrams.push(text[index] + "X");
    }
    return digrams;
  }

  // Build the Playfair encryption matrix using the key
  buildMatrix(key) {
    key = key.toUpperCase().replace(/ /g, "");
    let x = 0,
      y = 0;

    // Add characters from the key to the matrix
    for (let char of key) {
      if (this.indices.has(char)) continue;
      if (
        (char === "I" && this.indices.has("J")) ||
        (char === "J" && this.indices.has("I"))
      )
        continue;

      this.matrix[x][y] = char;
      this.indices.set(char, [x, y]);

      [x, y] = this.incrementPointer(x, y);
      if (x === -1 && y === -1) break;
    }

    // Add remaining alphabet characters to the matrix
    for (let char of this.alphabet) {
      if (this.indices.has(char)) continue;
      if (
        (char === "I" && this.indices.has("J")) ||
        (char === "J" && this.indices.has("I"))
      )
        continue;

      this.matrix[x][y] = char;
      this.indices.set(char, [x, y]);

      [x, y] = this.incrementPointer(x, y);
      if (x === -1 && y === -1) break;
    }
  }

  // Shift a position to the right in the matrix
  shiftRight(x, y) {
    return [x, (y + 1) % this.cols];
  }

  // Shift a position to the left in the matrix
  shiftLeft(x, y) {
    return [x, (y + this.cols - 1) % this.cols];
  }

  // Shift a position down in the matrix
  shiftDown(x, y) {
    return [(x + 1) % this.rows, y];
  }

  // Shift a position up in the matrix
  shiftUp(x, y) {
    return [(x + this.rows - 1) % this.rows, y];
  }

  // Encrypt a given text using the Playfair cipher
  encrypt(text) {
    text = text.replace(/ /g, "");
    let digrams = this.diagraminate(text);
    let encrypted = "";

    for (let digram of digrams) {
      let [first, second] = digram;
      let [fx, fy] = this.indices.get(first);
      let [sx, sy] = this.indices.get(second);

      if (fx === sx) {
        let [newFx, newFy] = this.shiftRight(fx, fy);
        let [newSx, newSy] = this.shiftRight(sx, sy);
        encrypted += this.matrix[newFx][newFy] + this.matrix[newSx][newSy];
      } else if (fy === sy) {
        let [newFx, newFy] = this.shiftDown(fx, fy);
        let [newSx, newSy] = this.shiftDown(sx, sy);
        encrypted += this.matrix[newFx][newFy] + this.matrix[newSx][newSy];
      } else {
        encrypted += this.matrix[fx][sy] + this.matrix[sx][fy];
      }
    }

    return encrypted;
  }

  // Decrypt a given text using the Playfair cipher
  decrypt(encrypted) {
    encrypted = encrypted.replace(/ /g, "");
    let digrams = this.diagraminate(encrypted);
    let decrypted = "";

    for (let digram of digrams) {
      let [first, second] = digram;
      let [fx, fy] = this.indices.get(first);
      let [sx, sy] = this.indices.get(second);

      if (fx === sx) {
        let [newFx, newFy] = this.shiftLeft(fx, fy);
        let [newSx, newSy] = this.shiftLeft(sx, sy);
        decrypted += this.matrix[newFx][newFy] + this.matrix[newSx][newSy];
      } else if (fy === sy) {
        let [newFx, newFy] = this.shiftUp(fx, fy);
        let [newSx, newSy] = this.shiftUp(sx, sy);
        decrypted += this.matrix[newFx][newFy] + this.matrix[newSx][newSy];
      } else {
        decrypted += this.matrix[fx][sy] + this.matrix[sx][fy];
      }
    }

    return decrypted.replace(/X/g, "");
  }
}

// Example usage
const key = "SUPERSPY";
const cipher = new PlayFair(key);

const encryptedText = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const decryptedText = cipher.decrypt(encryptedText);

console.log(decryptedText); // Expected output: 'HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA'
