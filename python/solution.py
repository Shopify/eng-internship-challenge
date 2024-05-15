import string


key = 'SUPERSPY'
key = "".join(dict.fromkeys(key))

encoded_text = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'
num_pairs = int (len(encoded_text)/2)

pairs = [encoded_text[i:i+2] for i in range(0, len(encoded_text), 2)]



N = 5
cols, rows = 5, 5
arr = [['A' for i in range(cols)] for j in range(rows)]
counter = 0
alpha_counter = 0
S = set()
for i in range(len(arr)):
    for j in range(len(arr)):
        if counter < len(key):
            arr[i][j] = key[counter]
            S.add(key[counter])
            counter += 1
        else:
            while string.ascii_uppercase[alpha_counter] in S:
                alpha_counter += 1
            if string.ascii_uppercase[alpha_counter] == 'J':
                alpha_counter += 1
            arr[i][j] = string.ascii_uppercase[alpha_counter]
            alpha_counter += 1


decrypt_pair = []
for pair in pairs:
    for i in range(len(arr)):
        if pair[0] in arr[i]:
            if pair[1] in arr[i]:

                p0 = arr[i].index(pair[0])-1
                p1 = arr[i].index(pair[1])-1

                if arr[i].index(pair[0])-1 < 0:
                    p0 = 4
                if arr[i].index(pair[1]) - 1 < 0:
                    p1 = 4

                decrypt_pair.append(arr[i][p0]+arr[i][p1])
            else:
                #for j in range(len(arr)):#
                  #  if pair[1] == arr[i][j]:#
                       # print(pair + " column")#
                for k in range(len(arr)):
                    if pair[1] in arr[k]:

                        pi = arr[i].index(pair[0])
                        pk = arr[k].index(pair[1])

                        d_pi = arr[i][pk]
                        d_pk = arr[k][pi]
                        decrypt_pair.append(d_pi+ d_pk)


decrypt_txt = ""
for pair in decrypt_pair:
    if pair[0] != 'X':
        decrypt_txt = decrypt_txt+pair[0]
    if pair[1] != 'X':
        decrypt_txt = decrypt_txt + pair[1]

print(decrypt_txt)


