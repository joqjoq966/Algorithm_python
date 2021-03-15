import sys
input = sys.stdin.readline

def solve(n,arr):
    ans = "YES"
    arr = set(arr)
    if len(arr) != n:
        return "NO" 
    
    arr = sorted(arr, reverse=True)
    # a = [0]*n
    aa = arr[0] // (2*n)
    if (arr[0]%(2*n))!=0:
        return "NO"
    # a[0] = (arr[0]//(2*n))
    
    for i in range(1,n):
        if ((arr[i]-2*aa) % (2*n-2*i)) != 0:
            return "NO"
        if arr[i]-2*aa <= 0:
            return "NO"
        # a[i] = (arr[i]-2*sum(a)) // (2*n-2*i)
        aa += (arr[i]-2*aa) // (2*n-2*i)
    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(solve(n,arr))
