const encryptedText = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const splitEncText = "IK EW EN EN XL NQ LP ZS LE RU MR HE ER YB OF NE IN CH CV";
const answerText = "HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA";
const cipherKey = "SUPERSPY";

const keyTable = [
    ["S", "U", "P", "E", "R"],
    ["Y", "A", "B", "C", "D"],
    ["F", "G", "H", "I", "K"],
    ["L", "M", "N", "O", "Q"],
    ["T", "V", "W", "X", "Z"]
];

/**
 * Represents the key table:
 *      S U P E R
 *      Y A B C D
 *      F G H I K
 *      L M N O Q
 *      T V W X Z
 */
const keyTableMap = {
    "S": [0, 0],
    "U": [1, 0],
    "P": [2, 0],
    "E": [3, 0],
    "R": [4, 0],
    "Y": [0, 1],
    "A": [1, 1],
    "B": [2, 1],
    "C": [3, 1],
    "D": [4, 1],
    "F": [0, 2],
    "G": [1, 2],
    "H": [2, 2],
    "I": [3, 2],
    "K": [4, 2],
    "L": [0, 3],
    "M": [1, 3],
    "N": [2, 3],
    "O": [3, 3],
    "Q": [4, 3],
    "T": [0, 3],
    "V": [1, 3],
    "W": [2, 3],
    "X": [3, 3],
    "Z": [4, 3]
};

/**
 * Decrypts playfair cipher encrypted text.
 * @param {*} encryptedText 
 * @returns String - decrypted text
 */
function playfairDecryptor(encryptedText) {
    return "";
}

/**
 * Splits encrypted text into pairs of letters.
 * @param {String} text 
 * @returns String[]
 */
function splitEncText(text) {
    return [];
}


/**
 * Decrypts encrypted text represented as pairs of letters.
 * @param {String[]} encTxtArr
 * @returns String - decrypted string
 */
function decrypt(encTextArr) {
    /**
     * 1. If same row, get the letters (x_1 - 1, y_1), (x_2 - 1, y_2), wrapping around
     * 2. If same column, get the letters (x_1, y_1 - 1), (x_2, y_2 - 1), wrapping around
     * 3. If same column, get the letters (x_1, y_1), (x_2, y_2) --> (x_2, y_1), (x_1, y_2)
     */

    return "";
}

/**
 * Returns letters located 1 unit above the given letters in the key
 * table. Wraps around if table limits are exceeded.
 * @returns String - decoded letter pair
 */
function decryptColumnRule(l1, l2) {
    return "";
}

/**
 * Returns letters located 1 unit to the left of the given letters in
 * the key table. Wraps around if table limits are exceeded.
 * @returns String - decoded letter pair
 */
function decryptRowRule(l1, l2) {
    return "";
}

/**
 * Switches the x-coordinates of given coordinates.
 * @returns String - decoded letter pair
 */
function decryptRectRule(l1, l2) {
    return "";
}