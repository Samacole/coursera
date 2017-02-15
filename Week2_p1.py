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

print(*skew("TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"), sep=' ')
