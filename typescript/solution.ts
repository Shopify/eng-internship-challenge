// Define the properties for the main function
interface MainProps {
    key: string;
    message: string;
}
// Define the alphabet used in the encryption
const alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ";

// Main function to run the decryption process
function main({key, message}: MainProps) {
    // Generate the key map and key table structures based on the key
    const {keyMap, keyTable} = generateStructures(key);
    // Generate digrams (pairs of letters) from the message
    const digrams = generateDigrams(message);
    // Decrypt the message using the key structures and digrams
    const decryptedMessage = decrypt(keyMap, keyTable, digrams);
    // Output the decrypted message
    console.log(decryptedMessage);
}

// Decrypt the message using the key map, key table, and digrams
function decrypt(keyMap: Map<string, [number, number]>, keyTable:string[][],  digrams: Array<[string,string]>){
    const decryptedMessage: string[] = [];
    // Loop through each pair of letters (digram)
    for (let [letter1, letter2] of digrams){
        const letter1Coords = keyMap.get(letter1);
        const letter2Coords = keyMap.get(letter2);
        // Check if both letters have coordinates in the key map
        if(!letter1Coords || !letter2Coords){
            console.error(`Unknown letter(s) encountered ${letter1}/${letter2}`)
            continue;
        }

        // Case 1: Both letters are in the same row
        if(letter1Coords[0] === letter2Coords[0]){
            decryptedMessage.push(keyTable[letter1Coords[0]][shiftWithWrap(letter1Coords[1])])
            decryptedMessage.push(keyTable[letter2Coords[0]][shiftWithWrap(letter2Coords[1])])
        }
        // Case 2: Both letters are in the same column
        else if(letter1Coords[1] === letter2Coords[1]) {
            decryptedMessage.push(keyTable[shiftWithWrap(letter1Coords[0])][letter1Coords[1]])
            decryptedMessage.push(keyTable[shiftWithWrap(letter2Coords[0])][letter2Coords[1]])
        }
        // Case 3: Letters form a rectangle
        else {
            decryptedMessage.push(keyTable[letter1Coords[0]][letter2Coords[1]])
            decryptedMessage.push(keyTable[letter2Coords[0]][letter1Coords[1]])
        }
    }
    // Join the decrypted message and remove 'X' characters used as padding
    return decryptedMessage.join('').replace(/X/g, '');
}
// Helper function to shift index with wrap-around for decryption
function shiftWithWrap(value: number) {
    if(value - 1 >= 0) {
        return value - 1;
    }
    else {
        return 4
    }
}
// Generate digrams (pairs of letters) from the message
function generateDigrams(message: string): Array<[string,string]> {
    const digrams: Array<[string,string]> = [];
    const splitMessage = message.split('');
    // Split the message into pairs of letters (digrams)
    while(splitMessage.length) digrams.push(splitMessage.splice(0,2) as [string,string])
    
    return digrams  
}
// Define the structure of the generated key map and key table
interface GeneratedKeyStructures {
    keyMap: Map<string, [number, number]>;
    keyTable: string[][]
}
// Generate key map and key table based on the provided key
function generateStructures(key: string): GeneratedKeyStructures{
    const keyMap = new Map<string, [number, number]>();
    const keyTable: string[][] = [[],[],[],[],[]];
    const rawInput = `${key}${alphabet}`.split('')
    const uniqChars = [...new Set(rawInput)];
    // Fill the key map and key table with unique characters
    for (let i=0; i<uniqChars.length; i++) {
        const key = uniqChars[i];
        if(i<5){
            keyMap.set(key, [Math.floor(i/5), i])
            keyTable[0].push(key) 
        }
        else{
            keyMap.set(key, [Math.floor(i/5), i % 5])
            keyTable[Math.floor(i/5)].push(key) 
        }
    }
    return {keyMap, keyTable};
}
// Run the main function with a provided key and message
main({key: "SUPERSPY", message: "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"});