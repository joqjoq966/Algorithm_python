import sys
input = sys.stdin.readline

# def linear(array, n, m):
#     top = array[0]
#     right = [ array[i][m-1] for i in range(1,n)]
#     bottom = array[n-1][-2::-1]
#     left = [ array[i][0] for i in range(n-2,0,-1)]
#     return top, right, bottom, left

def rotate(p):
    
    temp = arr[p][p]
    
    for i in range(p, M-p-1):
        arr[p][i] = arr[p][i+1]
    
    for i in range(p, N-p-1):
        arr[i][M-1-p] = arr[i+1][M-1-p]

    for i in range(M-p-1, p, -1):
        arr[N-p-1][i]  = arr[N-p-1][i-1]
    
    for i in range(N-p-1, p, -1):
        arr[i][p] = arr[i-1][p]

    arr[p+1][p] = temp


N, M, R = map(int,input().split())
n, m = N, M
arr = [] 
for i in range(N):
    arr.append(list(map(int, input().split())))

s = min(N,M)//2

for i in range(min(N,M)//2):
    for _ in range(R):
        rotate(i)

for a in arr:
    print(*a)
