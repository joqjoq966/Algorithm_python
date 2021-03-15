n = int(input())
point = []
dp = [0]*(n)
for _ in range(n):
    p = int(input())
    point.append(p)

dp[0] = point[0]
if n>=2:
    dp[1] = point[0] + point[1]
if n>=3:
    dp[2] = max(dp[0] + point[2], point[1] + point[2])

for i in range(3,n):
    dp[i] = max(dp[i-3]+point[i-1]+point[i], dp[i-2]+point[i])

print(dp[-1])
