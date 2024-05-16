# decrypted string must by entirely **UPPER CASE**, 
# and not include `spaces`, the letter `"X"`, or `special characters`

# encrypted message: IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV
# key to the cipher: SUPERSPY

''' key table:

    S U P E R 
    Y A B C D
    F G H I K   
    L M N O Q
    T V W X Z
'''

table =[["S", "U", "P", "E", "R"],
        ["Y", "A", "B", "C", "D"],
        ["F", "G", "H", "I", "K"],
        ["L", "M", "N", "O", "Q"],
        ["T", "V", "W", "X", "Z"]]

encrypted = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
decrypted = ""

# iterate the encrypted string, 2 letters a step
for i in range(len(encrypted)//2): 
    # declare the positions of the first and second letter in the string pair
    fst = []
    snd = []
    
    # go through the key table to find the position 
    for j in range(5):
        for k in range(5):
            if table[j][k] == encrypted[2*i]:
                fst = [j,k]
            if table[j][k] == encrypted[2*i + 1]:
                snd = [j,k]
                
    # first case: 2 letters in the same row, then each one move one step to the left
    if fst[0] == snd[0]:
        fst[1] = (fst[1] - 1 + 5) % 5
        snd[1] = (snd[1] - 1 + 5) % 5
    
    # second case: 2 letters in the same column, then each one move one step up
    elif fst[1] == snd[1]:
        fst[0] = (fst[0] - 1 + 5) % 5
        snd[0] = (snd[0] - 1 + 5) % 5
    
    # third case: not case 1 or case 2, then x-coordinates keep as is, the y-coordinates exchange
    else:
        snd_y = snd[1]
        snd[1] = fst[1]
        fst[1] = snd_y
        
    new_fst = table[fst[0]][fst[1]]
    new_snd = table[snd[0]][snd[1]]
    
    # decrypted string does not include the letter `"X"
    if new_fst == "X":
        new_fst = ""
    if new_snd == "X":
        new_snd = ""
    
    decrypted += (new_fst + new_snd) 

# "HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA" is printed here as the expected_output in solution.test.py
# but the test fails, it seems this print output is not catched, weird..
print(decrypted)