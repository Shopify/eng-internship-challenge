const ENCYPT_MSG = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
const KEY = "SUPERSPY"

class KeyTable {

    static alphabet: string[] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    private table: string[];

    constructor (key: string) {
        this.table = this.makeKeyTable(key);
        console.log(this.table);
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

let testTable = new KeyTable(KEY);