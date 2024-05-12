/**
 * Generates a 5x5 cipher matrix based on a given key.
 * 
 * @param {string} key - The secret key used to generate the cipher matrix.
 * @returns {Array<Array<string>>} The generated cipher matrix.
 */
function generateCipherMatrix(key) {
    // Created a string of unique characters by combining the key and standard alphabet (excluding 'J')
    const uniqueChars = [...new Set(key + "ABCDEFGHIKLMNOPQRSTUVWXYZ")];
    const matrix = [];

    for (let i = 0; i < uniqueChars.length; i += 5) {
        matrix.push(uniqueChars.slice(i, i + 5));
    }

    return matrix;
}