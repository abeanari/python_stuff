'''
CS458
Project 6
Abraham Cheng

'''
import random

#----choosing 2-4 closest keys of a letter on keyboard----
AA = ['q', 'w', 's', 'z']
BB = ['v', 'g', 'h', 'n']
CC = ['x', 'd', 'f', 'v']
DD = ['s', 'e', 'r', 'f']
EE = ['w', 's', 'd', 'r']
FF = ['d', 'r', 'g', 'v']
GG = ['f', 't', 'h', 'b']
HH = ['g', 'y', 'j', 'n']
II = ['u', 'j', 'k', 'o']
JJ = ['h', 'u', 'i', 'k']
KK = ['j', 'i', 'o', 'l']
LL = ['k', 'o', 'p']
MM = ['n', 'j', 'k']
NN = ['b', 'h', 'j', 'm']
OO = ['i', 'k', 'l', 'p']
PP = ['o', 'l']
QQ = ['a', 'w']
RR = ['e', 'd', 'f', 't']
SS = ['a', 'w', 'e', 'd']
TT = ['r', 'f', 'g', 'y']
UU = ['y', 'h', 'j', 'i']
VV = ['c', 'f', 'g', 'b']
WW = ['q', 'a', 's', 'e']
XX = ['z', 's', 'd', 'c']
YY = ['t', 'g', 'h', 'u']
ZZ = ['a', 's', 'x']



def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def file_corrupt(inputFile, outputFile):
    wr = open(outputFile, 'w')

    with open(inputFile) as op:
        while True:
            c = op.read(1)
            c = c.lower()

    #----random number between 1-100
    #----10% corruption is any number <=10
            if c.isalpha() == True and random.randint(1, 100) <= 10:
                if c == 'a':
                    c = random.choice(AA)
                    #wr.write(c)
                if c == 'b':
                    c = random.choice(BB)
                    #wr.write(c)
                if c == 'c':
                    c = random.choice(CC)
                    #wr.write(c)
                if c == 'd':
                    c = random.choice(DD)
                    #wr.write(c)
                if c == 'e':
                    c = random.choice(EE)
                    #wr.write(c)
                if c == 'f':
                    c = random.choice(FF)
                    #wr.write(c)
                if c == 'g':
                    c = random.choice(GG)
                    #wr.write(c)
                if c == 'h':
                    c = random.choice(HH)
                    #wr.write(c)
                if c == 'i':
                    c = random.choice(II)
                    #wr.write(c)
                if c == 'j':
                    c = random.choice(JJ)
                    #wr.write(c)
                if c == 'k':
                    c = random.choice(KK)
                    #wr.write(c)
                if c == 'l':
                    c = random.choice(LL)
                    #wr.write(c)
                if c == 'm':
                    c = random.choice(MM)
                    #wr.write(c)
                if c == 'n':
                    c = random.choice(NN)
                    #wr.write(c)
                if c == 'o':
                    c = random.choice(OO)
                    #wr.write(c)
                if c == 'p':
                    c = random.choice(PP)
                    #wr.write(c)
                if c == 'q':
                    c = random.choice(QQ)
                    #wr.write(c)
                if c == 'r':
                    c = random.choice(RR)
                    #wr.write(c)
                if c == 's':
                    c = random.choice(SS)
                    #wr.write(c)
                if c == 't':
                    c = random.choice(TT)
                    #wr.write(c)
                if c == 'u':
                    c = random.choice(UU)
                    #wr.write(c)
                if c == 'v':
                    c = random.choice(VV)
                    #wr.write(c)
                if c == 'w':
                    c = random.choice(WW)
                    #wr.write(c)
                if c == 'x':
                    c = random.choice(XX)
                    #wr.write(c)
                if c == 'y':
                    c = random.choice(YY)
                    #wr.write(c)
                if c == 'z':
                    c = random.choice(ZZ)
                    #wr.write(c)
            wr.write(c)
            if not c:
                break
    wr.close()


print(file_len('unabom.txt'), "lines in file")
file_corrupt('unabom.txt', 'corrupted.txt')