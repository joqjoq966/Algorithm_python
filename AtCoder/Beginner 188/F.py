import sys
from collections import deque
input = sys.stdin.readline

x,y = map(int,input().split())
cnt = 0
ans = 0
q = deque()

while 4*x<y:
	x*=2
	cnt+=1
	
q.append((x,cnt))
while True:
	ans = q.popleft()
	if ans[0]==y:
		break
	
	q.append((ans[0]+1,ans[1]+1))
	q.append((ans[0]*2,ans[1]+1))
	q.append((ans[0]-1,ans[1]+1))	
	
print(ans[1])