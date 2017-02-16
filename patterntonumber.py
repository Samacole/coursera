def patterntonumber(pattern):
    define = {"A" : 0, "C" : 1, "G" : 2, "T" : 3}
    if len(pattern) == 0:
        return 0
    s = pattern[len(pattern)-1]
    pre = pattern[:len(pattern)-1]
    s = define[s]
    return (4 * patterntonumber(pre)) + s

def numbertopattern(index, k):
    l = ["A", "C", "G", "T"]
    if k == 1:
        return l[index]
    d = index / 4
    s = index % 4
    q = l[s]
    prepat = numbertopattern(d, k-1)
    return prepat + q

def computingfrequencies(Text, k):
    i = 0
    j = 0
    freq = []
    for i in range(0, 4**k):
        freq.append(0)
    for i in range(0, len(Text)-k + 1):
        a = Text[i:i + k]
#        print (a)
        b = patterntonumber(a)
#        print (b)
        freq[b] = freq[b] + 1
        i += 1
    return (freq)


def fasterfreqwords(Text, k):
    freqpat = []
    freqarray = computingfrequencies(Text, k)
    maxcount = max(freqarray)
    for i in range(0, 4 ** k):
        if freqarray[i] == maxcount:
            pat = numbertopattern(freqarray[i:k])
            freqpat.append(pat)
    return (freqpat)



def clumpfinding(genome, k, t, L):
    freqpat = []
    clump = []
    freqarray =[]
    for i in range(0, 4**k):
        clump.append(0)
    text = genome[:L]
    freqarray = computingfrequencies(text, k)
    for i in range(0, 4**k):
        if freqarray[i] >= t:
            clump[i] = clump[i] + 1
        for i in range (1, len(genome) - L + 1):
            fp = genome[i - 1:i - 1+ k]
            index = patterntonumber(fp)
            freqarray[index] = freqarray[index] - 1
            lp = genome[i + L - k:i + L]
            index = patterntonumber(lp)
            freqarray[index] = freqarray[index] + 1
            if freqarray[index] >= t:
                clump[index] = clump[i] + 1
        for i in range(0, 4**k):
            print(clump)
            if clump[i] == 1:
                pat = numbertopattern(i, k)
                freqpat.append(pat)
            return (freqpat)
gen1 = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
k1 = 5
L1 = 50
t1 = 4
print (clumpfinding(gen1, k1, t1, L1))
