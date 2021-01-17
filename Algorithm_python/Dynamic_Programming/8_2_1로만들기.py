
n = 300
dp = [0]+[0]*n
dp[1] = 0

for i in range(2,n+1):
	dp[i] = dp[i-1]+1
	if i%5==0:
		dp[i] = min(dp[i-1]+1,dp[i//5]+1)
	if i%3==0:
		dp[i] = min(dp[i-1]+1,dp[i//3]+1)
	if i%2==0:
		dp[i] = min(dp[i-1]+1,dp[i//2]+1)


print(dp)