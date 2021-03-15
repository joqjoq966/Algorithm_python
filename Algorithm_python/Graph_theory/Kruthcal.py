def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
v, e = map(int, input().split())
parent = [0]*(v+1)
for i in range(1,v+1):
    parent[i] = i

distance = []
total_distance = 0

for i in range(e):
    a, b, w = map(int,input().split())
    distance.append((w,(a,b)))

distance = sorted(distance, key=lambda x: x[0])
for dist, edge in distance:
    if find_parent(parent,edge[0]) != find_parent(parent,edge[1]):
        total_distance += dist
        union_parent(parent,edge[0],edge[1])
    
print(parent)
print(distance)
print(total_distance)


