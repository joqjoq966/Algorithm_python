import copy
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
dp = [1]*n
dp_arr = []
temp_arr = []
max_dp = 0
temp = 0
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] <= dp[j]:
            dp[i] += 1

ans = max(dp)
print(ans)
for i in range(n-1,-1,-1):
    if dp[i]==ans:
        dp_arr.append(arr[i])
        ans-=1

print(*dp_arr[::-1])