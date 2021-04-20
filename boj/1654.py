import sys
input = sys.stdin.readline

K, N = map(int, input().split())
arr = []
for _ in range(K):
    arr.append(int(input()))

min_len = 1
max_len = max(arr)
mid = (min_len + max_len)//2
cnt = 0
while min_len <= max_len:
    mid = (min_len + max_len)//2
    cnt = 0
    for i in range(K):
        cnt += arr[i]//mid
    print(mid, cnt)
    if cnt >= N:
        min_len = mid + 1
    else:
        max_len = mid - 1
    
print(min_len - 1)

