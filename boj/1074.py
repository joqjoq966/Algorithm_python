import sys
sys.setrecursionlimit(10**5)

N, r, c = map(int,input().split())
ans = 0
row = r
col = c

def find(N,r,c):
    global ans
    global row, col
    if N==1:
        return
    
    if r >= 2**(N-1):
        r = r-2**(N-1)
        ans += 2**(2*N-1)

    if c >= 2**(N-1):
        c = c-2**(N-1)
        ans += 2**(2*N-2)
    row = r
    col = c
    
    N -= 1
    find(N,r,c)
    return

find(N,r,c)
ans += 2*row + col
print(ans)
