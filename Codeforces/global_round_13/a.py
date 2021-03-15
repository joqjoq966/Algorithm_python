import sys
input = sys.stdin.readline

def solve(n,q,arr):
    

    return 

n,q = map(int, input().split())
arr = list(map(int, input().split()))
one = 0

for i in range(len(arr)):
    if arr[i]==1:
        one += 1
    
for _ in range(q):
    a, b = map(int,input().split())
    if a==1:
        if arr[b-1]==1:
            arr[b-1] = 0
            one -=1
        else:
            arr[b-1] = 1
            one += 1
    else:
        if b <= one:
            print(1)
        else:
            print(0)
    