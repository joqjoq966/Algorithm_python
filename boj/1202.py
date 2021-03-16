import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
q = []
jew = [0]*N
bag = [0]*K
ans = 0

for i in range(N):
    M, V = map(int, input().split())
    jew[i] = (M,V)

for i in range(K):
    bag[i] = int(input())

jew = sorted(jew)
bag = sorted(bag)
idx = 0
for i in range(K):
    
    while idx < N and jew[idx][0] <= bag[i]:
        heapq.heappush(q, -jew[idx][1])
        idx += 1
    
    if q:
        ans += -heapq.heappop(q)

print(ans)