import sys
from collections import deque
input = sys.stdin.readline

def bfs(a, b): # 먹을 수 있는 물고기들의 좌표와 거리 리턴
    global eaten_cnt
    global shark_size
    q = deque()
    q.append((a,b,0))
    arr[a][b] = 0
    visited = [[False]*N for _ in range(N)]
    candidate = []

    while q:
        x, y, dist = q.popleft()
        # visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny]:
                continue
            
            if arr[nx][ny] != 0 and arr[nx][ny] < shark_size:
                # print(nx, ny,"wow")
                visited[nx][ny] = True
                q.append((nx,ny,dist+1))
                candidate.append((dist+1,nx,ny))
            elif arr[nx][ny] == 0 or arr[nx][ny] == shark_size:
                # print(nx,ny)
                q.append((nx,ny,dist+1))
                visited[nx][ny] = True

    if len(candidate) > 0:
        candidate.sort()
        # print(candidate[0][1],candidate[0][2],candidate[0][0])
        arr[candidate[0][1]][candidate[0][2]] = 0
        return candidate[0]
    return 0,0,0

            

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
shark = [0, 0]

fish_list = []
shark_size = 2
eaten_cnt = 0
ans = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            fish_list.append((arr[i][j], i, j))
        if arr[i][j] == 9:
            shark = [i,j]

while True:
    move, shark[0], shark[1] =  bfs(shark[0], shark[1])
    # print(shark[0], shark[1], move)
    if move == 0:
        break
    eaten_cnt += 1
    if shark_size == eaten_cnt:
        shark_size += 1
        eaten_cnt = 0
    ans += move

print(ans)
