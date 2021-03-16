import sys
input = sys.stdin.readline


n = int(input())
arr = [0]*(n+1)
for i in range(1,n+1):
    arr[i] = int(input())

i, j = 1, n
ans = 0
while i < j:
    
    start_i = i
    while i < j and arr[start_i] >= arr[i]:
        i += 1
    ans += max(arr[start_i:i+1]) - min(arr[start_i:i+1])

    start_j = j
    while i < j and arr[start_j] >= arr[j]:
        j -= 1
    ans += max(arr[j:start_j+1]) - min(arr[j:start_j+1])

print(ans)