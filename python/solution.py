def solution(message, key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    # create polybius string
    polybiusString = ""
    
    for c in key:
        if c not in polybiusString:
            polybiusString += c
            alphabet = alphabet.replace(c, "")

    # dump remaining alphabet in polybius string
    polybiusString += alphabet

    digrams = [message[i:i+2] for i in range(0, len(message), 2)]

    ans = ""
    
    for pair in digrams:
        fst = polybiusString.index(pair[0])
        snd = polybiusString.index(pair[1])
        # same column rule
        if abs(fst - snd) == 5:
            ans += polybiusString[fst-5]
            ans += polybiusString[snd-5]
        # same row rule
        elif fst//5 == snd//5:
            if fst%5 == 0: fstIdx = fst+4
            else: fstIdx = fst-1
            if snd%5 == 0: sndIdx = snd+4
            else: sndIdx = snd-1

            ans += polybiusString[fstIdx]
            ans += polybiusString[sndIdx]
        else:
            # width of rect
            w = abs(fst%5 - snd%5)
            # height of rect
            h = abs(fst//5 - snd//5)

            # if 1st char is on right side of rect
            if fst%5 > snd%5:
                ans += polybiusString[fst-w]
            else: # if 1st char on left side of rect
                ans += polybiusString[fst+w]

            # if 1st char is on bottom side of rect
            if fst//5 > snd//5:
                ans += polybiusString[fst-(h*5)]
            else: # if 1st char is on top side of rect
                ans += polybiusString[fst+(h*5)]

    # remove X's
    ans = ans.replace("X", "")

    print(ans)

solution("IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV", "SUPERSPY")