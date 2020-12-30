N = int(input())
dir = input().split()

x,y = 1,1 #초기위치
dx,dy = [0,-1,0,1],[-1,0,1,0] #LURD 순서
move = ['L','U','R','D']

for d in dir: # 입력된 방향을 순서대로 처리
	for i in range(len(move)): # LURD 중 해당하는 것과 일치하면 이동
		if d == move[i]:
			nx = x + dx[i]
			ny = y + dy[i]
			break
	if nx>=1 and ny>=1 and nx<=N and ny<=N: #공간을 벗어나지 않으면 이동
		x = nx
		y = ny

print(x,y)

#시간복잡도 : O(dir * 4)==O(dir)