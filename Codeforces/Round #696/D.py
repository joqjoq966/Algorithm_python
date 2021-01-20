import sys
input = sys.stdin.readline

def swap(arr,i):
    arr[i],arr[i+1] = arr[i+1],arr[i]
    return arr

def solve(n,arr):
    check = False
    temp = arr[:]
    for i in range(n-1):
        arr[i+1]-=arr[i]
        if arr[i+1] < 0:
            if check == False:
                check =True
                arr[i+1] = -arr[i+1]
    if arr[n-1]==0:
        return "YES"

    temp[-1],temp[-2] = temp[-2],temp[-1]
    
    for i in range(n-1):
        temp[i+1]-=temp[i]
        if temp[i+1] < 0:
            break    
    if temp[n-1]==0:
        return "YES"
    return "NO"
    

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(solve(n,arr))
