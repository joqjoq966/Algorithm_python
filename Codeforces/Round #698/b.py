import sys
input = sys.stdin.readline

def solve(n,d):
    if n >= 10*d:
        return "YES"
    
    while n>0:
        if n%d==0:
            return "YES"
        else:
            n-=10
    return "NO"

t = int(input())
for _ in range(t):
    q,d = map(int,input().split())
    arr = list(map(int,input().split()))
    for i in range(q):
        print(solve(arr[i],d))
