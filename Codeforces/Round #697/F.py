import sys
input = sys.stdin.readline

def solve():
    ans = 0
    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    a = [[""] for _ in range(n)]
    b = [[""] for _ in range(n)]
    
    for i in range(n):
        a[i] = input().rstrip()
    space = input().rstrip()
    for i in range(n):
        b[i] = input().rstrip()
    print(a)
    print(b)
    # solve()
