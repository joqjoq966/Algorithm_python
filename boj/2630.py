import sys
input = sys.stdin.readline

N = int(input())
graph = [[0]*N for _ in range(N)]
white = 0
blue = 0

def check(x, y, n):
    s = 0
    global white
    global blue
    
    for i in range(x,x+n):
        for j in range(y,y+n):
            s += graph[i][j]
    if s == 0:
        white += 1
    elif s == n*n:
        blue += 1
    else:
        check(x, y, n//2)
        check(x, y+n//2, n//2)
        check(x+n//2, y, n//2)
        check(x+n//2, y+n//2, n//2)


for i in range(N):
    graph[i] = list(map(int,input().split()))

check(0,0,N)
print(white)
print(blue)
