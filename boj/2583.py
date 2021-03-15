import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(x,y):
    global s
    graph[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx and nx<m and 0<=ny and ny<n and not graph[nx][ny]:
            dfs(nx,ny)
            s+=1
    return s

m,n,k = map(int,input().split())
graph = [[False]*(n) for _ in range(m)]
s=1; cnt=0; ans = []
dx = [-1,0,1,0]
dy = [0,1,0,-1]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            graph[m-j-1][i] = True

# for i in range(m):
#     print(graph[i])
for i in range(m):
    for j in range(n):
        if not graph[i][j]:
            s=1
            cnt+=1
            ans.append(dfs(i,j))
ans.sort()
print(cnt)
if len(ans)==0:
    print(0)
else:
    print(*ans)