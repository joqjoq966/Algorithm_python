N = int(input())
K = int(input())
board = [[0]*(N+1) for _ in range(N+1)] # 맵 초기화
move = list() # 회전에 대한 정보 저장

for i in range(K):
	a,b = map(int,input().split())
	board[a][b]='a' #사과가 있는 곳은 'a'로 표시

L = int(input())
for i in range(L):
	t,d = input().split()
	move.append((int(t),d))

dx = [0,1,0,-1] #동쪽부터 시계방향 (동,남,서,북)
dy = [1,0,-1,0] 

def turn(direction, c): #회전하면 어느방향을 가리키는지 출력하는 함수
	if c=='L':
		direction = (direction+3)%4
	else:
		direction = (direction+1)%4
	return direction

def solution():
	x,y = 1,1  #초기위치(머리가 있는 위치)
	board[x][y]=1 #뱀이 있는 곳은 1로 표시
	direction = 0
	seconds = 0 #경과시간
	body = [(x,y)] #뱀이 존재하는 위치 모두 저장
	i=0 # 방향전환 가리키는 인덱스

	while True:
		# print(x,y)
		nx = x+dx[direction]
		ny = y+dy[direction]
		seconds+=1
		if 1<=nx<=N and 1<=ny<=N and board[nx][ny]!=1: #맵을 벗어나지 않고 몸에 부딪히지 않으면 진행
			
			if board[nx][ny]=='a': # 사과가 있는 칸에 도착
				board[nx][ny]=1 
				body.append((nx,ny))
			elif board[nx][ny]!='a': # 사과가 없는 칸에 도착
				board[nx][ny]=1
				body.append((nx,ny))
				tx, ty = body.pop(0) #꼬리부분은 맵에서 제거
				board[tx][ty] = 0
			x,y = nx,ny
		else: #맵을 벗어났거나 몸에 부딪힌 경우 반복문 종료
			break
		
		if i<L and move[i][0]==seconds: #방향 전환해야하는 경우 시간 순서대로 처리
			direction = turn(direction,move[i][1])
			i+=1

	return seconds

print(solution())
