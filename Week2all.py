

#code to show the skew of G vs C (G-C where A and T are null skew) outputs in a list
def skew(Genome):
    countskew = 0
    skewlist = [0]
    count = 0
    Define = {"A": 0, "C" : -1, "G" : 1, "T" : 0}
    while count < len(Genome):
        countskew = countskew + Define[Genome[count]]
        skewlist.append(countskew)
        count += 1
    return (skewlist)

def remove_duplicates(Freq):
    return list(set(Freq))
#code that uses skew to find out the index's where minimum is attained
def Minskew(Genome):
    skewlist = skew(Genome)
    minvalue = min(skewlist)
    minindex = [i for i in range(0,len(skewlist)) if skewlist[i] == minvalue]
    return minindex

# code to find the 'Hammingdistance' between 2 patterns of equal lengh (the int differnce in bases)
def hammingdistance(p, q):
    count = 0
    Ham = 0
    for i in range(0, len(p)):
        if p[count] == q[count]:
            count +=1
        else:
            Ham += 1
            count += 1
    return Ham

# code to output the positions of pattern within the genome where pattern approx matches, max hammingdistance d
def aproxpatternmatch (pattern, text, d): # input - pattern being looked for, genome and max hamming distance
    indlist = []
    for i in range(len(text)-len(pattern)+1):
        check = text[i:i+len(pattern)]
        checked = hammingdistance(pattern, check)
        if checked <= d:
            indlist.append(i)
    return (indlist)

#code to impliment appox pattern count
#input - pattern, text and d (approve mismatches aloud as int)
#output - count of pattern within text given the number of missmatches aloud
def aproxpatterncount(pattern, text, d):
    count = 0
    for i in range(0, len(text) - len(pattern) + 1):
        pattern2 = text[i:i + len(pattern)]
        if hammingdistance(pattern, pattern2) <= d:
            count = count + 1
    return (count)

#sub routine to help with finding possible neghours in a genome
#input - pattern
#output - list of possible patterns given 1 change is relivant (d = 1)
'''
def imneghbours(pattern):
    neighbourhood = [pattern]
    for i in range(1, len(pattern) + 1):
        symbol = pattern[i]
    #    for i in

    '''
def neghbours(pattern, d):
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return ["A", "C", "G", "T"]
    Neghbourhood = []
    suffixnegh = neghbours(pattern[1:], d)
    for text in suffixnegh:
        if hammingdistance(pattern[1:], text) < d:
            for x in ["A", "C", "G", "T"]:
                Neghbourhood.append(x + text)
        else:
            Neghbourhood.append(pattern[:1] + text)
    return (Neghbourhood)
#print(*neghbours("CTGAGCTAAG", 3), sep ='\n')

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

# sub routine to help with implimentation with aprox frequent words - will generate a list of potential
# patterns of k lengh within a genome given mismatch int of d
#inputs - text (genome), k (lengh of pattern), d (int denoting max number of mismatches)
#output - freq array of possible potential matches given d (in index form) (using pattern to number varient "neghbours")
def compfreqwithmismatches(text, k, d):
    freqarray = []
    for i in range(0, 4 ** k):
        freqarray.append(0)
    for i in range(0, len(text) - k + 1 ):
        pattern = text[i:i + k]
        neighbourhood = neghbours(pattern, d)
        for aprox in neighbourhood:
            j = patterntonumber(aprox)
            freqarray[j] = freqarray[j] + 1
    return (freqarray)
# Frequent words with mismatches - leverages above algo for inclusion of "mistmatchs" of order d
# input - Genome, pattern lengh (k), hamming distance units (d)
# Output - List of the most frequent patterns seporated by a space (given the hamming distance provided)
'''
def freqwordswithmismatches(text, k , d):
    freqpat = []
    neghbourhood = []
    for i in range(0, len(text) - k + 1):
        neghbourhood.append(neghbours(text[i:i+k],d))
    neghbourhoodarray = reduce(operator.concat, neghbourhood)
    for i in neghbourhoodarray:
        pattern = neghbourhoodarray[i]
        index
'''
#the psudo code is hard to understand so will impliment my own
def freqwordsmismatch(text, k, d):
    freqpat = []
    freqarray = compfreqwithmismatches(text, k, d)
    maxcount = max(freqarray)
    for i in range(0, 4 ** k):
        if freqarray[i] == maxcount:
            pat = numbertopattern(i, k)
            freqpat.append(pat)
    return (freqpat)

#gen5 = "ATAATAGTCGTATACTGTCGTTAATAACTACTGTCGATAACTGTCGTTATTATATTTAATAATAATATATGTCGGTCGTTATATTTATTATTAACTGTCGTATATATATTTAATATTAATAATAATATATTATTATATAATATTATTAACTGTCGTTAGTCGGTCGTTAATAGTCGGTCGATATATTATTATTATTATACTGTCGGTCGATATTATTAGTCGACTATATTAGTCGACTGTCGATAATAGTCGTTAATAACTTTAACTTTAGTCGGTCGGTCGATAATAGTCGGTCGGTCGTTATTAACTTATTTATATTTATTAATATTAATAGTCGGTCGGTCGATAATAGTCGTATTTAACTTATATAACT"
#print(*freqwordsmismatch(gen5, 7, 2), sep=' ')

#adding in some functions from week 1 to do with reverse complements
def reverse(text):
    position = len(text) - 1
    empty = ""
    empty += text[position]
    position -= 1
    while position >= 0:
        empty += text[position]
        position -= 1
    return empty

def compliment(text):
    Definition = {'A' : 'T', 'G' : 'C', 'T' : 'A', 'C' : 'G'}
    EmpString = ""
    Count = 0
    MaxLength = len(text) - 1
    Nucleo = text[Count]
    EmpString += Definition[Nucleo]
    while Count < MaxLength:
        Count += 1
        Nucleo = text[Count]
        EmpString += Definition[Nucleo]
    return EmpString

def reversecomplement(text):
        a = compliment(text)
        return reverse(a)

#freq array generator to include mismatches as rever compliments
def compfreqwithmismatchesreversecomp(text, k, d):
    freqarray = []
    for i in range(0, 4 ** k):
        freqarray.append(0)
    for i in range(0, len(text) - k + 1 ):
        pattern = text[i:i + k]
        neighbourhood = neghbours(pattern, d)
        for aprox in neighbourhood:
            a = reversecomplement(aprox)
            b = patterntonumber(a)
            j = patterntonumber(aprox)
            freqarray[j] = freqarray[j] + 1
            freqarray[b] = freqarray[b] +1
    return (freqarray)


def freqwordsmismatchRC(text, k, d):
    freqpat = []
    freqarray = compfreqwithmismatchesreversecomp(text, k, d)
    maxcount = max(freqarray)
    for i in range(0, 4 ** k):
        if freqarray[i] == maxcount:
            pat = numbertopattern(i, k)
            freqpat.append(pat)
    return (freqpat)


#gen4 = "ACACGCGCCCGGCCCGCCGACCTAACCTACCGACCCGCCGGCGCCCGCCGCCGACACCCGCCGCCGCCGCCGACGCACACCCGGCGCACCCGCCGGCCTACCGCCGGCGCCCGCCGCTAGCGCCTAGCGCACCCGGCCCGACCTAACGCCCGCCGCCGGCGCGCCCGCTAGCCTACCGGCCCGCTACCGCTACCGGCGCGCCTAACCTACCGGCCTAACCCGGCGCCCGCTACCG"

#print(*freqwordsmismatchRC(gen4, 5, 3), sep = ' ')
