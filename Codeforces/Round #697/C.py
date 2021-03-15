import sys
input = sys.stdin.readline

def solve(a,b,k):
    ans = 0
    ca = [0]*(a+1)
    cb = [0]*(b+1)
    for i in range(k):    
        ca[aa[i]]+=1
        cb[bb[i]]+=1
    for i in range(k):
        ans += k + 1 - ca[aa[i]] -cb[bb[i]]
    return ans//2

t = int(input())
for i in range(t):
    a,b,k = map(int,input().split())
    aa = list(map(int,input().split()))
    bb = list(map(int,input().split()))
    print(solve(a,b,k))