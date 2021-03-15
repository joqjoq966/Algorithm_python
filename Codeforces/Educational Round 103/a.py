import sys
input = sys.stdin.readline

def solve(n,k):
    ans = 0
    if k==1 or n%k==0:
        return 1
    while n>k:
        k+=k
    if k%n==0:
        ans += k//n
    else:
        ans += k//n +1
    
    return ans

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    print(solve(n,k))
