import sys
input = sys.stdin.readline

def dfs(x):
    visit[x] = True
    for i in graph[x]:
        if not visit[i]:
            dfs(i)

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [False]*(n+1)
cnt = 0
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    if not visit[i]:
        dfs(i)
        cnt+=1
print(cnt)
