#인접 리스트로 나타냄
def dfs(graph, v, visited):
	visited[v]=True
	print(v,end=' ')

	for i in graph[v]:
		if not visited[i]:
			dfs(graph,i,visited)

graph =[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
visited = [False]*9
dfs(graph,1,visited)

#인접 행렬로 나타냄
def dfs(matrix, v, visited):
	visited[v]=True
	print(v,end=' ')

	for i in range(len(matrix[v])):
		if not visited[i] and matrix[v][i]>0:
			dfs(matrix,i,visited)

graph =[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
matrix = [[0]*9 for _ in range(9)]

for i in range(len(graph)):
	for j in graph[i]:
		matrix[i][j]=1

visited = [False]*9
dfs(matrix,1,visited)