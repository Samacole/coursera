def HammingDistance(p, q):
    count = 0
    Ham = 0
    for i in range(0, len(p)):
        if p[count] == q[count]:
            count +=1
        else:
            Ham += 1
            count += 1
    return Ham

string1 = "CTTGAAGTGGACCTCTAGTTCCTCTACAAAGAACAGGTTGACCTGTCGCGAAG"
string2 = "ATGCCTTACCTAGATGCAATGACGGACGTATTCCTTTTGCCTCAACGGCTCCT"
print (HammingDistance(string1, string2))
