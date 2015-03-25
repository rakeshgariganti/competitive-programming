import random
from math import *
from fractions import gcd
mapper=map
mi=int
mf=float
inf=mf('inf')
ri=raw_input


t=mi(ri())
while t>0:
    t-=1
    n=mi(ri())
    lis=mapper(mi,ri().split())
    ocheck=False
    for i in lis:
        for j in lis:
            if gcd(i,j)==1:
                print "YES"
                ocheck=True
                break
        if ocheck:
            break
    if not ocheck:
        print "NO"