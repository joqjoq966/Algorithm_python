import sys
input = sys.stdin.readline

def dfs(x,y):
    if cnt[x][y] != 0:
        return cnt[x][y]
    
    cnt[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and ny >= 0 and nx < n and ny < n and graph[nx][ny] > graph[x][y]:
            cnt[x][y] = max(cnt[x][y], dfs(nx,ny)+1)
        
    return cnt[x][y]

n = int(input())
graph = [[0]*n for _ in range(n)]
cnt = [[0]*n for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
# ans = 0

for i in range(n):
    graph[i] = list(map(int,input().split()))

for i in range(n):
    for j in range(n):
        cnt[i][j] = dfs(i,j)

for i in range(4):
    print(cnt[i])
print(max(map(max,cnt)))
