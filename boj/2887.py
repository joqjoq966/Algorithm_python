import sys
input = sys.stdin.readline

def find_parent(parent, a):
    if parent[a] != a:
        return find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
planet = [[0,0,0] for _ in range(N)]
x_list = [(0,0)]*N
y_list = [(0,0)]*N
z_list = [(0,0)]*N

parent = [i for i in range(N)]
edges = [] #거리, node_1, node_2

for i in range(N):
    x,y,z = map(int,input().split())
    x_list[i] = (x,i)
    y_list[i] = (y,i)
    z_list[i] = (z,i)

x_list = sorted(x_list)
y_list = sorted(y_list)
z_list = sorted(z_list)

for i in range(N-1):
    edges.append((x_list[i+1][0] - x_list[i][0], x_list[i+1][1], x_list[i][1]))
    edges.append((y_list[i+1][0] - y_list[i][0], y_list[i+1][1], y_list[i][1]))
    edges.append((z_list[i+1][0] - z_list[i][0], z_list[i+1][1], z_list[i][1]))

edges = sorted(edges)
total = 0

for edge in edges:
    dist, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent, a,b)
        total += dist

print(total)