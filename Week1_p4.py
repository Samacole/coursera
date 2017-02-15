def PatternToNumber(Pattern):
    Count = 0
    Tresult = 0
    MaxCount = len(Pattern) - 1
    Bine = {"A" : 0, "C" : 1, "G" : 2, "T" : 3}
    while Count < MaxCount:
        Tresult += Bine[Pattern[Count]]
        Count += 1
    Tresult = 4 ** Tresult
    Tresult = Tresult + Bine[Pattern[len(Pattern) - 1]]
    print (Tresult)

#PatternToNumber("AGT")
#sum([Bine[x] for x in Pattern])

#'AGT'
#['A', 'G', 'T']
#[0, 2, 3]

#pattern= 'ATGCAA'
#032100

pa = "TATCGAATTCATTAAGGGGGGGTTTTTATCTGTCGGATTATTAGTACCTTCACGTGCCCTGCTGCCGTATACTTAATGAGGGCTGATTAGCGTCCTGTTGTGGGGGTCGTACAGTGCATCTTCAAGATTTAGGCGTCGTGGGCTCAACAGGGGGGTATCGGCTATTGGCAGCACTTCTAGCGTCGTGCGGAAACCCCGCAGTAAACTCAGATCAACCCCAGTAGCCAACAGAAAAAATCTCGAGGGCACGTCATCCTGGCAAGTCCTACCCCTCCGGGCAGCAATTGCGATTCGGGGTAATAAGTACGGATCTACCACAGAGACGTGGACCTTTATCAGACGTTTATGAAAGTCTGGTGCTGGCACGGGGCGCGTTCCCTCATAAGGACTCTCATGGAGACTAGCAGACCGACGTCGCCAATAATGGACCTACGTGAGCGGATACGTGTAGACCTCATCGTCTGGTCAATTAACTAAAGCAAGCTAGAAACGTCCGAGGGGAGACAATGTCTACGCTCCCTCCCGACGCGCGGGCACACAAGGGCGGCACCTGCGCTCACGGGGCGAGCATCATATGTGGCTTTCTTCGAACCTAGACACGCAGGCCAAGCGGATATTTGTAGACCTATTGATGGTAAACAAACTCCAACCGATGGCACTTTCCCGTCACAAACATAAGAGCCGCCACCTGCCCCTGTGCTTAATGGATGTAGGACCCTTTCATTTGAAGA"
def pattern_to_number(pattern):
    Bine = {"A" : 0, "C" : 1, "G" : 2, "T" : 3}
    a = [Bine[y] for y in pattern]
    index = 0
    total = 0
    while index < len(a):
        total += 4 ** (index + 1) * a[len(a) - index - 1]
        if len(a) ** (index + 1) * a[len(a) - index - 1] > 65536:
            print(index, 4 ** (index + 1) * a[len(a) - index - 1])
        index += 1
    return total

BINE = {"A" : 0, "C" : 1, "G" : 2, "T" : 3}

def pattern_t_n(pattern):
    if len(pattern) == 0:
        return 0
    prefix = pattern[0:-1]
    symbol = pattern[-1]
    print('dogs', pattern, symbol, pattern_t_n(prefix), BINE.get(symbol, 0))
    return 4 ** (pattern_t_n(prefix) + BINE.get(symbol, 0))

def ComputingFrequencies(Text, k):
    i = 0
    frequency_array = [0 for x in range(0, 4 ** k)]
    count = 0
    while count <= len(Text) - k:
        pattern = Text[count:count+k]
        print(pattern)
        j = pattern_t_n(pattern)
        print('cats')
        frequency_array[j] = frequency_array[j] + 1
        count += 1

    return frequency_array

print(ComputingFrequencies(pa, 8))
#print (*ComputingFrequencies(pa, 8), sep=' ')

# 6^4 5^4 4^4 3^4 2^2 1^4
# 1024 256  64  16 4 1

# 1^4 * 2  = 8
# 0    3    2   1  0 0
# 0    768 128 16  0 0  =
#
# ^2
# 8 4 2 1
# 0 1 0 1
# 0 4 0 1 = 5
#
# 7^4   6^4  5^4  4^4 3^4 2^4 1^4
# 4096  1024 256  64  16   4   1
#
# 5437
# 1110331
# CCCATTC
# 1
# 1341
# 1
# 317
# 1
# 61
# 3
# 13
# 3
# 1
# 0
#
# [0, 0, 0, 0, 0]
