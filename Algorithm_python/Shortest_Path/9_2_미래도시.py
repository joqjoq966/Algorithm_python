import sys
input = sys.stdin.readline

# 양방향
# 연결되어 있으면 1만큼의 시간으로 이동
# 1 -> K -> X

INF = int(1e9)
n,m = map(int,input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1
x,k = map(int,input().split())

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

ans = graph[1][k] + graph[k][x]
if ans >= int(1e9):
    print(-1)
else:
    print(ans)
