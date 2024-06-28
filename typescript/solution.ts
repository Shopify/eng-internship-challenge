/**
 * Constants
 */
const ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
const OMITTED = 'J'
const PADDING = 'X'

/**
 * Removes instances of `remove` omitted from `str` when found by
 * scanning from beginning to end of `str`.
 * 
 * @param str String to process
 * @param remove Substring to be removed from `str`
 * @returns `str` with  `remove` removed
 * @example removeInstancesOf('ABCBA', 'B') => 'ACA'
 */
const removeInstancesOf = (str: string, remove: string): string => {
    return str.split(remove).join('')
}

/**
 * Creates a 2D array that is split into groups of length `size`.
 * The last chunk may have length less than `size`.
 * 
 * @param arr Array to process
 * @param size Size of each chunk
 * @returns 2D array of chunks containing values of `arr`
 * @example chunk([1,2,3,4,5], 2) => [[1,2], [3,4], [5]]
 */
const chunk = <T>(arr: T[], size: number): T[][] => {
    const chunked: T[][] = []
    for (let i = 0; i < arr.length; i += size) {
        chunked.push(arr.slice(i, i + size))
    }
    return chunked
}

/**
 * Creates a 5x5 matrix of characters representing the Playfair cypher key table
 * using `key` as the keyword.
 * 
 * `OMITTED` (default 'J') is used as the character that is not included in the key table.
 * 
 * @param key Cypher key
 * @returns 5x5 Playfair cypher key table
 */
const generateKeyTable = (key: string): string[][] => {
    const usedChars = new Set<string>()
    const cypherChars: string[] = []
    const charsInInsertionOrder = removeInstancesOf(key  + ALPHABET, OMITTED)
    for (const char of charsInInsertionOrder) {
        if (!usedChars.has(char)) {
            cypherChars.push(char)
            usedChars.add(char)
        }
    }
    return chunk(cypherChars, 5)
}

/**
 * Generates a dictionary containing row and column of each character in `table`
 * - Dictionary keys are characters in `table`
 * - Dictionary values are tuples of [row, column]
 * 
 * Allows for constant time index lookup.
 * 
 * @param table 5x5 Playfair Cypher Key Table
 * @returns Dictionary of type {char: [number, number]}
 */
const generateKeyTableMetadata = (table: string[][]): Record<string, [number, number]> => {
    const data: Record<string, [number, number]> = {}
    for (let row = 0; row < 5; row++) {
        for (let col = 0; col < 5; col++) {
            const char = table[row][col]
            data[char] = [row, col]
        }
    }
    return data
}

/**
 * Given `encryptedText` and `keyword` generated using the Playfair cypher, 
 * decodes and returns the original plaintext
 * 
 * `PADDING` (default 'X') is assumed to be the padding letter used to generate `encryptedText`
 * 
 * @param encryptedText Playfair encrypted text
 * @param keyword Playfair keyword
 * @returns Decoded plaintext of `encryptedText` using `keyword` as key
 */
const decode = (encryptedText: string, keyword: string): string => {
    const keyTable = generateKeyTable(keyword)
    const characterLocations = generateKeyTableMetadata(keyTable)
    const encryptedCharacterPairs = chunk(encryptedText.split(''), 2)
    let plaintext = ""

    for (let [charA, charB] of encryptedCharacterPairs) {
        const [rowA, colA] = characterLocations[charA]
        const [rowB, colB] = characterLocations[charB]

        if (rowA === rowB) {
            plaintext += keyTable[rowA][(colA + 4) % 5]
            plaintext += keyTable[rowB][(colB + 4) % 5]
        } else if (colA === colB) {
            plaintext += keyTable[(rowA + 4) % 5][colA]
            plaintext += keyTable[(rowB + 4) % 5][colB]
        } else {
            plaintext += keyTable[rowA][colB]
            plaintext += keyTable[rowB][colA]
        }
    }

    return removeInstancesOf(plaintext, PADDING)
}


/**
 * Example Usage
 */
const ENCRYPTED_TEXT = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'
const CYPHER_KEY = 'SUPERSPY'

console.log(decode(ENCRYPTED_TEXT, CYPHER_KEY))