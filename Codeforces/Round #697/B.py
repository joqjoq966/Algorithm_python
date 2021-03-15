import sys
input = sys.stdin.readline

def solve(n):
    ans = "NO"
    if n<2020:
        return "NO"
    q = n//2020
    for i in range(q+1):
        if i*2020 + (q-i)*2021==n:
            return "YES"
    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
