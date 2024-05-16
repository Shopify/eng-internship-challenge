const decryptCipher = (key: string) => {
    const cipher = buildCipher(key);
    console.log(cipher);
    let map = new Map<string, number[]>();

    
   
}


const buildCipher = (keyword: string): string[][] => {
    const cipher: string[][] = [[],[],[],[],[]]; //nature of playfair cipher only ever has 5 arrays or rows
    const set = new Set<string>();
    let row = 0;

    for (const char of keyword) {
        if (set.has(char) || char === "J"){
            continue;
        }
        set.add(char);
        if (cipher[row].length >= 5){
            row++;
        }
        cipher[row].push(char);
    }

    for (let i = 65; i<= 90; i++){
        const char = String.fromCharCode(i);
        if (set.has(char) || char === "J"){
            continue;
        }
        set.add(char);
        if (cipher[row].length >= 5){
            row++;
        }
        cipher[row][].push(char);
    }

    return cipher;
}


 
decryptCipher("SUPERSPY");

//I unfortunately was not able to complete this problem 
//in time as I attempted to complete it using a language I have never used
//and was only able to work on it for the past 1.5 hours due to class commitments in the AM and from only receiving the github link this morning.
//With some more time I'm sure I could finish the problem so any consideration for more time or for another opportunity to display my skills would be
//greatly greatly appreciated. Completely understand that this will likely not be the case but I appreciate the time reviewing my application regardless. Thanks so much!