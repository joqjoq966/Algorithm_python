import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def melt(x,y):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx and nx<n and 0<=ny and ny<m and graph[nx][ny]==0:
            cnt+=1
    return cnt

def dfs(x,y):
    visit[x][y]=True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<1 or nx>=n-1 or ny<1 or ny>=m-1:
            continue

        if graph[nx][ny]!=0 and not visit[nx][ny]:
            dfs(nx,ny)

n,m = map(int,input().split())
dx = [-1,0,1,0]
dy = [0,1,0,-1]
graph = []
melt_now = [[0]*m for _ in range(n)]
ice_cnt = 0
time = 0
check = False
visit = [[False]*m for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int,input().split())))

while True:
    time += 1
    ice_cnt=0
    for i in range(1,n-1):
        for j in range(1,m-1):
            if graph[i][j]!=0:
                melt_now[i][j] = melt(i,j)

    for i in range(1,n-1):
        for j in range(1,m-1):
            graph[i][j] = max(0,graph[i][j]-melt_now[i][j])
    
    # 빙산의 개수 세기
    for i in range(n):
        for j in range(m):
            if graph[i][j]!=0 and not visit[i][j]:
                dfs(i,j)
                ice_cnt+=1
    # print("ice ",ice_cnt)
    if ice_cnt>1:
        break
    
    #빙산이 다 녹았으면 0을 출력
    check = False
    for i in range(n):
        for j in range(m):
            if graph[i][j]!=0:
                check = True
    if check==False:
        break

    #빙산이 한개라면 다시 초기화
    for i in range(n):
        for j in range(m):
            melt_now[i][j]=0
            visit[i][j]=False

if check==False:
    print(0)
else:
    print(time)