import sys
input = sys.stdin.readline

def solve(n,k,arr):
    ans = 0
    num = [0]*1001
    for i in arr:
        num[i] += 1
    s = set(arr)
    

    return ans

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    solve(n,k,arr)
