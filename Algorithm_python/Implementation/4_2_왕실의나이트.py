knight = list(input())

x = ord(knight[0])-ord('a')+1 # x좌표를 x축으로 설정 (a~h)
y = int(knight[1])

#왼쪽 2칸 위로 1칸 부터 시계방향으로 돌면서 8가지 좌표 설정
dx = [-2,-1,1,2,2,1,-1,-2] 
dy = [-1,-2,-2,-1,1,2,2,1]

ans = 0
for i in range(8):
	nx = x + dx[i]
	ny = y + dy[i]
	if 1<=nx<=8 and 1<=ny<=8:
		ans+=1
print(ans)

#시간 복잡도 : O(1)