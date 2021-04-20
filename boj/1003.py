import sys
input = sys.stdin.readline

c = [[0,0]]*41
c[0] = [1,0]
c[1] = [0,1]

t = int(input())

while t:
    n = int(input())
    if n==0:
        print(c[0]) 
    elif n==1:
        print(c[1]) 
    else:
        print(c[n-1],c[n-2]) 
