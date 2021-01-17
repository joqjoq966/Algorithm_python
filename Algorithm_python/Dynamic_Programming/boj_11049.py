import sys
input = sys.stdin.readline

N = int(input())
mat = []
dp = [[0]*N for _ in range(N)]

for i in range(N):
	a,b = map(int,input().split())
	mat.append((a,b))

for i in range(1,N):
	for start in range(N-i):
		end = i+start
		print(start,end)
		
		if start!=end:
			dp[start][end] = sys.maxsize

		for k in range(start,end):
			dp[start][end] = min(dp[start][end], dp[start][k] + dp[k+1][end] + mat[start][0]*mat[k][1]*mat[end][1])


print(dp)