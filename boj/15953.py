import sys
input = sys.stdin.readline


t = int(input())
contest1 = [0] + [500] + [300]*2 + [200]*3 + [50]*4 + [30]*5 + [10]*6
contest2 = [0] + [512]*1 + [256]*2 + [128]*4 + [64]*8 + [32]*16
for _ in range(t):
    a, b = map(int,input().split())
    if a > 21:
        a = 0
    if b > 31:
        b = 0
    print(10000*(contest1[a] + contest2[b]))