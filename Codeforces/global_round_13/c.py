import copy
import sys
input = sys.stdin.readline

def jump(start,arr):
    while start + arr[start] < n:
        arr[start] -= 1
        start += arr[start]
    return arr            

def solve(n,arr):
    a = []
    for i in range(n):
        idx = i
        cnt = 0
        if arr[idx] != 1:
            cnt = 1
        while idx+arr[idx] < n:
            idx += arr[idx]
            if arr[idx] != 1:
                # arr[idx] -= 1
                cnt+=1
        a.append(cnt)
    
    return a
        
    

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(n,arr))