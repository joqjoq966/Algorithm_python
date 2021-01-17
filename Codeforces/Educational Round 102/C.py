import sys
input = sys.stdin.readline

# 1,2,,,x-1,x,,,k,k-1,,,x
def solution(n,k):
	arr = []
	for i in range(1,k-(n-k)):
		arr.append(i)
	for i in range(k,k-(n-k)-1,-1):
		arr.append(i)
	return arr

t = int(input())

for i in range(t):
	n,k = map(int,input().split())
	print(*solution(n,k))
