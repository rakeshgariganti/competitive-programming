from math import ceil
a,b,n=map(int,raw_input().split())
x=a-b
print int(ceil(float(n-b)/x))