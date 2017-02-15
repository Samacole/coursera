def PatternMatching (Pattern, Genome):
    Matches = []
    Count = 0
    MaxCount = len(Genome) - 1
    while Count < MaxCount:
        if Genome[Count:Count + len(Pattern)] == Pattern:
            Matches.append(Count)
            Count += 1
        else:
            Count += 1
    print(*Matches, sep=' ')

file = open('vibcol.txt', 'r')
P1 = "CTTGATCAT"
G1 = file.read()

PatternMatching(P1, G1)
