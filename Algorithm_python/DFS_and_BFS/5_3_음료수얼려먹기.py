N, M = map(int, input().split())
graph = []
for i in range(N):
	s = list(map(int,input()))
	graph.append(s)

def dfs(x,y):
	if x<0 or y<0 or x>N-1 or y>M-1:
		return False
	if graph[x][y]==0:
		graph[x][y]=-1
		dfs(x-1,y)
		dfs(x+1,y)
		dfs(x,y-1)
		dfs(x,y+1)
		return True
	return False
	
cnt = 0
for i in range(N):
	for j in range(M):
		if dfs(i,j)==True:
			cnt+=1

print(cnt)