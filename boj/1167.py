import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, dist):
    visit[x] = dist
    for vertex, weight in edge[x]:
        if visit[vertex] == 0:
            dfs(vertex, dist+weight)
    return

V = int(input())
edge = [[] for _ in range(V+1)]
visit = [0]*(V+1)
ans = 0

for i in range(1,V+1):
    edge_info = list(map(int, input().split()))
    j = 1
    while j < len(edge_info):
        if edge_info[j] == -1:
            break
        edge[edge_info[0]].append((edge_info[j],edge_info[j+1]))
        j += 2

# 아무 점에서 시작 --> 1은 항상 존재하므로 1에서 시작함
dfs(1,0)
visit[1] = 0

# 가장 먼 지점 찾기
idx = visit.index(max(visit))

#초기화
for i in range(V+1):
    visit[i] = 0
#idx에서 가장 먼 지점 찾기
dfs(idx,0)
visit[idx] = 0
ans += max(visit)
print(ans)
