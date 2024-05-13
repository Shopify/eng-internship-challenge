// To generate the table in Playfair Cipher, I used the same rule as in Wikipedia Example which omitted J (I = J)
// "X" is used as a filler when (1) two letters in the pair are the same; (2) size of the encrypted message is odd
// (3) if the plain text (decrypted message) contains 'J', it is then replaced by 'I'

// The rule of decryption is slighyly different from the Wikipedia one (shift right -> shift left when on the same row) according to the solution.test
// The "X" in the solution is also removed


function createTable(key)
{
    let letters = key + 'ABCDEFGHIKLMNOPQRSTUVWXYZ';
    let table_letters = simplify(letters);
    let curr = 0;
    
    let table = [[], 
                 [], 
                 [], 
                 [], 
                 []];
    
    for (let row = 0; row < 5; row ++) {
        for (let col = 0; col < 5; col ++) {
            table[row][col] = table_letters[curr];
            curr ++;
        }
    }

    return table;
}

function simplify(str)
{
    let simplified_str = "";
    let str_size = str.length;
    let curr_idx;

    simplified_str += str[0];

    for (curr_idx = 0; curr_idx < str_size; curr_idx ++) {

        for (let idx = 0; idx < curr_idx; idx ++) {
            if (str[curr_idx] == str[idx]) {
                break;
            } else if (idx == curr_idx - 1) {
                simplified_str += str[curr_idx];
            }
        }
    }

    return simplified_str;
}

function messageDecrypt(p1, p2, table)
{
    let row_1, col_1;
    let row_2, col_2;

    let decrypt_r1, decrypt_c1;
    let decrypt_r2, decrypt_c2;

    for (let r_idx = 0; r_idx < 5; r_idx ++) {
        for (let c_idx = 0; c_idx < 5; c_idx ++) {
            if (table[r_idx][c_idx] == p1) {
                row_1 = r_idx;
                col_1 = c_idx;
            }
            if (table[r_idx][c_idx] == p2) {
                row_2 = r_idx;
                col_2 = c_idx;
            }
        }
    }

    // (1) letters are on the same row of the table
    if (row_1 == row_2) 
    {
        decrypt_r1 = row_1;
        decrypt_r2 = row_2;
        if (col_1 - 1 >= 0) {
            decrypt_c1 = col_1 - 1;
        } else {
            decrypt_c1 = 4;
        }
        if (col_2 + 1 >= 0) {
            decrypt_c2 = col_2 - 1;
        } else {
            decrypt_c2 = 4;
        }
    } 
    // (2) letters are on the same column of the table
    else if (col_1 == col_2)
    {
        decrypt_c1 = col_1;
        decrypt_c2 = col_2;
        if (row_1 + 1 < 5) {
            decrypt_r1 = row_1 + 1;
        } else {
            decrypt_r1 = 0;
        }
        if (row_2 + 1 < 5) {
            decrypt_r2 = row_2 + 1;
        } else {
            decrypt_r2 = 0;
        }
    }
    // (3) letters form a rectangle
    else
    {
        decrypt_r1 = row_1;
        decrypt_r2 = row_2;
        decrypt_c1 = col_2;
        decrypt_c2 = col_1;
    }
    
    let decrypted_pair1 = table[decrypt_r1][decrypt_c1];
    let decrypted_pair2 = table[decrypt_r2][decrypt_c2];
    if (decrypted_pair1 == 'X') {
        decrypted_pair1 = "";
    }
    if (decrypted_pair2 == 'X') {
        decrypted_pair2 = "";
    }
    let decrypted_pair = decrypted_pair1 + decrypted_pair2;
    return decrypted_pair;
}

let table = createTable('SUPERSPY');

let message = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV';
let msg_size = message.length;
let pair_1_idx, pair_2_idx;
let pair;
let solution = "";

for (pair_1_idx = 0; pair_1_idx < msg_size; pair_1_idx += 2) {
    // (2) size of the encrypted message is odd
    if (pair_1_idx + 1 >= msg_size) {
        pair_2 = 'X';
    } else {
        pair_2_idx = pair_1_idx + 1;
        pair_2 = message[pair_2_idx];
    }
    pair_1 = message[pair_1_idx];
    // (1) two letters in the pair are the same
    if (pair_1 == pair_2) {
        pair_2 = 'X';
        pair_1_idx --;
    }
    // (3) the plain text (decrypted message) contains 'J'
    if (pair_1 == 'J') {
        pair_1 = 'I';
    }
    if (pair_2 == 'J') {
        pair_2 = 'I';
    }

    pair = pair_1 + pair_2;
    solution += messageDecrypt(pair_1, pair_2, table);
}

console.log(solution);

