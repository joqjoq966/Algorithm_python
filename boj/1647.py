import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())

graph = []
parent = [i for i in range(N+1)]
total_distance = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    graph.append((c,a,b))

graph.sort()
last = 0
for dist, a, b in graph:
    if find_parent(parent, a) != find_parent(parent, b):
        total_distance += dist
        union_parent(parent, a, b)
        last = dist

print(total_distance-last)