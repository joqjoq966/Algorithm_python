
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
dp = {0:0}

for _ in range(n):
	weight,value = map(int,input().split())
	t={}
	
	for w,v in dp.items():
		nw = w + weight
		nv = v + value
		if nw <= k and dp.get(nw,0) < nv:
			t[nw]=nv
	dp.update(t)
	
print(max(dp.values()))
