
#code the converts a pattern of k lengh into an integer to be used as an index in a frequency matching capacity. This uses "to the log4" methodology
def patterntonumber(pattern):
    define = {"A" : 0, "C" : 1, "G" : 2, "T" : 3}
    if len(pattern) == 0:
        return 0
    s = pattern[len(pattern)-1]
    pre = pattern[:len(pattern)-1]
    s = define[s]
    return (4 * patterntonumber(pre)) + s

#code to convert an integer to the log4 of k lengh back into a pattern - basis base nucleotides obv
def numbertopattern(index, k):
    l = ["A", "C", "G", "T"]
    if k == 1:
        return l[index]
    d = index / 4
    s = index % 4
    q = l[int(s)]
    prepat = numbertopattern(int(d), k-1)
    return prepat + q
#code to create a list of possible index's bases on the genome lengh and k lengh criteria, then iterates through the
#genome provided adding a 1 to any index that has a pattern which can later be converted back pattern - idea is
#you dont have to use so much memory storeing each combination of pattern k lengh
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

#algo that uses the index log4 idea vs storing the patterns themselves in a list - much faster for bigger Genomes ,much slower for smaller
#as allot of memory would be used to convert them back and forth
def fasterfreqwords(Text, k):
    freqpat = []
    freqarray = computingfrequencies(Text, k)
    maxcount = max(freqarray)
    for i in range(0, 4 ** k):
        if freqarray[i] == maxcount:
            pat = numbertopattern(freqarray[i:k])
            freqpat.append(pat)
    return (freqpat)

#algo that leverages the previous log4 model and frequent words algo to find all patters that appear in genome that have
#the following criteria: apear within the sliding window of L lengh, have a k lengh and apear atleast t times within that window
#this is built on the idea that you can 'slide' the window accross by removing the first pattern and adding the last pattern
#rather than iterating through the L window end to end with only moving 1 index
#this model also uses the log 4 compression as per above, would be much faster to store the patterns themselves if the genome is short
def clumpfinding(genome, k, t, L):
    freqpat = []
    clump = []
    freqarray =[]
    for i in range(0, 4**k):
        clump.append(0)
    text = genome[:L]
    freqarray = computingfrequencies(text, k)
#    print(freqarray)
    for i in range(0, 4**k):
        if freqarray[i] >= t:
            clump[i] = 1
    #    print(clump)
    for i in range (1, len(genome) - L + 1):
        fp = genome[i - 1:i - 1+ k]
        #print(fp)
        index = patterntonumber(fp)
        freqarray[index] = freqarray[index] - 1
        lp = genome[i + L - k:i + L]
        index = patterntonumber(lp)
        freqarray[index] = freqarray[index] + 1
        if freqarray[index] >= t:
        #    print(freqarray[index])
            clump[index] = 1
    for i in range(0, 4**k):
        if clump[i] == 1:
            #print(freqarray[388])
            pat = numbertopattern(i, k)
            freqpat.append(pat)
    return (freqpat)
gen1 = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
k1 = 5
L1 = 50
t1 = 4
print (*clumpfinding(gen1, k1, t1, L1), sep=' ')
