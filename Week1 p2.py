def Reverse(text):
    position = len(text) - 1
    empty = ""
    empty += text[[position]]
    empty -= 1
    while empty >= 0:
        empty += text[position]
        position -= 1
    return empty



def Compliment(text):
    Definition = {'A' : 'T', 'G' : 'C', 'T' : 'A', 'C' : 'G'}
    EmpString = ""
    Count = 0
    MaxLength = len(text) - 1
    Nucleo = text[Count]
    EmpString += Definition[Nucleo]
    while Count < MaxLength:
        Count += 1
        Nucleo = text[Count]
        EmpString += Definition[Nucleo]
    return EmpString

def ReverseComplement(thingy):
        a = Compliment(thingy)
        return reverse(a)

ReverseComplement("AAAACCCGGT")
