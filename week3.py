# Motif Enumeration
#input - int k and d , collection of str DNA
#Output - all (k,d)-Motifs in DNA
#used to find transcription factor binding sites for specifc genes within a collection of DNA strings
#example of use would be to find the binding sites for carcadian genes within plants
def motifenumeration(DNA, k, d):
    patterns = []
    for i in DNA:
        pat = DNA[i]
        for i in range(0, len(pat) - k + 2):
            pat2 = pat[i, i + k]
            
