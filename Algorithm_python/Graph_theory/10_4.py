from collections import deque

N = int(input())
time = [0]*(N+1)
time_inc = [0]*(N+1)
lecture = [[] for _ in range(N+1)]
indegree = [0]*(N+1)

for i in range(N):
    lec = input()
    
    info = list(map(int,lec.split()))
    time[i+1] = info[0]
    if info[1] == -1:
        continue
    else:
        j = 1
        while info[j] != -1:
            indegree[i+1] += 1
            lecture[info[j]].append(i+1)
            j+=1

def topo_sort():
    result = []
    q = deque()
    
    for i in range(1,N+1):
        if indegree[i]==0:
            q.append(i)

    while q:
        x = q.popleft()
        for lec in lecture[x]:
            time_inc[lec] += time[x]
        
        result.append(x)
        for i in lecture[x]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    return time_inc

time_inc = topo_sort()
for i in range(len(time)):
    time[i] += time_inc[i]
print(time)
            
            
