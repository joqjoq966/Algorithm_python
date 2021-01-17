import sys
input = sys.stdin.readline
# 2차원 DP로 풀어야함
def solution(n,m,oper):
	dp = [[0]*(n) for _ in range(n+1)]
	for i in range(len(dp)):
		for j in range(len(dp)):
			if oper[j]=="+":
				dp[i][j] = dp[i][j-1]+1
			elif oper[j]=="-":
				dp[i][j] = dp[i][j-1]-1
	print(dp)
	for i in range(m):
		l,r = map(int,input().split())
		print(dp[])
		
t = int(input())

for i in range(t):
	n,m = map(int,input().split())
	oper = input()
	solution(n,m,oper)
