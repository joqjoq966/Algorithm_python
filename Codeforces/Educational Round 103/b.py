import sys
input = sys.stdin.readline

def solve(n,k,arr):
    ans = 0
    s = arr[0]
    for i in range(1,n):
        if arr[i]*100 <= s*k:
            s+=arr[i]
            continue
        else:
            if (100*arr[i])%k==0:
                temp = (100*arr[i])//k
            else:
                temp = (100*arr[i])//k + 1
            ans += temp-s
            # print(temp-s)
            s = temp + arr[i]
        # print(">>>",i,ans) 
    return ans

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    print(solve(n,k,arr))
