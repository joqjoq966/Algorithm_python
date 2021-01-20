import sys
input = sys.stdin.readline
import heapq

v,e = map(int,input().split())
start = int(input())
INF = int(1e9)
graph = [[] for _ in range(v+1)]
distance =[0] + [INF]*(v)
q = []
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    distance[start] = 0
    heapq.heappush(q,(0,start))
    # (dist, idx)
    while q:
        dist, idx = heapq.heappop(q)

        if distance[idx] < dist:
            continue
    
        for i in graph[idx]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)
for i in range(1,v+1):
    if distance[i]==int(1e9):
        print("INF")
    else:
        print(distance[i])