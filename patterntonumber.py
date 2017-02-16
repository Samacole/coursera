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
        if freqarray(i) == maxcount:
            pat = numbertopatter(i:k)
            freqpat.append(pat)
    return (freqpat)

print (fasterfreqwords())
