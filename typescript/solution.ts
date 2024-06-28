const ENCYPT_MSG = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
const KEY = "SUPERSPY"

class KeyTable {

    static alphabet: string[] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    private table: string[];

    constructor (key: string) {
        this.table = this.makeKeyTable(key);
    }

    private makeKeyTable(text: string) {
        let lettersUsed = new Set<string>();
        let letters: string[] = []
        let appendUniqueChar = (char: string) => {
            char = (char == 'J') ? 'I' : char
            if (!lettersUsed.has(char)) {
                letters.push(char)
                lettersUsed.add(char);
            }
        }
        text.toUpperCase()
            .split('')
            .forEach(appendUniqueChar);
        KeyTable.alphabet.forEach(appendUniqueChar);
        return letters;
    }
}

class Decryptor {

    private table: KeyTable

    constructor(table: KeyTable) {
        this.table = table;
    }

    public decrypt(msg: string) {
        let pairs = this.toPairs(msg);
    }

    toPairs(text: string): string[] {
        let pairs: string[] = []
        for (let i = 0; i < text.length; i = i + 2)
            pairs.push(text.substring(i, i + 2));
        return pairs;
    }
}

let testTable = new KeyTable(KEY);
let decryptor = new Decryptor(testTable);
decryptor.decrypt(ENCYPT_MSG);