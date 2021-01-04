def rotation(s): #시계방향으로 90도 회전
	ret = []
	for i in range(len(s)):
		temp = []
		for j in range(len(s)-1,-1,-1):
			temp.append(s[j][i])
		ret.append(temp)
	return ret

# def move(s,n): #Key의 이동 // n=0,1,2,3 각각 상하좌우    
# 	if n==0:
# 		s.append([0]*len(s))
# 		s.pop(0)
# 	elif n==1:
# 		s.insert(0,[0]*len(s))
# 		s.pop()
# 	elif n==2:
# 		for i in range(len(s)):
# 			for j in range(len(s)-1):
# 				s[i][j]=s[i][j+1]
# 			s[i][-1]=0
# 	elif n==3:
# 		for i in range(len(s)):
# 			for j in range(len(s)-1,0,-1):
# 				s[i][j]=s[i][j-1]
# 			s[i][0]=0
# 	return s

def add_matrix(a,b):
    for i in range(len(a)):
        for j in range(len(b)):
            a[i][j]+=b[i][j]
            a[i][j]%=2
    return a

def check(board):
    N = len(board)//3
    for a in range(N,2*N):
        for b in range(N,2*N):
            if board[a][b]!=1:
                return False
    return True
    
def solution(key, lock):
    answer = True
    M = len(key)
    N = len(lock)
    board = [[0]*3*N for _ in range(3*N)]
    temp = [[0]*3*N for _ in range(3*N)]
    for i in range(N,2*N):
        for j in range(N,2*N):
            board[i][j]=lock[i-N][j-N]
            # temp[i][j]=lock[i-N][j-N]
    
    for i in range(len(board)-M+1):
        for j in range(len(board)-M+1):
            for _ in range(4):
                key = rotation(key)
                board = [[0]*3*N for _ in range(3*N)]
                for k in range(N,2*N):
                    for l in range(N,2*N):
                        board[k][l]=lock[k-N][l-N]
                for a in range(M):
                    for b in range(M):
                        board[i+a][j+b] = key[a][b]^board[i+a][j+b]
                if i==0 and j==0:
                    print(board)
                if check(board):
                    return True
                    
    return False