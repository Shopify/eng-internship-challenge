function toLowerCase(msg) {
    return msg.toLowerCase();
}

function toUpperCase(msg) {
    return msg.toUpperCase();
}

function removeSpaces(msg) {
    return msg.split(' ').join('');
}

function generateKeyTable(key) {
    // generates the 5x5 key square
    let keyT = new Array(5).fill(null).map(() => new Array(5).fill(''));
    let dicty = {};
    for (let i = 0; i < 26; i++) {
        dicty[String.fromCharCode(i + 97)] = 0;
    }

    for (let i = 0; i < key.length; i++) {
        if (key[i] != 'j') {
            dicty[key[i]] = 2;
        }
    }
    dicty['j'] = 1;

    let i = 0, j = 0, k = 0;
    while (k < key.length) {
        if (dicty[key[k]] == 2) {
            dicty[key[k]] -= 1;
            keyT[i][j] = key[k];
            j += 1;
            if (j == 5) {
                i += 1;
                j = 0;
            }
        }
        k += 1;
    }

    
    for (let k in dicty) {
        if (dicty[k] == 0) {
            keyT[i][j] = k;
            j += 1;
            if (j == 5) {
                i += 1;
                j = 0;
            }
        }
    }

    return keyT;
}
