def solution(n,arr):
	dp = [0]*(n)
	ans = 0
	for i in range(n-1,-1,-1):
		if i+arr[i]>=n:
			dp[i]=arr[i]
		else:
			dp[i] = arr[i]+dp[i+arr[i]]
		ans = max(ans,dp[i])
	return ans
		
t = int(input())

for i in range(t):
	n = int(input())
	arr = list(map(int,input().split()))

	print(solution(n,arr))
