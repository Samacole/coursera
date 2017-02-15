def patterntonumber(pattern):
    define = {"A" : 0, "C" : 1, "G" : 2, "T" : 3}
    if len(pattern) == 0:
        return 0
    s = pattern[len(pattern)-1]
    pre = pattern[:len(pattern)-1]
    s = define[s]
    return (4 * patterntonumber(pre)) + s

def numbertopattern(index, k):
    l = ["A", "C", "G", "T"]
    if k == 1:
        return l[index]
    d = index / 4
    s = index % 4
    q = l[s]
    prepat = numbertopattern(d, k-1)
    return prepat + q

print (numbertopattern(8779, 11))
