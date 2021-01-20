import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)
graph = [ [INF]*(n+1) for _ in range(n+1)]
# distanse = [ [INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = min(graph[a][b],c)

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0
    
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(n+1):
    for j in range(n+1):
        if graph[i][j]==int(1e9):
            graph[i][j]=0
for i in range(1,n+1):
    print(*graph[i][1:])




