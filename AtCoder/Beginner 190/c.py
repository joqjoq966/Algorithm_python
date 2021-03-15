from itertools import combinations
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a,b,c,d = [],[],[],[]
for _ in range(m):
    aa,bb = map(int,input().split())
    a.append(aa)
    b.append(bb)
k= int(input())
for _ in range(k):
    cc,dd = map(int,input().split())
    c.append(cc)
    d.append(dd)
ans = 0
choose = set()

for x in range(k+1):
    combi = combinations([y for y in range(1,k+1)],x)
    # print(list(combi))
    for co in combi:
        for i in range(1,k+1):
            if i in co:
                choose.add(c[i-1])
            else:
                choose.add(d[i-1])
        tmp = 0
        for i in range(m):
            if a[i] in choose and b[i] in choose:
                tmp +=1
        ans= max(ans,tmp)
        # print(choose)
        choose.clear()
print(ans)