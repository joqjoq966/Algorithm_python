import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
dp = [1]*(n)
ans = 1
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] <= dp[j] :
            dp[i]+=1
        ans = max(ans, dp[i])

print(ans)
        