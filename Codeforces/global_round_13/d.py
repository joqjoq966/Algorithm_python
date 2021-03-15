from collections import deque
import copy
import sys
input = sys.stdin.readline


def solve(u,v):
    
    a = []
    b = []
    for bit in range(30):
        if u & (1<<bit):
            a.append(bit)
        if v & (1<<bit):
            b.append(bit)
    
    ans = True

    if len(a) < len(b):
        ans = False
    else:
        for i in range(len(b)):
            if a[i] > b[i]:
                ans = False
    ans &= (u<=v)
    if ans ==True:
        return "YES"
    else:
        return "NO"

t = int(input())
for _ in range(t):
    u, v = map(int, input().split())
    print(solve(u,v))
    
    