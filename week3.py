


from Week2all import *


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


# Motif Enumeration
#input - int k and d , collection of str DNA
#Output - all (k,d)-Motifs in DNA
#used to find transcription factor binding sites for specifc genes within a collection of DNA strings
#example of use would be to find the binding sites for carcadian clock genes within plants
#def motifenumeration(DNA, k, d):
#    patterns = []
#    for i in DNA:
#        pat = DNA[i]
#        for i in range(0, len(pat) - k + 2):
#            pat2 = pat[i, i + k]
#            Patnegh = neghbours(pat2, d)
#            for i in patnegh:
#                if # having trouble looping through DNA[], the idea is you would loop through every "neghbour" of every pattern with
                #each strand of DNA and if they are in all len(DNA) strings of DNA then add them to the list then remove dupes at the end
                # this example is not meant to be efficient and has confused me


# code to output the positions of pattern within the genome where pattern approx matches, max hammingdistance d
def aproxpatternmatch (pattern, text, d): # input - pattern being looked for, genome and max hamming distance
    indlist = []
    for i in range(len(text)-len(pattern)+1):
        check = text[i:i+len(pattern)]
        checked = hammingdistance(pattern, check)
        if checked <= d:
            indlist.append(i)
    return (indlist)


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


#code the converts a pattern of k lengh into an integer to be used as an index in a frequency matching capacity. This uses "to the log4" methodology
#def patterntonumber(pattern):
#    define = {"A" : 0, "C" : 1, "G" : 2, "T" : 3}
#    if len(pattern) == 0:
    #    return 0
#    s = pattern[len(pattern)-1]
#    pre = pattern[:len(pattern)-1]
#    s = define[s]
    #return (4 * patterntonumber(pre)) + s

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


def freqwordsmismatch(text, k, d):
    freqpat = []
    freqarray = compfreqwithmismatches(text, k, d)
    maxcount = max(freqarray)
    for i in range(0, 4 ** k):
        if freqarray[i] == maxcount:
            pat = numbertopattern(i, k)
            freqpat.append(pat)
    return (freqpat)

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
# Motif Enumeration
#input - int k and d , collection of str DNA
#Output - all (k,d)-Motifs in DNA
#used to find transcription factor binding sites for specifc genes within a collection of DNA strings
#example of use would be to find the binding sites for carcadian clock genes within plants
def motifenumeration(DNA, k, d):
    patterns = []
    pat = DNA[0]
    l = len(pat)
    l_dna = len(DNA)
    for i in range(l - k + 1):
        cur = pat[i:i+k]
        neighbors = neghbours(cur, d)
        for neighbor in neighbors:
            oc = 0
            for str in DNA:
                pos = freqwordsmismatch(neighbor, str, d)
                if len(pos) > 0:
                    oc += 1
            if oc == l_dna:
                patterns.add(neighbor)
    return patterns

#DNA_1 = ["ATTTGGC", "TGCCTTA", "CGGTATC", "GAAAATT"]
#K_1 = 3
#D_1 = 1

#print(motifenumeration(DNA_1, K_1, D_1))


print(patterntonumber("AATTA"))
