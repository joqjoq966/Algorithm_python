import sys
from itertools import combinations
input = sys.stdin.readline

def distance(a,b):
	return abs(a[0]-b[0])+abs(a[1]-b[1])

def min_dist(h,open): #집의 좌표가 나오면 폐업하지 않은 가장 가까운 치킨집 까지의 거리
	ans = N**3;
	for op in open:
		ans = min(ans,distance(h,op)) # 집과 치킨집사이의 거리 중 최소 구하기
	return ans

N, M = map(int,input().split())
graph = [[0]*N for _ in range(N)]
home = []
chicken = []
result = N**3; ans = N**3
for i in range(N):
	graph[i] = list(map(int,input().split()))

for i in range(N):
	for j in range(N):
		if graph[i][j]==1:
			home.append((i,j))
		elif graph[i][j]==2:
			chicken.append((i,j))

open = list(combinations(chicken,M))
# print(open)
for op in open:
	ans = 0
	for h in home:
		ans += min_dist(h,op)
	result = min(result,ans)

print(result)

# print(min_dist(3,2,open))

			
