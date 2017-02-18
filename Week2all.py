

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

pat = "GCTCCA"
gen = "GGGTGCGGGTGGAATATTCGGGGACAATCCATTCTCGTTTGAACTACTCCAGGATTCGAGTTGGCTCCACGTATTATGTCGCAGTAATGCCTTAGGAAAAATCATACCCTCTTGAGCGTGACCGCTCTAATCCTTTAAAATGAATCGCATACAGGCAACCCACTTCGAAGAAAACACTAAGTTCTGAAAAGAGCTACAGTCTCCTGTGTGTATAAAGAGCCCACTACATTGTGCGCTACGCGTCCTCCCCCTTCTTTGTGCGAGTGGATCGGGTTCTAGCGGACAATACCAAGCATTAGAATGGGCTATGTAAGATCCACCCAATTTACCATATTAACTAGACTAACGCTGCAAGGACTGGCAAGGAGGTGCTAAGGACAAGTTAT"
d = 3

print(aproxpatterncount(pat, gen, d))
