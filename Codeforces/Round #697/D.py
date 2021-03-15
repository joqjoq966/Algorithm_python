import sys
input = sys.stdin.readline

def solve(n,m,c):
    ans = 0
    c = sorted(c,reverse = True)
    free = 0
    for i in range(n):
        free += c[i][0]
    if free < m:
        return -1
    
    
    return ans

t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = [(x,y) for x,y in zip(a,b)]
    print(solve(n,m,c))