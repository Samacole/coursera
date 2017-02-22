
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
def motifenumeration(DNA, k, d):
    patterns = []
    for i in DNA:
        pat = DNA[i]
        for i in range(0, len(pat) - k + 2):
            pat2 = pat[i, i + k]
            Patnegh = neghbours(pat2, d)
            for i in patnegh:
                if # having trouble looping through DNA[], the idea is you would loop through every "neghbour" of every pattern with
                #each strand of DNA and if they are in all len(DNA) strings of DNA then add them to the list then remove dupes at the end
                # this example is not meant to be efficient and has therefore confused me
