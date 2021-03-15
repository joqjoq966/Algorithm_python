import sys
input = sys.stdin.readline

def solve(n,arr):
    # ans = 0
    c =[0]*(n+1)
    for i in range(n):
        c[arr[i]]+=1
    return max(c)

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(solve(n,arr))
