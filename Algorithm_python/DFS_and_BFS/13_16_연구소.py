# 3개의 벽을 세울 수 있는 모든 경우의 수 탐색
# 3개의 벽을 세운 후 바이러스를 퍼뜨린 지도를 만든다
# 안전 영역의 개수를 센다
# 2,3을 반복하면서 안전영역의 최대를 찾는다
from itertools import combinations
import sys
input = sys.stdin.readline

#바이러스가 퍼지는 것을 구현하는 함수
def virus_spread(x,y):
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]	
		if nx<0 or ny<0 or nx>=N or ny>=M:
			continue
		if graph[nx][ny]==0:
			graph[nx][ny]=2
			virus_spread(nx,ny)
		
# 안전구역의 갯수 세는 함수
def safe_area(graph):
	cnt =0
	for i in range(len(graph)):
		for j in range(len(graph[i])):
			if graph[i][j]==0:
				cnt +=1
	return cnt

#벽을 3개 세우는 것을 조합으로 한 개씩 고려하면서 안전구역의 최대개수를 구하는 함수
def dfs(graph):
	global ans,N,M
	for w in wall:
		# 원본 그래프를 유지하기위해 temp에 임시저장
		for i in range(N):
			for j in range(M):
				temp[i][j]=graph[i][j]
		# wall에 있는 벽 3개를 순차적으로 놓으면서		
		for i,j in w:
			graph[i][j]=1
		#바이러스를 퍼뜨리고	
		for i,j in virus:
			virus_spread(i,j)
		#현재의 안전 영역의 최대값을 구한다
		ans = max(ans,safe_area(graph))
		# temp에 있는 원본 그래프를 다시 가져옴
		for i in range(N):
			for j in range(M):
				graph[i][j]=temp[i][j]
	
	return ans

N, M = map(int,input().split())
graph = [[0]*M for _ in range(N)] #연구소 지도
temp = [[0]*M for _ in range(N)] #연구소 지도
visit = [[False]*M for _ in range(N)] #방문 체크
empty = [] #빈 곳을 체크 --> 3개의 벽을 놓을 때 조합을 이용해서 활용
virus = [] #바이러스가 있는 곳 체크
dx = [-1,1,0,0] #상하좌우
dy = [0,0,-1,1]
ans = 0

for i in range(N):
	graph[i] = list(map(int,input().split()))

for i in range(N):
	for j in range(M):
		if graph[i][j]==2:
			virus.append((i,j))
		elif graph[i][j]==0:
			empty.append((i,j))
#벽 3개를 놓는 모든 경우의 수
wall = list(combinations(empty,3))
print(dfs(graph))
