from collections import deque

v,e = map(int,input().split())
indegree = [0]*(v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a,b = map(int, input().split())
    indegree[b] += 1
    graph[a].append(b)


def topo_sort():
    result = []
    q = deque()

    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)
        
    while q:
        x = q.popleft()
        result.append(x)
        
        for i in graph[x]:
            indegree[i] -= 1
            
            if indegree[i] == 0:
                q.append(i)
    return result

result = topo_sort()
for i in result:
    print(i, end = ' ')
            

