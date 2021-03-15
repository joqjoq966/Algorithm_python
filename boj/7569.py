from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    while q:
        a,b,c = q.popleft()
        visit[a][b][c] = 1
        for i in range(6):
            nz = a + dz[i]
            nx = b + dx[i]
            ny = c + dy[i]

            if 1<=nz<=h and 0<=nx<n and 0<=ny<m and tomato[nz][nx][ny]==0 and visit[nz][nx][ny]==0:
                q.append((nz,nx,ny))
                tomato[nz][nx][ny] = tomato[a][b][c]+1
                visit[nz][nx][ny] = 1
                
    

m,n,h = map(int,input().split())
tomato = [ [ [] for _ in range(n)] for _ in range(h+1)]
visit = [ [ [0]*m for _ in range(n)] for _ in range(h+1)]
dx = [-1,0,1,0,0,0]
dy = [0,1,0,-1,0,0]
dz = [0,0,0,0,1,-1]
ans = 0
impossible = False
q = deque()
for i in range(1,h+1):
    for j in range(n):
        a = list(map(int,input().split()))
        tomato[i][j] = a

for i in range(1,h+1):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k]==1 :
                q.append((i,j,k))
bfs()
for i in range(1,h+1):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k]==0:
                impossible = True
            else:
                ans = max(ans, tomato[i][j][k])
if impossible:
    print(-1)
else:
    print(ans-1)
                

# for i in range(1,h+1):
#     for j in range(n):
#         print(tomato[i][j])
# print()
# for i in range(1,h+1):
#     for j in range(n):
#         print(visit[i][j])

# # print(c)
