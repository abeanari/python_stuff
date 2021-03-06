'''
CS458
Project 2
Abraham Cheng

'''


import re

acronyms = []
PATTERN = r'[A-Z][A-Z][A-Z]+'
def acro_search(input_string):
    #acronyms = []
    for x in re.findall(PATTERN,input_string):
        x.strip()
        if (len(x)>1):
            acronyms.append(x)
    return (acronyms)

def acro_iter(input):
    qwer = re.finditer(PATTERN,input)
    return qwer

def backTrackAll(C, X, Y, i, j):
    if i == 0 or j == 0:
        return set([""])
    elif X[i-1] == Y[j-1]:
        return set([Z + X[i-1] for Z in backTrackAll(C, X, Y, i-1, j-1)])
    else:
        R = set()
        if C[i][j-1] >= C[i-1][j]:
            R.update(backTrackAll(C, X, Y, i, j-1))
        if C[i-1][j] >= C[i][j-1]:
            R.update(backTrackAll(C, X, Y, i-1, j))
        return R

def lcs(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
    # read the substring out from the matrix
    result = ""
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]
            result = a[x-1] + result
            x -= 1
            y -= 1
    return result

'''
test_string = "DOE Department of Energy FBI CIA  Rawr rAwr RAwe RaWR RAWr rAWR sigNATURE"
PATTERN = r'[A-Z][A-Z][A-Z]+'
print(acro_search(test_string))


PATTERN = r'[A-Z][A-Z][A-Z]+'
testfile = open('acrotextfile.txt', 'r')
text_in_file = testfile.read()
testfile.close()
print(acro_search(text_in_file))

testfile1 = open('acrotextfile2.txt', 'r')
text_in_file = testfile1.read()
testfile1.close()
print(acro_search(text_in_file))
'''

'''
#for match in regex1.finditer(text_in_file):
#    print ("%s: %s" %(match.start(), match.group(1)))

acro_len_list = []
for j in acronym:
    acro_len_list.append((len(acronym)*2))
for i in m.group():
    if x = m.group()
    lcs(m.group(), acronym)

'''
testfile1 = open('acrotextfile2.txt', 'r')
text_in_file = testfile1.read()
testfile1.close()
regex1 = re.compile(PATTERN)
for m in regex1.finditer(text_in_file):
    print (m.start(), m.group())