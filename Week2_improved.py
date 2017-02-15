def patternMatch (Genome, Pattern, d):
    pos = {}
    for i in range(0,len(Genome)-len(Pattern)-1):
        if HammingDistance(Pattern, Genome(i:i))