import sys 
from collections import defaultdict
input = sys.stdin.readline

def solve(n,m):
    if n ==1:
        return 1
    if n ==2:
        if (arr[0] + arr[1]) % m ==0:
            return 1
        else:
            return 0
    ans = 0
    d = defaultdict()
    for i in range(n):
        arr[i] = arr[i] % m 
        if arr[i] in d:
            d[arr[i]] += 1
        else:
            d[arr[i]] = 1
    arr.sort()
    
    for i in range(n):
        if n-arr[i] in d.keys() and abs(d[arr[i]] - d[n-arr[i]]) > 1:
            ans += abs(d[arr[i]]-d[n-arr[i]])
        else:
            ans += 1
    print(d)
    print(arr)
    return ans

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(n,m))
	