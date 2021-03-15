import sys
input = sys.stdin.readline

def solve(n,arr):
    ans = 0
    for i in range(n-1):
        if abs(arr[i] - arr[i+1]) >1:
            return 0
    arr.sort()
    if arr[0]==arr[n-1]:
        ans = min(u+v,2*v)
    else:
        ans = min(u,v)
    return ans

t = int(input())
for _ in range(t):
    n,u,v = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(n,arr))