import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
dp = [0]*(1001)
sum_dp = [0]*n
ans = 0
# for i in range(n):
#     max_sum = 0
#     for j in range(i):
#         if arr[i] > arr[j] and sum_dp[i] < sum_dp[j]:
#             max_sum = max(max_sum, sum_dp[j])
#     sum_dp[i] = max_sum + arr[i]
#     ans = max(ans,sum_dp[i])
# # print(sum_dp)
# print(ans)
        
for i in range(n):
    dp[arr[i]] = max(dp[:arr[i]]) + arr[i]
print(max(dp))