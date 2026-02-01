function createKeySquare(keyword: string): string[][]{
    const alpha = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'; // J should be excluded
    let key = '';
    const seen: { [char: string]: boolean} = {};

    for (let char of keyword) {
        if(!seen[char]){
            seen[char] = true;
            key += char;
        }
    }

    for (let char of alpha){
        if(!seen[char]){
            seen[char] = true;
            key += char;
        }
    }

    const keySquare = [];
    for (let i= 0; i<5; i++){
        keySquare.push(key.slice(i*5, i*5+5).split(''));
    }

    return keySquare;

}

function findPosition(keySquare: string[][], char: string): [number, number]{
    for(let row=0; row < 5; row++) {
        for (let col = 0; col < 5; col++){
            if (keySquare[row][col] === char){
                return [row, col];
            }
        }
    }
    throw new Error(`char ${char} not found in the keysquare`);
}

function decryptedDigraph(digraph: string, keySquare: string[][]): string{
    const [char1, char2] = digraph.split('');
    let [row1, col1] = findPosition(keySquare, char1);
    let [row2, col2] = findPosition(keySquare, char2);

    if (row1 === row2){
        col1 = (col1+4)%5;
        col2 = (col2+4)%5;
    } else if (col1 === col2){
        row1 = (row1+4)%5;
        row2 = (row2+4)%5;
    } else {
        [col1, col2] = [col2, col1];
    }

    return keySquare[row1][col1] + keySquare[row2][col2];
}

function decryptMsg(encrypteddMsg: string, keyword: string): string{
    const keySquare = createKeySquare(keyword);
    const digraphs = encrypteddMsg.match(/.{1,2}/g) || [];
    let decryptedMsg = '';

    for(const digraph of digraphs){
        decryptedMsg += decryptedDigraph(digraph, keySquare);
    }
    return decryptedMsg.replace(/X/g, '');

}
const encryptedMessage = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const keyword = "SUPERSPY";
const decryptedMessage = decryptMsg(encryptedMessage, keyword);
console.log(decryptedMessage);