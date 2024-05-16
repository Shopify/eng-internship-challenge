
def generate_table(keyword):

    # Initializing 5x5 empty array (Playfair table)
    playfair_table = [[None]*5 for i in range(5)]
    
    # Cleaning up the string: no duplicate letters allowed, and since the challenge did not specify,
    # J's and Q's will be kept
    newStr = ""
    for char in keyword:
        if char not in newStr:
            newStr += char.upper()
    keyword = newStr

    # Checks if keyword is bigger than the table. In that case, in order to prevent IndexError,
    # it slices the string
    if len(keyword) > 25:
        keyword = keyword[:25]

    # Populates empty table with the letters from the keyword
    for i in range(len(keyword)):
        playfair_table[i//5][i%5] = keyword[i]

    # Continues to populate the table with letters from the alphabet, starting after the keyword
    # Makes sure to skip letters from the alphabet that were already included in the keyword, to avoid repetition
    j=0
    for i in range(25):
        if playfair_table[i//5][i%5] != None:
            continue
        if chr(ord('A')+j) in keyword:
            j+=1
        playfair_table[i//5][i%5] = chr(ord('A')+j)
        j+=1
    
    return playfair_table




table = generate_table("HELLOWORLD")
for row in table:
    print(row)