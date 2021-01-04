def rotation(s): #시계방향으로 90도 회전
	ret = []
	for i in range(len(s)):
		temp = []
		for j in range(len(s)-1,-1,-1):
			temp.append(s[j][i])
		ret.append(temp)
	return ret

def check(board): # 자물쇠가 열리는 상황인지를 체크
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
    # 보드의 크기를 가로 세로를 각각 3배로 확장하여 정중앙에 자물쇠가 위치하도록 설정
    board = [[0]*3*N for _ in range(3*N)]
    temp = [[0]*3*N for _ in range(3*N)]
    for i in range(N,2*N):
        for j in range(N,2*N):
            board[i][j]=lock[i-N][j-N]
    # 열쇠의 왼쪽 위 칸을 기준으로 한칸씩 이동하며 자물쇠가 열리는 상태인지 확인한다.
    for i in range(len(board)-M+1):
        for j in range(len(board)-M+1):
	     for _ in range(4):
                # 한 위치에서 4번 회전하여 모든 경우를 체크
		key = rotation(key)
		# board에 초기 자물쇠 상태를 저장
		board = [[0]*3*N for _ in range(3*N)]
                for k in range(N,2*N):
                    for l in range(N,2*N):
                        board[k][l]=lock[k-N][l-N]
                # 키와 자물쇠의 XOR연산
		for a in range(M):
                    for b in range(M):
                        board[i+a][j+b] = key[a][b]^board[i+a][j+b]
                if i==0 and j==0:
                    print(board)
                if check(board):
                    return True                    
    return False

# 시간 복잡도 : O(board_len*board_len*N) --> O(N^3)
