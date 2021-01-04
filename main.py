N,M,B = map(int,input().split())
ground = [[0]*M for i in range(N)]
# 최소, 최대높이 초기화, 현재 인벤토리에 있는 블록의 갯수 저장
min_height = 10**9
max_height = -1
total_blocks = B

# 각 위치마다 높이를 입력받고, 전체의 최소높이, 최대높이를 구한다.
for i in range(N):
	ground[i]=list(map(int,input().split()))
	total_blocks+=sum(ground[i])
	min_height = min(min_height,min(ground[i]))
	max_height = max(max_height,max(ground[i]))

def solution(N,M,B,ground):
	ans_time = 2*(10**9)
	# 최대높이부터 최소높이까지 모든 경우를 탐색한다
	for height in range(max_height,min_height-1,-1):
		# 필요한 블록의 개수가 전체 블록의 개수보다 많으면 건너뜀 
		if height*N*M > total_blocks:
			continue
		temp_time = 0
		# 각 칸 별로 해당 height에 비해 높거나 낮을 때 각각 필요한 시간을 구한다
		for i in range(N):
			for j in range(M):
				if ground[i][j]>height:
					temp_time += 2*(ground[i][j]-height)
				else:
					temp_time += (height-ground[i][j])
		# ans_time = min(ans_time, temp_time)
		# 최소시간을 찾고 그 때의 높이를 구한다.
		if ans_time > temp_time:
			ans_time = temp_time
			ans_height = height
	return ans_time, ans_height

print(*solution(N,M,B,ground))

# 시간 복잡도 : O(max_height*N*M)
# 사용한 방식 : 브루트포스, 낮은 
		
