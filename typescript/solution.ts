const ENCYPT_MSG = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
const KEY = "SUPERSPY"

class KeyTable {

    static alphabet: string[] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    private table: string[];

    constructor (key: string) {
        this.table = this.makeKeyTable(key);
    }

    public getPos(char: string): [number, number] {
        let index = this.table.indexOf(char);
        return [index % 5, Math.floor(index / 5)]
    }

    public getChar(pos: [number, number]) {
        let index = pos[1] * 5 + pos[0];
        return this.table[index];
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

enum Shape {
    ROW = "row",
    COL = "collumn",
    RECT = "rectangle"
}

class Decryptor {

    private table: KeyTable;

    constructor(table: KeyTable) {
        this.table = table;
    }

    public decrypt(msg: string) {
        let pairs = this.toPairs(msg);
        let decryptedMsg = pairs
            .map(pair => this.decryptPair(pair))
            .join('')
            .split('')
            .filter(char => char != 'X')
            .join('');
        return decryptedMsg;
    }

    public decryptPair(pair: [string, string]): string {
        const pos1 = this.table.getPos(pair[0]);
        const pos2 = this.table.getPos(pair[1]);
        let newPos1: [number, number] = [pos1[0], pos1[1]];
        let newPos2: [number, number] = [pos2[0], pos2[1]];
        switch(this.shape(pos1, pos2)) {
            case Shape.ROW: {
                newPos1[0] = (pos1[0] + 4) % 5;
                newPos2[0] = (pos2[0] + 4) % 5;
                break;
            }
            case Shape.COL: {
                newPos1[1] = (pos1[1] + 4) % 5;
                newPos2[1] = (pos2[1] + 4) % 5;
                break;
            }
            case Shape.RECT: {
                newPos1[0] = pos2[0];
                newPos2[0] = pos1[0];
                break;
            }
        }
        return (this.table.getChar(newPos1) + this.table.getChar(newPos2));
    }

    toPairs(text: string): [string, string][] {
        let pairs: [string, string][] = []
        for (let i = 0; i < text.length; i = i + 2)
            pairs.push([text.charAt(i), text.charAt(i + 1)]);
        return pairs;
    }

    shape(pos1: [number, number], pos2: [number, number]): Shape {
        if (pos1[1] == pos2[1])
            return Shape.ROW;
        if (pos1[0] == pos2[0])
            return Shape.COL;
        return Shape.RECT;
    }
}

const table = new KeyTable(KEY);
const decryptor = new Decryptor(table);
const msg = decryptor.decrypt(ENCYPT_MSG);
console.log(msg);