import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)
n,m,c = map(int,input().split())
graph = [ [] for _ in range(n+1) ]
distance = [INF]*(n+1)
for _ in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))

def dijkstra(c):
    q = []
    heapq.heappush(q,(0,c))

    while q:
        dist, idx = heapq.heappop(q)

        if distance[idx] < dist:
            continue

        for i in graph[idx]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(c)
ans = [0,0]
for i in range(1,n+1):
    if distance[i] < INF:
        ans[1] = max(ans[1], distance[i])
        ans[0] += 1
print(*ans)

