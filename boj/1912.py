import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*n
arr = list(map(int,input().split()))

dp[0] = arr[0] 

for i in range(1,n):
    if arr[i-1] < 0:
        dp[i] = max(dp[i-2] + arr[i-1] + arr[i], arr[i])
    else:
        dp[i] = dp[i-1] + arr[i]
print(max(dp))