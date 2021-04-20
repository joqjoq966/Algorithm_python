import sys
import heapq
input = sys.stdin.readline
q = []
N = int(input())
for _ in range(N):
    x = int(input())
    if x > 0:
        heapq.heappush(q, (x, 1))
    elif x < 0:
        heapq.heappush(q, (-x, -1))
    else:
        if not q:
            print(0)
        else:
            num, sign = heapq.heappop(q)
            if sign < 0:
                num *= -1
            print(num)