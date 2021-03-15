from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visit = [False]*(N+1)
dfs_ans = []
bfs_ans = []


for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# for i in range(N):
#     graph[i].sort()

def dfs(x):
    visit[x] = True
    dfs_ans.append(x)
    
    for i in graph[x]:
        if not visit[i]:
            dfs(i)
    return 

def bfs(x):
    q = deque()
    q.append(x)
    visit[x] = True
    
    while q:     
        a = q.popleft()
        bfs_ans.append(a)
        for i in graph[a]:
            if not visit[i]:
                q.append(i)
                visit[i] = True
                
    
for i in range(N+1):
    graph[i].sort()

dfs(V)
visit = [False]*(N+1)
bfs(V)
print(*dfs_ans)
print(*bfs_ans)
