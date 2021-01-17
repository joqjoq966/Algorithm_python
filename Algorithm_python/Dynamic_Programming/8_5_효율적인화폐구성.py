import sys
input = sys.stdin.readline

N,M = map(int,input().split())
money = []
dp = [0]*(10001)
for i in range(N):
	money.append(int(input()))
	dp[money[i]]=1

for i in range(1,M+1):
	check = False
	temp = 100000
	for m in money:
		if i-m > 0 and dp[i-m]!=0:
			temp = min(temp,dp[i-m])
			check = True
	if check:
		dp[i] = temp + 1
		check = False

if dp[M]==0:
	print(-1)
else:
	print(dp[M])