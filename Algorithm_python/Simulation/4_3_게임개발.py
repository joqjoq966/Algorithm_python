N,M = map(int,input().split())
x,y,d = map(int,input().split())

m =[] #게임의 map
for i in range(N):
	m.append(list(map(int,input().split())))

check = [[0]*M for i in range(N)] # 가보지 않은 칸인지 확인
direction = [0,1,2,3] #북 동 남 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

ans = 1 #처음 시작 위치는 방문한 것으로 함
check[x][y]=1 # 처음 시작 위치는 방문했다고 체크

print(x,y)
while True:
	d = (d+3)%4 #왼쪽으로 90도 회전
	for i in range(len(direction)):
		if direction[i]==d:
			nx = x + dx[i]
			ny = y + dy[i]
			if 0<=nx<N and 0<=ny<M and m[nx][ny]==0 and check[nx][ny]==0: #범위 안에 있고, 육지이고, 아직 방문 안했으면 이동
				x = nx
				y = ny
				check[x][y]=1 #방문했다고 체크
				ans+=1
				# print(x,y)
				break
	
	cnt = 0 # 4면이 모두 불가능한 경우를 대비한 count
	for i in range(4):
		if x+dx[i]<0 or y+dy[i]<0 or x+dx[i]>=N or y+dy[i]>=M :
			cnt += 1
			pass
		elif 0<=(x+dx[i])<N and 0<=(y+dy[i])<M :	
			if (m[x+dx[i]][y+dy[i]]==1 or check[x+dx[i]][y+dy[i]]==1):
				cnt+=1

	if cnt ==4:	#4면이 모두 갈 수 없는 곳이면 뒤로 한 칸
		x -= dx[direction.index(d)]
		y -= dy[direction.index(d)]
		d = (d-3)%4 #이 while문의 시작에서 회전부터 시작하므로 뒤로 이동할 때는 회전을 고려하면 안되므로 반대방향으로 회전시켜서 상쇄
		if x<0 or x>=N or y<0 or y>=M or m[x][y]==1 :	
			break
		
print(ans)

#시간 복잡도 : 최악의 경우에 모든 육지를 다 돌아야 하므로 O(N*M)