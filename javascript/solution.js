/*
 * PlayFair Cipher Decryption
 * By:    Martin Atanacio
 * Date:  May 13th, 2024
 * 
 * Description: This program decrypts an encrypted message that uses the Playfair 
 * cipher algorithm. 5x5 matrix is created based on the key and the modified
 * alphabet. The message is then split into digrams and decrypted using the 
 * matrix and the dictionary of letter positions.
*/


/*
 * Creates a matrix based on the key provided and a modified alphabet
 * Returns a 5x5 matrix
*/
const create_matrix = (user_key) => {

     // J and I are equivalent in Playfair cipher, thus, J is removed from the alphabet
     const MODIFIED_ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ";
     const MATRIX_DIMENSION = 5;   // dimension of matrix, default is 5x5
     
     let characters = "";               // empty string to store characters
     let unique_letters = new Set();    // empty set to store unique characters
     let matrix = [];                   // empty 1x1 matrix to store characters
     let formatted_matrix = [];         // formatted matrix to store 5x5 matrix

     user_key.toUpperCase().replace(/J/g, "I");   // convert to uppercase and replace J with I
     characters = user_key + MODIFIED_ALPHABET;   // combine key and modified alphabet

     characters.split("").forEach((char) => {     // loop through each character
          if (!unique_letters.has(char)) {        // if character is not in set
               unique_letters.add(char);          // add character to set
               matrix.push(char);                 // add character to matrix
          }
     });

     for (let i = 0; i < matrix.length; i += MATRIX_DIMENSION) { // loop through matrix
          let entries = matrix.slice(i, i + MATRIX_DIMENSION);   // get 5 characters
          formatted_matrix.push(entries);                        // add 5 characters to matrix
     }

     return formatted_matrix; // return 5x5 matrix
};


/*
 * Gets the row and column indices of a target character in a 5x5 matrix
 * Returns the row and column indices
*/
const get_matrix_indices = (matrix, target) => {

     for (let i = 0; i < matrix.length; i++) {         // loop through matrix
          if (matrix[i].includes(target)) {            // if target is found in matrix
               return [i, matrix[i].indexOf(target)];  // return [row, col] indices
          }
     }
     return [-1, -1];    // return -1, -1 if target character is not found
};


/*
 * Decrypts the message using the 5x5 matrix
 * Returns the decrypted message
*/
const decrypt_message = (encrypted_message, user_key) => {
     let matrix = create_matrix(user_key);   // create a 5x5 matrix based on user key
     let first_letter = "";                  // empty string to store first letter
     let second_letter = "";                 // empty string to store second letter
     let [row1, col1] = [0, 0];              // row and column indices of first letter
     let [row2, col2] = [0, 0];              // row and column indices of second letter
     let decrypted_message = "";             // empty string to store decrypted text

     // loop through encrypted message by 2, since Playfair uses digrams
     for (let i = 0; i < encrypted_message.length; i += 2) {     
          first_letter = encrypted_message[i];          // get first letter
          second_letter = encrypted_message[i + 1];     // get second letter

          // get row and column indices of first and second letters
          [row1, col1] = get_matrix_indices(matrix, first_letter);
          [row2, col2] = get_matrix_indices(matrix, second_letter);

          // if the letters are in the same row, shift them to the left
          if (row1 === row2) {
               decrypted_message += matrix[row1][(col1 + 4) % 5]; // shift to the left
               decrypted_message += matrix[row1][(col2 + 4) % 5]; // wrap if necessary
          }
          // if the letters are in the same column, shift them up
          else if (col1 === col2) {
               decrypted_message += matrix[(row1 + 4) % 5][col1]; // shift up
               decrypted_message += matrix[(row2 + 4) % 5][col1]; // wrap if necessary
          }
          // if the letters form a rectangle, use the opposite corners
          else {
               decrypted_message += matrix[row1][col2];     // opposite corner
               decrypted_message += matrix[row2][col1];     // opposite corner
          }
     }

     // return decrypted message, removing any X's and spaces
     return decrypted_message.replace(/[X ]/g, "");
};

// Test case - expected output: "HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA"
const ENCRYPTED_MESSAGE = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const KEY = "SUPERSPY";

// Output the decrypted message to the console
console.log(decrypt_message(ENCRYPTED_MESSAGE, KEY));