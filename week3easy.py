

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

a = ["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"]


print(Score(a))
