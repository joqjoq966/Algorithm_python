N = int(input())
K = int(input())
apple = list()
for i in range(K):
	a,b = map(int,input().split())
	apple.append((a,b))

L = int(input())
move = list()
for i in range(K):
	t,d = input().split()
	move.append((int(t),d))

board = [[0]*(N+1) for _ in range(N+1)]
for a in apple:
	board[a[0]][a[1]]='a' #사과 위치

def check(x,y,N):
	if x<1 or y<1 or x>=N or y>=N: #보드 밖으로 나가면 False
		return False
	return True

def go(x,y,d,turn_dir): #d : 보고 있는 방향 상하좌우  0,1,2,3
	if turn_dir=='D':
		if d==0: 
			y+=1; d=3
		elif d==1: 
			y-=1; d=2
		elif d==2: 
			x-=1; d=0
		elif d==3: 
			x+=1; d=1
	
	elif turn_dir=='L':
		if d==0: 
			y-=1; d=2 
		elif d==1: 
			y+=1; d=3
		elif d==2: 
			x+=1; d=1
		elif d==3: 
			x-=1; d=0 
	else:
		if d==0: x-=1
		elif d==1: x+=1
		elif d==2: y-=1
		elif d==3: y+=1 
	return x,y,d 

x=1; y=1; d=3 #초기 위치
# head = [x,y]; tail=[x,y]
tx,ty = 1,1
second = 0; i=0
while True:
	second+=1
	
	if i<len(move) and move[i][0]==second-1:
		# nx,ny = x,y
		x,y,d=go(x,y,d,move[i][1])
		if (x,y) in apple:
			board[tx][ty]=1
			apple.pop(apple.index((x,y)))
		else:
			board[tx][ty]=0
		i+=1
	else:
		# tx,ty = x,y
		x,y,d=go(x,y,d,'not')
		# board[x][y]=1
		if (x,y) in apple:
			board[tx][ty]=1
			apple.pop(apple.index((x,y)))
		else:
			board[tx][ty]=0

	print(x,y)
	if check(x,y,N)==False or board[x][y]==1: # 아직 자기 몸에 부딪히는건 고려 안함
		break
	board[x][y]=1

print(board)
print(second)

	
