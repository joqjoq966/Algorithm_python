import sys
input = sys.stdin.readline

def dfs(x,y):
	global cnt
	print(x,y)
	if x==w and y==h:
		cnt += 1
		return

	visit[x][y]=True

	if ground[x][y]=='X':
		for i in range(2):
			nx = x+dx[i]
			ny = y+dy[i]
			if 1<=nx<=h and 1<=ny<=w and visit[nx][ny]==False:
				dfs(nx,ny)
				visit[nx][ny]=False
	elif ground[x][y]=='D':
		nx = x+1
		ny = y
		if 1<=nx<=h and 1<=ny<=w and visit[nx][ny]==False:
			dfs(nx,ny)
			visit[nx][ny]=False
	elif ground[x][y]=='R':
		nx = x
		ny = y+1		
		if 1<=nx<=h and 1<=ny<=w and visit[nx][ny]==False:
			dfs(nx,ny)
			visit[nx][ny]=False
	else:
		for i in range(3):
			ground[x][y]=write[i]
			dfs(x,y)
	
H,W,K = map(int,input().split())
ground = [[0]*(W+1) for _ in range(H+1)]
visit = [[False]*(W+1) for _ in range(H+1)]
write = ['X','R','D']
dx = [1,0]
dy = [0,1]
cnt = 0

for i in range(K):
	_h,_w,c = input().split()
	h = int(_h)
	w = int(_w)
	ground[h][w]=c

dfs(1,1)
# print(ground)
# print(visit)
# print(cnt)


		



