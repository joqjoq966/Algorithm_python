from collections import deque
import sys
input = sys.stdin.readline

def bfs(n,k):
    ans = 0
    if n>k:
        return n-k
    q = deque()
    q.append((n,0))
    while q:
        location, step = q.popleft()
        visit[location] = 1
        if location == k:
            ans = step
            break
        
        if location-1 >= 0 and visit[location-1]==0:
            q.append((location-1,step+1))
        if location+1 <= 100000 and visit[location+1]==0:
            q.append((location+1, step+1))
        if location*2 <=100000 and visit[location*2]==0:
            q.append((location*2, step+1))

    return ans

n,k = map(int,input().split())
visit = [0]*100001
print(bfs(n,k))
