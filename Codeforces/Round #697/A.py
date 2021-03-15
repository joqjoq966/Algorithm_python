import sys
input = sys.stdin.readline

def solve(n):
    ans = "NO"
    if n==1:
        return "YES"
    while True:
        if n%2==0 and n>1:
            n//=2
        else:
            break
    if n!=1:
        return "YES"
    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
