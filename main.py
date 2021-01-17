import sys
input = sys.stdin.readline

n,k = map(int,input().split())
w,v =[],[]

for _ in range(n):
	weight,value = map(int,input().split())
	w.append(weight)
	v.append(value)

dp = [[0]*(k+1) for _ in range(n)]
for i in range(n):
	for j in range(k+1):
		if j-w[i]>=0:
			dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i] )
		else:
			dp[i][j] = dp[i-1][j]

print(dp[-1][-1])

import sys
input = sys.stdin.readline

n,k = map(int,input().split())
dp = {0:0}

for _ in range(n):
	weight,value = map(int,input().split())
	t={}
	# 현재 dp(dict)에는 이번 물품을 넣기 전 가능한 모든(무게:가치)의 조합이 들어있음
	for w,v in dp.items():
		nw = w + weight
		nv = v + value
		if nw <= k and dp.get(nw,0) < nv:
			t[nw]=nv
	dp.update(t)
	
print(max(dp.values()))
