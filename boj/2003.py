N, M = map(int,input().split())
arr = list(map(int, input().split()))
cnt = 0

i, j = 0, 0 
temp_sum = arr[0]
while i < N and j < N:
    # print(i, j)
    if temp_sum == M:
        # print("fit")
        cnt += 1
        j += 1
        if j == N:
            break
        temp_sum += arr[j]
    elif temp_sum > M:
        # print("bigger")
        temp_sum -= arr[i]
        i += 1
    elif temp_sum < M:
        # print("smaller")
        j += 1
        if j == N:
            break
        temp_sum += arr[j]
    

print(cnt)