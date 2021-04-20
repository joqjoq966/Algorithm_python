import sys
import heapq
input = sys.stdin.readline
q = []
N = int(input())
for _ in range(N):
    x = int(input())
    if x > 0:
        heapq.heappush(q, -x)
    else:
        if not q:
            print(0)
        else:
            print(-heapq.heappop(q))