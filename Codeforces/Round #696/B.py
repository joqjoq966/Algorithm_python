import sys
import math
input = sys.stdin.readline

def solve(d):
    first = 0
    second = 0
    for p in prime:
        if p-1 >= d:
            first = p
            break
    for p in prime:
        if p-first >= d:
            second = p
            break
    return first*second

prime = [2]
for i in range(3,int(1e6)):
    check = True
    for j in range(2,int(math.sqrt(i)+1)):
        if i%j==0:
            check = False
            break
    if check:
        prime.append(i)

t = int(input())
for _ in range(t):
    d = int(input())
    print(solve(d))