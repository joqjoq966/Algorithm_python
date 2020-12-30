import numpy as np
t = int(input())

for i in range(t):
	n = int(input())
	num = list(map(int,input().split()))
	and_list = [[0]*n for _ in range(n)]
	or_list = [[0]*n for _ in range(n)]
	
	ans = 0
	
	for a in range(n):
		for b in range(n):
			and_list[a][b]=num[a]&num[b]
			or_list[a][b]=num[a]|num[b]

	and_list = np.array(and_list)
	or_list = np.array(or_list)
	ans = np.sum(np.dot(and_list,or_list))
	ans %=(10**9+7)
	print(ans)