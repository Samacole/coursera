def PatternMatch(Genome, Pattern, d):
    pos = []
	for i in range(len(Genome) - len(Pattern) + 1):
	    if HammingDistance(Pattern, Genome[i:i+len(Pattern)]) <= d:
		    pos.append(i)
	return (pos)
def HammingDistance(Pattern, q):
    count = 0
    Ham = 0
    for i in range(0, len(p)):
        if p[count] == q[count]:
            count +=1
        else:
            Ham += 1
            count += 1
    return Ham

print (PatternMatch("CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT", "ATTCTGGA", 3))
