#code to show the skew of G vs C (G-C where A and T are null skew) outputs in a list
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

#code that uses skew to find out the index's where minimum is attained
def Minskew(Genome):
    skewlist = skew(Genome)
    minvalue = min(skewlist)
    minindex = [i for i in range(0,len(skewlist)) if skewlist[i] == minvalue]
    return minindex

def removespaces(text):
    new = ""
    for i in range(0, len(text)):
        if text[i] != "":
            new = new + text[i]
    return new



Senterica = (open('Senterica3.txt', 'r')).read()
# not working as file may have line breaks? not sure how to fix so will go on to next Week as this is optional

print(Minskew(str(Senterica)))
