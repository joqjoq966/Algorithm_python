from collections import deque
N, M = map(int, input().split())
graph = list()
for i in range(N):
	s = input()
	graph.append(list(map(int,s)))

dx = [0,-1,0,1]
dy = [-1,0,1,0] #좌상우하 

def bfs(x,y):
	q = deque()
	q.append((x,y))
	while q:
		x,y = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if nx<0 or ny<0 or nx>=N or ny>=M: #미로를 벗어나는 경우 
				continue
			
			if graph[nx][ny]==0: #괴물이 있는 부분
				continue

			if graph[nx][ny]==1: # 아직 방문하지 않은 노드
				graph[nx][ny]=graph[x][y]+1 #지금까지 지나온 칸 수를 계산
				q.append((nx,ny))

	return graph[N-1][M-1]

print(bfs(0,0))

