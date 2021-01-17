import math
def solution(n,x,arr):
	max_ans = 0
	for i in range(n):
		max_ans += math.ceil(arr[i]/x)
	min_ans = math.ceil(sum(arr)/x)
	return min_ans,max_ans
	

t = int(input())
for i in range(t):
	n,x = map(int,input().split())
	arr = list(map(int,input().split()))
	print(*solution(n,x,arr))
	
	