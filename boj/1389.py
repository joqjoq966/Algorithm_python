import sys
input = sys.stdin.readline

N, M = map(int,input().split())
INF = int(1e9)
graph = [[INF]*(N+1) for _ in range(N+1)]
ans = 0
ans_dist = INF

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(N+1):
    graph[i][i] = 0

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1,N+1):
    if ans_dist > sum(graph[i][1:]):
        ans_dist = sum(graph[i][1:])
        ans = i
print(ans)