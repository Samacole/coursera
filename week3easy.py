
import math
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

def Consensus(Motifs):
    count = Count(Motifs)
    k = len(count["A"])
    consensus = ""
    for j in range(k):
        m = 0
        freqsymbol = ""
        for i in "ACGT":
            if count[i][j] > m:
                m = count[i][j]
                freqsymbol = i
        consensus += freqsymbol
    return consensus


def Score(Motifs):
    consen = Consensus(Motifs)
    num = len(Motifs)
    basenum = len(Motifs[0])
    count = 0
    for i in range(basenum):
        for j in range(num):
            if Motifs[j][i]!= consen[i]:
                count = count + 1
    return(count)
def Pr(Text, Profile):
    k = len(Text)
    prob = 1
    for i in range(k):
        let = Text[i]
        prob = prob * Profile[let][i]
    return prob


def ProfileMostProbablePattern(Text, k, Profile):
    m = 0
    loc = 0
    for i in range(len(Text) - k):
        textnow = Text[i:i+k]
        Probnow = Pr(textnow, Profile)
        if Probnow > m:
            m = Probnow
            loc = i
    return Text[loc:loc + k]



def Profile(Motifs):
    count = Count(Motifs)
    k = len(count["A"])
    letters = "ACGT"
    for i in range(4):
        let = letters[i]
        for j in range(k):
            count[let][j] = count[let][j] / k
    return (count)

def Entrop(profile):
    entrolist = []
    k = len(profile["A"])
    for a in range(0, k):
        entrolist.append(0)
    letter = "ACGT"
    for i in range(0,k):
        entronum = 0
        for j in range(0,3):
            poslet = letter[j]
            entropart = profile[poslet][i]
            if entropart == 0.0:
                entrocalc = 0
            else:
                entrocalc = entropart * math.log2(entropart)
            entronum = entronum + entrocalc
            entrolist[i] = -(entronum)
    return entrolist


def sument(profile):
    numb = Entrop(profile)
    k = len(numb)
    count = 0
    for i in range(0, k):
        count = count + numb[i]
    return count


def GreedyMotifSearch(dna, k ,t):
    bestmotifs = []
    for i in range(0, t):
        bestmotifs.append(dna[i][0:k])
    n = len(dna[0])
    for i in range(n-k+1):
        motifs = []
        motifs.append(dna[0][i:i+k])
        for j in range(1, t):
            p = Profile(motifs[0:j])
            motifs.append(ProfileMostProbablePattern(dna[j], k, p))
        if Score(motifs) < Score(bestmotifs):
            bestmotifs = motifs
    return bestmotifs
#dna2 = ["GCAGGTTAATACCGCGGATCAGCTGAGAAACCGGAATGTGCGT", "CCTGCATGCCCGGTTTGAGGAACATCAGCGAAGAACTGTGCGT", "GCGCCAGTAACCCGTGCCAGTCAGGTTAATGGCAGTAACATTT", "AACCCGTGCCAGTCAGGTTAATGGCAGTAACATTTATGCCTTC", "ATGCCTTCCGCGCCAATTGTTCGTATCGTCGCCACTTCGAGTG"]

#dna3 = ["GCAGGTTAATACCGCGGATCAGCTGAGAAACCGGAATGTGCGT", "CCTGCATGCCCGGTTTGAGGAACATCAGCGAAGAACTGTGCGT", "GCGCCAGTAACCCGTGCCAGTCAGGTTAATGGCAGTAACATTT", "AACCCGTGCCAGTCAGGTTAATGGCAGTAACATTTATGCCTTC", "ATGCCTTCCGCGCCAATTGTTCGTATCGTCGCCACTTCGAGTG"]

M = [
"TCGGGGGTTTTT",
"CCGGTGACTTAC",
"ACGGGGATTTTC",
"TTGGGGACTTTT",
"AAGGGGACTTCC",
"TTGGGGACTTCC",
"TCGGGGATTCAT",
"TCGGGGATTCCT",
"TAGGGGAACTAC",
"TCGGGTATAACC"
]



A1 =[0.4, 0.3, 0.0, 0.1, 0.0, 0.9]
C2 = [0.2, 0.3, 0.0, 0.4, 0.0, 0.1]
G2 = [0.1, 0.3, 1.0, 0.1, 0.5, 0.0]
T2 = [0.3, 0.1, 0.0, 0.4, 0.5, 0.0]

prof123 = {"A":A1, "C":C2, "G":G2, "T":T2}
#a = ["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"]

#prof1 = {"A":[0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0], "C": [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6], "G": [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0], "T": [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]}
#prof2 = {"A":[0.7, 0.2, 0.1, 0.5, 0.4, 0.3, 0.2, 0.1], "C": [0.2, 0.2, 0.5, 0.4, 0.2, 0.3, 0.1, 0.6], "G": [0.1, 0.3, 0.2, 0.1, 0.2, 0.1, 0.4, 0.2], "T": [0.0, 0.3, 0.2, 0.0, 0.2, 0.3, 0.3, 0.1]}
#prof3 = {"A":[0.2, 0.2, 0.3, 0.2, 0.3], "C": [0.4, 0.3, 0.1, 0.5, 0.1], "G": [0.3, 0.3, 0.5, 0.2, 0.4], "T": [0.1, 0.2, 0.1, 0.1, 0.2]}
#t1 ="TTACCATGGGACCGCTGACTGATTTCTGGCGTCAGCGTGATGCTGGTGTGGATGACATTCCGGTGCGCTTTGTAAGCAGAGTTTA"
#print(ProfileMostProbablePattern(t1, 5, prof3))
#print(GreedyMotifSearch(dna3, 6, 5))
#print(Profile(Motifs))
#print(sument(Profile(M)))

#print(sument(Profile(M)))9
print(-(0.2 * (math.log2(0.2)) + 0.6 * (math.log2(0.6)) + 0.2 * (math.log2(0.2))))


# may be an issue if there is a 0 in the log as log0 is error - no issue with teh summing , will have to test one by one later
