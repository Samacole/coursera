

def Count(Motifs):
    k = len(Motifs[0])
    count = {}
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return (count)

def Profile(Motifs):
    count = Count(Motifs)
    num = len(count)
    k = len(count["A"])
    print(count[num])
'''    for i in range(num):
        for j in range(k):
            symb = count[i][j]
            count[i][symb][j] = count[i][symb][j] / num
    return (count)
'''
a = ["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"]

'''
print(Profile(a))

'''

Profile(a)
